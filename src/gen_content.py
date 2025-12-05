import re

from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str) -> str:
    matches = re.search(r"^#\s+(.*)", markdown, re.MULTILINE)
    if matches:
        return matches.group(1).strip()
    
    raise ValueError("markdown missing title")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print("Generating page from {from_path} to {dest_path} using {template_path}")
    
    try:
        content = Path(from_path).read_text()
        template = Path(template_path).read_text()
    except Exception as e:
        print(f"error: reading contents from {from_path}: {e}")

    html_title = extract_title(content)
    html_doc = markdown_to_html_node(content).to_html()
    print(html_title, html_doc)
    
    template = re.sub("{{ Title }}", html_title, template, flags=re.MULTILINE)
    template = re.sub("{{ Content }}", html_doc, template, flags=re.MULTILINE)

    Path(dest_path).write_text(template)
