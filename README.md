For locking:
1. Install either xscreensaver or light-locker
  a. light-locker only if you're using lightdm instead of gdm
2. Update the config to uncomment the key combo and the startup for the one you're using (light-locker vs xscreensaver)

Light-Locker will simply use the lightdm login screen, configure it accordingly.

xscreensaver is configured via xscreensaver-demo

Built-in widgets:
1. Power icon in the taskbar is available thru xfce4-power-manager if the xfce4-power-manager-settings enables the taskbar option
2. Bluetooth is available in the taskbar with the blueman-applet
2.a. For bluetooth to work, bluetoothctl also has to be running
3. Volume can also be provided with pasystray on xfce4 or gallium

Rofi:
sudo apt-get install rofi

Configuration should already be setup independently.  Useful for window selection menu, runner, etc

quickswitch-for-i3:
This is like a rofi alternative for just interacting with windows and workspaces.  It greatly extends
the functionality of what can be done in i3.

It requires i3-py to be installed from pip (Python 2.7) or pip3 (Python 3.2.3)

i3-easyfocus:
Configured by modifying the src/config.h file directly.

Requires i3ipc-glib which is in a new repo.

sudo add-apt-repository ppa:aacebedo/libi3ipc-glib
sudo apt-get update
sudo apt-get install libi3ipc-glib

And some development header dependencies:
sudo apt-get install libjson-glib-dev libglib2.0-dev libxcb1-dev libxcb-keysyms1-dev

It's configured via the src/config.h file.  An pre-configured one prefering home-row keys, a better font, and the Return key for exiting without selection is provided as i3-easyfocus-config.h that can be copied:

cp i3-easyfocus-config.h i3-easyfocus/src/config.h