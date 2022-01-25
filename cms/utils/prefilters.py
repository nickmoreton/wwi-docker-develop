from bs4 import BeautifulSoup
from wagtail_wordpress_import.block_builder_defaults import get_or_save_image
from wagtail_wordpress_import.prefilters.handle_shortcodes import (
    BlockShortcodeHandler,
    register,
)


@register()
class AnchorImageHandler(BlockShortcodeHandler):
    shortcode_name = "anchor_image"

    def pre_filter(self, string):
        soup = BeautifulSoup(string, "html.parser")
        anchor_tags = soup.find_all("a")

        anchors = []
        for anchor in anchor_tags:
            if anchor.find("img"):
                anchors.append(anchor)

        for a in anchors:
            attrs = {}
            attrs["data-src"] = a.find("img").attrs["src"]
            attrs["data-href"] = a.attrs["href"]
            replacement_custom_tag = soup.new_tag(self.element_name)
            replacement_custom_tag.attrs = attrs
            a.replace_with(replacement_custom_tag)

        return str(soup)

    def construct_block(self, soup):
        image_file = get_or_save_image(soup.attrs["data-src"])

        if image_file:
            # The implementation here uses the provided ImageBlock which has
            # caption and alignment fields.
            # If you need these fields to be populated the values could be
            # extacted in the pre_filter method and passed as attrs to
            # Beautiful Soup when the custom tag is created.
            return {
                "type": "image",
                "value": {
                    "image": image_file.id,
                    "caption": "",
                    "alignment": "",
                    "link": soup.attrs.get("data-href"),
                },
            }
        else:
            # This is to prevent the import from
            # failing if the image is unreachable.
            return {
                "type": "raw_html",
                "value": str(soup),
            }
