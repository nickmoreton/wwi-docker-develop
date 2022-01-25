from wagtail_wordpress_import.handle_inline_shortcodes import InlineShortcodeHandler


# Subclasses should declare a shortcode_name and provide
# a construct_html_tag method for converting the shortcode to a HTML tag.
# @register()
class StockHandler(InlineShortcodeHandler):
    """
    The Wordpress shortcode is replaced by a custom HTML tag. The shortcode attrubutes
    are preserved and can be included in the custom HTML tag.

    Sample wordpress stock shortcode:
    [stock symbol="TSLA"]

    all matching shortcodes are replaced by:

    <span data-stock="TSLA">$TSLA</span>
    """

    # The shortcode name that appears after the first "["
    # The matching for the shortcode name will end at the first space
    shortcode_name = "stock"

    def construct_html_tag(self, html):
        # Generate an HTML tag that will
        # entirely replace the occurrence of all matching shortcodes
        # in the html string.

        matches = self._pattern.finditer(html)

        for match in matches:
            attrs = self.get_shortcode_attrs(match.groupdict()["attrs"])
            html = html.replace(
                match.group(),
                f'<{self.element_name} data-{self.shortcode_name}="{attrs["symbol"]}">${attrs["symbol"]}</span>',
            )

        return html


stock_handler = StockHandler()


# Subclasses should declare a shortcode_name and provide
# a construct_html_tag method for converting the shortcode to a HTML tag.
# @register()
class EarningPotentialHandler(InlineShortcodeHandler):
    """
    The Wordpress shortcode is replaced by a custom HTML tag. The shortcode attrubutes
    are preserved and can be included in the custom HTML tag.

    Sample wordpress stock shortcode:
    [stock symbol="TSLA"]

    all matching shortcodes are replaced by:

    <span data-stock="TSLA">$TSLA</span>

    Snippet frontend html:

    <aside class="flair-earningPotential nitro-offscreen" data-uw-rm-sr="">
        <strong>Earning Potential</strong> $50,371
        <span class="earning__timeframe">/yr</span>
        <a href="#/" class="" data-toggle="tooltip" data-placement="bottom" title=""
            data-original-title="Every bit you make or save each month gets you closer to financial independence.
            Create an account to calculate how many days of freedom this will earn you in the future."
            data-uw-rm-brl="false" aria-label="question-circle" data-uw-rm-empty-ctrl="">
            <i class="fas fa-question-circle"></i>
        </a>
    </aside>

    """

    # The shortcode name that appears after the first "["
    # The matching for the shortcode name will end at the first space
    shortcode_name = "earningPotential"
    # element_name = "aside"

    def construct_html_tag(self, html):
        # Generate an HTML tag that will
        # entirely replace the occurrence of all matching shortcodes
        # in the html string.

        matches = self._pattern.finditer(html)

        for match in matches:
            attrs = self.get_shortcode_attrs(match.groupdict()["attrs"])
            html = html.replace(
                match.group(),
                f'<{self.element_name} data-{self.shortcode_name}="[amount:{attrs["amount"]};timeframe:{attrs["timeframe"]}]">{attrs["amount"]} {attrs["timeframe"]}</{self.element_name}>',  ## noqa
            )

        return html


earning_potential_handler = EarningPotentialHandler()
