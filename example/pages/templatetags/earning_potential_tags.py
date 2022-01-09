import re
from django import template

register = template.Library()


def earning_potential(value):

    """\[(?P<attrs>.*)(?:\])"""  # from regex101
    return re.compile(
        r"\["  # matches the opening [
        + self.shortcode_name
        + r"\b"  # matches a word boundary
        + r"(?P<attrs>[^\]]*)"  # capture 'attrs', matching anything but ]
        + r"\]"  # matches the closing ] of the opening tag
        + r"(?P<content>.*?)"  # non-greedily captures 'content' between the tags
        + r"\[\/"  # matches the  [/ of the closing tag
        + self.shortcode_name
        + r"\]"  # matches the closing ]
    )

    regex = r"(?:\[earningPotential)\b(?P<attrs>.*)(?:\])"

    # match = re.search(regex, str(value), re.MULTILINE | re.UNICODE)
    # print(match)
    matches = re.findall(regex, str(value))
    # matches = re.findall(regex, str(value), re.MULTILINE | re.UNICODE)
    for match_obj in matches:
        print(match_obj)
    # attrs = match.group('attrs')

    subst = "<aside></aside>"

    result = re.sub(regex, subst, str(value), 0)
    return result


register.filter("earning_potential", earning_potential)
