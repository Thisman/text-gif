from os import path
from PIL import Image, ImageFont, ImageDraw

def create_text_mask(text, size, font_path):
    text_font = _load_font_for_text(text, font_path, size[0])
    text_bound = text_font.getsize(text)
    text_coords = _get_text_coords(text_bound, size)

    text_mask_img = Image.new('RGBA', size, color=(255, 255, 255))
    renderer = ImageDraw.Draw(text_mask_img)
    renderer.text(text_coords, text, font=text_font, fill=(0, 0, 0, 0))

    return _crop_space_around_text(
        text_mask_img,
        text,
        text_font
    ).convert('RGBA')

def _load_font_for_text(text, font_path, max_width):
    font_size = 10
    font = _load_font(font_path, font_size)
    width = font.getsize(text)[0]
    while width < max_width:
        font_size = font_size + 1
        font = _load_font(font_path, font_size)
        width = font.getsize(text)[0]

    return _load_font(font_path, font_size - 1)

def _load_font(font_path, size):
    return ImageFont.truetype(font_path, size=size)

def _get_text_coords(text_bound, size):
    return [0, 0]

def _crop_space_around_text(image, text, font):
    ascent, _ = font.getmetrics()
    (_, _), (_, offset_y) = font.font.getsize(text)
    text_crop_offset = 3

    return image.crop((
        0,
        offset_y - text_crop_offset,
        image.size[0],
        ascent + text_crop_offset,
    ))