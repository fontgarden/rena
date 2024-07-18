# Run this script from the root level of the Rena git repository. For example:
# $ git clone https://github.com/fontgarden/rena && cd rena
# $ python3 documentation/images/pre-alpha/wip-001.py --output documentation/images/pre-alpha/wip-001.png


import math
import argparse
import drawBot as db
import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 1080, 1920, 20, 20, 50
MAIN_FONT_PATH = "fonts/RenaVF.ttf"
MAIN_TEXT_OPSZ = 144
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d-%m-%Y")
GRID_VIEW = False


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


# FontTools docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    db.stroke(1, 1, 1, 0.125)
    db.strokeWidth(2)
    step_x = 0
    step_y = 0
    increment_x, increment_y = U, U
    db.rect(M, M, W - (M * 2), H - (M * 2))
    for x in range(49):
        db.polygon((M + step_x, M), (M + step_x, H - M))
        step_x += increment_x
    for y in range(49):
        db.polygon((M, M + step_y), (W - M, M + step_y))
        step_y += increment_y
    db.stroke(1, 0, 0, 0.5)
    db.fill(None)
    db.polygon((W / 2, 0), (W / 2, H))
    db.polygon((0, H / 2), (W, H / 2))
    #db.rect(M, M+(U*8), W-(M*2), H-(M*2)-(U*16))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Transformed Sin
def t_sin(x):
    return (math.sin(x) + 1) / 2


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
TEXT_001 = "Font.Garden"


# Main Animation Loop
#for frame in range(6):
for frame in range(F-1):
    # Main Text
    draw_background()
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

    #varWght = remap(pt.easeInOutQuint(step),0,1,400,700)
    #varWght = remap(pt.easeInOutExpo(step),0,1,400,700)
    #varWght = remap(pt.linear(step),0,1,400,700)
    #varWght = remap(pt.easeInOutCubic(step),0,1,400,700)
    varWght = remap(t_sin(step),0,1,400,700)
    if varWght >= 699:
        varWght = 700
    db.fontVariations(wght=varWght)
    print("varWght =", varWght)
    print("step =", step)
    print(" ")


    ypos = 86
    r,g,b = 0.5,0.5,0.2
    for i in range(12): 
        db.fill(r,g,b)
        db.text(TEXT_001, (W/2, M+(U*ypos)), align="center")
        ypos -= 7.75
        r -= 0.02
        g += 0.02
        b -= 0.02


    if step >= 1:
        phase += 1
    else:
        pass

    if phase == 0:
        step += 0.04

    if phase == 1:
        step -= 0.04


    # Auxillary text
    #db.fill(0.5)
    db.fontSize(80)
    db.fontVariations(opsz=14)
    #db.text("font.garden/rena", (M-(U*0.1), M+(U*0)))
    #db.text("Open Font License OFL v1.1", (M+(U*31), M+(U*0)))
    #db.text(f"Rena: opsz: {MAIN_TEXT_OPSZ} wght: {int(varWght)}", (M-(U*0.1), M+(U*47)))
    #db.text(f"Rena Regular: opsz {MAIN_TEXT_OPSZ}", (M-(U*0.1), M+(U*47)))
    #db.text(f"Pre-Alpha: ce23b9c {FORMATTED_DATE}", (M+(U*28.25), M+(U*47)))

    # Horizontal divider lines
    db.stroke(1, 1, 1, 1.0)
    #db.stroke(0.5)
    db.strokeWidth(8)
    #db.polygon((M, M+(U*2)), (W-M, M+(U*2)))
    #db.polygon((M, M+(U*46)), (W-M, M+(U*46)))


db.saveImage(args.output)
print("DrawBot: Done\n")

