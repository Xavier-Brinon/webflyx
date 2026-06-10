import os
# directory will be treated as a relative path within the working_directory.
# directory can be set by the agent.
# working_directory can only be set by the user, us.
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        if not os.path.isdir(directory):
            return f"Error: \"{directory}\" is not a directory"

        abs_path_wd = os.path.abspath(working_directory)
        full_path_d = os.path.normpath(os.path.join(abs_path_wd, directory))
        within_wd = os.path.commonpath([abs_path_wd, full_path_d]) == abs_path_wd

        if not within_wd:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

        return f"Success: \"{directory}\" is within the working directory"
    except Exception as e:
        return f"Error: {e}"
