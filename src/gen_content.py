import re
import os

from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str) -> str:
    matches = re.search(r"^#\s+(.*)", markdown, re.MULTILINE)
    if matches:
        return matches.group(1).strip()
    
    raise ValueError("markdown missing title")

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print("Generating page from {from_path} to {dest_path} using {template_path}")
    
    try:
        content = Path(from_path).read_text()
        template = Path(template_path).read_text()
    except Exception as e:
        print(f"error: reading contents from {from_path}: {e}")

    html_title = extract_title(content)
    html_doc = markdown_to_html_node(content).to_html()
    html_doc = re.sub(r'href=\"\/', f'href=\"{basepath}', html_doc) 
    html_doc = re.sub(r'src=\"\/', f'src=\"{basepath}', html_doc)
    print(html_title, html_doc)
    

    template = re.sub("{{ Title }}", html_title, template, flags=re.MULTILINE)
    template = re.sub("{{ Content }}", html_doc, template, flags=re.MULTILINE)

    Path(dest_path).write_text(template)

def generate_pages_recursive(
        source_dir_path: str,
        template_path: str,
        dest_dir_path: str,
        basepath: str
) -> None:
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        dest_filepath = dest_path[:-2]
        dest_filepath += "html"
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_filepath, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

