from slugify import slugify
import uuid

def generate_slug(title: str) -> str:
    base_slug = slugify(title)
    return base_slug
