"""
file: txt2soup.py
author: Mason Armand
date created: Dec 23, 2023
last modified: Dec 23, 2023
"""
import os
import sys
import markdown2
from datetime import datetime


def main() -> None:
    argc: int = len(sys.argv)
    dest: str = ""
    src: str = ""
    template: str = ""
    postdir: str = ""
    posts: list = []

    if argc < 3:
        print(f"Usage: {sys.argv[0]} <source directory> <destination directory>")
        exit(1)

    dest = os.path.normpath(sys.argv[2])
    src = os.path.normpath(sys.argv[1])
    template = os.path.join("_templates", "template.html")
    postdir = os.path.join(dest, "posts")

    if not os.path.isdir(src):
        print(f"ERROR: Source directory '{src}' does not exist")
        exit(1)

    os.makedirs(dest, exist_ok=True)
    os.makedirs(postdir, exist_ok=True)

    for filename in os.listdir(src):
        if filename.endswith(".md"):
            # Extract date from the filename
            date_parts = filename.split('-')[:3]  # Take the first three parts
            date_str = '-'.join(date_parts)  # Join the parts to get the date string
            
            # Convert date string to datetime object if needed
            # Example: date_object = datetime.strptime(date_str, "%Y-%m-%d")
            
            with open(os.path.join(src, filename), 'r', encoding="utf-8") as f:
                content = f.read()
                metadata, md_content = extract_metadata(content)
                
                # Append the date to the metadata hashtable
                metadata['date'] = date_str
                
                html_content = convert_to_html(template, md_content, metadata)
                post_filename = os.path.join(postdir, filename.replace('.md', '.html'))
                
                with open(post_filename, 'w') as html_file:
                    html_file.write(html_content)
                
                posts.append((metadata, post_filename))

    create_index(src, dest, posts)


def create_index(src: str, dest: str, posts: list) -> None:
    """
    create index.html from template in src directory

    args:
        src: src directory containig the template
        dest: destination directory to write to
        posts: lists of post metadata and filenames for the nav links
    """
    index_template_path: str = os.path.join("_templates", 'index.html')
    nav_html: str = "<ol class='links-list'>\n"

    for post_metadata, post_filename in posts:
        relative_link: str = os.path.relpath(post_filename, dest)
        nav_html += f'    <li><span>{post_metadata["date"]}</span><a href="{relative_link}">{post_metadata["title"]}</a></li>\n'
    nav_html += "  </ol>\n"
    index_content: str = ""
    err = False

    try:
        with open(index_template_path, 'r', encoding="utf-8") as f:
            index_content = f.read()
    except FileNotFoundError:
        print(f"Warning: index.html template not found in '{src}'.")
        err = True
    except IOError:
        print(f"Warning: unable to read from index.html from '{src}'.")
        err = True

    # create index page
    with open(f"{dest}/index.html", 'w', encoding="utf-8") as index_file:
        if err:
            index_file.write(nav_html)
        else:
            index_html: str = index_content.replace("{nav}", nav_html)
            index_file.write(index_html)



def extract_metadata(content: str) -> tuple[dict[str, str], str]:
    """
    Get keywords and their values in the metadata headers
    and puts them into a hashtable.

    args:
        content - markdown content
    returns - tuple containing hashtable and str containing rest of md content
    """
    lines: list = content.split("\n")
    metadata: dict = {}

    if '---' not in lines:
        print(f"ERROR: Metadata delimiter '---' not found in blog post.")
        exit(1)

    for line in lines[1:lines.index('---', 1)]:
        key, val = line.split(':', 1)
        metadata[key.strip()] = val.strip()

    return metadata, '\n'.join(lines[lines.index('---', 1) + 1:])


def convert_to_html(template_file: str, md: str, metadata: dict[str, str]) -> str:
    """
    Converts markdown to html blog posts
    args:
        template_file - blog template html file
        md - markdown content
        metadata - metadata hashtable
    returns: HTML content of blog post as a str
    """
    html: str = markdown2.markdown(md)
    full_html: str = ""
    template_content: str = ""
    err = False

    html = html.replace("{title}", metadata["title"])
    html = html.replace("{date}", metadata["date"])

    try:
        with open(template_file, 'r', encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Warning: template.html not found")
        err = True
    except IOError:
        print(f"Warning: unable to read from template.html")
        err = True

    if err:
        return html

    date_obj = datetime.strptime(metadata["date"], "%Y-%M-%d")
    new_date = date_obj.strftime("%B %d, %Y")

    full_html = template_content.replace("{title}", metadata["title"])
    full_html = full_html.replace("{description}", metadata["description"])
    full_html = full_html.replace("{date}", new_date)
    full_html = full_html.replace("{md}", html)

    return full_html

if __name__ == "__main__":
    main()
