#!/bin/bash
# == ==============================================================
#   Copyright (C) 2024 www.361way.com site All rights reserved.
#
#   Filename      ：config-env.sh
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2024-12-17 20:10
#   Description   ：
# ================================================================
cd $HOME
if [ ! -d $HOME/MyConf ]; then
    git clone https://github.com/gongshangzheng/MyConf.git
fi
if [ ! -d $HOME/.config ]; then
    mkdir $HOME/.config
fi
cd MyConf

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
            ln -s $filepath $HOME/MyConf/$filename
        fi
    else
        mv $filepath $HOME/MyConf/$filename
        ln -s $HOME/MyConf/$filename $filepath
    fi
}

function link_rc(){
    if [ ！ -d $HOME/MyConf/$1 ]; then
        echo "You have not installed $1"
        return
    fi
    if [ ! -e $HOME/$1 ]; then
        ln -s $HOME/MyConf/$1 $HOME/$1
    else
        # ask user
        echo "You have already installed $1, do you want to replace it?"
        read -p "(y/[n])" replace
        if [ "$replace"  =  "y" ]; then
            rm -rf $HOME/$1
            ln -s $HOME/MyConf/$1 $HOME/$1
        elif [[ "$replace"  =  "n" || "$replace"  =  "" ]]; then
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

case $1 in
    "all")
        $0 rc
        $0 config
        ;;
    rc)
        link_rc .zshrc
        link_rc .bashrc
        link_rc .vimrc
        link_rc .xinitrc
        link_rc .yarnrc
        link_rc .nvidia-settings-rc
        link_rc .xinputrc
        ;;
    config)
        link_config bspwm
        link_config autokey
        link_config sxhkd
        link_config rofi
        link_config picom
        link_config alacritty
        #link_config termite
        link_config polybar
        link_config shell_gpt
        ;;
    f2l)
        file_to_link $2
        ;;
    *)
        echo "Usage: $0 [all|rc|config] [file/dir]"
        echo "Usage: $0 f2l [file/dir]"
        ;;
esac
