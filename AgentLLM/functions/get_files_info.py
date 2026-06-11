import functools
import os
# directory will be treated as a relative path within the working_directory.
# directory can be set by the agent.
# working_directory can only be set by the user, us.
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path_wd = os.path.abspath(working_directory)
        full_path_d = os.path.normpath(os.path.join(abs_path_wd, directory))
        within_wd = os.path.commonpath([abs_path_wd, full_path_d]) == abs_path_wd

        if not within_wd:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

        if not os.path.isdir(full_path_d):
            return f"Error: \"{directory}\" is not a directory"

        def details_name(acc: str, name: str) -> str:
            full_path_name = os.path.normpath(os.path.join(full_path_d, name))
            return acc + f"- {name}:\tfile_size={os.path.getsize(full_path_name)} bytes,\tis_dir={os.path.isdir(full_path_name)}\n"

        details_listdir = functools.reduce(details_name, os.listdir(full_path_d), "")
        return details_listdir

    except Exception as e:
        return f"Error: {e}"

# functions/schemas.py
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory, providing file size and directory status.",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from.",
                },
            },
            "required": ["directory"],
        },
    },
}
