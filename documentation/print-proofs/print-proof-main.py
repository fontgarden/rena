# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Unit Space: 72dpi (dots per inch)
import math
import subprocess
import argparse
import drawBot as db
import pytweening as pt
from fontTools.ttLib import TTFont
from datetime import datetime


# CONSTANTS
W = 792    # Width
H = 612   # Height
M = 36    # Margin
U = 9       # Unit
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d.%m.%Y")
MY_HASH_SHORT = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
MY_HASH = subprocess.check_output("git rev-parse --verify HEAD", shell=True).decode()
RENA_VF = "fonts/RenaVF.ttf"
GRID_VIEW = True


# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


# FontTools docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(RENA_VF)


# Draws a grid
def grid():
    db.stroke(1, 0, 0, 0.5)
    db.strokeWidth(0.5)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = M/2, M/2
    db.rect(M, M, W-(M*2), H-(M*2))
    for x in range(41):
        db.polygon((M+STEP_X, M), (M+STEP_X, H-M))
        STEP_X += INCREMENT_X
    for y in range(31):
        db.polygon((M, M+STEP_Y), (W-M, M+STEP_Y))
        STEP_Y += INCREMENT_Y
    db.polygon((W/2, 0), (W/2, H))
    db.polygon((0, H/2), (W, H/2))


# Draw page info
def draw_page_info(page_number, section):
    db.fill(0)
    db.stroke(0)
    db.strokeWidth(1)
    db.line((M, H-M-(U*2)), (W-M, H-M-(U*2)))
    db.line((M, M+(U*2)), (W-M, M+(U*2)))
    db.font(RENA_VF)
    db.stroke(None)
    db.fontSize(12)
    db.text("Page: "+str(int(page_number)), (M, M+(U*0)))
    if section == 0:
        db.text("Section 0: Cover Page", (M, H-M-(U*1)))
    if section == 1:
        db.text("Section 1: Cover Letter", (M, H-M-(U*1)))
    if section == 2:
        db.text("Section 2: Hasubi Mono Specimen", (M, H-M-(U*1)))
    

    db.text("Git Hash: "+MY_HASH, (W-M, H-M-(U*1)), align="right")
    db.text(FORMATTED_DATE, (W-M, M+(U*0)), align="right")
    print("PAGE!")


# New Page
def new_page():
    db.newPage(W, H)
    db.fill(0.9)
    db.rect(-2, -2, W+2, H+2)
    if GRID_VIEW:
        grid()
    else:
        pass


# TEST FONTS
#db.font(RENA_VF)
#for axis, data in db.listFontVariations().items():
#    print((axis, data))
# for eachFontName in installedFonts():
#    print(eachFontName)


# Constants
LOREM_IPSUM = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."



db.newDrawing()
page_number = 0
new_page() #--------------------------------------------------#
draw_page_info(page_number, 0)
db.font(RENA_VF)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.fontSize(92)
db.stroke(None)
db.fill(0)
db.text("Rena Typeface", (M+(U*0), M+(U*46)))
db.text("Print Proof", (M+(U*0), M+(U*36)))
db.text(FORMATTED_DATE, (M+(U*0), M+(U*26)))
#db.text(MY_HASH_SHORT, (M+(U*0), M+(U*10)))
page_number += 1


new_page() #--------------------------------------------------#
draw_page_info(page_number, 1)
db.fontSize(26)
db.stroke(None)
db.fill(0)

db.text("Contact Info", (M+(U*0), M+(U*52)))
db.fontSize(13)

db.fontSize(26)
db.text("Sample Text", (M+(U*42), M+(U*52)))

db.fontSize(13)
db.lineHeight(18)
db.textBox(LOREM_IPSUM*4, (M+(U*42), M+(U*4), U*38, U*43.5))
#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)
page_number += 1












# Saving and post-processing #--------------------------------#
db.saveImage(args.output)
print("DrawBot: Done :-)")


