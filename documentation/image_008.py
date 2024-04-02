# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ python3 documentation/image_001.py --output documentation/image_001.png

import argparse
import subprocess

import drawBot as db
from fontTools.misc.fixedTools import floatToFixedToStr
from fontTools.ttLib import TTFont

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 4096, 4096, 256, 1
MAIN_FONT_PATH = "fonts/Rena-Regular.ttf"
AUXILIARY_FONT = "Helvetica"

# Toggle this for a grid overlay
GRID_VIEW = True  # Toggle this for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(MAIN_FONT_PATH)


# Draws a grid
def grid():
    """Draws a grid using DrawBot-Skia"""
    db.stroke(1, 1, 1, 0.5)
    db.fill(None)
    db.strokeWidth(2)
    step_x = 0
    step_y = 0
    increment_x, increment_y = MARGIN / 2, MARGIN / 2
    db.rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        db.polygon((MARGIN + step_x, MARGIN), (MARGIN + step_x, HEIGHT - MARGIN))
        step_x += increment_x
    for y in range(29):
        db.polygon((MARGIN, MARGIN + step_y), (WIDTH - MARGIN, MARGIN + step_y))
        step_y += increment_y
    db.polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    db.polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    db.newPage(WIDTH, HEIGHT)
    db.fill(0.2)
    db.fill(0.025)
    db.fill(0, 0, 1)
    db.rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
GRID_VIEW = False  # Toggle this for a grid overlay


def draw_main_text_001():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(512 + 32)
    db.fontSize(159)
    db.lineHeight(160 * 1.12)
    # db.tracking(3)
    db.textBox(
        "\n\n\n\n\nThe problem of monetizing digital content is reproducible information is effectively infinite in supply, leaving it impossible to price, free like air.  Primitive attempts at digital monetization try to create artificial scarcity through paywalls and DRM, technically ineffective against any piracy but backed by socialized pressure and threats of legal action. These models of course unethically restrict the free flow of information. \n\n\n\n NFT’s are an alternative form of creating artificial digital scarcity, so it’s easy to make the intuitive leap that they also negatively limit free information. However, by changing the value proposition of digital goods from a scarcity based on limiting information access to one based on provable provenance, they have no need to rely on gatekeeping access to NFT content to secure value. This is a great boon for the freedom of information movement. \n\n ",
        (MARGIN, MARGIN - (256 + 490), MARGIN * 14, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.5))
    # db.rect(MARGIN * 8, MARGIN, MARGIN * 7, MARGIN * 4)


def draw_main_text_002():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(512 + 32)
    db.fontSize(152)
    # db.lineHeight(120)
    db.tracking(2)
    db.textBox(
        "\n\n\n\n\n\nMemecoins and NFT’s are an alternative form of creating artificial digital scarcity, so it’s easy to make the intuitive leap that they also negatively limit free information. However, by changing the value proposition of digital goods from a scarcity based on limiting information access to one based on provable provenance, they have no need to rely on gatekeeping access to NFT content to secure value. This is a great boon for the freedom of information movement. \n\n ",
        (MARGIN, MARGIN - (256 + 56), MARGIN * 13, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.5))
    # db.rect(MARGIN * 8, MARGIN, MARGIN * 7, MARGIN * 4)


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text_001()
    # draw_main_text_002()
    # Save output, using the "--output" flag location
    db.saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
