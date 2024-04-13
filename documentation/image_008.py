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
GRID_VIEW = False  # Toggle this for a grid overlay

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
    db.fill(0.3)
    db.fill(0.012, 0.22, 0.96)
    db.rect(0, 0, WIDTH, HEIGHT)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text


def draw_main_text_001():
    # db.image("documentation/auxiliary-images/cb-blue.png", (0, 0), alpha=1.0)
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(200)
    db.lineHeight(200 * 1.115)
    # db.tracking(None)
    db.textBox(
        "Money is not impure, it’s information. Prices communicate knowledge and complex economies build culture. \nThe issue with monetization on the\nold internet is there wasn’t enough,\nit wasn’t integrated natively. The new internet will be hyperfinancialized.",
        (MARGIN, MARGIN - (1850), MARGIN * 14, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.37))
    db.text("001", (MARGIN * 13.75, MARGIN * 14.37))


def draw_main_text_002():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    # db.fontSize(200)
    db.fontSize(206)
    # db.lineHeight(200 * 1.110)
    db.lineHeight(200 * 1.110)
    db.tracking(2)
    # db.tracking(None)
    db.textBox(
        # "The problem of monetizing digital content is reproducible information is effectively infinite in supply, leaving it impossible to price, free like air. Prim-\nitive attempts at digital monetization try to create artificial scarcity through paywalls and DRM, technically in-\neffective against any piracy but backed by socialized pressure and threats of legal action. These models of course unethically restrict the free flow of information.",
        # "The problem of monetizing digital content is reproducible information is effectively infinite in supply, leaving it impossible to price, free like air. Prim-\nitive attempts at digital monetization try to create artificial scarcity through paywalls and DRM, technically in-\neffective against any piracy but backed by socialized pressure and threats of legal action.",
        "The problem of monetizing digital content is reproducible information is effectively infinite in supply, leaving it impossible to price, free like air. Primitive attempts at digital monetization try to create artificial scarcity through paywalls and DRM, technically ineffective against any piracy but backed by socialized pressure and threats of legal action.",
        (MARGIN, MARGIN - (1090), MARGIN * 14, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.37))
    db.text("002", (MARGIN * 13.5, MARGIN * 14.37))


def draw_main_text_003():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(159)
    db.fontSize(165)
    # db.lineHeight(165 * 1.2)
    db.tracking(1)
    db.textBox(
        "NFT’s and memecoins are an alternative form of creating artificial digital scarcity, so it’s easy to make the intuitive leap that they also negatively limit free information. However, by changing the value proposition of digital goods from a scarcity based on limiting information access to one based on provable provenance, they have no need to rely on gatekeeping access to content to secure value. This is a great boon for the freedom of information movement.",
        (MARGIN, MARGIN - (1155), MARGIN * 13.4, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.5))


def draw_main_text_004():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    GRID_VIEW = False  # Toggle this for a grid overlay
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(159)
    db.fontSize(165)
    # db.lineHeight(165 * 1.2)
    db.tracking(1)
    db.textBox(
        "Blockchain is a naturalistic technology, it would have been developed in a thousand timelines, just as the CPU would have, just as double book accounting or abstracted money would have—or AI will—but copyright law was a confusing and awkward historical aberration.",
        (MARGIN, MARGIN - (2285), MARGIN * 14, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.5))


def draw_main_text_005():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    GRID_VIEW = False  # Toggle this for a grid overlay
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(159)
    db.fontSize(165)
    # db.lineHeight(165 * 1.2)
    db.tracking(1)
    db.textBox(
        "Digital scarcity instituted by legal infrastructure was an awkward, artificial and ethically problematic intervention on the free flow of information; NFTs managing scarcity as a trustless bookkeeping allows accessibility to be achieved without undermining production incentives.",
        (MARGIN, MARGIN - (2000), MARGIN * 13.5, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.5))


def draw_main_text_006():
    # db.image("documentation/auxiliary-images/bg_001.png", (0, 0), alpha=1.0)
    GRID_VIEW = False  # Toggle this for a grid overlay
    db.fill(1)
    db.stroke(None)
    db.font(MAIN_FONT_PATH)
    db.fontSize(159)
    db.fontSize(165)
    # db.lineHeight(165 * 1.2)
    db.tracking(1)
    db.textBox(
        "Crypto solves the problem of trustless digital deeds of ownership, making the need to conflate ownership with content accessibility in copyable digital media outmoded—and with it, convoluted and invasive DRM solutions, unclear licensing rights and likely one day, paywalling altogether.",
        (MARGIN, MARGIN - (2000), MARGIN * 14, MARGIN * 14),
        align="left",
    )
    db.text("Crypto and Free Information", (MARGIN, MARGIN * 14.5))


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text_002()
    # Save output, using the "--output" flag location
    db.saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
