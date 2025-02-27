
# coding=utf8
#!/usr/bin/env python
# ===============================================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：qutebrowser-config.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-16 15:58
#   Description   ：
# ===============================================================================
# import subprocess
# import os
from qutebrowser.api import interceptor
import sys
import theme
config.load_autoconfig()
"""
qutebrowser settings for video
for more settings check out
https://qutebrowser.org/doc/help/settings.html
"""

# ================== Theme ======================= {{{
"""
load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

set the flavor you'd like to use
valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
last argument (optional, default is False): enable the plain look for the menu rows
"""
theme.setup(c, 'mocha', True)

c.content.user_stylesheets = ['~/.config/qutebrowser/css/mocha-all-sites.css']
config.bind('<Ctrl-R>', 'config-cycle content.user_stylesheets "~/.config/qutebrowser/css/apprentice-all-sites.css" "~/.config/qutebrowser/css/darculized-all-sites.css" "~/.config/qutebrowser/css/gruvbox-all-sites.css" "~/.config/qutebrowser/css/solarized-dark-all-sites.css" "~/.config/qutebrowser/css/solarized-light-all-sites.css" "~/.config/qutebrowser/css/mocha-all-sites.css" "~/.config/qutebrowser/css/latte-all-sites.css"')

config.bind('<t><d>', 'set colors.webpage.darkmode.enabled true')
config.bind('<t><b>', 'set colors.webpage.darkmode.enabled false')

if sys.platform.startswith('darwin'):
    c.editor.command = ["mvim", "-f", "{file}", "-c", "normal {line}G{column0}1"]
    editor_value = "mvim"
else:
    editor_value = "neovide" # or "gvim"
    # editor_value,
    c.editor.command = [
        "neovide",
        # "--",
        "{file}",
        "+call cursor({line}, {column0})",
    ]

browser_value = "qutebrowser"

# }}}
# ================== Youtube Add Blocking ======================= {{{
def filter_yt(info: interceptor.Request):
    """Block the given request if necessary."""
    url = info.request_url
    if (
        url.host() == "www.youtube.com"
        and url.path() == "/get_video_info"
            and "&adformat=" in url.query()
    ):
        info.block()

interceptor.register(filter_yt)
# }}}
# ====================== Special Format Yanking =========== {{{
config.bind("<y><o>", "yank inline [[{url}][{title}]]")
# }}}
# ======================= Redline Insert Mode ============= {{{

config.bind(",m", "spawn umpv {url}")
config.bind("<c><s>", "config-source")
# config.bind("<Ctrl-i>", "edit-text")
config.bind(",M", "hint links spawn umpv {hint-url}")
config.bind(";M", "hint --rapid links spawn umpv {hint-url}")
config.bind("<Ctrl-h>", "fake-key <Backspace>", "insert")
config.bind("<Ctrl-a>", "fake-key <Home>", "insert")
config.bind("<Ctrl-e>", "fake-key <End>", "insert")
config.bind("<Ctrl-b>", "fake-key <Left>", "insert")
config.bind("<Mod1-b>", "fake-key <Ctrl-Left>", "insert")
config.bind("<Ctrl-f>", "fake-key <Right>", "insert")
config.bind("<Ctrl-i>", "fake-key i", "normal")
config.bind("<Mod1-f>", "fake-key <Ctrl-Right>", "insert")
config.bind("<Ctrl-p>", "fake-key <Up>", "insert")
config.bind("<Ctrl-n>", "fake-key <Down>", "insert")
config.bind("<Ctrl-f>", "fake-key <Right>")
config.bind("<Ctrl-b>", "fake-key <Left>")
config.bind("<Ctrl-p>", "fake-key <Up>")
config.bind("<Ctrl-n>", "fake-key <Down>")
config.bind("<Mod1-d>", "fake-key <Ctrl-Delete>", "insert")
config.bind("<Ctrl-d>", "fake-key <Delete>", "insert")
config.bind("<Ctrl-w>", "fake-key <Ctrl-Backspace>", "insert")
config.bind("<Ctrl-u>", "fake-key <Shift-Home><Delete>", "insert")
config.bind("<Ctrl-k>", "fake-key <Shift-End><Delete>", "insert")

# }}}
# ====================== wandering ======================= {{{

config.bind("e", "scroll-page 0 -0.5", "normal")
config.bind("d", "scroll-page 0 0.5", "normal")
config.bind("s", "scroll down", "normal")
config.bind("w", "scroll up", "normal")
config.bind("x", "tab-close", "normal")
config.bind("X", "undo", "normal")
config.bind("I", "hint inputs", "normal")
config.bind("<Alt-x>", "cmd-set-text :", "normal")

# }}}
# === open new link in new tab === {{{

config.bind("gc", "config-edit")
config.bind("ge", "edit-text")
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind("S", "back")
config.bind("D", "forward")
config.bind("<Ctrl+g>", "fake-key <Esc>")
config.bind("<Space><Space>", "cmd-set-text :")
# Open
config.unbind('o', mode='normal')
config.bind('O', 'hint links tab', mode='normal')
config.bind('oh', "history", mode='normal')
config.bind('on', "open -t", mode='normal')
config.bind('ob', "bookmark-list --jump", mode='normal')
config.bind('oo', 'cmd-set-text -s :open', mode='normal')
config.bind('go', 'cmd-set-text -s :open', mode='normal')
config.bind('gO', 'cmd-set-text -s :open -t', mode='normal')
config.bind('ot', 'cmd-set-text -s :open -t', mode='normal')
config.bind('tt', 'cmd-set-text -s :open -t', mode='normal')
config.bind(';u', 'cmd-set-text :open {url:pretty}')
config.bind('ou', 'cmd-set-text :open {url:pretty}')
# }}}
# ===================== quickmark functions ======================= {{{
config.bind("\\f", "spawn firefox {url}")
config.bind("\\m", "quickmark-load mainonly")
config.bind("\\t", "quickmark-load translate")
config.bind("gz", "zotero")
config.bind("gs", "doi")
# config.bind("<Ctrl+x>", "quickmark-load roam")
config.bind("<Ctrl+x>", "jseval -f ~/scripts/jscripts/org-roam-protocol.js")
config.bind("<Ctrl+X>", "jseval -f ~/scripts/jscripts/org-roam-protocol-temp.js")
config.bind("cb", "open -t http://87.106.191.101:9090/bookmarks/new?url={url}&auto_close")
config.bind("gr", "open -t http://87.106.191.101:181/public.php?op=bookmarklets--subscribe&&feed_url={url}")

#config.bind("<Ctrl-r>", "open javascript:location.href='org-protocol://roam-ref?template=r&ref='+encodeURIComponent(location.href)+'&title='+encodeURIComponent(document.title)")
# config.bind("D", "quickmark-load kill-element")
with config.pattern('*://*.youtube.com/*') as p:
    config.bind('\\u', 'hint links spawn -u untrack-url -O {hint-url}')
    config.bind('\\U', 'spawn -u untrack-url -p {clipboard}')
with config.pattern('*://*.zhihu.com/*') as p:
    # p.content.images = False
    config.bind('\\k', 'quickmark-load kill-element')
    config.bind('\\c', 'quickmark-load clean-zhihu')

with config.pattern('*://*.github.com/*') as p:
    config.bind('\\g', 'spawn git clone {url} --depth=1 ~/application/')

# }}}
# ===================== aliases ======================= {{{

c.aliases = {'w': 'session-save',
             'q': 'close',
             'qa': 'quit',
             'wq': 'quit --save',
             'wqa': 'quit --save',
             'zotero': 'spawn --userscript zotero',
             'doi': 'spawn --userscript doi',
             'untrack-url': 'spawn -u untrack-url -p {clipboard}',
             'tm': 'spawn -u tab-manager /sessions/ open -f',
             'meta': 'spawn --userscript script-runner.py',
             'web2pdf': "open -t https://www.web2pdfconvert.com#{url}",
             'short-link': "open -t https://zzb.bz/bookmark/?url={url}",
}

# append to the list
c.aliases['web2pdf'] = "open -t https://www.web2pdfconvert.com#{url}"
c.aliases['short-link'] = "open -t https://zzb.bz/bookmark/?url={url}"
c.aliases['page-performance'] = 'jseval javascript:window.location=\'https://developers.google.com/speed/pagespeed/insights/?url={url};\''
c.aliases['email-personal'] = 'jseval javascript:(function() {  const email = "personal.xinyuzheng@gmail.com";  const dummyElement = document.createElement("textarea");  document.body.appendChild(dummyElement);  dummyElement.value = email;  dummyElement.select();  document.execCommand("copy");  document.body.removeChild(dummyElement);})();'
c.aliases['email-working'] = 'jseval javascript:(function() {  const email = "xinyuzheng31@gmail.com";  const dummyElement = document.createElement("textarea");  document.body.appendChild(dummyElement);  dummyElement.value = email;  dummyElement.select();  document.execCommand("copy");  document.body.removeChild(dummyElement);})();'
c.aliases['analyze-site'] = 'jseval javascript:(function() { var currentSite = window.location.hostname; var redirectUrl = "https://w3techs.com/sites/info/" + currentSite; window.location.href = redirectUrl; })();'

# }}}
# =====================tab manager ======================{{{
# - general bind, to manually enter commands, flags and arguments
config.bind("zg", "set-cmd-text -s :spawn --userscript tab-manager sessions/")
# - open one or more sessions as HTML, or open index
config.bind("zo", "set-cmd-text -s :spawn --userscript tab-manager sessions/ open -f")
# - restore specified sessions, or the current open HTML file if it is a valid session
config.bind("zr", "set-cmd-text -s :spawn --userscript tab-manager sessions/ restore -f")
# - restore, same as above but close all open tabs first
config.bind("zR", "set-cmd-text -s :spawn --userscript tab-manager sessions/  restore -c -f")
# - save all and overwrite specified session (update session, don't append):
config.bind("za", "set-cmd-text -s :spawn --userscript tab-manager sessions/ save-all -o -f")
# - append current focused tab to specified session
config.bind("zs", "set-cmd-text -s :spawn --userscript tab-manager sessions/ save -f")
# - delete session
config.bind("zD", "set-cmd-text -s :spawn --userscript tab-manager sessions/ delete -f")
# - open this file
config.bind("zh", "spawn --userscript tab-manager sessions/ help")

config.bind('<Alt-1>', 'tab-focus 1', mode='insert')
config.bind('<Alt-2>', 'tab-focus 2', mode='insert')
config.bind('<Alt-3>', 'tab-focus 3', mode='insert')
config.bind('<Alt-4>', 'tab-focus 4', mode='insert')
config.bind('<Alt-5>', 'tab-focus 5', mode='insert')
config.bind('<Alt-6>', 'tab-focus 6', mode='insert')
config.bind('<Alt-7>', 'tab-focus 7', mode='insert')
config.bind('<Alt-8>', 'tab-focus 8', mode='insert')
config.bind('<Alt-9>', 'tab-focus -1', mode='insert')
# }}}
# ===================== custom values ======================= {{{
c.url.default_page = 'file:///home/xinyu/MyConf/tab/index.html'
c.url.start_pages = ['file:///home/xinyu/MyConf/tab/index.html']
c.tabs.background = False
# }}}
