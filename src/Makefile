
# FIXME
# slugify

.PONY: help
help:
	@echo "serve"
	@echo "clean"
	@echo "build"

.PHONY: dev
dev:
	pipx install -f mkdocs==1.6.1
	pipx inject mkdocs mkdocs-get-deps==0.2.0 mkdocs-material==9.6.9 mkdocs-material-extensions==1.3.1 mkdocs-macros-plugin

.PHONY: serve
serve:
	mkdocs serve -v -a 0.0.0.0:8000


.PHONY: static-serve
static-serve:
	cd ../ && python -m http.server

.PHONY: img-resize
img-resize:
	convert -background none -resize 1200x800 -gravity center -extent 1200x800 -alpha on $(src) $(dst)

# FIXME - create all
.PHONY: qr-codes
qr-codes:
	qrencode -t svg -l H -o content/displays/dragoons/qr-code.svg https://jakegatsby.github.io/displays/dragoons/


.PHONY: clean
clean:
	cd ../ && rm 404.html  assets  css  displays  events  js  sitemap.xml  sitemap.xml.gz -rf


.PHONY: build
build: clean
	mkdocs build --clean -d public/
	mv public/* ../
	rmdir public/
	rm ../search -rf
