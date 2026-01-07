import os

def get_files_info(working_directory, directory="."):

    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpoath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'

    try:
        for item in target_dir
            target_dir_data += f'- {os.listdir(item)}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}\n'
        return target_dir_data
    except:
        return f'Error: Could not fetch data from: {target_dir}'
        