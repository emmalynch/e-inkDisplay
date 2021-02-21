#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:

    epd = epd2in7.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    altFont1 = ImageFont.truetype(os.path.join(picdir, 'alt1.otf'), 40)
    altFont2 = ImageFont.truetype(os.path.join(picdir, 'alt2.ttf'), 40)
    
    # Text and Lines
    Himage = Image.new('1', (epd.height, epd.width), 255) #clear the screen, swap height & width for a portrait image
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), "Hello World", font = altFont1, fill=0)
    draw.line((5, 50, 5, 100), width = 4, fill=0)
    draw.line((epd.height - 5, 50, epd.height - 5, 100), width = 4, fill=0)
    
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    #Display image
    Himage = Image.open(os.path.join(picdir, 'example.bmp'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    #Display image at location on screen
    Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    Himage2.paste(bmp, (50,10))
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)
    
    #Display multiple images on screen
    Himage3 = Image.new('1', (epd.height, epd.width), 255)
    Himage3.paste(bmp, (5, 10))
    Himage3.paste(bmp, (epd.height - 105, 10))
    epd.display(epd.getbuffer(Himage3))
    time.sleep(2)
    
    #Greyscale
    epd.Init_4Gray()
    
    Limage = Image.new('L', (epd.height, epd.width), 0)  # Image mode L = 8-bit pixels, black and white
    draw = ImageDraw.Draw(Limage)
    draw.text((20, 0), u'Gray1', font = font35, fill = epd.GRAY1)
    draw.text((20, 50), u'Gray2', font = font35, fill = epd.GRAY2)
    draw.text((20, 100), u'Gray3', font = font35, fill = epd.GRAY3)
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)
    
    #Display Greyscale image
    Himage = Image.open(os.path.join(picdir, 'example_grey.bmp'))
    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    time.sleep(2)

    logging.info("Clear...")
    epd.Clear(0xFF)
    logging.info("Goto Sleep...")
    epd.sleep()
    time.sleep(3)
    
    epd.Dev_exit()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
