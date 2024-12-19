#!/bin/bash
# ================================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：git-push.sh
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-19 00:58
#   Description   ：
# ================================================================

xargs -a ./files_to_add.txt git add

if [ -z "$1" ]; then
    git commit
else
    git commit -m "$1"
fi

git push origin master
