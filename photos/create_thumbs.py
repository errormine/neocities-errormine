import os
from wand.image import Image
from PIL import Image as PILImage
from PIL.ExifTags import TAGS
import argparse

def get_date_taken(image_path):
    try:
        with PILImage.open(image_path) as img:
            info = img._getexif()
            if info is not None:
                for tag, value in info.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == 'DateTimeOriginal':
                        return value
    except (AttributeError, KeyError, IndexError):
        pass
    return None

def generate_html_only(img_dir):
    # Get a list of jpg files with date taken information
    image_files = []
    for filename in os.listdir(img_dir):
        if filename.endswith(".jpg"):
            date_taken = get_date_taken(f"{img_dir}/{filename}")
            if date_taken:
                image_files.append((filename, date_taken))

    # Sort files by date taken in descending order
    image_files.sort(key=lambda x: x[1], reverse=True)

    # Generate HTML element for each file
    for filename, date_taken in image_files:
        html_element = f"""            <figure>
                <a href="/photos/img/{filename}" class="glightbox">
                    <img src="/photos/img/thumbs/{filename.replace('.jpg', '.webp')}" alt="">
                </a>
            </figure>"""
        print(html_element)

def generate_thumbnails_and_html(img_dir, thumbs_dir):
    # Create thumbs directory if it doesn't exist
    os.makedirs(thumbs_dir, exist_ok=True)

    # Get a list of jpg files with date taken information
    image_files = []
    for filename in os.listdir(img_dir):
        if filename.endswith(".jpg"):
            date_taken = get_date_taken(f"{img_dir}/{filename}")
            if date_taken:
                image_files.append((filename, date_taken))

    # Sort files by date taken in descending order
    image_files.sort(key=lambda x: x[1], reverse=True)

    # Loop through sorted files, create thumbnails, and generate HTML
    for filename, date_taken in image_files:
        # Create thumbnail using ImageMagick
        with Image(filename=f"{img_dir}/{filename}") as img:
            img.resize(int(img.width * 0.2), int(img.height * 0.2))
            img.save(filename=f"{thumbs_dir}/{filename.replace('.jpg', '.webp')}")

        # Generate HTML element
        html_element = f"""            <figure>
                <a href="/photos/img/{filename}" class="glightbox">
                    <img src="/photos/img/thumbs/{filename.replace('.jpg', '.webp')}" alt="">
                </a>
            </figure>"""

        # Output HTML to console
        print(html_element)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate HTML and thumbnails for JPG images.')
    parser.add_argument('--html-only', action='store_true', help='Generate only HTML without processing images')
    args = parser.parse_args()

    img_dir = "img"
    thumbs_dir = "img/thumbs"

    if args.html_only:
        generate_html_only(img_dir)
    else:
        generate_thumbnails_and_html(img_dir, thumbs_dir)