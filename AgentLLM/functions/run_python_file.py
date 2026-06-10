import os
import subprocess
from config import MAX_CHARS

# directory will be treated as a relative path within the working_directory.
# directory can be set by the agent.
# working_directory can only be set by the user, us.
def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_path_wd = os.path.abspath(working_directory)
        file_full_path = os.path.normpath(os.path.join(abs_path_wd, file_path))
        within_wd = os.path.commonpath([abs_path_wd, file_full_path]) == abs_path_wd

        if not within_wd:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_full_path]
        if isinstance(args, list) and len(args) > 0:
            command.extend(args)
            print(f"about to execute {command}")

        completed_process = subprocess.run(
            command,
            capture_output=True,
            timeout=30,
            text=True,
            cwd=os.path.dirname(file_full_path)
        )
        return_process: str = ""
        returncode = completed_process.returncode
        if not returncode == 0:
            return_process += f"Process exited with code {returncode}\n"

        stdout = completed_process.stdout
        stderr = completed_process.stderr
        if stdout == None and stderr == None:
            return_process += f"No output produced\n"
        else:
            return_process += f"STDOUT: {stdout}\n" if not stdout == None else ""
            return_process += f"STDERR: {stderr}\n" if not stderr == None else ""

        return return_process
    except Exception as e:
        return f"Error: executing Python file: {e}"
