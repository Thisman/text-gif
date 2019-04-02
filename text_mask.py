from os import path
from PIL import Image, ImageFont, ImageDraw

FONT_NAME = 'Ultra-Regular.ttf'
FONT_DIR = path.abspath('./fonts')

class TextMask:
    def __init__(self, text, size):
        self.text = text
        self.size = size

        self.__create_mask()

    def get(self):
        return self.mask.convert("RGBA")

    def __create_mask(self):
        text_font = self.__load_font_for_text(self.text, self.size[0])
        text_bound = text_font.getsize(self.text)
        text_coords = self.__get_text_coords(text_bound)

        text_mask_img = Image.new('RGBA', self.size, color=(255, 255, 255))
        renderer = ImageDraw.Draw(text_mask_img)
        renderer.text(text_coords, self.text, font=text_font, fill=(0, 0, 0, 0))

        self.mask = text_mask_img
    
    def __load_font_for_text(self, text, max_width):
        font_size = 10
        font = self.__load_font(FONT_NAME, font_size)
        width = font.getsize(text)[0]
        while width < max_width:
            font_size = font_size + 1
            font = self.__load_font(FONT_NAME, font_size)
            width = font.getsize(text)[0]

        return self.__load_font(FONT_NAME, font_size)
    
    def __load_font(self, name, size):
        return ImageFont.truetype('{}/{}'.format(FONT_DIR, name), size=size)

    def __get_text_coords(self, text_bound):
        return [0, (self.size[1] / 2) - (text_bound[1] / 2)]
