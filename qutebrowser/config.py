
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
import subprocess
import os
from qutebrowser.api import interceptor
import sys
import theme

# ================== Theme ======================= {{{

config.load_autoconfig()

# load your autoconfig, use this, if the rest of your config is empty!
# config.load_autoconfig()

# set the flavor you'd like to use
# valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
# last argument (optional, default is False): enable the plain look for the menu rows
theme.setup(c, 'mocha', True)

c.content.user_stylesheets = ['~/.config/qutebrowser/css/mocha-all-sites.css']
config.bind('<Ctrl-R>', 'config-cycle content.user_stylesheets "~/.config/qutebrowser/css/apprentice-all-sites.css" "~/.config/qutebrowser/css/darculized-all-sites.css" "~/.config/qutebrowser/css/gruvbox-all-sites.css" "~/.config/qutebrowser/css/solarized-dark-all-sites.css" "~/.config/qutebrowser/css/solarized-light-all-sites.css" "~/.config/qutebrowser/css/mocha-all-sites.css" "~/.config/qutebrowser/css/latte-all-sites.css"')

config.bind('<t><t>', 'set colors.webpage.darkmode.enabled true')
config.bind('<t><f>', 'set colors.webpage.darkmode.enabled false')

if sys.platform.startswith('darwin'):
    editor.command = ["mvim", "-f", "{file}", "-c", "normal {line}G{column0}1"]
    editor_value = "mvim"
else:
    editor_value = "gvim" # or "gvim"
    # editor_value,
    c.editor.command = [
        "gvim",
        "-f",
        "{file}",
        "-c",
        "normal {line}G{column0}1",
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
# }}}
# ====================== Special Format Yanking =========== {{{
config.bind("<y><o>", "yank inline [[{url}][{title}]]")
# }}}
# ====================== Open Notes From Qutebrowser ====== {{{

#``os.environ["TERMINAL"] + " -e " +
# }}}

# ======================= Redline Insert Mode ============= {{{
# Awesome way to open vim from qutebrowser
#

config.bind(",m", "spawn umpv {url}")
config.bind("<c><s>", "config-source")
config.bind("<Ctrl-i>", "edit-text")
config.bind(",M", "hint links spawn umpv {hint-url}")
config.bind(";M", "hint --rapid links spawn umpv {hint-url}")
config.bind("<Ctrl-h>", "fake-key <Backspace>", "insert")
config.bind("<Ctrl-a>", "fake-key <Home>", "insert")
config.bind("<Ctrl-e>", "fake-key <End>", "insert")
config.bind("<Ctrl-b>", "fake-key <Left>", "insert")
config.bind("<Mod1-b>", "fake-key <Ctrl-Left>", "insert")
config.bind("<Ctrl-f>", "fake-key <Right>", "insert")
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

# insert wandering
config.bind("e", "scroll-page 0 -0.5", "normal")
config.bind("d", "scroll-page 0 0.5", "normal")
config.bind("s", "scroll down", "normal")
config.bind("w", "scroll up", "normal")
config.bind("x", "tab-close", "normal")
config.bind("X", "undo", "normal")
# config.bind("<Ctrl-s>", "scro
config.bind("<Alt-x>", "cmd-edit", "normal")

config.bind("ab", "open -t http://16.171.150.115:9090/bookmarks/new?url={url}")
config.bind("gr", "open -t http://87.106.191.101:181/public.php?op=bookmarklets--subscribe&&feed_url={url}")
config.bind("gc", "config-edit")
config.bind("ge", "edit-text")
config.bind("D", "quickmark-load kill-element")
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind("<Ctrl+g>", "fake-key <Esc>")
# config.bind("<Space>bd", "cmd-edit")
config.bind("gz", "zotero")
config.bind("gs", "doi")
config.bind("\\f", "spawn firefox {url}")
config.bind("\\m", "quickmark-load mainonly")
config.bind("\\t", "quickmark-load translate")
config.bind("<Ctrl+r>", "quickmark-load roam")
config.bind("<Ctrl-r>", "open javascript:location.href='org-protocol://roam-ref?template=r&ref='+encodeURIComponent(location.href)+'&title='+encodeURIComponent(document.title)")
with config.pattern('*://*.youtube.com/*') as p:
    config.bind('\\u', 'hint links spawn -u untrack-url -O {hint-url}')
    config.bind('\\U', 'spawn -u untrack-url -p {clipboard}')
with config.pattern('*://*.zhihu.com/*') as p:
    # p.content.images = False
    config.bind('\\k', 'quickmark-load kill-element')
    config.bind('\\c', 'quickmark-load clean-zhihu')

with config.pattern('*://*.github.com/*') as p:
    config.bind('\\g', 'spawn git clone {url} --depth=1 ~/application/')
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
             'page-performance': 'jseval javascript:window.location=\'https://developers.google.com/speed/pagespeed/insights/?url={url};\'',
             'email-personal': 'jseval javascript:(function() {  const email = "personal.xinyuzheng@gmail.com";  const dummyElement = document.createElement("textarea");  document.body.appendChild(dummyElement);  dummyElement.value = email;  dummyElement.select();  document.execCommand("copy");  document.body.removeChild(dummyElement);})();',
             'email-working': 'jseval javascript:(function() {  const email = "xinyuzheng31@gmail.com";  const dummyElement = document.createElement("textarea");  document.body.appendChild(dummyElement);  dummyElement.value = email;  dummyElement.select();  document.execCommand("copy");  document.body.removeChild(dummyElement);})();',
             'analyze-site': 'jseval javascript:(function() { var currentSite = window.location.hostname; var redirectUrl = "https://w3techs.com/sites/info/" + currentSite; window.location.href = redirectUrl; })();',
             'web2pdf': "open -t https://www.web2pdfconvert.com#{url}",
             'short-link': "open -t https://zzb.bz/bookmark/?url={url}",
}
# config.bind("<Ctrl-x><Ctrl-e>", "config-edit")
# }}}

# def redirect(info: interceptor.Request, domain, new_domain):
    # if info.request_url.host() == domain:
        # new_url = info.request_url
        # new_url.setHost(new_domain)
        # try:
            # info.redirect(new_url)
        # except interceptors.RedirectFailedException:
            # pass


# def intercept(info: interceptor.Request):
    # redirect(info, "youtube.com", "yewtu.be")
    # redirect(info, "www.youtube.com", "yewtu.be")

    # redirect(info, "twitter.com", "nitter.it")
    # redirect(info, "www.twitter.com", "nitter.it")

# interceptor.register(intercept)

# {{{ tab manager
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
# }}}
