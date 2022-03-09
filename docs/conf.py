# -- Project information -----------------------------------------------------

project = "Pegasus Tutorials"
copyright = "2020 - 2022 The Broad Institute, Inc. and Genentech, Inc. All rights reserved."
author = (
    "Yiming Yang, Joshua Gould and Bo Li"
)

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
#needs_sphinx = '1.7'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#    "sphinx.ext.autodoc",
#    "sphinx.ext.intersphinx",
#    "sphinx.ext.doctest",
#    "sphinx.ext.todo",
#    "sphinx.ext.mathjax",
#    "sphinx.ext.coverage",
#    "sphinx.ext.imgmath",
#    "sphinx.ext.ifconfig",
#    "sphinx.ext.viewcode",
#    "sphinx.ext.githubpages",
#    "sphinx.ext.autosummary",
#    "sphinx.ext.napoleon",
#    "sphinx_autodoc_typehints",
#]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"navigation_depth": 4}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_context = dict(
    display_github=True,  # Integrate GitHub
    github_user="lilab-bcb",  # Username
    github_repo="pegasus-tutorials",  # Repo name
    github_version="main",  # Version
    conf_py_path="/docs/",  # Path in the checkout to the docs root
)
