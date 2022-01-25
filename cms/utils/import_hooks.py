from pages.models import Author
from wagtail_wordpress_import.block_builder_defaults import get_or_save_image


# See pages/models.py:
def header_image(imported_pages, data, items_cache):
    print("Importing header image")
    """use this for the import authors version"""
    lookup = f"wp_post_meta__{data}"
    for attachment in items_cache:
        thumbnail_id = attachment.get("wp:post_id")
        pages = imported_pages.filter(**{lookup: thumbnail_id})
        if pages.exists():
            image = get_or_save_image(attachment.get("guid"))
            pages.update(header_image=image)
            print("Attaching header images to pages:", pages)


# See pages/models.py:
def authors(imported_pages, data, tags_cache):
    print("Importing authors")
    # breakpoint()
    lookup = f"wp_post_meta__{data}"
    for author in tags_cache:
        author_login = author.get("wp:author_login")
        pages = imported_pages.filter(**{lookup: author_login})
        if pages:
            first_name = (
                author.get("wp:author_first_name")
                if author.get("wp:author_first_name")
                else "not"
            )
            last_name = (
                author.get("wp:author_last_name")
                if author.get("wp:author_last_name")
                else "known"
            )
            email_address = author.get("wp:author_email")
            obj, created = Author.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                email_address=email_address,
            )
            if pages.exists():
                pages.update(author=obj)
                print("Attaching authors to pages:", pages)
