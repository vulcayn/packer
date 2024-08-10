# Import the main modules
from . import packer
from . import packer_general
from . import packer_nextjs

# You can also expose specific functions or classes if needed
# For example:
# from .packer import main
# from .packer_general import repo_to_markdown as general_repo_to_markdown
# from .packer_nextjs import repo_to_markdown as nextjs_repo_to_markdown

# If you want to define what gets imported with "from packer import *"
__all__ = ['packer', 'packer_general', 'packer_nextjs']