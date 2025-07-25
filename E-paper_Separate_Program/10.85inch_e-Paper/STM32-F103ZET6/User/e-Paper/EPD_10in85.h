/*****************************************************************************
* | File      	:   EPD_10in85.h
* | Author      :   Waveshare team
* | Function    :   10.85inch e-paper
* | Info        :
*----------------
* |	This version:   V1.0
* | Date        :   2024-08-19
* | Info        :
* -----------------------------------------------------------------------------
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
******************************************************************************/
#ifndef __EPD_10in85_H_
#define __EPD_10in85_H_

#include "DEV_Config.h"


// Display resolution
#define EPD_10in85_WIDTH       1360/2
#define EPD_10in85_HEIGHT      480

void EPD_10in85_Init(void);
void EPD_10in85_Init_Part(void);
void EPD_10in85_Init_GUI(void);
void EPD_10in85_Clear(void);
void EPD_10in85_Clear_Black(void);
void EPD_10in85_Display(const UBYTE *Image);
void EPD_10in85_Display2(const UBYTE *Image);
void EPD_10in85b_Display_Partial(const UBYTE *Image, UWORD Xstart, UWORD Ystart, UWORD Xend, UWORD Yend);
void EPD_10in85_Sleep(void);


#endif
