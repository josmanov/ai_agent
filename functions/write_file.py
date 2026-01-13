import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content into a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write the content into"),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file"),
        },
        required=["file_path", "content"]
    ),
)

def write_file(working_directory, file_path, content):
        
    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        return 2
    if os.path.isdir(target_dir) == True:
        print(f'Error: Cannot write to "{file_path}" as it is a directory')
        return 2

    while (1):
        try:
            # Fixed bug. Used target_dir for the path of the file.
            os.path.exists(target_dir)
            with open(target_dir, "w") as f:
                f.write(content)
            print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
            return
        except:
            print("Error: Couldn't write into file")
            