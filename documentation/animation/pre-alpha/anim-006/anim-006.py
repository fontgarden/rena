import math
import argparse
import drawBot as db
import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 1080, 1080, 60, 60, 50
# W, H, M, U, F = 1080, 1080, 40, 40, 50
MAIN_FONT_PATH = "fonts/RenaVF.ttf"
MAIN_TEXT_OPSZ = 144
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d-%m-%Y")
GRID_VIEW = True


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


# FontTools docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    db.stroke(0.9, 0.0, 0.0, 1)
    db.strokeWidth(1)
    step_x = 0
    step_y = 0
    increment_x, increment_y = U, U
    db.rect(M, M, W - (M * 2), H - (M * 2))
    for x in range(16):
        db.polygon((M + step_x, M), (M + step_x, H - M))
        step_x += increment_x
    for y in range(30):
        db.polygon((M, M + step_y), (W - M, M + step_y))
        step_y += increment_y
    db.stroke(0.9, 0.0, 0.0, 1.0)
    db.fill(None)
    db.polygon((W / 2, 0), (W / 2, H))
    db.polygon((0, H / 2), (W, H / 2))



# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# For looping animations
def sin_loop(x):
    # Scale the input to the range [0, 2π] and shift by -π/2
    scaled_input = 2 * math.pi * (x % 1) - (math.pi / 2)
    # Calculate the sine of the scaled input
    return (math.sin(scaled_input) + 1) / 2


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    db.newPage(W, H)
    db.fill(0.025)
    db.fill(0.03)
    db.rect(-2, -2, W + 2, H + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Set font and style before animation
varWght = 0
#step = -1
step = 0
phase = 0
r,g,b = 0.75,0.75,0.75
TEXT_001 = "Font.Garden"
xpos = 0


# Main Animation Loop
#for frame in range(6):
for frame in range(F-1):
    # Main Text
    draw_background()
    
    db.fill(None)
    db.stroke(1,0,0)
    #db.rect(0,420,1080,1080)

    db.fill(0.975)
    db.fill(0.9)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.tracking(None)
    #for axis, data in db.listFontVariations().items():
    #   print((axis, data))
    
    db.fontSize(180)
    db.openTypeFeatures(dlig=True)
    db.fontVariations(opsz=MAIN_TEXT_OPSZ)
    db.fontVariations(wght=700)
    #db.text("Mark Tobey", (M+(U*0), M+(U*38)-(U*2)))
    db.openTypeFeatures(dlig=False)

    ypos = remap(pt.easeInOutExpo(sin_loop(step)),0,1,1035,1440)
    xpos = remap(pt.easeInOutExpo(sin_loop(step)),0,1,345,720)
    
    varWght = remap(pt.easeInOutQuart(sin_loop(step)),0,1,400,700)
    if varWght >= 699:
        varWght = 700
    db.fontVariations(wght=varWght)
    
    db.fontSize(910)
    db.text("&", (M+(U*8.1), M+(U*2)), align="center")

    xpos += 0.02    
    step += 0.02

    # Auxillary text
    #db.fill(0.5)
    db.fontSize(32)
    db.fill(0.25)
    db.fill(1.0,0.4,0)
    db.fontVariations(opsz=64)
    db.fontVariations(wght=400)
    db.text("Website: font.garden/rena", (M-(U*0.1), M+(U*0)))
    db.text("License: OFL v1.1", (M+(U*10.75), M+(U*0)))
    db.text(f"Rena U+0026: Weight: {int(varWght)}", (M-(U*0.1), M+(U*15)))
    db.text(f"Pre-Alpha: {FORMATTED_DATE}", (M+(U*9), M+(U*15)))

    # Horizontal divider lines
    db.stroke(1, 1, 1, 1.0)
    #db.stroke(0.5)
    db.strokeWidth(4)
    #db.polygon((M, M+(U*1)), (W-M, M+(U*1)))
    #db.polygon((M, M+(U*15)), (W-M, M+(U*15)))


db.saveImage(args.output)
print("DrawBot: Done\n")

