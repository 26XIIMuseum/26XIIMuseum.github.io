SHELL := /bin/bash
MAKEFLAGS := --always-make

PYTHON := ~/.local/share/pipx/venvs/staticjinja/bin/python


build: build-clean
	$(PYTHON) build.py

all: all-clean galleries build
	@echo build complete

build-clean:
	sudo rm public/displays public/_* -rf

all-clean:
	sudo rm public/displays public/galleries public/_* -rf

init:
	pipx install staticjinja
	pipx inject staticjinja Markdown jinja2-simple-tags pillow python-slugify


# FIXME - put these in subdirs
fetch-static:
	mkdir -p public/static/{css,js,img}
	mkdir -p public/static/{pico,aos}
	curl https://unpkg.com/aos@next/dist/aos.css -o public/static/aos/aos.css
	curl https://unpkg.com/aos@next/dist/aos.js -o public/static/aos/aos.js
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css -o public/static/css/pico.min.css
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css -o public/static/css/pico.classless.min.css
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.fluid.classless.min.css -o public/static/css/pico.fluid.classless.min.css
	curl https://github.com/michalsnik/aos/archive/master.zip -o public/static/aos/master.zip
	#curl https://cdn.jsdelivr.net/npm/swiffy-slider@1.6.0/dist/css/swiffy-slider.min.css -o public/static/css/swiffy-slider.min.css
	#curl https://cdn.jsdelivr.net/npm/swiffy-slider@1.6.0/dist/js/swiffy-slider.min.js -o public/static/js/swiffy-slider.min.js
	#curl https://app.unpkg.com/lightgallery@2.9.0-beta.1/css/lightgallery-bundle.min.css -o public/static/css/lightgallery-bundle.min.css
	#curl https://app.unpkg.com/lightgallery@2.9.0-beta.1/lightgallery.min.js -o public/static/js/lightgallery.min.js
	curl https://unpkg.com/photoswipe@5.4.2/dist/photoswipe.css -o public/static/css/photoswipe.css
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.js -o public/static/js/photoswipe-lightbox.esm.js
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.js.map -o public/static/js/photoswipe-lightbox.esm.js.map
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe.esm.js -o public/static/js/photoswipe.esm.js
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe.esm.js.map -o public/static/js/photoswipe.esm.js.map
	curl https://codeload.github.com/kristoferjoseph/flexboxgrid/zip/refs/tags/v6.3.1 -o public/static/css/flexboxgrid.zip
	#curl https://fslightbox.com/f/1/fslightbox-basic-3.7.4.zip -o public/static/js/fslightbox-basic-3.7.4.zip

serve:
	@ip -br -4 a show eth0
	cd public && python3 -m http.server -b 0.0.0.0


thumbnails:
	convert M-Vimy-LEAD-crop-scaled.jpg -resize "600x600^" -gravity center -crop "600x600+0+0" M-Vimy-LEAD-crop-scaled--thumbnail.jpg




fussel-build:
	cd fussel && docker build -t fussel .

gallery:  # FIXME - 192 addr
	sigal build -c sigal/sigal.conf.py gallery public/gallery

sigal:
	pipx install -f ~/src/sigal

slugify:
	$(PYTHON)