# 用于描述 Sphinx 文档的配置文件
#
# 配置的变量，可以查看下面的文档：
# https://sphinx-doc.cn/en/master/usage/configuration.html

# -- 项目信息 -----------------------------------------------------
# 具体格式，查看网页：
# https://sphinx-doc.cn/en/master/usage/configuration.html#project-information

project = 'wenjinglin\'s blog' # 网页的主题
copyright = '2025, wenjinglin'
author = 'wenjinglin' # 作者
release = 'v1' # 版本号

# -- 常规配置 ---------------------------------------------------
# 具体格式，查看网页：
# https://sphinx-doc.cn/en/master/usage/configuration.html#general-configuration

# 添加支持的扩展
extensions = [
    'recommonmark', # markdown文件支持
    'sphinx_markdown_tables', # markdown表格支持
]

# 整个文档书的根
master_doc = 'index' # index.md 作为根

# 源文件编码
source_encoding = 'utf-8'

# 源文件后缀
source_suffix = {
    '.md':'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- HTML 输出选项 -------------------------------------------------
# 具体格式，查看网页：
# https://sphinx-doc.cn/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # html 主题

# 主题对应的配置，sphinx_rtd_theme 可以配置：
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
# https://sphinx-locales.github.io/sphinx_rtd_theme/zh-CN/configuring.html
html_theme_options = {
    'collapse_navigation': False,           # 导航条目可以扩展 
    'navigation_depth': 5,                  # 目录树的最大深度（显示子标题层级）
    'sticky_navigation': True,              # 当你滚动页面时，导航与主页面内容一起滚动
    'includehidden': True,                  # 包含隐藏项
    'style_external_links': True,           # 为外部链接添加图标
    'prev_next_buttons_location': 'bottom', # 显示 Next 和 Previous 按钮的位置
    'style_external_links': True,           # 在外部链接旁边添加一个图标
    'logo_only': False,                     # 仅显示 Logo，隐藏项目名
    'display_version': True,                # 显示当前版本
}

# 自定义的 JS 文件
html_static_path = ['_static'] # 自定义的 JS 目录
html_js_files = [] # 自定义的 JS 文件名

# 设置网站 Logo
# html_logo = "path/to/logo.png"

# 设置网站图标（Favicon）
# html_favicon = "path/to/favicon.ico"