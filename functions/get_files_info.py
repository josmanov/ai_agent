import os

def get_files_info(working_directory, directory="."):

    # fix bug "pkg" is nota directory

    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        # Fix bug where directory content are being printed rather than printing only directory value
        print(f"Error: Cannot list {target_directory} as it is outside the permitted working directory")
    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'

    target_dir_data = ""
    try:
        if directory == '.':
            target_dir_data = "Result for current directory:\n"
        else:
            target_dir_data = (f'Result for {directory} directory:\n')
        try:
            for file in os.listdir(target_dir):
                file_size = os.path.getsize(target_dir + "/" + file)
                is_dir = os.path.isdir(target_dir + "/" + file)
                target_dir_data += (f'  - {file}: file_size={file_size} bytes, is_dir={is_dir}\n')
        except Exception as e:
            print(e)
    except:
        return f'Error: Could not fetch data from: {target_dir}'

    print(target_dir_data[:-1])