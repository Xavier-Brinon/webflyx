from collections.abc import Callable
from ollama          import Message

WORKING_DIR = "./calculator"

from functions.get_files_info   import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file  import schema_run_python_file, run_python_file
from functions.write_file       import schema_write_file, write_file

available_functions = [
    schema_get_file_content,
    schema_run_python_file,
    schema_get_files_info,
    schema_write_file
]

function_map: dict[str, Callable[..., str]] = {
    "get_files_info"  : get_files_info,
    "get_file_content": get_file_content,
    "write_file"      : write_file,
    "run_python_file" : run_python_file
}

def call_function(tool_call: Message.ToolCall, verbose: bool = False) -> Message:
    function_name = tool_call.function.name or ""
    function_args = dict(tool_call.function.arguments) if tool_call.function.arguments else {}
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    fn = function_map.get(function_name)
    if fn is None:
        return Message(
            role="tool",
            tool_name=function_name,
            content=f"error: Unknown function: {function_name}",
        )

    function_args["working_directory"] = WORKING_DIR
    function_result = fn(**function_args)
    return Message(
        role="tool",
        tool_name=function_name,
        content=str(function_result)
    )
