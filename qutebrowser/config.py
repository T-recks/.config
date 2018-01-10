# General
c.editor.command = ["urxvt", "-e", "vim", "-f", "{}"]
c.downloads.location.directory = '~/Downloads'
c.completion.height ="30%"
c.tabs.last_close = 'blank'
c.url.start_pages = ['file:///home/tim/.config/qutebrowser/start.html']

# Bindings
config.bind('J', 'tab-prev', mode='normal')
config.bind('K', 'tab-next', mode='normal')
config.bind('d', 'scroll-page 0 0.5', mode='normal')
config.bind('u', 'scroll-page 0 -0.5', mode='normal')
config.bind('<Ctrl-D>', 'tab-close', mode='normal')
config.bind('<Ctrl-U>', 'undo', mode='normal')
config.bind('<Escape>', 'leave-mode', mode='passthrough')

config.bind(';q', 'quit')
config.bind(';W', 'session-save')
config.bind(';wq', 'quit --save')
config.bind(',h', ':help')
config.bind(',gg', ':open github.com')
config.bind(',gG', ':open -t github.com')
config.bind(',gr', ':open reddit.com')
config.bind(',gR', ':open -t reddit.com')
config.bind(',gy', ':open youtube.com')
config.bind(',gY', ':open -t youtube.com')

# Aliases
c.aliases['gh'] = 'open -t https://github.com'

# Search
c.url.searchengines['w'] = 'https://en.wikipedia.org/w/?search={}'
c.url.searchengines['wt'] = 'https://en.wiktionary.org/w/?search={}'
c.url.searchengines['aw'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['dw'] = 'https://wiki.debian.org/FrontPage?action=fullsearch&value={}'
c.url.searchengines['gw'] = 'https://wiki.gentoo.org/?search={}'
c.url.searchengines['ow'] = 'https://orthodoxwiki.org/?search={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}'
c.url.searchengines['go'] = 'https://google.com/search?q={}'
#c.url.searchengines['g/'] = 'https://github.com/{}/{}'
c.url.searchengines['r'] = 'https://reddit.com/r/{}'
c.url.searchengines['ru'] = 'https://reddit.com/user/{}'
c.url.searchengines['4'] = 'https://4chan.org/{}'
c.url.searchengines['y'] = 'https://youtube.com/results?search_query={}'
c.url.searchengines['yt'] = 'https://youtube.com/results?search_query={}'
c.url.searchengines['t'] = 'https://twitter.com/{}'
c.url.searchengines['a'] = 'https://www.amazon.com/s/?field-keywords={}'
c.url.searchengines['e'] = 'https://www.ebay.com/sch/i.html?_nkw={}'
