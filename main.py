import argparse
import os
from os import path
from PIL import Image, ImageFont, ImageDraw, ImageSequence
import shutil
import sys

from text_mask import create_text_mask

DEFAULT_FONT_PATH = path.abspath('./fonts/Ultra-Regular.ttf')
DEFAULT_RESULT_PATH = path.abspath('./result.gif')

parser = argparse.ArgumentParser(description='Create gif with text mask')
parser.add_argument('-t', '--text', required=True, type=str, help='Text for mask')
parser.add_argument('-s', '--source', required=True, type=str, help='Path to source gif')
parser.add_argument('-f', '--font', type=str, help='Path to font using for mask', default=DEFAULT_FONT_PATH)
parser.add_argument('-r', '--result', type=str, help='Path for result gif', default=DEFAULT_RESULT_PATH)

def main():
    args = parser.parse_args()
    gif_text = args.text
    gif_path = path.abspath(args.source)
    font_path = args.font
    result_path = args.result

    with Image.open(gif_path) as gif:
        gif_size = gif.size
        gif_frames = []
        for frame in ImageSequence.Iterator(gif):
            gif_frames.append(frame.convert("RGBA"))

    text_mask_img = create_text_mask(gif_text, gif_size, font_path)

    for gif_frame in gif_frames:
        gif_frame.paste(text_mask_img, (0, 0), text_mask_img)
    
    gif_frames[0].save(
        result_path,
        save_all=True,
        append_images=gif_frames[1:],
        duration=100,
        loop=0)

if __name__ == "__main__":
    main()
