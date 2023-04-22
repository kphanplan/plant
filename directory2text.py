import os

def list_files(startpath, max_depth=2, exclude_dirs=['.git']):
    text_output = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level > max_depth:
            continue

        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        indent = ' ' * 4 * (level)
        text_output += f"{indent}{os.path.basename(root)}\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith('.py'):
                text_output += f"{subindent}{f}\n"
    return text_output

project_directory = os.path.dirname(os.path.realpath(__file__))
text_representation = list_files(project_directory)

with open("project_structure.txt", "w") as text_file:
    text_file.write(text_representation)

print("Project structure saved to project_structure.txt")