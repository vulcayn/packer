import os

def get_repo_files(repo_path):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for filename in filenames:
            if not filename.startswith('.') and not 'node_modules' in root:
                files.append(os.path.relpath(os.path.join(root, filename), repo_path))
    return sorted(files)

def create_tree_structure(files):
    tree = "```\n"
    tree += ".\n"
    current_path = []
    for file in files:
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
    files = get_repo_files(repo_path)
    
    with open(output_file, 'w', encoding='utf-8') as out:
        repo_name = os.path.basename(os.path.abspath(repo_path))
        out.write(f"# Repository: {repo_name}\n\n")
        out.write("## Project Structure\n\n")
        out.write(create_tree_structure(files))
        out.write("\n\n## Code Files\n\n")
        
        for file in files:
            out.write(file_to_markdown(repo_path, file))