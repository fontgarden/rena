import math
import argparse
import drawBot as db
import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 1080*2, 1080*2, 120, 60, 50
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
    db.fill(None)
    db.stroke(1,0,0)
    db.strokeWidth(1)
    step_x = 0
    step_y = 0
    increment_x, increment_y = U, U
    db.rect(M, M, W - (M * 2), H - (M * 2))
    for x in range(36*2):
        db.polygon((M + step_x, M), (M + step_x, H - M))
        step_x += increment_x
    for y in range(36*2):
        db.polygon((M, M + step_y), (W - M, M + step_y))
        step_y += increment_y
    #db.stroke(0.9, 1.0, 0.0, 1.0)
    #db.fill(None)
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
    db.fill(0.05)
    db.fill(0.05)
    db.rect(-2, -2, W + 2, H + 2)
 

    im = db.ImageObject()
    with im:
        # set a size for the image
        db.size(2160*2, 2160*2)
        # draw something
        #db.fill(0.1)
        #db.rect(0, 0, 2160, 2160)
        #db.fill(0.8, 0.4, 0)
        #db.rect(0, 0, 1080*2, 1080*2)
        #db.fill(0.5, 0.0, 1.0)
        #db.rect(0, 0, 540*2, 540*2)
    im.gaussianBlur(radius=300)
    im.boxBlur(radius=100)
    #db.blendMode("color")
    db.image(im, (1000, -1500))
    db.blendMode("clear")
    
    #db.fill(0.6)
    #db.rect(-2, -2, W + 2, H + 2)

    if GRID_VIEW:
        grid()
    else:
        pass

# Main Text
draw_background()
db.font(MAIN_FONT_PATH)
db.openTypeFeatures(dlig=False)
#db.openTypeFeatures(dlig=True)
#for axis, data in db.listFontVariations().items():
#   print((axis, data))

db.stroke(None)
db.tracking(None)
db.fontVariations(wght=700)
db.fontVariations(opsz=144)
#db.tracking(-1)
MAIN_TEXT_LOOP = "Graphic Design"
#MAIN_TEXT_LOOP = "$SPOON TO THE MOON"

db.fontSize(412)
db.fill(0.0,1.0,0.3)
db.text("SPOON", (M-(U*(0.1)), M+(U*(6))), align="left")
db.image("documentation/images/pre-alpha/flux/spoonbender-001.png", (M+(U*17.45), M-(U*0.08)), alpha=1.0)
db.text("BENDER", (M-(U*(0.1)), M+(U*(0))), align="left")

db.fontSize(49)
db.fontVariations(wght=400)
db.fontVariations(opsz=14)
#db.text("https://font.garden", (M+(U*(0)), M-(U*(0.85))), align="left")
#db.text("Rena Pre-Alpha: Git-1e9127d624d48fe55b3ef", (M+(U*(8.5)), M-(U*(0.85))), align="left")

db.fontVariations(wght=700)
db.fontVariations(opsz=144)
db.fontSize(266)
db.fill(0.85)
db.tracking(-1)
START = 28.5
db.text(MAIN_TEXT_LOOP, (M-(U*(0.2)), M+(U*(START))), align="left")
db.text(MAIN_TEXT_LOOP, (M-(U*(0.2)), M+(U*(START-(4*1)))), align="left")
db.text(MAIN_TEXT_LOOP, (M-(U*(0.2)), M+(U*(START-(4*2)))), align="left")
db.text(MAIN_TEXT_LOOP, (M-(U*(0.2)), M+(U*(START-(4*3)))), align="left")
db.text(MAIN_TEXT_LOOP, (M-(U*(0.2)), M+(U*(START-(4*4)))), align="left")
db.image("documentation/images/pre-alpha/flux/spoonbender-002.png", (M+(U*7.5), M+(U*18.42)), alpha=1.0)


db.saveImage(args.output)
print("DrawBot: Done\n")

