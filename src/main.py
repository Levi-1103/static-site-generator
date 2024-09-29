import os
import shutil

def main():
    source_dir = "static"
    dest_dir = "public"

   

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    copy_files(source_dir, dest_dir)

    


def copy_files(source_dir, dest_dir):

    paths = os.listdir(source_dir)

    for path in paths:
        combined_path = os.path.join(source_dir, path)
        if os.path.isfile(combined_path):
            shutil.copy(combined_path, dest_dir)
            # print("File" + combined_path)
        else:
            copy_files(combined_path, dest_dir)

        
        

def copy_files_using_shutil(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    shutil.copytree(source_dir, dest_dir)


if __name__ == "__main__":
    main()
