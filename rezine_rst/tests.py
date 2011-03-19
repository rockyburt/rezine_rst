import unittest


class PackageTests(unittest.TestCase):
    def test_rst_parser(self):
        from rezine_rst import RSTParser
        parser = RSTParser(None)

        # replace docutils_publish because we don't need to test docutils
        def publish(*args, **kwargs):
            return {'args': args,
                    'kwargs': kwargs,
                    'html_body': 'foo'}
        parser.docutils_publish = publish

        from rezine.utils.zeml import RootElement
        self.assertTrue(isinstance(parser.parse('abc', None), RootElement))

    def test_setup(self):
        from rezine_rst import setup, RSTParser

        run = []

        class App(object):
            def add_parser(self, *args, **kwargs):
                run.append((args, kwargs))

        setup(App(), None)
        self.assertEqual(run,
                         [(('rezine_restructuredtext', RSTParser), {})])
