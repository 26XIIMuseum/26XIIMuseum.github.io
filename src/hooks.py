import os
from pathlib import Path

import markdown

IMAGE_SUFFIXES = [
  ".jpg",
  ".jpeg",
]

def on_config(config):
  global BASEDIR
  BASEDIR = Path(config["docs_dir"])


def is_display(page):
	return Path(page.url).parent.name == "displays"

def is_artifact(page):  
  return Path(page.url).parent.name == "artifacts"
  
def get_page_title(page=None, page_dir=None):
  if page_dir:
    index_data = (page_dir / "index.md").read_text(encoding="utf-8")
  md = markdown.Markdown(extensions=['meta'])
  md.convert(index_data)
  return md.Meta["title"][0]
  

def get_display(page):  
  return {
    "title": get_page_title(page_dir=Path(page.file.abs_src_path).parent.parent.parent),
    "url": "/" + str(Path(page.url).parent.parent) + "/"
  }
	
def get_artifacts(page):
  artifacts = []
  for artifact_dir in (BASEDIR / Path(page.url) / "artifacts").glob("*"):
    url = str(artifact_dir).replace(str(BASEDIR), "") + "/"
    title = get_page_title(page_dir=artifact_dir)
    artifacts.append({
      "title": title,
      "url": url,
    })   
  return sorted(artifacts, key=lambda a: a["url"])


def get_audio(page):
  return "audio.mp3" if (BASEDIR / page.url / "audio.mp3").exists() else None


def get_images(page):	
  return [p.name for p in (BASEDIR / page.url).glob("*") if p.suffix in IMAGE_SUFFIXES]


def on_env(env, config, files):
  env.filters["get_audio"] = get_audio
  env.filters["get_images"] = get_images
  env.filters["is_display"] = is_display
  env.filters["is_artifact"] = is_artifact
  env.filters["get_display"] = get_display  
  env.filters["get_artifacts"] = get_artifacts
  return env
