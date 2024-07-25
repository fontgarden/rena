import math
import argparse
import drawBot as db
import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# Width, Height, Margin, Unit, Frames
W, H, M, U, F = 1080*2, 1080*2, 120, 30, 50
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
    db.stroke(0.9, 0.3, 0.0, 1)
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
    db.fill(0.05)
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
xpos = 0


# Main Text
draw_background()

db.font(MAIN_FONT_PATH)
db.fill(0.9)
db.stroke(None)
db.tracking(None)
db.fontSize(180)
db.fontVariations(opsz=144)
db.fontVariations(wght=700)
db.openTypeFeatures(dlig=False)
#db.openTypeFeatures(dlig=True)
#for axis, data in db.listFontVariations().items():
#   print((axis, data))

db.fontSize(195)
#db.fill(0.03)
#db.rect(0,0,W,U*5+1)
db.fill(0.8)
TOP_ROW = 58
db.text("abcdefghijklmnopq", (M+(U*1), M+(U*(TOP_ROW-0))), align="left")
db.text("rstuvwxyz.,:;(){}[]!?", (M+(U*1), M+(U*(TOP_ROW-7))), align="left")
db.text("ABCDEFGHIJKLMN", (M+(U*1), M+(U*(TOP_ROW-14))), align="left")
db.text("OPQRSTUVWXYZ&", (M+(U*1), M+(U*(TOP_ROW-21))), align="left")
db.text("1234567890₿", (M+(U*1), M+(U*(TOP_ROW-28))), align="left")
db.text("ÁĂÂÄÀĀÅÃ", (M+(U*1), M+(U*(TOP_ROW-35))), align="left")
db.text("áăâäàāåã", (M+(U*1), M+(U*(TOP_ROW-42))), align="left")
db.text("áăâäàāåã", (M+(U*1), M+(U*(TOP_ROW-49))), align="left")
db.text("+−×÷=<>", (M+(U*1), M+(U*(TOP_ROW-56))), align="left")
#db.text("Bahá’í Faith", (M+(U*0), M+(U*12)), align="left")
#db.text("Eli Heuer", (M+(U*0), M+(U*2)), align="left")

db.saveImage(args.output)
print("DrawBot: Done\n")

