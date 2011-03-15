import docutils.core
from rezine.i18n import _
from rezine.parsers import BaseParser
from rezine.utils.zeml import parse_html

# necessary for docutils directive registrations
from rezine_rst import directives


class RSTParser(BaseParser):
    """A reStructured Text parser."""

    name = _(u'Rezine-rST')
    settings = dict(file_insertion_enabled=0,
                    raw_enabled=0,
                    output_encoding='unicode',
                    input_encoding='unicode',
                    initial_header_level=4)

    def parse(self, input_data, reason):
        parts = docutils.core.publish_parts(
            input_data, writer_name='html', settings_overrides=self.settings)
        return parse_html(parts['html_body'])


def setup(app, plugin):
    app.add_parser('rezine_restructuredtext', RSTParser)
