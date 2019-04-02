import sys
import shutil
import os
from os import path
from PIL import Image, ImageFont, ImageDraw, ImageSequence

from text_mask import TextMask

FONT_DIR = path.abspath('./fonts')
RESULT_DIR = path.abspath('./result')

def main():
    args = sys.argv[1:]
    gif_text = args[0]
    gif_name = args[1]
    gif_path = path.abspath(gif_name)

    with Image.open(gif_path) as gif:
        gif_size = gif.size
        gif_frames = []
        for frame in ImageSequence.Iterator(gif):
            gif_frames.append(frame.convert("RGBA"))

        text_mask_img = TextMask(gif_text, gif_size).get()

    for gif_frame in gif_frames:
        gif_frame.paste(text_mask_img, (0, 0), text_mask_img)
    
    gif_frames[0].save(
        '{}/result.gif'.format(RESULT_DIR),
        save_all=True,
        append_images=gif_frames[1:],
        duration=100,
        loop=0)

if __name__ == "__main__":
    main()
