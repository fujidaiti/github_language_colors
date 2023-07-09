import yaml
import sys
from jinja2 import Template


def load_palette(src_file):
    languages = yaml.safe_load(src_file)
    return {
        name: meta["color"].replace("#", "0x", 1)
        for (name, meta) in languages.items()
        if "color" in meta
    }


def inject(palette):
    with open("templates/github_language_colors.dart.jinja") as f:
        template = Template(f.read())
    return template.render(palette=palette)


if __name__ == "__main__":
    src_file = sys.argv[1]
    with open(src_file) as f:
        palette = load_palette(f)
    print(inject(palette))
