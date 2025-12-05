import os
import shutil
import sys

from copy_static import copy_files_recursive
from gen_content import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
from_path = "./content"
to_path = "./docs"
template_path = "./template.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    
    print(
        f"Generating HTML from '{from_path}' using "
        f"'{template_path}', writing to '{to_path}'"
    )
    generate_pages_recursive(from_path, template_path, to_path, basepath)
    

main()

