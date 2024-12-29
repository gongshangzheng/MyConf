const commonStyles = `
/* Edit these variables for easy theme making */
:root {
  /* Font */
  --font: 'Source Code Pro', Ubuntu, sans;
  --font-size: 12;
  --font-weight: bold;

  /* -------------- */
  /* --- THEMES --- */
  /* -------------- */

  /* -------------------- */
  /* -- Tomorrow Night -- */
  /* -------------------- */
  /* -- DELETE LINE TO ENABLE THEME
  --fg: #C5C8C6;
  --bg: #282A2E;
  --bg-dark: #1D1F21;
  --border: #373b41;
  --main-fg: #81A2BE;
  --accent-fg: #52C196;
  --info-fg: #AC7BBA;
  --select: #585858;
  -- DELETE LINE TO ENABLE THEME */

  /* Unused Alternate Colors */
  /* --cyan: #4CB3BC; */
  /* --orange: #DE935F; */
  /* --red: #CC6666; */
  /* --yellow: #CBCA77; */

  /* -------------------- */
  /* --      NORD      -- */
  /* -------------------- */
  /* -- DELETE LINE TO ENABLE THEME
  --fg: #E5E9F0;
  --bg: #3B4252;
  --bg-dark: #2E3440;
  --border: #4C566A;
  --main-fg: #88C0D0;
  --accent-fg: #A3BE8C;
  --info-fg: #5E81AC;
  --select: #4C566A;
  -- DELETE LINE TO ENABLE THEME */

  /* Unused Alternate Colors */
  /* --orange: #D08770; */
  /* --red: #BF616A; */
  /* --yellow: #EBCB8B; */

  /* -------------------- */
  /* --    DOOM ONE    -- */
  /* -------------------- */
  --fg: #51AFEF;
  --bg: #2E3440;
  --bg-dark: #21242B;
  --border: #2257A0;
  --main-fg: #51AFEF;
  --accent-fg: #98be65;
  --info-fg: #C678DD;
  --select: #4C566A;

  /* Unused Alternate Colors */
  /* --border-alt: #282C34; */
  /* --cyan: #46D9FF; */
  /* --orange: #DA8548; */
  /* --red: #FF6C6B; */
  /* --yellow: #ECBE7B; */

  /* -------------------- */
  /* --    MONOKAI    -- */
  /* -------------------- */
  /* -- DELETE LINE TO ENABLE THEME
  --fg: #F8F8F2;
  --bg: #272822;
  --bg-dark: #1D1E19;
  --border: #2D2E2E;
  --main-fg: #F92660;
  --accent-fg: #E6DB74;
  --info-fg: #A6E22E;
  --select: #556172;
  -- DELETE LINE TO ENABLE THEME */

  /* Unused Alternate Colors */
  /* --red: #E74C3C; */
  /* --orange: #FD971F; */
  /* --blue: #268BD2; */
  /* --violet: #9C91E4; */
  /* --cyan: #66D9EF; */
}
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

//export default commonStyles + (isDarkMode ? darkTheme : lightTheme);
export default commonStyles + darkTheme
