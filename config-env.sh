#!/bin/bash
# == ==============================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：config-env.sh
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-17 20:10
#   Description   ：
# ================================================================
#cd $HOME
if [ ! -d $HOME/MyConf ]; then
    git clone https://github.com/gongshangzheng/MyConf.git
fi
if [ ! -d $HOME/.config ]; then
    mkdir $HOME/.config
fi
#cd MyConf

function fonts(){
    if [ ! -d $HOME/MyConf/fonts ]; then
        echo "There is no fonts in MyConf"
        return
    fi
    if [ ! -d $HOME/.local/share/fonts ]; then
        mkdir $HOME/.local/share/fonts
    fi
    cp $HOME/MyConf/fonts/*/*.ttf $HOME/.local/share/fonts
}
function file_to_link(){
    # get the path of the file/dir, move it to MyConf, Link it back to its path
    # if the file/dir exists, ask user if he wants to replace it

    filepath=$1
    filename=$(basename $filepath)
    if [ "$filepath" = "$filename" ]; then
        filepath="./$filename" # current dir + filename
    fi
    if [ -e $HOME/MyConf/$filename ]; then
        echo "You have already installed $filename, do you want to replace it?"
        read -p "(yes, I want to replace it/[n])" replace
        if [ "$replace" = "yes, I want to replace it" ]; then
            rm -rf $HOME/MyConf/$filename
            ln $filepath $HOME/MyConf/$filename
        fi
    else
        mv $filepath $HOME/MyConf/$filename
        ln $HOME/MyConf/$filename $filepath
    fi
}

function link_rc(){
    local source_file=$HOME/MyConf/$1
    local target_file=${2:-$HOME/$1}  # Use $2 if provided, otherwise default to $HOME/$1

    if [ ! -f "$source_file" ]; then
        echo "There is no $1 in MyConf"
        return
    fi

    if [ ! -f "$target_file" ]; then
        ln "$source_file" "$target_file"
    else
        echo "You have already installed $target_file, do you want to replace it?"
        read -p "(y/[n])" replace
        if [ "$replace" = "y" ]; then
            rm -rf "$target_file"
            ln "$source_file" "$target_file"
        elif [[ "$replace" = "n" || "$replace" = "" ]]; then
            return
        fi
    fi
}


#...

# Make the following code a function

function link_config(){
    if [ ! -d $HOME/MyConf/$1 ]; then
        echo "You have not installed $1 config"
        return
    fi
    if [ ! -d $HOME/.config/$1 ]; then
        ln -s $HOME/MyConf/$1 $HOME/.config/$1
    else
        # ask user
        echo "You have already installed $1 config, do you want to replace it?"
        read -p "(yes/[no])" replace
        if [ -z $replace ]; then
            replace="n"
        fi
        if [ "$replace"  =  "yes" ]; then
            rm -rf $HOME/.config/$1
            ln -s $HOME/MyConf/$1 $HOME/.config/$1
        fi
    fi
}


parent_path=$( cd "$(dirname "${bash_source[0]}")" ; pwd -P )
#printf "Config path: %s\n" $parent_path

cd "$parent_path"

case $1 in
    "all")
        bash $0 rcs
        bash $0 configs
        bash $0 fonts
        ;;
    rcs)
        link_rc .zshrc
        link_rc .bashrc
        link_rc .xinitrc
        link_rc .yarnrc
        link_rc .nvidia-settings-rc
        link_rc .xinputrc
        ;;
    configs)
        link_config bspwm
        link_config autokey
        link_config sxhkd
        link_config rofi
        link_config picom
        link_config mpd
        link_config keyd
        link_config alacritty
        #link_config termite
        link_config qutebrowser
        link_config polybar
        link_config shell_gpt
        ;;
    fonts)
        fonts
        ;;
    rc)
        link_rc $2 $3
        ;;
    config)
        link_config $2
        ;;
    f2l)
        file_to_link $2
        ;;
    *)
        echo "Usage: $0 [all|rcs|configs]"
        echo "Usage: $0 [rc] [file/dir] [destination]"
        echo "Usage: $0 [config] [file/dir]"
        echo "Usage: $0 f2l [file/dir]"
        ;;
esac
