#!/usr/bin/env python3
# build.py
import os
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from jinja2 import Environment, FileSystemLoader
from jinja2_simple_tags import ContainerTag

from staticjinja import Site

TEMPLATE_DIR = "src"
PUBLIC_DIR = "public"
J2_ENV = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True)
IMG_GLOBS = [
    "*.jpg",
    "*.jpeg",
    "*.png",
]
GALLERY_THUMBNAIL_FILENAME = "thumb.jpg"
GALLERY_THUMBNAIL_SIZE = (600,600)
GALLERY_THUMBNAIL_DARKEN = 0.2
GALLERY_THUMBNAIL_TEXT = "Image Gallery"
GALLERY_THUMBNAIL_TEXT_POSITION = (50, 50)
GALLERY_THUMBNAIL_TEXT_COLOR = (255, 255, 255)
try:
    GALLERY_THUMBNAIL_FONT = ImageFont.truetype("DejaVuSerif.ttf", 40)
except IOError:
    print("Font 'arial.ttf' not found. Using default font.")
    GALLERY_THUMBNAIL_FONT = ImageFont.load_default()

class GalleryImage:
    def __init__(self, static_path, width, height):
        self.static_path = static_path
        self.width = width
        self.height = height


class SectionExtension(ContainerTag):
    tags = {"section"}
    def render(self, section_id=None, section_title=None, caller=None):
        template = J2_ENV.get_template("_section.j2")
        return template.render({
            "section_id": section_id,
            "section_title": section_title,
            "section_content": caller(),
        })

def create_thumbnail(src_image):
    thumb_dst = src_image.parent / GALLERY_THUMBNAIL_FILENAME
    if thumb_dst.exists():
        thumb_dst.unlink()
    img = Image.open(src_image)
    thumb_img = img.copy()
    thumb_img.thumbnail(GALLERY_THUMBNAIL_SIZE)
    enhancer = ImageEnhance.Brightness(thumb_img)
    thumb_img = enhancer.enhance(GALLERY_THUMBNAIL_DARKEN)
    thumb_draw = ImageDraw.Draw(thumb_img)
    text_posn_x = (thumb_img.width // 2)
    text_posn_y = (thumb_img.width // 3)
    thumb_draw.text((text_posn_x, text_posn_y), GALLERY_THUMBNAIL_TEXT, font=GALLERY_THUMBNAIL_FONT, fill=GALLERY_THUMBNAIL_TEXT_COLOR, anchor="mt")
    thumb_img.save(thumb_dst)
    thumb_img.show()


def carousel_global(static_dir):
    images = []
    thumbnail = None
    for g in IMG_GLOBS:
        for found_img in (Path("public") / Path(static_dir)).glob(g):
            if not thumbnail and found_img.name != GALLERY_THUMBNAIL_FILENAME:
                create_thumbnail(found_img)
                thumbnail = True
            images.append(Path("/") / Path(*found_img.parts[1:]))
    template = J2_ENV.get_template("_carousel.j2")
    return template.render({"images": images})

site = Site.make_site(
    searchpath=TEMPLATE_DIR,
    outpath=PUBLIC_DIR,
    extensions=[
        SectionExtension,
    ],
    env_globals={
        "carousel": carousel_global,
    }
)

site.render(use_reloader=True)
