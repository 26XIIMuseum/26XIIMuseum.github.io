
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
	pipx inject mkdocs mkdocs-get-deps==0.2.0 mkdocs-material==9.6.9 mkdocs-material-extensions==1.3.1 beautifulsoup4

.PHONY: serve
serve:
	mkdocs serve -v --watch-theme -a 0.0.0.0:8000


.PHONY: img-resize
img-resize:
	convert -background none -resize 1200x800 -gravity center -extent 1200x800 -alpha on $(src) $(dst)

# FIXME - create all
.PHONY: qr-codes
qr-codes:
	qrencode -t svg -l H -o content/displays/dragoons/qr-code.svg https://jakegatsby.github.io/displays/dragoons/


.PHONY: clean
clean:
	rm ../css ../displays ../js ../search ../sitemap.xml ../sitemap.xml.gz -rf


.PHONY: build
build: clean
	mkdocs build --clean -d public/
	mv public/* ../
	rmdir public/
	rm ../search -rf
