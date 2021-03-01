# Vim Clutch

**Raspberry Pi Zero W**

( Raspberry Pi 0 Wireless, Wi-Fi / Bluetooth )

( Tested v1.1 2016 )

## Setting up Pi Zero 1-Cable USB
### The quick way (No USB keyboard, mouse, HDMI monitor or adapters needed)    

**More details** - [http://blog.gbaman.info/?p=791](http://blog.gbaman.info/?p=791)     
    
For this method, alongside your Pi Zero, MicroUSB cable and MicroSD card, only an additional computer is required.

Windows computers must be running [Bonjour](https://support.apple.com/kb/DL999) (should be installed if iTunes or Quicktime is installed). Mac OS has Bonjour installed by default. Linux uses the Avahi Daemon. Ubuntu has it built-in, but you can check that it's running with: `sudo service avahi-daemon status`.

**1.** You'll need a microSD card reader or adapter. Plug it in. Use the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to install RaspberryPi OS onto the microSD card.

The RPi Imager can be installed on Ubuntu 20.04 with:
`sudo apt-get install rpi-imager`

**2.** Once Raspberry Pi OS is flashed, open up the boot partition (in Windows Explorer, Finder, Terminal Emulator, etc.) and add to the bottom of the `config.txt` file `dtoverlay=dwc2` on a new line, then save the file. 

On Ubuntu 20.04, the config.txt file would be located at `/media/$USER/boot/config.txt`

**3.** If using a recent release of Jessie (Dec 2016 onwards), then create a new file simply called `ssh` in the SD card as well. On Ubuntu 20.04: `sudo touch /media/$USER/boot/ssh`. By default SSH is now disabled so this is required to enable it. **Remember** - Make sure your file doesn't have an extension (like .txt etc)!    

---
THESE STEPS ARE DIFFERENT

**4.** Finally, open up the `cmdline.txt`. Be careful with this file, it is very picky with its formatting! Each parameter is seperated by a single space (it does not use newlines). Insert `modules-load=dwc2,g_ether` after `rootwait`. To compare, an edited version of the `cmdline.txt` file at the time of writing, can be found [here](http://pastebin.com/WygSaptQ).    

**5.** That's it, eject the SD card from your computer, put it in your Raspberry Pi Zero and connect it via USB to your computer. It will take up to 90s to boot up (shorter on subsequent boots). It should then appear as a USB Ethernet device. You can SSH into it using `raspberrypi.local` as the address.  
---

Setup Headless Pi:
[Setup Headless Pi 0 WiFi](https://desertbot.io/blog/setup-pi-zero-w-headless-wifi)

The Pi needs to be setup as a USB input device:
[Setup Pi 0 as Human Interface Device (HID)](https://gndtovcc.home.blog/2020/04/17/turn-your-raspberry-pi-zero-into-a-usb-keyboard-hid/comment-page-1/?unapproved=2111&moderation-hash=a6db68e6d3caa5708e7279ef30ac555a#comment-2111)

