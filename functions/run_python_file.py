import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs speicifc python file with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file_path of the python file that will run and return the received output",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="optional arguments to give",
            ),
        },
        required=["file_path"]
    ),
)

def run_python_file(working_directory, file_path, args=None):
            
    working_dir_abs = os.path.abspath("calculator")
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(target_dir) == False:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if file_path.endswith('.py') == False:
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_dir]
    if not args:
        pass
    else:
        command.extend(args)
    try:
        output_parts = []
        result = subprocess.run(command, cwd=working_dir_abs , capture_output=True, text=True, timeout=30)
        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.returncode != 0:
                output_parts.append(f"Process exited with code {result.returncode}")
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")
        output = "\n".join(output_parts)
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
