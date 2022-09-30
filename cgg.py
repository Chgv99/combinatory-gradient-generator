import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import argparse
import os

parser = argparse.ArgumentParser(description='Generate gradients from pairs of colors.')
parser.add_argument('-d', '--directory', type=str,
                    default="./result/",
                    help='Result directory.')
parser.add_argument('-W', '--width', type=int,
                    default=100,
                    help='Image width.')
parser.add_argument('-H', '--height', type=int,
                    default=200,
                    help='Image height.')
parser.add_argument('-m', '--mode', type=str,
                    nargs='?',
                    choices=('combinatory', 'pairs'),
                    help="Choose between combinatory or pairs mode.\n"
                         "-c COMBINATORY\n\n\tGenerates a gradient for every combination of the colors introduced.\n"
                         "-p PAIRS\n\tGenerates gradients by selecting the colors introduced in pairs of two.")
#parser.add_argument('-c', '--combinatory', action="store_true",
                    #help='Allows generation of a gradient for every combination of the colors introduced.')
parser.add_argument('colors', nargs='+',
                    default=[],
                    help='List of colors.')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Enables verbose.')

args = parser.parse_args()

#### Directory
#if not args.dir == "":
#    result_path = args.dir
#else:
#    result_path = "./result/"

result_path = args.directory
if not os.path.exists(result_path):
    os.makedirs(result_path)

width = args.width
height = args.height

colors = args.colors

log = ""
gradient = 0

def diff_rgb(rgb1: tuple, rgb2: tuple):
    return ((rgb2[0] - rgb1[0]),
            (rgb2[1] - rgb1[1]),
            (rgb2[2] - rgb1[2]))


def split_colors(hex: str):
    return hex[0:1], hex[2:3], hex[4:5]


def add_dec_to_hex(dec: int, hex: hex):
    return


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def generate_gradient(color1, color2):
    global log, gradient
    gradient += 1
    rgbcolor1 = hex_to_rgb(color1)
    rgbcolor2 = hex_to_rgb(color2)
    log += "\n----------------------\n"
    log += "Creating gradient for: "
    log += str(rgbcolor1[0]) + ", " + str(rgbcolor1[1]) + ", " + str(rgbcolor1[2]) + " and "
    log += str(rgbcolor2[0]) + ", " + str(rgbcolor2[1]) + ", " + str(rgbcolor2[2]) + "\n"
    diff = diff_rgb(rgbcolor1, rgbcolor2)
    log += "Difference: "
    log += str(diff[0]) + ", " + str(diff[1]) + ", " + str(diff[2]) + "\n"
    log += "Step: "
    step_diff = (diff[0] / height,
                 diff[1] / height,
                 diff[2] / height)
    log += str(step_diff[0]) + ", " + str(step_diff[1]) + ", " + str(step_diff[2]) + "\n"
    img = Image.new(mode="RGB", size=(width, height))

    current_color = rgbcolor1
    for y in range(0, height):
        current_color = (current_color[0] + step_diff[0],
                         current_color[1] + step_diff[1],
                         current_color[2] + step_diff[2])
        # log += "current: " + str(current_color[0]) + ", " + str(current_color[1]) + ", " + str(current_color[2]) + "\n"
        # print("current_color " + str(gradient) + ": " + str(current_color[0]) + ", " + str(current_color[1]) + ", " + str(current_color[2]))
        for x in range(0, width):
            img.putpixel((x, y),
                         (math.floor(current_color[0]),
                          math.floor(current_color[1]),
                          math.floor(current_color[2])))
    # print("e")
    img = img.filter(ImageFilter.DETAIL)
    img = img.filter(ImageFilter.SHARPEN)
    img.save(result_path + str(gradient) + '.jpg', quality=95)
    # img.show()
    # used.append(((color1, color2)))


def generate_pairs_gradient():
    global log
    if not len(colors) % 2 == 0:
        log += "ERROR: Color quantity must be even."
        return
    for i in range(0, len(colors), 2):
        color1 = colors[i]
        color2 = colors[i+1]
        generate_gradient(color1, color2)


def generate_combinatory_gradient():
    for color1 in colors:
        for color2 in colors:
            generate_gradient(color1, color2)


if args.mode == "combinatory":
    log += "COMBINATORY mode\n"
    generate_combinatory_gradient()
elif args.mode == "pairs":
    log += "PAIRS mode\n"
    log += "PAIRS mode\n"
    generate_pairs_gradient()

if args.verbose: print(log);
# if __name__ == '__main__':
