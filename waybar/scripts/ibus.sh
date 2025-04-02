#!/bin/bash

# 检测 IBus 当前输入法
get_ibus() {
    current_engine=$(ibus engine)
    case "$current_engine" in
        "xkb:us::eng") echo "⌨️ EN" ;;
        "xkd:fr::fra")      echo "⌨️ FR" ;;
        "rime")        echo "⌨️ 中州韵" ;;
        *)             echo "⌨️ $current_engine" ;;
    esac
}

# 检测 Fcitx5 当前输入法
get_fcitx5() {
    current_engine=$(fcitx5-remote -n)
    case "$current_engine" in
        "keyboard-us") echo "⌨️ EN" ;;
        "keyboard-fr")      echo "⌨️ FR" ;;
        "rime")        echo "⌨️ 中州韵" ;;
        *)             echo "⌨️ $current_engine" ;;
    esac
}

# 自动检测输入法框架
if command -v ibus &> /dev/null; then
    get_ibus
elif command -v fcitx5 &> /dev/null; then
    get_fcitx5
else
    echo "⌨️ ?"
fi
