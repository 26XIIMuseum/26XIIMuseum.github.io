from pathlib import Path

from jinja2 import Template

IMAGE_SUFFIXES = [".jpg", ".jpeg", ".png"]


CAROUSEL_TEMPLATE = r"""
<div class="swiffy-slider">
    <ul class="slider-container">
{% for image_path in image_paths %}
        <li><img src="{{ image_path }}" style="max-width: 100%;height: auto;"></li>
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

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    @env.macro
    def carousel(img_dir):  # FIXME account for single image
        images = [p for p in Path(img_dir).glob("*") if p.suffix in IMAGE_SUFFIXES]
        if not images:
            raise ValueError(f"No images in {img_dir}")
        image_paths = [str(i).replace('content/', '/') for i in images]
        template = Template(CAROUSEL_TEMPLATE)
        return template.render(image_paths=image_paths)

    @env.macro
    def audio(audio_file):
        if not Path(audio_file).exists():
            raise ValueError(f"No audio.mp3 in {audio_dir}")
        html = '<div style="text-align: center" class="audio-controls">'
        a_url = audio_file.replace("content/", "/")
        html += f'<audio class="audio" controls src="{a_url}"></audio>'
        html += "</div>"
        return html

    # create a jinja2 filter


#    @env.filter
#    def reverse(x):
#        "Reverse a string (and uppercase)"
#        return x.upper()[::-1]
