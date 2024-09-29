import os
import shutil

# Own Implementation using recursion
def copy_files(source_dir, dest_dir):

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    
    paths = os.listdir(source_dir)

    for path in paths:
        from_path = os.path.join(source_dir, path)
        dest_path = os.path.join(dest_dir, path)
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files(from_path, dest_path)

        

# Implementation using shutil library
def copy_files_using_shutil(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    shutil.copytree(source_dir, dest_dir)