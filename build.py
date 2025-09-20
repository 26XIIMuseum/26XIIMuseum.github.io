#!/usr/bin/env python3
# build.py
import json
import os
import logging
import re
import subprocess
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from jinja2 import Environment, FileSystemLoader
from jinja2_simple_tags import ContainerTag
from slugify import slugify
from staticjinja import Site

logging.basicConfig(level=logging.INFO)

TEMPLATE_DIR = "src"
PUBLIC_DIR = "docs"
J2_ENV = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True)
IMG_EXTENSIONS = [
    ".webp",
]

class SectionExtension(ContainerTag):
    tags = {"section"}
    def render(self, section_id=None, section_title=None, caller=None):
        template = J2_ENV.get_template("_section.html.j2")
        return template.render({
            "section_id": section_id,
            "section_title": section_title,
            "section_content": caller(),
        })

class MarkdownExtension(ContainerTag):
    tags = {"markdown"}
    def render(self, caller=None):
        return markdown.markdown(caller())

# convert M-Vimy-LEAD-crop-scaled.jpg -resize "600x600^" -gravity center -crop "600x600+0+0" M-Vimy-LEAD-crop-scaled--thumbnail.jpg
def make_thumbnail(img):
    thumb = Path(f"{img.parent}/{img.stem}--thumbnail{img.suffix}")
    if thumb.exists():
        return thumb
    subprocess.check_output([
        "convert",
        str(img),
        "-resize",
        "600x600^",
        "-gravity",
        "center",
        "-crop",
        "600x600+0+0",
        str(thumb)
    ])
    return thumb


def gallery(img_dir, num_col=3):
    public_dir = Path(PUBLIC_DIR) / img_dir.lstrip("/")
    images = []
    for img in [i for i in public_dir.glob("*") if i.is_file() and i.suffix in IMG_EXTENSIONS]:
        if "--thumbnail" in str(img):
            continue
        thumb = make_thumbnail(img)
        images.append({
            "img": re.sub(f'^{PUBLIC_DIR}', '', str(img)),
            "thumb": re.sub(f'^{PUBLIC_DIR}', '', str(thumb))
        })
    template = J2_ENV.get_template("_gallery.html.j2")
    return template.render({
        "num_col": num_col,
        "images": images,
    })


def hero_banner(hero_title, hero_image):
    template = J2_ENV.get_template("_hero_banner.html.j2")
    return template.render({
        "hero_image": hero_image,
        "hero_title": hero_title,
    })

def audio(audio_src):
    template = J2_ENV.get_template("_audio.html.j2")
    return template.render({
        "audio_src": audio_src,
    })

site = Site.make_site(
    searchpath=TEMPLATE_DIR,
    outpath=PUBLIC_DIR,
    extensions=[
        MarkdownExtension,
        SectionExtension,
    ],
    filters={
        "audio": audio,
        "gallery": gallery,
        "hero_banner": hero_banner,
    }
)

site.render(use_reloader=True)
