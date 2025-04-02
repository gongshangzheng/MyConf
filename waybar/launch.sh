#!/bin/bash
# 检测屏幕并启动对应实例
killall waybar
PRIMARY=$(hyprctl monitors -j | jq -r '.[] | select(.focused) | .name')
SECONDARY=$(hyprctl monitors -j | jq -r '.[] | select(.focused == false) | .name')
# 启动主屏Waybar
WAYBAR_OUTPUT=$PRIMARY waybar -c ~/.config/waybar/config.primary &

# 启动副屏Waybar
WAYBAR_OUTPUT=$SECONDARY waybar -c ~/.config/waybar/config.secondary &
