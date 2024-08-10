# Packer

Pack the code and structure of a repo into a single markdown file to be used as context in an LLM

## Features

- Supports general repositories and Next.js projects
- Creates a structured Markdown file with:
  - Project structure overview
  - File contents in code blocks
- Excludes unnecessary files and directories (e.g., `.git`, `node_modules`)
- For Next.js projects, it includes `components/ui` in the structure but excludes their content

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/packer.git
   cd packer
   ```

2. Install the package:
   ```
   pip install .
   ```

   Or, for development:
   ```
   pip install -e .
   ```

## Usage

After installation, you can use the `packer` command from anywhere in your terminal:

```
packer <repo_type> <repo_path> <output_file>
```

- `<repo_type>`: Type of the repository. Current options are `general` or `nextjs`.
- `<repo_path>`: Path to the repository you want to pack.
- `<output_file>`: Name of the output Markdown file (`.md` extension will be added if not provided).

### Examples

For a general repository:
```
packer general /path/to/your/repo output
```

For a Next.js project:
```
packer nextjs /path/to/your/nextjs/project output
```

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.