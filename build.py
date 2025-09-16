#!/usr/bin/env python3
# build.py
import json
import os
import logging
from pathlib import Path

import markdown
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from jinja2 import Environment, FileSystemLoader
from jinja2_simple_tags import ContainerTag
from slugify import slugify
from staticjinja import Site

logging.basicConfig(level=logging.INFO)

TEMPLATE_DIR = "src"
PUBLIC_DIR = "public"
J2_ENV = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True)

class SectionExtension(ContainerTag):
    tags = {"section"}
    def render(self, section_id=None, section_title=None, caller=None):
        template = J2_ENV.get_template("_section.j2")
        return template.render({
            "section_id": section_id,
            "section_title": section_title,
            "section_content": caller(),
        })

def gallery(gallery_href):
    template = J2_ENV.get_template("_gallery.j2")
    return template.render({
        "gallery_href": gallery_href,
    })

site = Site.make_site(
    searchpath=TEMPLATE_DIR,
    outpath=PUBLIC_DIR,
    extensions=[
        SectionExtension,
    ],
    filters={
        "gallery": gallery,
    }
)

site.render(use_reloader=True)
