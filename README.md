# Vim Clutch

**Raspberry Pi Zero W**

( Raspberry Pi 0 Wireless, Wi-Fi / Bluetooth )

( Tested on v1.1 2016 )

![pi_in_a_pedal](https://user-images.githubusercontent.com/23065167/119210762-11117580-ba7c-11eb-8453-3acd4dfde7e4.jpg)

## Setting up Pi Zero

### HEADLESS
#### (No USB keyboard, mouse, HDMI monitor or adapters needed)

**More details** - [http://blog.gbaman.info/?p=791](http://blog.gbaman.info/?p=791)

For this method, alongside your Pi Zero, MicroUSB cable and MicroSD card, only an additional computer is required. **Make sure your USB cable works**. I used 2 faulty cables and wasted about 4 hours going down a dead-end rabbit hole. You should use a USB cable that transfers data, and isn't used just for charging. After flashing the microSD card and connecting the Pi via USB, running `dmesg` on the host computer can help diagnose the cable.

Windows computers must be running [Bonjour](https://support.apple.com/kb/DL999) (should be installed if iTunes or Quicktime is installed). Mac OS has Bonjour installed by default. Linux uses the Avahi Daemon. Ubuntu has it built-in, but you can check that it's running with: `sudo service avahi-daemon status`. This will let you use the `raspberrypi.local` address out-of-the-box.

#### **1. Flash the microSD**
You'll need a microSD card reader or adapter. Plug it in. Use the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to install RaspberryPi OS onto the microSD card.

The RPi Imager can be installed on Ubuntu 20.04 with:
`sudo apt-get install rpi-imager`

#### **2. Edit `config.txt`**
Once Raspberry Pi OS is flashed, open up the boot partition (in Windows Explorer, Finder, Terminal Emulator, etc.) and add to the bottom of the `config.txt` file `dtoverlay=dwc2` on a new line, then save the file.

On Ubuntu 20.04, the config.txt file would be located at `/media/$USER/boot/config.txt`

#### **3. Enable SSH**
If using a recent release of Jessie (Dec 2016 onwards), then create a new file simply called `ssh` in the SD card as well. On Ubuntu 20.04: `sudo touch /media/$USER/boot/ssh`. By default SSH is now disabled so this is required to enable it. **Remember** - Make sure your file doesn't have an extension (like .txt etc)!

#### **4. Edit `modules`**
Add `dwc2` and `libcomposite` to the `modules` file. On Ubuntu 20.04, the file is at `/media/$USER/rootfs/etc/modules`. You can run:

#### **5. Boot up the Pi** That's it, eject the SD card from your computer, put it in your Raspberry Pi Zero and connect it via USB to your computer. It will take up to 90s to boot up (shorter on subsequent boots).

We didn't add `g_ether`, so is won't appear as a USB Ethernet device. Use `ssh pi@raspberrypi.local` to SSH into the Pi on your network. If you have multiple Pi's on the network, rename the existing hosts or use [Fing](https://www.fing.com/products/development-toolkit) to discover the Pi's IP address.

#### **6. Install script requirements**
Install python3-pip on your Raspberry Pi:
`sudo apt-get install python3-pip`

Install python requirements:
`sudo pip3 install -r requirements.txt`

#### **7. Execute script on boot**
Add the Python script to `rc.local` so that the pedal will work immediately upon power-up:

`sudo vim /etc/rc.local`

Then add the following line before the end of the file:
`python3 /home/pi/vim-clutch/vim-clutch.py`

#### **8. Tweak the settings**
Adjust the `sleep()` times for best results.

---

Other Useful Resources:

Setup Headless Pi:
[Setup Headless Pi 0 WiFi](https://desertbot.io/blog/setup-pi-zero-w-headless-wifi)

The Pi needs to be setup as a USB input device:
[Setup Pi 0 as Human Interface Device (HID)](https://gndtovcc.home.blog/2020/04/17/turn-your-raspberry-pi-zero-into-a-usb-keyboard-hid/comment-page-1/?unapproved=2111&moderation-hash=a6db68e6d3caa5708e7279ef30ac555a#comment-2111)

