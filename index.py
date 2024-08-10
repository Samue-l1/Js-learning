import os

def generate_directory_structure(directory):
    structure = []

    for root, dirs, files in os.walk(directory):
        # Exclude the .git directory
        dirs[:] = [d for d in dirs if d != '.git']

        # Build the directory path
        path_parts = root.replace(directory, '').strip(os.sep).split(os.sep)
        indent = '    ' * len(path_parts)
        if dirs or files:
            structure.append(f'{indent}- **[{os.path.basename(root)}]**')

        # Add Markdown files within this directory
        for f in files:
            if f.endswith('.md'):
                file_indent = '    ' * (len(path_parts) + 1)
                structure.append(f'{file_indent}- {f}')

    return '\n'.join(structure)

directory = '.'  # Replace with the path to your directory
structure = generate_directory_structure(directory)
output = f'# Directory Structure\n\n{structure}'

with open('help.md', 'w') as f:
    f.write(output)

print(output)
