import os
import shutil

from copy_static import copy_files_recursive
from gen_content import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
from_path = "./content/index.md"
to_path = "./public/index.html"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    
    print(
        f"Generating HTML from '{from_path}' using "
        f"'{template_path}', writing to '{to_path}'"
    )
    generate_page(from_path, template_path, to_path)


main()

