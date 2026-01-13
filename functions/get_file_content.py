import os
import config
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The specified file path for printing content"),
        },
        required=["file_path"],
    ),
)

def get_file_content(working_directory, file_path):
    
    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return 2
    if os.path.isfile(target_dir) == False:
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return 2
    try:
        f = open(target_dir)
        content = f.read(config.MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        print(content)
    except:
        return f'Error: Could not read data from: {target_dir}'