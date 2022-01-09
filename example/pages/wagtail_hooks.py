import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.core import hooks

from draftjs_exporter.dom import DOM
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineEntityElementHandler,
)

""" Uncomment to use inline shortcodes handler"""
# @hooks.register("register_rich_text_features")
# def register_stock_feature(features):
#     features.default_features.append("stock")
#     """
#     Registering the `stock` feature, which uses the `STOCK` Draft.js entity type,
#     and is stored as HTML with a `<span data-stock>` tag.
#     """
#     feature_name = "stock"
#     type_ = "STOCK"

#     control = {
#         "type": type_,
#         "label": "$",
#         "description": "Stock",
#     }

#     features.register_editor_plugin(
#         "draftail",
#         feature_name,
#         draftail_features.EntityFeature(
#             control, js=["stock.js"], css={"all": ["stock.css"]}
#         ),
#     )

#     features.register_converter_rule(
#         "contentstate",
#         feature_name,
#         {
#             # Note here that the conversion is more complicated than for blocks and inline styles.
#             "from_database_format": {
#                 "span[data-stock]": StockEntityElementHandler(type_)
#             },
#             "to_database_format": {
#                 "entity_decorators": {type_: stock_entity_decorator}
#             },
#         },
#     )


# def stock_entity_decorator(props):
#     """
#     Draft.js ContentState to database HTML.
#     Converts the STOCK entities into a span tag.
#     """
#     return DOM.create_element(
#         "span",
#         {
#             "data-stock": props["stock"],
#         },
#         props["children"],
#     )


# class StockEntityElementHandler(InlineEntityElementHandler):
#     """
#     Database HTML to Draft.js ContentState.
#     Converts the span tag into a STOCK entity, with the right data.
#     """

#     mutability = "IMMUTABLE"

#     def get_attribute_data(self, attrs):
#         """
#         Take the ``stock`` value from the ``data-stock`` HTML attribute.
#         """
#         return {
#             "stock": attrs["data-stock"],
#         }


# @hooks.register("register_rich_text_features")
# def register_earning_potential_feature(features):
#     features.default_features.append("earningpotential")
#     """
#     Registering the `earning potential` feature, which uses the `STOCK` Draft.js entity type,
#     and is stored as HTML with a `<span data-earningpotenital>` tag.
#     """
#     feature_name = "earningpotential"
#     type_ = "EARNINGPOTENTAIL"

#     control = {
#         "type": type_,
#         "label": "£",
#         "description": "Earning Potential",
#     }

#     features.register_editor_plugin(
#         "draftail",
#         feature_name,
#         draftail_features.EntityFeature(control, js=["ep.js"], css={"all": ["ep.css"]}),
#     )

#     features.register_converter_rule(
#         "contentstate",
#         feature_name,
#         {
#             # Note here that the conversion is more complicated than for blocks and inline styles.
#             "from_database_format": {
#                 "span[data-earningpotential]": EarningPotentialEntityElementHandler(
#                     type_
#                 )
#             },
#             "to_database_format": {
#                 "entity_decorators": {type_: earning_potential_entity_decorator}
#             },
#         },
#     )


# def earning_potential_entity_decorator(props):
#     """
#     Draft.js ContentState to database HTML.
#     Converts the STOCK entities into a span tag.
#     """
#     return DOM.create_element(
#         "span",
#         {
#             "data-earningpotential": props["eariningpotential"],
#         },
#         props["children"],
#     )


# class EarningPotentialEntityElementHandler(InlineEntityElementHandler):
#     """
#     Database HTML to Draft.js ContentState.
#     Converts the span tag into a STOCK entity, with the right data.
#     """

#     mutability = "IMMUTABLE"

#     def get_attribute_data(self, attrs):
#         """
#         Take the ``stock`` value from the ``data-stock`` HTML attribute.
#         """
#         return {
#             "earningpotential": attrs["data-earningpotential"],
#         }
