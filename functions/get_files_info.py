import os
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):

    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        # Fixed directory content being printed
        print(f'Result for \'{directory}\' directory:')
        print(f'    Error: Cannot list \"{directory}\" as it is outside the permitted working directory')
        return 2
    # fixed wrong variable usage for os.path.isdir function
    if os.path.isdir(target_dir) == False:
        print(f'Result for \'{directory}\' directory:')
        print(f'    Error: \'{directory}\' is not a directory')
        return 2

    target_dir_data = ""
    try:
        if directory == '.':
            target_dir_data = "Result for current directory:\n"
        else:
            target_dir_data = (f'Result for \'{directory}\' directory:\n')
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