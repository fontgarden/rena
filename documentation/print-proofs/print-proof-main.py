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
W = 792     # Width
H = 612     # Height
M = 36      # Margin
U = 9       # Unit
CURRENT_DATE = datetime.now()
FORMATTED_DATE = CURRENT_DATE.strftime("%d.%m.%Y")
MY_HASH_SHORT = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
MY_HASH = subprocess.check_output("git rev-parse --verify HEAD", shell=True).decode()
RENA_VF = "fonts/RenaVF.ttf"
GRID_VIEW = False 


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
    db.fontVariations(wght = 400)
    db.fontVariations(opsz = 14)

    db.text("Page: "+str(int(page_number)), (M, M+(U*0)))
    if section == 0:
        db.text("Font.Garden Print Proof—Section 0: Cover Page", (M, H-M-(U*1)))
    if section == 1:
        db.text("Font.Garden Print Proof—Section 1: Character Set", (M, H-M-(U*1)))
    if section == 2:
        db.text("Font.Garden Print Proof—Section 2: Spacing Strings", (M, H-M-(U*1)))
    if section == 3:
        db.text("Font.Garden Print Proof—Section 3: Text Samples", (M, H-M-(U*1)))
    if section == 4:
        db.text("Font.Garden Print Proof—Section 4: Sandbox", (M, H-M-(U*1)))
    
    db.text("Git Hash: "+MY_HASH, (W-M, M+(U*0)), align="right")
    db.text(FORMATTED_DATE, (W-M, H-M-(U*1)), align="right")
    print("PAGE!")


# New Page
def new_page():
    db.newPage(W, H)
    db.fill(None)
    #db.rect(-2, -2, W+2, H+2)
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


def create_spacing_strings_upper(characters):
    spacing_strings = "" 
    for char in characters:
        spacing_string = "HH"+char+"OHO"+char+"OO\n"
        spacing_strings = spacing_strings+spacing_string
    return spacing_strings


def create_spacing_strings_lower(characters):
    spacing_strings = "" 
    for char in characters:
        spacing_string = "nn"+char+"ono"+char+"oo\n"
        spacing_strings = spacing_strings+spacing_string
    return spacing_strings


def create_spacing_strings_number(characters):
    spacing_strings = "" 
    for char in characters:
        spacing_string = "11"+char+"010"+char+"00\n"
        spacing_strings = spacing_strings+spacing_string
    return spacing_strings


# Constants
LOREM_IPSUM = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
BITCOIN = "A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending. We propose a solution to the double-spending problem using a peer-to-peer network. The network timestamps transactions by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work. The longest chain not only serves as proof of the sequence of events witnessed, but proof that it came from the largest pool of CPU power. As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers. The network itself requires minimal structure. Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone. Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties to process electronic payments. While the system works well enough for most transactions, it still suffers from the inherent weaknesses of the trust based model. Completely non-reversible transactions are not really possible, since financial institutions cannot avoid mediating disputes. The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions, and there is a broader cost in the loss of ability to make non-reversible payments for nonreversible services. With the possibility of reversal, the need for trust spreads. Merchants must be wary of their customers, hassling them for more information than they would otherwise need. A certain percentage of fraud is accepted as unavoidable. These costs and payment uncertainties can be avoided in person by using physical currency, but no mechanism exists to make payments over a communications channel without a trusted party. What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party. Transactions that are computationally impractical to reverse would protect sellers from fraud, and routine escrow mechanisms could easily be implemented to protect buyers. In this paper, we propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions. The system is secure as long as honest nodes collectively control more CPU power than any cooperating group of attacker nodes. "


chars_to_proof_lower = "abcdefghijklmnopqrstuvwxyz"
chars_to_proof_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars_to_proof_number = "1234567890-+=_)(*%$#@!.:"
#chars_to_proof_lower = "abcdefghijklmnopqrstuvwxyz"
#chars_to_proof_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#chars_to_proof_number = "1234567890-+=_)(*%$#@!.:"
spacing_strings_upper = create_spacing_strings_upper(chars_to_proof_upper)
spacing_strings_lower = create_spacing_strings_lower(chars_to_proof_lower)
spacing_strings_number = create_spacing_strings_number(chars_to_proof_number)
#spacing_strings_upper_extra = create_spacing_strings_upper(chars_to_proof_upper_extra)
#spacing_strings_lower_extra = create_spacing_strings_lower(chars_to_proof_lower_extra)
#spacing_strings_number_extra = create_spacing_strings_number(chars_to_proof_number_extra)


# Start making pages
db.newDrawing()


new_page() #--------------------------------------------------#
page_number = 0
draw_page_info(page_number, 0)
db.font(RENA_VF)
db.fontVariations(wght = 700)
db.fontVariations(opsz = 144)
db.fontSize(92)
db.stroke(None)
db.fill(0)
db.text("Rena Typeface", (M+(U*0), M+(U*46)))
db.text("Print Proof", (M+(U*0), M+(U*36)))
db.text(FORMATTED_DATE, (M+(U*0), M+(U*26)))
db.text("Git: "+MY_HASH_SHORT, (M+(U*0), M+(U*6)))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 1)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.text("wght:700—opsz:144—72pt", (M+(U*0), M+(U*55)))

db.fontSize(72)
db.fontVariations(wght = 700)
db.fontVariations(opsz = 144)
db.text("abcdefghijklmnopq", (M+(U*0), M+(U*46)))
db.text("rstuvwxyzß.,:;-–—”!?", (M+(U*0), M+(U*36)))
db.text("ABCDEFGHIJKLMN", (M+(U*0), M+(U*26)))
db.text("OPQRSTUVWXYZ&", (M+(U*0), M+(U*16)))
db.text("1234567890₿$¢€¥", (M+(U*0), M+(U*6)))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 1)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.text("wght:550—opsz:144—72pt", (M+(U*0), M+(U*55)))

db.fontSize(72)
db.fontVariations(wght = 550)
db.fontVariations(opsz = 144)
db.text("abcdefghijklmnopq", (M+(U*0), M+(U*46)))
db.text("rstuvwxyzß.,:;-–—”!?", (M+(U*0), M+(U*36)))
db.text("ABCDEFGHIJKLMN", (M+(U*0), M+(U*26)))
db.text("OPQRSTUVWXYZ&", (M+(U*0), M+(U*16)))
db.text("1234567890₿$¢€¥", (M+(U*0), M+(U*6)))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 1)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.text("wght:400—opsz:144—72pt", (M+(U*0), M+(U*55)))

db.fontSize(72)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.text("abcdefghijklmnopq", (M+(U*0), M+(U*46)))
db.text("rstuvwxyzß.,:;-–—”!?", (M+(U*0), M+(U*36)))
db.text("ABCDEFGHIJKLMN", (M+(U*0), M+(U*26)))
db.text("OPQRSTUVWXYZ&", (M+(U*0), M+(U*16)))
db.text("1234567890₿$¢€¥", (M+(U*0), M+(U*6)))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 2)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:400—opsz:144", (M+(U*0), M+(U*55)))
db.text("wght:700—opsz:144", (M+(U*40), M+(U*55)))

db.fontSize(14)
db.lineHeight(14.85)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.textBox(spacing_strings_upper, (M+(U*0), M+(U*3), U*12, U*49))
db.textBox(spacing_strings_lower, (M+(U*13), M+(U*3), U*12, U*49))
db.textBox(spacing_strings_number, (M+(U*24), M+(U*3), U*12, U*49))


db.fontVariations(wght = 700)
db.fontVariations(opsz = 144)
db.textBox(spacing_strings_upper, (M+(U*40), M+(U*3), U*12, U*49))
db.textBox(spacing_strings_lower, (M+(U*53), M+(U*3), U*12, U*49))
db.textBox(spacing_strings_number, (M+(U*64), M+(U*3), U*12, U*49))

#fill(1,0,0)
#rect(MARGIN+(UNIT*42), MARGIN+(UNIT*4), UNIT*38, UNIT*44)


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 3)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:400—opsz:14—12:13", (M+(U*0), M+(U*55)))
db.text("wght:400—opsz:14—10:11", (M+(U*42), M+(U*55)))

db.fontSize(12)
db.lineHeight(13)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.textBox(BITCOIN*2, (M+(U*0), M+(U*4), U*38, U*48))

db.fontSize(10)
db.lineHeight(11)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.textBox(BITCOIN*2, (M+(U*42), M+(U*4), U*38, U*48))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 3)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:700—opsz:14—12:13", (M+(U*0), M+(U*55)))
db.text("wght:700—opsz:14—10:11", (M+(U*42), M+(U*55)))

db.fontSize(12)
db.lineHeight(13)
db.fontVariations(wght = 700)
db.fontVariations(opsz = 14)
db.textBox(BITCOIN*2, (M+(U*0), M+(U*4), U*38, U*48))

db.fontSize(10)
db.lineHeight(11)
db.fontVariations(wght = 700)
db.fontVariations(opsz = 14)
db.textBox(BITCOIN*2, (M+(U*42), M+(U*4), U*38, U*48))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 3)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:700—opsz:72—24:25", (M+(U*0), M+(U*55)))

db.fontSize(24)
db.lineHeight(25)
db.fontVariations(wght = 700)
db.fontVariations(opsz = 72)
db.textBox(BITCOIN*2, (M+(U*0), M+(U*4), U*72, U*48))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 3)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:400—opsz:72—24:25", (M+(U*0), M+(U*55)))

db.fontSize(24)
db.lineHeight(25)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 72)
db.textBox(BITCOIN*2, (M+(U*0), M+(U*4), U*72, U*48))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 3)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:700—opsz:144", (M+(U*0), M+(U*55)))

db.fontVariations(wght = 700)
db.fontVariations(opsz = 144)
db.fontSize(72)
db.text("Northwest Techno", (M+(U*0), M+(U*46)))
db.text("Graphic Design", (M+(U*0), M+(U*38)))
db.text("THE DESIGN OF THE", (M+(U*0), M+(U*22)))
db.text("UNIX SYSTEM", (M+(U*0), M+(U*14)))
db.text("GRID PROGRAM", (M+(U*0), M+(U*6)))


new_page() #--------------------------------------------------#
page_number += 1
draw_page_info(page_number, 3)
db.fontSize(12)
db.fontVariations(wght = 400)
db.fontVariations(opsz = 14)
db.text("wght:400—opsz:144", (M+(U*0), M+(U*55)))

db.fontVariations(wght = 400)
db.fontVariations(opsz = 144)
db.fontSize(72)
db.text("Northwest Techno", (M+(U*0), M+(U*46)))
db.text("Graphic Design", (M+(U*0), M+(U*38)))
db.text("THE DESIGN OF THE", (M+(U*0), M+(U*22)))
db.text("UNIX SYSTEM", (M+(U*0), M+(U*14)))
db.text("GRID PROGRAM", (M+(U*0), M+(U*6)))

# Saving and post-processing #--------------------------------#
db.saveImage(args.output)
print("DrawBot: Done :-)")


