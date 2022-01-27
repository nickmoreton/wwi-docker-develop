# PROVIDED BY PACKAGE
"""Enable CATEGORIES import"""
WAGTAIL_WORDPRESS_IMPORT_CATEGORY_PLUGIN_ENABLED = True
WAGTAIL_WORDPRESS_IMPORT_CATEGORY_PLUGIN_MODEL = "pages.models.Category"

# SPECIFIC USE CASE
"""Enable ITEMS import
This imports header images. See pages/import_hooks.py for more info."""
# the wp:postmeta key to search for leading _ is removed also any : is replaced with _
# WORDPRESS_IMPORT_HOOKS_ITEMS_TO_CACHE = {
#     "attachment": {  # the item of type
#         "DATA_TAG": "thumbnail_id",
#         "FUNCTION": "pages.import_hooks.header_image",
#     }
# }

"""Enable TAGS import
This import authors. See pages/import_hooks.py for more info."""
# WORDPRESS_IMPORT_HOOKS_TAGS_TO_CACHE = {
#     "wp:author": {  # the XML tag (top level)
#         "DATA_TAG": "dc_creator",  # the item tag to get value of
#         "FUNCTION": "pages.import_hooks.authors",
#     }
# }

"""Misc settings"""

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'wordpresswagtail',
#         'USER': 'wordpresswagtail',
#         'PASSWORD': 'wordpresswagtail',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# WAGTAILADMIN_RICH_TEXT_EDITORS = {
#     "default": {
#         "WIDGET": "wagtail.admin.rich_text.DraftailRichTextArea",
#         "OPTIONS": {
#             "features": [
#                 "anchor-identifier",
#                 "h1",
#                 "h2",
#                 "h3",
#                 "h4",
#                 "h5",
#                 "h6",
#                 "bold",
#                 "italic",
#                 "ol",
#                 "ul",
#                 "hr",
#                 "link",
#                 "document-link",
#                 "image",
#                 "embed",
#                 "superscript",
#                 "subscript",
#                 "strikethrough",
#                 "blockquote",
#                 "stock",
#                 "earningpotential",
#             ]
#         },
#     }
# }

# WAGTAIL_WORDPRESS_IMPORTER_INLINE_SHORTCODE_HANDLERS = [
#     "pages.inline_shortcodes.stock_handler",
# ]

# WAGTAIL_WORDPRESS_IMPORT_PREFILTERS = [
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.linebreaks_wp",
#     },
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.transform_shortcodes",
#     },
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.transform_inline_styles",
#     },
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.bleach_clean",
#         "OPTIONS": {
#             "ADDITIONAL_ALLOWED_ATTRIBUTES": {
#                 "wagtail_block_anchor_image": "data-href",
#                 "wagtail_block_anchor_image": "data-src",
#             },
#         },
#     },
# ]

# WAGTAIL_WORDPRESS_IMPORT_PREFILTERS = [
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.linebreaks_wp",
#     },
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.transform_inline_styles",
#     },
#     {
#         "FUNCTION": "wagtail_wordpress_import.prefilters.bleach_clean",
#         "OPTIONS": {
#             "ADDITIONAL_ALLOWED_TAGS": ["h9"],
#             "ADDITIONAL_ALLOWED_ATTRIBUTES": {"*": ["id"]},
#             "ADDITIONAL_ALLOWED_STYLES": [
#                 "font-weight: bold",
#                 "font-style: italic",
#             ],
#         },
#     },
# ]

# WAGTAIL_WORDPRESS_IMPORT_DEBUG = True

# WAGTAIL_WORDPRESS_IMPORT_YOAST_PLUGIN_ENABLED = True

# WAGTAIL_WORDPRESS_IMPORT_YOAST_PLUGIN_MAPPING = {
#     "xml_item_key": "wp:postmeta",
#     "description_key": "wp:meta_key",
#     "description_value": "wp:meta_value",
#     "description_key_value": "_yoast_wpseo_metadesc",
# }

# WAGTAIL_WORDPRESS_IMPORTER_CONVERT_HTML_TAGS_TO_BLOCKS = {
#     "h1": "wagtail_wordpress_import.block_builder_defaults.build_heading_block",
#     "table": "wagtail_wordpress_import.block_builder_defaults.build_table_block",
#     "iframe": "wagtail_wordpress_import.block_builder_defaults.build_iframe_block",
#     "form": "wagtail_wordpress_import.block_builder_defaults.build_form_block",
#     "img": "wagtail_wordpress_import.block_builder_defaults.build_image_block",
#     "blockquote": "wagtail_wordpress_import.block_builder_defaults.build_block_quote_block",
# }
