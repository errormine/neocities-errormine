import os
import sys
import json
from pathlib import Path
from string import Template

# Function to convert filename to title case
def title_case(filename):
    return ' '.join(word.capitalize() for word in filename.replace('.epub', '').replace('-', ' ').split())

# Function to extract last name from author's name
def get_last_name(author):
    return author.split()[-1]

# Check if JSON file already exists
json_file = 'books.json'
if os.path.exists(json_file):
    with open(json_file, 'r') as f:
        books = json.load(f)
else:
    books = []

# Get the list of EPUB files in the current directory
epub_files = [file for file in os.listdir() if file.endswith('.epub')]

# Process each EPUB file
for file in epub_files:
    # Check if the file already exists in the JSON file
    if any(book['filename'] == file for book in books):
        continue

    # Ask user for the author's name unless program argument is provided
    if len(sys.argv) > 1 and sys.argv[1] == '--generate-html':
        author = ''
    else:
        author = input(f"Enter the author of the book '{file}': ")

    # Add book to the list
    book = {
        'filename': file,
        'author': author,
        'is_epub': True
    }
    books.append(book)

# Sort the books by author's last name
books.sort(key=lambda x: get_last_name(x['author']))

# Save the updated JSON file
with open(json_file, 'w') as f:
    json.dump(books, f, indent=4)

# Check if program argument is provided to generate HTML
if len(sys.argv) > 1 and sys.argv[1] == '--generate-html':
    # HTML template
    html_template = Template('''
        <figure class="book">
            <a href="$href" class="overlay">$link_text</a>
            <img src="/library/covers/$filename.jpg" alt="" class="book-cover">
            <figcaption>
                <b>$title</b>
                <i>$author</i>
            </figcaption>
        </figure>
    ''')

    # Generate HTML for each book
    html_output = ''
    for book in books:
        filename = os.path.splitext(book['filename'])[0]  # Exclude file extension
        author = book['author']
        title = title_case(filename)
        
        if book['is_epub']:
            href = f'/library/books/{filename}.epub'
            link_text = 'DOWNLOAD'
        else:
            href = book.get('link', '')  # Use custom link from the JSON attribute "link"
            link_text = 'READ ONLINE'

        html = html_template.substitute(href=href, link_text=link_text, filename=filename, title=title, author=author)
        html_output += html.strip() + '\n\t'  # Append stripped HTML with new line and tab

    # Print the generated HTML
    print(html_output.strip())  # Strip leading/trailing whitespace from the final output
