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

class MarkdownExtension(ContainerTag):
    tags = {"markdown"}
    def render(self, caller=None):
        return markdown.markdown(caller())


def gallery_link(gallery_link_href):
    template = J2_ENV.get_template("_gallery_link.j2")
    return template.render({
        "gallery_link_href": gallery_link_href,
    })

def audio(audio_src):
    template = J2_ENV.get_template("_audio.j2")
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
        "gallery_link": gallery_link,
    }
)

site.render(use_reloader=True)
