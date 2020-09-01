# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
sys.path.append(os.path.abspath("./_ext"))
import sphinx_ecolage_theme

# -- Project information -----------------------------------------------------

project = 'Ecolage : Mathématiques 6h'
copyright = '2020, Benoit Jadin, Dany Legrand, Juliette Krug, Marine Branders'
author = 'Benoit Jadin, Dany Legrand'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.tikz', 'sphinx.ext.imgmath','syllabus_directives','youtube','sphinx_ecolage_theme']
imgmath_add_tooltips = False
imgmath_latex_preamble = '''
\\usepackage[utf8]{inputenc}
\\usepackage{gensymb}
'''
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

tikz_proc_suite = 'pdf2svg'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'

html_theme_options = {
    
    'bootswatch_theme' : "yeti"
    #'navbar_links': [
    #        ("{% if logged_in is not none %}Log out ({{ logged_in['username'] }}){% else %}Log in{% endif %}", "{% if logged_in is not none %}/logout{% else %}/login{% endif %}", True),
    #    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = sphinx_ecolage_theme.get_html_theme_path()
