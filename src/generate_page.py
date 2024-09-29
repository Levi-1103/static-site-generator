import os
import pathlib

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("MD needs to start with title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    f = open(from_path, "r")
    markdown = f.read()
    f.close()

    f = open(template_path)
    template = f.read()
    f.close()

    html = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    f = open(dest_path, "w")
    f.write(template)
    f.close()


def generate_pages_recursive(content_dir, template_path, public_dir):

    paths = os.listdir(content_dir)
    for path in paths:
        from_path = os.path.join(content_dir, path)
        dest_path = os.path.join(public_dir, path)

        if os.path.isfile(from_path):
            dest_path = pathlib.Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)