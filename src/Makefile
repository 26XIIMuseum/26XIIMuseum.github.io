
# FIXME
# slugify

.PHONY: install
install:
	# FIXME - install mkdocs and markdown in a venv

.PHONY: serve
serve:
	mkdocs serve -v --watch-theme -a 0.0.0.0:8000

.PHONY: mogrify
mogrify:
	find content/displays/ -name *.jpg -exec mogrify -resize 1200x800 -background black -gravity center -extent 1200x800 {} \;

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
