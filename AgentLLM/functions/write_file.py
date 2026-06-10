import os
from config import MAX_CHARS

# directory will be treated as a relative path within the working_directory.
# directory can be set by the agent.
# working_directory can only be set by the user, us.
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path_wd = os.path.abspath(working_directory)
        file_full_path = os.path.normpath(os.path.join(abs_path_wd, file_path))
        within_wd = os.path.commonpath([abs_path_wd, file_full_path]) == abs_path_wd

        if not within_wd:
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

        if os.path.isdir(file_full_path):
            return f"Error: Cannot write to \"{file_path}\" as it is a directory"

        os.makedirs(os.path.dirname(file_full_path), exist_ok=True)

        with open(file_full_path, "w") as f:
            nb_chars: int = f.write(content)
            return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"

    except Exception as e:
        return f"Error: {e}"
