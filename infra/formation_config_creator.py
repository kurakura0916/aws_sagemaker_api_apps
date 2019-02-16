import os

from jinja2 import Environment, FileSystemLoader, Template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join("cloudformation.yml.tpl")
OUTPUT = os.path.join(BASE_DIR, "cloudformation.yml")


def get_template(file) -> Template:
    env = Environment(loader=FileSystemLoader(BASE_DIR))
    template = env.get_template(file)
    return template


def create_formation(file_name, text):
    with open(file_name, "w") as file:
        file.write(text)


if __name__ == '__main__':
    print(BASE_DIR)
    template = get_template(TEMPLATE)
    formation = template.render()
    create_formation(OUTPUT, formation)



