#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：pdfjs_darkmode.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-30 01:47
#   Description   ：
# ===============================================================================
import os
from qutescript import userscript

@userscript
def activate_dark_scheme(request, pdfjs_path = "/usr/share/javascript/pdf/"):
    """
    Modify PDF.js to always use the dark color scheme.

    Args:
        pdfjs_path (str): Path to the PDF.js directory.
    """
    viewer_html_path = os.path.join(pdfjs_path, 'web', 'viewer.html')
    custom_css = """
    <style>
        :root {
            --main-color: rgba(249, 249, 250, 1);
            --body-bg-color: rgba(42, 42, 46, 1);
            --errorWrapper-bg-color: rgba(169, 14, 14, 1);
            --progressBar-color: rgba(0, 96, 223, 1);
            --progressBar-indeterminate-bg-color: rgba(40, 40, 43, 1);
            --progressBar-indeterminate-blend-color: rgba(20, 68, 133, 1);
            --scrollbar-color: rgba(121, 121, 123, 1);
            --scrollbar-bg-color: rgba(35, 35, 39, 1);
            --toolbar-icon-bg-color: rgba(255, 255, 255, 1);
            --toolbar-icon-hover-bg-color: rgba(255, 255, 255, 1);

            --sidebar-narrow-bg-color: rgba(42, 42, 46, 0.9);
            --sidebar-toolbar-bg-color: rgba(50, 50, 52, 1);
            --toolbar-bg-color: rgba(56, 56, 61, 1);
            --toolbar-border-color: rgba(12, 12, 13, 1);
            --button-hover-color: rgba(102, 102, 103, 1);
            --toggled-btn-color: rgba(255, 255, 255, 1);
            --toggled-btn-bg-color: rgba(0, 0, 0, 0.3);
            --toggled-hover-active-btn-color: rgba(0, 0, 0, 0.4);
            --dropdown-btn-bg-color: rgba(74, 74, 79, 1);
            --separator-color: rgba(0, 0, 0, 0.3);
            --field-color: rgba(250, 250, 250, 1);
            --field-bg-color: rgba(64, 64, 68, 1);
            --field-border-color: rgba(115, 115, 115, 1);
            --treeitem-color: rgba(255, 255, 255, 0.8);
            --treeitem-hover-color: rgba(255, 255, 255, 0.9);
            --treeitem-selected-color: rgba(255, 255, 255, 0.9);
            --treeitem-selected-bg-color: rgba(255, 255, 255, 0.25);
            --sidebaritem-bg-color: rgba(255, 255, 255, 0.15);
            --doorhanger-bg-color: rgba(74, 74, 79, 1);
            --doorhanger-border-color: rgba(39, 39, 43, 1);
            --doorhanger-hover-color: rgba(249, 249, 250, 1);
            --doorhanger-hover-bg-color: rgba(93, 94, 98, 1);
            --doorhanger-separator-color: rgba(92, 92, 97, 1);
            --dialog-button-bg-color: rgba(92, 92, 97, 1);
            --dialog-button-hover-bg-color: rgba(115, 115, 115, 1);
        }

        body {
            background-color: var(--body-bg-color) !important;
            color: var(--main-color) !important;
        }
    </style>
    """

    try:
        if not os.path.exists(viewer_html_path):
            request.send_text(f"Error: viewer.html not found at {viewer_html_path}")
            return

        # Read the original viewer.html
        with open(viewer_html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Inject the custom dark scheme CSS into the <head>
        if "<head>" in html_content:
            updated_content = html_content.replace("<head>", f"<head>{custom_css}")
        else:
            request.send_text("Error: <head> tag not found in viewer.html.")
            return

        # Write the modified content back to viewer.html
        with open(viewer_html_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        #request.send_text("Dark scheme activated successfully!")
    except Exception as e:
        request.send_text(f"An error occurred: {e}")

if __name__ == "__main__":
# Usage
    # pdfjs_directory = "/usr/share/javascript/pdf/"  # Replace with the actual path to PDF.js
    activate_dark_scheme()

