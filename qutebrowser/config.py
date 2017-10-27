# General
c.editor.command = ["urxvt", "-e", "vim", "-f", "{}"]
c.downloads.location.directory = '~/Downloads'
c.completion.height ="30%"

# Bindings
config.bind('J', 'tab-prev', mode='normal')
config.bind('K', 'tab-next', mode='normal')
config.bind('d', 'scroll-page 0 0.5', mode='normal')
config.bind('u', 'scroll-page 0 -0.5', mode='normal')
config.bind('<Ctrl-D>', 'tab-close', mode='normal')
config.bind('<Ctrl-U>', 'undo', mode='normal')
config.bind('<Escape>', 'leave-mode', mode='passthrough')

# Search
c.url.searchengines['w'] = 'https://en.wikipedia.org/w/?search={}'
c.url.searchengines['wt'] = 'https://en.wiktionary.org/w/?search={}'
c.url.searchengines['aw'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['dw'] = 'https://wiki.debian.org/FrontPage?action=fullsearch&value={}'
c.url.searchengines['gw'] = 'https://wiki.gentoo.org/?search={}'
c.url.searchengines['ow'] = 'https://orthodoxwiki.org/?search={}'
c.url.searchengines['g'] = 'https://github.com/search?q={}'
#c.url.searchengines['g/'] = 'https://github.com/{}/{}'
c.url.searchengines['r'] = 'https://reddit.com/r/{}'
c.url.searchengines['4'] = 'https://4chan.org/{}'
c.url.searchengines['y'] = 'https://youtube.com/results?search_query={}'
c.url.searchengines['t'] = 'https://twitter.com/{}'
