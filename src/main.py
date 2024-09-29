import os
import shutil

def main():
    source_dir = "static"
    dest_dir = "public"

    copy_files(source_dir, dest_dir)

    


def copy_files(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    shutil.copytree(source_dir, dest_dir)


if __name__ == "__main__":
    main()
