#!/bin/sh

# /etc/X11/xinit/xinitrc
#
# global xinitrc file, used by all X sessions started by xinit (startx)

# invoke global X session script
. /etc/X11/Xsession
#exec bspwm
# 关闭屏幕保护程序
xset s off

# 禁用 DPMS（先禁用，然后再设置开启）
xset -dpms

# 设置 DPMS 参数（5分钟无操作后屏幕关闭，单位：秒）
xset dpms 300 300 300
