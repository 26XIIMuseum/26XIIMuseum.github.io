#!/usr/bin/env python3
# build.py
import os
from pathlib import Path

import markdown
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

class SectionExtension(ContainerTag):
    tags = {"section"}
    def render(self, section_id=None, section_title=None, caller=None):
        template = J2_ENV.get_template("_section.j2")
        return template.render({
            "section_id": section_id,
            "section_title": section_title,
            "section_content": caller(),
        })

def carousel_global(static_dir):
    images = []
    for g in IMG_GLOBS:
        for found_img in (Path("public") / Path(static_dir)).glob(g):
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
