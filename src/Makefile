
# FIXME
# slugify

.PONY: help
help:
	@echo "serve"
	@echo "clean"
	@echo "build"

.PHONY: dev
dev:
	pipx install mkdocs
	pipx inject mkdocs mkdocs-material

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
