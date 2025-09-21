SHELL := /bin/bash
MAKEFLAGS := --always-make

PYTHON := ~/.local/share/pipx/venvs/staticjinja/bin/python


build: build-clean
	$(PYTHON) build.py

all: all-clean galleries build
	@echo build complete

build-clean:
	sudo rm docs/displays docs/_* -rf

all-clean:
	sudo rm docs/displays docs/galleries docs/_* -rf

init:
	pipx install staticjinja
	pipx inject staticjinja Markdown jinja2-simple-tags pillow python-slugify


webp:
	mogrify -format webp *.jpg *.jpeg *.png; rm -f *.jpg *.jpeg *.png


# FIXME - put these in subdirs
fetch-static:
	mkdir -p docs/static/{css,js,img}
	mkdir -p docs/static/{pico,aos}
	curl https://unpkg.com/aos@next/dist/aos.css -o docs/static/aos/aos.css
	curl https://unpkg.com/aos@next/dist/aos.js -o docs/static/aos/aos.js
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css -o docs/static/css/pico.min.css
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css -o docs/static/css/pico.classless.min.css
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.fluid.classless.min.css -o docs/static/css/pico.fluid.classless.min.css
	curl https://github.com/michalsnik/aos/archive/master.zip -o docs/static/aos/master.zip
	#curl https://cdn.jsdelivr.net/npm/swiffy-slider@1.6.0/dist/css/swiffy-slider.min.css -o docs/static/css/swiffy-slider.min.css
	#curl https://cdn.jsdelivr.net/npm/swiffy-slider@1.6.0/dist/js/swiffy-slider.min.js -o docs/static/js/swiffy-slider.min.js
	#curl https://app.unpkg.com/lightgallery@2.9.0-beta.1/css/lightgallery-bundle.min.css -o docs/static/css/lightgallery-bundle.min.css
	#curl https://app.unpkg.com/lightgallery@2.9.0-beta.1/lightgallery.min.js -o docs/static/js/lightgallery.min.js
	curl https://unpkg.com/photoswipe@5.4.2/dist/photoswipe.css -o docs/static/css/photoswipe.css
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.js -o docs/static/js/photoswipe-lightbox.esm.js
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.js.map -o docs/static/js/photoswipe-lightbox.esm.js.map
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe.esm.js -o docs/static/js/photoswipe.esm.js
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe.esm.js.map -o docs/static/js/photoswipe.esm.js.map
	curl https://codeload.github.com/kristoferjoseph/flexboxgrid/zip/refs/tags/v6.3.1 -o docs/static/css/flexboxgrid.zip
	#curl https://fslightbox.com/f/1/fslightbox-basic-3.7.4.zip -o docs/static/js/fslightbox-basic-3.7.4.zip

serve:
	@ip -br -4 a show eth0
	cd docs && python3 -m http.server -b 0.0.0.0


thumbnails:
	convert M-Vimy-LEAD-crop-scaled.jpg -resize "600x600^" -gravity center -crop "600x600+0+0" M-Vimy-LEAD-crop-scaled--thumbnail.jpg




fussel-build:
	cd fussel && docker build -t fussel .

gallery:  # FIXME - 192 addr
	sigal build -c sigal/sigal.conf.py gallery docs/gallery

sigal:
	pipx install -f ~/src/sigal

slugify:
	$(PYTHON)