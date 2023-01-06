AUTHOR = 'Zac Bir'
SITENAME = 'Thinking and Occasionally Typing as a Service'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_CATEGORY = 'misc'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Menu items
MENUITEMS = (
    ('Mastodon', 'https://dice.camp/@zacbir'),
    ('Itch.io', 'https://zacbir.itch.io'),
    ('Geometriq', 'https://instagram.com/geometriq_studio'),
    ('Code', 'https://github.com/zacbir'),
    ('Archives', '/archives.html')
)

# Social widget
SOCIAL = ()

SUMMARY_MAX_LENGTH = None

DEFAULT_PAGINATION = 5

CATEGORIES = ()

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# AUTHOR_SAVE_AS = False
# AUTHORS_SAVE_AS = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = 'zacbir-Kiera'

# PLUGIN_PATHS = ['/Users/zbir/Dev/zacbir.net/pelican-plugins']
PLUGINS = ['liquid_tags', 'search', 'neighbors']

LIQUID_TAGS = ["img", "include_code"]

DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['code', 'images', 'static', '.well-known']

EXTRA_HEADER = '<link rel="me" href="https://dice.camp/@zacbir">'

HEADER_COVER = 'images/triangles-header.jpg'

COPYRIGHT = '2013-2022'
