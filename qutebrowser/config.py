###
# General
###
c.editor.command = ["urxvt", "-e", "vim", "-f", "{}"]
c.downloads.location.directory = '~/Downloads'
c.completion.height ="33%"
c.tabs.last_close = 'blank'
c.url.start_pages = ['file:///home/tim/.config/qutebrowser/start.html']

###
# Bindings
###
# Rebindings
config.bind('J', 'tab-prev', mode='normal')
config.bind('K', 'tab-next', mode='normal')
config.bind('d', 'scroll-page 0 0.5', mode='normal')
config.bind('u', 'scroll-page 0 -0.5', mode='normal')
config.bind('<Ctrl-D>', 'tab-close', mode='normal')
config.bind('<Ctrl-U>', 'undo', mode='normal')
config.bind('<Ctrl-G>', 'leave-mode', mode='command')
config.bind('<Ctrl-G>', 'leave-mode', mode='insert')
config.bind('<Ctrl-G>', 'leave-mode', mode='hint')
#config.bind('<Escape>', ':leave-mode', mode='passthrough')
# Easy access bindings
config.bind(';q', 'quit')
config.bind(',q', 'quit')
config.bind(';W', 'session-save')
config.bind(',W', 'session-save')
config.bind(';wq', 'quit --save')
config.bind(',wq', 'quit --save')
config.bind(',h', ':help')
config.bind(',H', ':open -t about:blank;;help')
# Open bindings
config.bind(',gg', ':open github.com')
config.bind(',Gg', ':open -t github.com')
config.bind(',gr', ':open reddit.com')
config.bind(',Gr', ':open -t reddit.com')
config.bind(',gy', ':open youtube.com')
config.bind(',Gy', ':open -t youtube.com')
config.bind(',ga', ':open amazon.com')
config.bind(',Ga', ':open -t amazon.com')
config.bind(',ge', ':open ebay.com')
config.bind(',Ge', ':open -t ebay.com')
config.bind(',gd', ':open duolingo.com')
config.bind(',Gd', ':open -t duolingo.com')
config.bind(',gt', ':open translate.google.com')
config.bind(',Gt', ':open -t translate.google.com')
config.bind(',gpa', ':open archlinux.org/packages')
config.bind(',Gpa', ':open -t archlinux.org/packages')
config.bind(',gpd', ':open packages.debian.org;;open packages.debian.org#search_packages')
config.bind(',Gpd', ':open -t packages.debian.org;;open packages.debian.org/#search_packages')
config.bind(',gpg', ':open packages.gentoo.org')
config.bind(',Gpg', ':open -t packages.gentoo.org')
config.bind(',gpf', ':open freebsd.org/ports')
config.bind(',Gpf', ':open -t freebsd.org/ports')
config.bind(',gmlbc', ':open my.lbcc.edu')
config.bind(',Gmlbc', ':open -t my.lbcc.edu')
# Config bindings
config.bind(',cs', ':config-source')
config.bind(',ce', ':config-edit')

###
# Aliases
###
c.aliases['gg'] = 'open -t https://github.com'

###
# Search
###
# General
c.url.searchengines['go'] = 'https://google.com/search?q={}'
# Wiki
c.url.searchengines['w'] = 'https://en.wikipedia.org/w/?search={}'
c.url.searchengines['wt'] = 'https://en.wiktionary.org/w/?search={}'
c.url.searchengines['wk'] = 'https://en.wiktionary.org/w/?search={}'
c.url.searchengines['ow'] = 'https://orthodoxwiki.org/?search={}'
	# Software Wiki
c.url.searchengines['ig'] = 'https://wiki.installgentoo.com/index.php?search={}'
	# Linux Wiki
c.url.searchengines['aw'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['dw'] = 'https://wiki.debian.org/FrontPage?action=fullsearch&value={}'
c.url.searchengines['gw'] = 'https://wiki.gentoo.org/?search={}'
	# BSD Wiki
c.url.searchengines['bw'] = 'https://wiki.freebsd.org/?action=fullsearch&value={}'
c.url.searchengines['fbw'] = 'https://wiki.freebsd.org/?action=fullsearch&value={}'
# Package Databases
c.url.searchengines['gp'] = 'https://packages.gentoo.org/packages/search?q={}'
c.url.searchengines['gpo'] = 'http://gpo.zugaina.org/Search?search={}'
# Development
c.url.searchengines['g'] = 'https://github.com/search?q={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}'
# Media
c.url.searchengines['y'] = 'https://youtube.com/results?search_query={}'
c.url.searchengines['yt'] = 'https://youtube.com/results?search_query={}'
# Social
c.url.searchengines['r'] = 'https://reddit.com/r/{}'
c.url.searchengines['ru'] = 'https://reddit.com/user/{}'
c.url.searchengines['4'] = 'https://4chan.org/{}'
c.url.searchengines['t'] = 'https://twitter.com/{}'
# Shopping
c.url.searchengines['a'] = 'https://www.amazon.com/s/?field-keywords={}'
c.url.searchengines['e'] = 'https://www.ebay.com/sch/i.html?_nkw={}'
