# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '知识库'
copyright = '2025, wenjinglin'
author = 'wenjinglin'
release = 'v1'

source_suffix = '.md'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 控制导航栏显示（可选）
html_theme_options = {
    "logo_only": False,           # 仅显示 Logo，隐藏项目名
    "collapse_navigation": False, # 自动折叠导航栏
    "style_external_links": True, # 为外部链接添加图标
    "navigation_depth": 4,        # 导航栏深度（显示子标题层级）
    "display_version": True,      # 显示当前版本
}


# 设置网站 Logo
# html_logo = "path/to/logo.png"

# 设置网站图标（Favicon）
# html_favicon = "path/to/favicon.ico"


