#!/usr/bin/env python3
# build.py
import os
from pathlib import Path

import markdown
from jinja2 import Template

from staticjinja import Site

CAROUSEL_TEMPLATE = r"""
<div class="swiffy-slider">
    <ul class="slider-container">
{% for img in images %}
        <li><img src="{{ img }}" style="max-width: 100%;height: auto;"></li>
{% endfor %}
    </ul>

    <button type="button" class="slider-nav"></button>
    <button type="button" class="slider-nav slider-nav-next"></button>

    <div class="slider-indicators">
        <button class="active"></button>
        <button></button>
        <button></button>
    </div>
</div>
"""

def markdown_global(text):
    md = markdown.Markdown(output_format="html5")
    return md.convert(text)

def carousel_global(img_path):
    images = list((Path(".").absolute() / "src" / img_path).glob("*.png"))
    images = [i.name for i in images]
    template = Template(CAROUSEL_TEMPLATE)
    return template.render({"images": images})

site = Site.make_site(
    searchpath="src",
    outpath="public",
    env_globals={
        "carousel": carousel_global,
        "markdown": markdown_global,
    }
)

site.render()
