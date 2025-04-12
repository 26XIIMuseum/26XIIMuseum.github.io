from pathlib import Path

IMAGE_SUFFIXES = [".jpg", ".jpeg", ".png"]


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    @env.macro
    def carousel(img_dir):
        images = [p for p in Path(img_dir).glob("*") if p.suffix in IMAGE_SUFFIXES]
        if not images:
            raise ValueError(f"No images in {img_dir}")
        slider_class = "slider-nav-visible slider-nav-touch slider-indicators-round" if len(images) > 1 else ""
        html = f'<div class="swiffy-slider {slider_class} slider-nav-animation slider-nav-animation-fadein">'
        html += '<ul class="slider-container">'
        for p in images:
            i = str(p).replace("content/", "/")
            html += f'<li><img src="{i}" style="max-width: 100%;height: auto;"></li>'
        html += "</ul>"
        html += "</div>"
        return html
        
    @env.macro
    def audio(audio_file):
        if not Path(audio_file).exists():
            raise ValueError(f"No audio.mp3 in {audio_dir}")
        html = '<div style="text-align: center" class="audio-controls">'
        a_url = audio_file.replace("content/", "/")
        html += f'<audio class="audio" controls src="{a_url}"></audio>'
        html += '</div>'
        return html

        

    # create a jinja2 filter


#    @env.filter
#    def reverse(x):
#        "Reverse a string (and uppercase)"
#        return x.upper()[::-1]
