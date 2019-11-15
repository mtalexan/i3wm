For i3-gaps on Ubuntu, check the installation instructions here: https://github.com/pasiegel/i3-gaps-install-ubuntu
------------------------------
Install dependencies
    sudo apt install libxcb1-dev libxcb-keysyms1-dev libpango1.0-dev libxcb-util0-dev libxcb-icccm4-dev libyajl-dev libstartup-notification0-dev libxcb-randr0-dev libev-dev libxcb-cursor-dev libxcb-xinerama0-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev autoconf xutils-dev libtool

Also, either:
    sudo apt-get install libxcb-xrm-dev
or install from source:
	mkdir tmp
	cd /tmp
	git clone https://github.com/Airblader/xcb-util-xrm
	cd xcb-util-xrm
	git submodule update --init
	./autogen.sh --prefix=/usr
	make
	sudo make install
    cd .. && rm -rf xcb-util-xrm

Then build and install i3-gaps from source (fixing any missing deps if detected):
	cd /tmp
	git clone https://www.github.com/Airblader/i3 i3-gaps
	cd i3-gaps
	git checkout gaps && git pull
	autoreconf --force --install
	rm -rf build
	mkdir build
	cd build
	../configure --prefix=/usr --sysconfdir=/etc
	make
	sudo make install
    cd .. && rm -rf i3-gaps

For locking:
------------------------------
1. Install either xscreensaver or light-locker
  a. light-locker only if you're using lightdm instead of gdm
2. Update the config to uncomment the key combo and the startup for the one you're using (light-locker vs xscreensaver)

Light-Locker will simply use the lightdm login screen, configure it accordingly.

xscreensaver is configured via xscreensaver-demo

Built-in widgets:
------------------------------
1. Power icon in the taskbar is available thru xfce4-power-manager if the xfce4-power-manager-settings enables the taskbar option
2. Bluetooth is available in the taskbar with the blueman-applet
2.a. For bluetooth to work, bluetoothctl also has to be running
3. Volume can also be provided with pasystray on xfce4 or gallium

i3 interface tools
-----------------------------
Most tools require i3ipc-glib which is in a new repo.

sudo add-apt-repository ppa:aacebedo/libi3ipc-glib
sudo apt-get update
sudo apt-get install libi3ipc-glib

quickswitch-for-i3:
-----------------------------
This is like a rofi alternative for just interacting with windows and workspaces.  It greatly extends
the functionality of what can be done in i3.

It requires i3-py to be installed from pip (Python 2.7) or pip3 (Python 3.2.3)

i3-easyfocus:
----------------------------
Configured by modifying the src/config.h file directly.

Requires i3ipc-glib which is in a new repo.

And some development header dependencies:
sudo apt-get install libjson-glib-dev libglib2.0-dev libxcb1-dev libxcb-keysyms1-dev xorg-dev

It's configured via the src/config.h file, though most settings are overridden via the command-line.

It uses xfont-terminus package

Fonts:
-----------------------------
The status bar uses icons from fonts-font-awesome package.  Install it and restart to get some of the icons
Easyfocus is configured to use fonts from the xfonts-terminus package.

notify-send
-----------------------------
Some notifications are done thru notify-send, which is part of package libnotify-bin

Misc Other packages
-----------------------------
i3status
dmenu
thunar or pcmanfm (pick one in the i3/config)
flameshot
xkill
chromium-browser or google-chrome-stable
copyq
nmapplet or nmtray or nm-applet (depending on Ubuntu version)
gnome-keyring policykit-1-gnome (optional, for credential caching)

Rofi:
-----------------------------
sudo apt-get install rofi

Configuration should already be setup independently.  Useful for window selection menu, runner, etc




