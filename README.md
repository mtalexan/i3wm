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