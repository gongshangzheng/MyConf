#!/bin/bash
# ================================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：current-dir.sh
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-20 22:50
#   Description   ：
# ================================================================

parent_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd -P )

echo $parent_dir
