#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd10in85
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd10in85 Demo")
    
    epd = epd10in85.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    
    # Drawing on the Vertical image
    logging.info("Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    draw.text((2, 0), 'hello world', font = font18, fill = 0)
    draw.text((2, 20), '10.85inch e-Paper', font = font18, fill = 0)
    draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw.line((10, 90, 60, 140), fill = 0)
    draw.line((60, 90, 10, 140), fill = 0)
    draw.rectangle((10, 90, 60, 140), outline = 0)
    draw.line((95, 90, 95, 140), fill = 0)
    draw.line((70, 115, 120, 115), fill = 0)
    draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw.rectangle((10, 150, 60, 200), fill = 0)
    draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)

    logging.info("read bmp file on window")
    Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    Himage2.paste(bmp, (50,10))
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)

    # Drawing on the Horizontal image
    logging.info("Drawing on the Horizontal image. ..")
    Limage = Image.open(os.path.join(picdir, '10in85.bmp'))
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)

    epd.init()
    Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((10, 20), '10.85inch e-Paper', font = font24, fill = 0)
    draw.text((150, 0), u'微雪电子', font = font24, fill = 0)
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    # partial update
    logging.info("show time")
    epd.init_Part()
    # # If you did not use epd.display_Base_color or epd.display_Base to refresh previously, 
    # # you will need to use these two functions for a refresh, or the local brush display will be problematic
    # Himage = Image.new('1', (epd.width, epd.height), 255)
    # draw = ImageDraw.Draw(Himage)
    num = 0
    while (True):
        draw.rectangle((10, 110, 120, 150), fill = 255)
        draw.text((10, 110), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        # newimage = Himage.crop([10, 110, 120, 150])
        # Himage.paste(newimage, (10,110)) 
        epd.display_Partial(epd.getbuffer(Himage),0, 0, epd.width, epd.height)
        num = num + 1
        if(num == 10):
            break
    
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e: 
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd10in85.epdconfig.module_exit(cleanup=True)
    exit()
