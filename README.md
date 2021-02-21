# e-inkDisplay
Python app to display text and images on Waveshare 2.7inch e-ink HAT module for Raspberry Pi.
Tested using a RaspberryPi 3 Model B, running [Raspberry Pi OS 32-bit (Kernel Version 5.4)](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit) and python 3.7.3.

The sample app can by run by executing:
`sudo python3 examples/sample_app.py`

# Raspberry Pi Setup

## Enable SPI interface:
- `sudo raspi-config`
- Choose Interfacing Options -> SPI -> Yes  to enable SPI interface
- `sudo reboot`

## Install BCM2835 libraries
- `wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz`
- `tar zxvf bcm2835-1.60.tar.gz`
- `cd bcm2835-1.60/`
- `sudo ./configure`
- `sudo make`
- `sudo make check`
- `sudo make install`

## Install wiringPi libraries
- `sudo apt-get install wiringpi`

## Install Python libraries
- `sudo apt-get update`
- `sudo apt-get install python3-pip`
- `sudo apt-get install python3-pil`
- `sudo apt-get install python3-numpy`
- `sudo pip3 install RPi.GPIO`
- `sudo pip3 install spidev`

# Links
[WaveShare Wiki](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT)
