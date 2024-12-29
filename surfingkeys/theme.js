const commonStyles = `
  body {
    font-family: "Input Mono", "DejaVu Sans Mono", DejaVu, Arial, sans-serif;
    font-size: 12pt;
  }

  #sk_keystroke kbd {
    font-family: "Sudo Nerd Font Mono", "Sudo Mono", "Sudo",
      "Input Mono Nerd Font", "Input Mono", "DejaVu Sans Mono", "DejaVu", "Arial",
      sans-serif;
    font-size: 10pt;
  }

  #sk_omnibarSearchArea {
    margin: 0 !important;
    padding: 0.5rem 1rem !important;
    border-bottom: none !important;
  }

  #sk_omnibarSearchResult {
    margin: 0 !important;
  }

  #sk_omnibar li {
    background: none !important;
    padding: 0.35rem 0.5rem !important;
  }

  #sk_omnibarSearchResult > ul:nth-child(1) {
    margin-bottom: 0px !important;
    padding: 0 !important;
    padding-bottom: 10px !important;
  }

  #sk_omnibar .separator {
    padding-left: 8px !important;
  }

  /* Disable RichHints CSS animation */
  .expandRichHints {
    animation: none;
  }
  .collapseRichHints {
    animation: none;
  }
`;

const lightTheme = `
  body {
    color: #483270;
  }

  #sk_omnibar {
    background-color: #f5f3fd !important;
    color: #59446f !important;
    box-shadow: 0px 3px 15px -6px rgba(53, 13, 81, 0.7) !important;
  }

  #sk_omnibar .prompt {
    color: #c2b2d7 !important;
  }

  #sk_omnibar .separator {
    color: #d4b1ff !important;
  }

  #sk_omnibar input {
    color: #351d53 !important;
  }

  #sk_omnibarSearchResult {
    border-top: 1px solid #e1cff5 !important;
  }

  #sk_omnibar li.focused {
    background-color: #e1ddff !important;
    color: #351d53 !important;
  }

  #sk_banner,
  #sk_keystroke {
    border: 1px solid #d7b0ff;
    background: #e9d9ee;
  }

  #sk_keystroke .annotation {
    color: #483270;
  }

  #sk_keystroke kbd {
    color: black;
    background: white;
  }

  #sk_keystroke kbd .candidates {
    color: #ff7a75;
  }
`;

const darkTheme = `
  body {
    color: #d7b0ff;
  }

  #sk_omnibar {
    background-color: #2a323e;
    color: #cad1d7;
  }

  #sk_omnibar .prompt {
    color: #eef5fb !important;
  }

  #sk_omnibar .separator {
    color: #8af4ff !important;
    padding-left: 8px !important;
  }

  #sk_omnibar input {
    color: white !important;
  }

  #sk_omnibarSearchResult {
    border-top: 1px solid #545f6f !important;
  }
  .sk_theme .url {
      color: #c584fd;
  }
  #sk_usage {
    background: #272f3a;
  }
color{
    color: #b876ff;
}
div.sk_tab {
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #4e4d4c), color-stop(100%, #010409));
    box-shadow: 0px 3px 7px 0px rgb(175 175 59 / 30%);
    }
.sk_theme .annotation {
    color: #9198a1;
}
.sk_theme kbd {
    background: #b9b4c9;
    color: #111;
}
  #sk_omnibar li.focused {
    background: #181d24 !important;
    color: #eef5fb !important;
  }

  #sk_banner,
  #sk_keystroke {
    border: 1px solid #d7b0ff;
    background: #483270;
  }

  #sk_keystroke .annotation {
    color: #d7b0ff;
  }

  #sk_keystroke kbd {
    color: #fff;
    background: #7a57a4;
    border: 1px solid #2d0080;
    box-shadow: none;
  }

  #sk_keystroke kbd .candidates {
    color: #ff8cf8;
  }

/* ---------- ACE Editor ---------- */
#sk_editor {
  background: var(--bg-dark) !important;
  height: 50% !important;
  /* Remove this to restore the default editor size */
}

.ace_dialog-bottom {
  border-top: 1px solid var(--bg) !important;
}

.ace-chrome .ace_print-margin,
.ace_gutter,
.ace_gutter-cell,
.ace_dialog {
  background: var(--bg) !important;
}

.ace-chrome {
  color: var(--fg) !important;
}

.ace_gutter,
.ace_dialog {
  color: var(--fg) !important;
}

.ace_cursor {
  color: var(--fg) !important;
}

.normal-mode .ace_cursor {
  background-color: var(--fg) !important;
  border: var(--fg) !important;
  opacity: 0.7 !important;
}

.ace_marker-layer .ace_selection {
  background: var(--select) !important;
}

.ace_editor,
.ace_dialog span,
.ace_dialog input {
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}
`;

const isDarkMode = typeof window !== 'undefined' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

export default commonStyles + (isDarkMode ? darkTheme : lightTheme);
