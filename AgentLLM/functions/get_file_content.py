import os
from config import MAX_CHARS

# directory will be treated as a relative path within the working_directory.
# directory can be set by the agent.
# working_directory can only be set by the user, us.
def get_file_content(working_directory: str, file_path: str = ".") -> str:
    try:
        abs_path_wd = os.path.abspath(working_directory)
        file_full_path = os.path.normpath(os.path.join(abs_path_wd, file_path))
        within_wd = os.path.commonpath([abs_path_wd, file_full_path]) == abs_path_wd

        if not within_wd:
            return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.isfile(file_full_path):
            return f"Error: File not found or is not a regular file: \"{file_path}\""

        with open(file_full_path, "r") as f:
            file_content: str = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"

        return file_content

    except Exception as e:
        return f"Error: {e}"
