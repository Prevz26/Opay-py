# Configuration file for the Sphinx documentation builder.
#


# -- Project information --
project = 'Opay Python Client Libary'
copyright = '2024, Precious Ojogu'
author = 'Precious Ojogu'

# -- General configuration --
extensions = [
    'sphinx.ext.autodoc',    # For auto-generating docs from docstrings
    'sphinx.ext.napoleon',   # To support Google and NumPy-style docstrings
    'sphinx.ext.viewcode'    # Adds links to highlighted source code
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output --
html_theme = 'alabaster'
html_static_path = ['_static']
