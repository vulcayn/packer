import os
import subprocess

def get_repo_files(repo_path):
    os.chdir(repo_path)
    result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
    all_files = result.stdout.splitlines()
    
    # Filter out unwanted files
    ignore_list = ['.gitignore', 'LICENSE', 'README.md']
    return [f for f in all_files if f not in ignore_list and not f.startswith('.')]

def create_toc(files):
    toc = "## Project Structure\n\n"
    for file in files:
        depth = file.count('/') + 1
        filename = file.split('/')[-1]
        link = filename.replace('.', '-')
        toc += f"{'  ' * depth}- [{filename}](#{link})\n"
    return toc

def file_to_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    filename = file_path.split('/')[-1]
    lang = filename.split('.')[-1] if '.' in filename else ''
    
    return f"### {filename}\n\n```{lang}\n{content}\n```\n\n"

def repo_to_markdown(repo_path, output_file):
    files = get_repo_files(repo_path)
    
    with open(output_file, 'w') as out:
        repo_name = os.path.basename(os.path.abspath(repo_path))
        out.write(f"# Repository: {repo_name}\n\n")
        out.write(create_toc(files))
        out.write("\n## Code Files\n\n")
        
        for file in files:
            out.write(file_to_markdown(file))

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