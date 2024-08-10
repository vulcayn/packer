import sys
import importlib
import os

def ensure_md_extension(filename):
    if not filename.lower().endswith('.md'):
        return filename + '.md'
    return filename

def main():
    if len(sys.argv) != 4:
        print("Usage: packer <repo_type> <repo_path> <output_file>")
        sys.exit(1)

    repo_type = sys.argv[1]
    repo_path = sys.argv[2]
    output_file = ensure_md_extension(sys.argv[3])

    try:
        packer_module = importlib.import_module(f"packer.packer_{repo_type}")
        packer_module.repo_to_markdown(repo_path, output_file)
        print(f"Markdown file '{output_file}' has been created successfully!")
    except ModuleNotFoundError:
        print(f"Error: Packer for repo type '{repo_type}' not found.")
        print("Available repo types: general, nextjs")
        sys.exit(1)

if __name__ == "__main__":
    main()