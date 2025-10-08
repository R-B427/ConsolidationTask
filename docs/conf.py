# confy.py - Sphinx configuration for EchoPulse

import os
import sys


# -- Path setup
# Add the project root to sys.path (adjust relative path if needed)
sys.path.insert(0, os.path.abspath('..'))

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'echopulse.settings'

# Setup Django
import django
django.setup()

# -- Project information
project = 'EchoPulse'
author = 'Ruben Brown'
copyright = '2025, Ruben Brown'
release = '1'

# -- General configuration -
# Extensions
extensions = [
    'sphinx.ext.autodoc',    # Pull docstrings from Python modules
    'sphinx.ext.napoleon',   # Support Google/NumPy style docstrings
    'sphinx.ext.viewcode',   # Add links to source code
    'sphinx.ext.intersphinx',# Optional: link to Python docs or other projects
]

# Paths for templates
templates_path = ['_templates']

# Patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Autodoc options
autodoc_member_order = 'bysource'    # List members in order they appear in code
autodoc_typehints = 'description'    # Show type hints in descriptions
autodoc_inherit_docstrings = True    # Include inherited docstrings

# -- Napoleon settings
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True

# Optional: link to Python documentation (if using intersphinx)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'django': ('https://docs.djangoproject.com/en/4.2/', None),
}