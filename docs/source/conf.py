# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# Add the project root to sys.path (adjust relative path if needed)
sys.path.insert(0, os.path.abspath('../..'))

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'echopulse.settings'

# Setup Django
import django
django.setup()


# -- Project information -----------------------------------------------------
project = 'EchoPulse'
author = 'Ruben Brown'
copyright = '2025, Ruben Brown'
release = '1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # optional for Google/NumPy style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
