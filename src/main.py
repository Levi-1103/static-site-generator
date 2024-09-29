import os
import shutil

from copystatic import copy_files
from generate_page import generate_pages_recursive

static_dir = "./static"
public_dir = "./public"
content_dir = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    print("Copying static files to public directory")
    copy_files(static_dir, public_dir)
    
    
    generate_pages_recursive(content_dir, template_path, public_dir)

   


if __name__ == "__main__":
    main()
