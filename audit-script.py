import os
import frontmatter

root_directory = "content/blog"  # Change this if needed

# Walk through the directory to find all Markdown files
for root, dirs, files in os.walk(root_directory):
    for file in files:
        # Process only Markdown files
        if file.endswith('.md'):
            file_path = os.path.join(root, file)

            # Read the front matter from the Markdown file
            post = frontmatter.load(file_path)

            # Check if 'width' exists and if its value is 'full'
            if post.metadata.get('width') == 'full':
                # Change 'full' to 'wide'
                post.metadata['width'] = 'wide'

                # Save the modified front matter back to the file
                frontmatter.dump(post, file_path)

                print(f"Changed 'width: full' to 'width: wide' in {file_path}")
            else:
                print(f"Skipping {file_path} as 'width' is not 'full'.")