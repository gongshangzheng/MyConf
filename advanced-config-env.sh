#!/bin/bash
# ================================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：create-symlink.sh
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-21 00:07
#   Description   ：Interactive symlink creator with multi/all selection
# ================================================================

# 颜色定义
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
PURPLE='\033[1;35m'
CYAN='\033[1;36m'
NC='\033[0m'

declare -A LINK_PAIRS=(
    ["bashrc"]="$HOME/MyConf/bashrc $HOME/.bashrc"
    ["zshrc"]="$HOME/MyConf/zshrc $HOME/.zshrc"
    ["keyd"]="$HOME/MyConf/keyd-default.conf /etc/keyd"
    ["mpv"]="$HOME/MyConf/mpv $HOME/.config/mpv"
    ["wofi"]="$HOME/MyConf/wofi $HOME/.config/wofi"
    ["hypr"]="$HOME/MyConf/hypr $HOME/.config/hypr"
    ["bspwm"]="$HOME/MyConf/bspwm $HOME/.config/bspwm"
    ["alacritty"]="$HOME/MyConf/alacritty $HOME/.config/alacritty"
    ["kitty"]="$HOME/MyConf/kitty $HOME/.config/kitty"
)

function create_symlink() {
    local name=$1
    local pair_info=(${LINK_PAIRS[$name]})
    local source_path=${pair_info[0]}
    local target_path=${pair_info[1]}

    echo -e "\n${BLUE}Processing: $name${NC}"
    echo "Source: $source_path"
    echo "Target: $target_path"

    # 检查源文件是否存在
    if [ ! -e "$source_path" ]; then
        echo -e "${RED}Error: Source file '$source_path' does not exist!${NC}"
        return 1
    fi

    # 处理已存在的目标
    if [ -e "$target_path" ]; then
        echo -e "${YELLOW}Warning: Target '$target_path' already exists!${NC}"
        read -p "Do you want to remove it? (y/n): " answer
        if [[ "$answer" =~ ^[Yy]$ ]]; then
            rm -rfv "$target_path"
            echo -e "${GREEN}Removed existing target.${NC}"
        else
            echo -e "${YELLOW}Skipping this link creation.${NC}"
            return 0
        fi
    fi

    # 判断是否需要sudo
    if [[ "$target_path" != "$HOME"/* ]]; then
        sudo_cmd="sudo"
        echo -e "${YELLOW}注意：目标路径在系统目录，将使用sudo${NC}"
    fi
    
    # 创建父目录
    $sudo_cmd mkdir -pv "$(dirname "$target_path")"

    # 创建符号链接
    $sudo_cmd ln -sv "$source_path" "$target_path"
    echo -e "${GREEN}Created symlink: $target_path -> $source_path${NC}"
}

# 显示帮助信息
function show_help() {
    echo -e "${CYAN}Selection Help:${NC}"
    echo -e " - ${YELLOW}TAB${NC}: Toggle multiple selection"
    echo -e " - ${YELLOW}Ctrl+A${NC}: Select all items"
    echo -e " - ${YELLOW}ESC${NC}: Clear selection"
    echo -e " - ${YELLOW}ENTER${NC}: Confirm selection\n"
}

# 获取链接名称列表
link_names=(${!LINK_PAIRS[@]})

# 显示交互界面
clear
show_help
echo -e "${PURPLE}Available symlinks to create:${NC}"
selected_links=($(printf '%s\n' "${link_names[@]}" | fzf --multi --bind 'ctrl-a:select-all+accept' --prompt="Select links (TAB: multi, Ctrl+A: all): "))

# 检查是否选择了内容
if [ ${#selected_links[@]} -eq 0 ]; then
    echo -e "${YELLOW}No selection made. Exiting.${NC}"
    exit 0
fi

# 显示确认信息
echo -e "\n${PURPLE}You have selected ${#selected_links[@]} items:${NC}"
printf ' - %s\n' "${selected_links[@]}"
echo -e "\n${CYAN}Source -> Target mappings:${NC}"
for link in "${selected_links[@]}"; do
    pair_info=(${LINK_PAIRS[$link]})
    echo -e " - ${YELLOW}${pair_info[0]}${NC} -> ${GREEN}${pair_info[1]}${NC}"
done

# 最终确认
read -p $'\n'"Proceed with creating these symlinks? (y/n): " confirm
if [[ "$confirm" =~ ^[Yy]$ ]]; then
    # 创建选中的符号链接
    for link in "${selected_links[@]}"; do
        create_symlink "$link"
    done
    echo -e "\n${GREEN}All selected symlinks processed!${NC}"
else
    echo -e "${YELLOW}Operation cancelled.${NC}"
fi
