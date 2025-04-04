#!/bin/bash
# ================================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：git-push.sh
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-19 00:58
#   Description   ：
# ================================================================

# read every lines in files_to_add.txt, if it begins with #, ignore it
# if it doesn't begin with #, add it to git

if [ -z "$1" ]; then
    git commit
else
    git commit -m "$1"
fi

git push origin master
