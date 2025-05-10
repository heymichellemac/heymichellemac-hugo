import os
import frontmatter

content_dir = "content/blog"  # Change this if needed

for root, dirs, files in os.walk(content_dir):
    for filename in files:
        if filename.endswith(".md"):
            path = os.path.join(root, filename)
            post = frontmatter.load(path)

            keys_to_remove = [key for key in post.keys() if key.startswith("subtitle")]
            if keys_to_remove:
                for key in keys_to_remove:
                    del post[key]
                with open(path, "w", encoding="utf-8") as f:
                    f.write(frontmatter.dumps(post))
                print(f"Removed image fields from: {path}")
