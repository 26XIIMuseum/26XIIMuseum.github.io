MAKEFLAGS := --always-make

build: clean
	~/.local/share/pipx/venvs/staticjinja/bin/python build.py
	cp src/displays/vimy-2025/*.png public/displays/vimy-2025/  # FIXME single static directory

clean:
	rm public/* -rf

init:
	pipx install staticjinja
	pipx inject staticjinja Markdown
