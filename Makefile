SHELL := /bin/bash
MAKEFLAGS := --always-make

build: build-clean
	~/.local/share/pipx/venvs/staticjinja/bin/python build.py

all: all-clean galleries build
	@echo build complete

build-clean:
	sudo rm public/displays public/_* -rf

all-clean:
	sudo rm public/displays public/galleries public/_* -rf

init:
	pipx install staticjinja
	pipx inject staticjinja Markdown jinja2-simple-tags pillow python-slugify

fetch-static:
	mkdir -p public/static/{css,js,img}
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css -o public/static/css/pico.min.css
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css -o public/static/css/pico.classless.min.css
	curl https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.fluid.classless.min.css -o public/static/css/pico.fluid.classless.min.css
	#curl https://cdn.jsdelivr.net/npm/swiffy-slider@1.6.0/dist/css/swiffy-slider.min.css -o public/static/css/swiffy-slider.min.css
	#curl https://cdn.jsdelivr.net/npm/swiffy-slider@1.6.0/dist/js/swiffy-slider.min.js -o public/static/js/swiffy-slider.min.js
	#curl https://app.unpkg.com/lightgallery@2.9.0-beta.1/css/lightgallery-bundle.min.css -o public/static/css/lightgallery-bundle.min.css
	#curl https://app.unpkg.com/lightgallery@2.9.0-beta.1/lightgallery.min.js -o public/static/js/lightgallery.min.js
	curl https://unpkg.com/photoswipe@5.4.2/dist/photoswipe.css -o public/static/css/photoswipe.css
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.js -o public/static/js/photoswipe-lightbox.esm.js
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.js.map -o public/static/js/photoswipe-lightbox.esm.js.map
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe.esm.js -o public/static/js/photoswipe.esm.js
	curl https://unpkg.com/photoswipe@5.4.4/dist/photoswipe.esm.js.map -o public/static/js/photoswipe.esm.js.map

serve:
	@ip -br -4 a show eth0
	cd public && python3 -m http.server -b 0.0.0.0

thumbnail:
ifndef in
	$(error in=/path/to/image required)
endif
ifndef out
	$(error out=/path/to/image required)
endif
	convert "$(in)" -fill black -colorize "75%" -resize 600x600 -gravity Center -pointsize 60 -fill white -annotate 0 "Image Gallery" "$(out)"


fussel-build:
	cd fussel && docker build -t fussel .

galleries:  # FIXME - 192 addr
	GALLERY_TITLE="Vimy 2025 Image Gallery" DISPLAY_URL="http://192.168.2.62:8000/displays/vimy-2025/" sigal build -c sigal/sigal.conf.py galleries/displays/vimy-2025/ public/galleries/displays/vimy-2025/ -n 1
