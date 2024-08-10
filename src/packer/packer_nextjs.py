import os

RELEVANT_DIRS = ['app', 'components', 'lib', 'pages', 'public', 'styles', 'utils']
RELEVANT_FILES = ['next.config.js', 'package.json', 'tsconfig.json', '.env.example']
EXCLUDE_DIRS = ['.next', 'node_modules', '.git']
STRUCTURE_ONLY_DIRS = ['components/ui', 'public']

def should_include(path):
    parts = path.split(os.sep)
    if any(excluded in parts for excluded in EXCLUDE_DIRS):
        return False
    if parts[0] in RELEVANT_DIRS:
        return True
    return any(path.endswith(file) for file in RELEVANT_FILES)

def is_structure_only(path):
    return any(path.startswith(dir) for dir in STRUCTURE_ONLY_DIRS)

def get_repo_files(repo_path):
    files = []
    structure_only_files = []
    for root, dirs, filenames in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for filename in filenames:
            path = os.path.relpath(os.path.join(root, filename), repo_path)
            if should_include(path):
                if is_structure_only(path):
                    structure_only_files.append(path)
                else:
                    files.append(path)
    return sorted(files), sorted(structure_only_files)

def create_tree_structure(files, structure_only_files):
    all_files = sorted(files + structure_only_files)
    tree = "```\n"
    tree += ".\n"
    current_path = []
    for file in all_files:
        parts = file.split(os.sep)
        for i, part in enumerate(parts[:-1]):
            if i >= len(current_path):
                tree += "│   " * i + "├── " + part + "/\n"
                current_path.append(part)
            elif part != current_path[i]:
                tree += "│   " * i + "├── " + part + "/\n"
                current_path[i:] = [part]
        tree += "│   " * (len(parts) - 1) + "├── " + parts[-1] + "\n"
    tree += "```"
    return tree

def file_to_markdown(repo_path, file_path):
    full_path = os.path.join(repo_path, file_path)
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        return f"### {file_path}\n\nBinary file, content not displayed.\n\n"
    
    lang = os.path.splitext(file_path)[1][1:]  # Get extension without dot
    return f"### {file_path}\n\n```{lang}\n{content}\n```\n\n"

def repo_to_markdown(repo_path, output_file):
    files, structure_only_files = get_repo_files(repo_path)
    
    with open(output_file, 'w', encoding='utf-8') as out:
        repo_name = os.path.basename(os.path.abspath(repo_path))
        out.write(f"# Repository: {repo_name}\n\n")
        out.write("## Project Structure\n\n")
        out.write(create_tree_structure(files, structure_only_files))
        out.write("\n\n## Code Files\n\n")
        
        for file in files:
            out.write(file_to_markdown(repo_path, file))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python3 packer.py <repo_path> <output_file>")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    output_file = sys.argv[2]
    
    if not output_file.endswith('.md'):
        output_file += '.md'
    
    repo_to_markdown(repo_path, output_file)
    print(f"Markdown file '{output_file}' has been created successfully!")