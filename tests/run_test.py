try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import unittest

import jqp


class RunTest(unittest.TestCase):

    def test1(self):
        inputs = StringIO('''{"name": "Taro", "age": 10}
''')
        outputs = StringIO()
        jqp.run(inputs, outputs, 'j["name"]')
        self.assertEqual(outputs.getvalue(), '"Taro"\n')

    def test_import(self):
        inputs = StringIO('''{"name": "Taro", "age": 10}
''')
        outputs = StringIO()
        jqp.run(inputs, outputs, 're.sub("a", "A", j["name"])', imports=['re'])
        self.assertEqual(outputs.getvalue(), '"TAro"\n')

    def test_sort_keys(self):
        # This command ignores input
        inputs = StringIO('''1
''')
        outputs = StringIO()
        jqp.run(inputs, outputs, '{"a": 0, "b": 0, "c": 0}', sort_keys=True)
        self.assertEqual(outputs.getvalue(), '{"a": 0, "b": 0, "c": 0}\n')

    def test_raw_input(self):
        inputs = StringIO(' a \n')
        outputs = StringIO()
        jqp.run(inputs, outputs, 'j', raw_input_mode=True)
        self.assertEqual(outputs.getvalue(), '" a "\n')

    def test_raw_output(self):
        # This command ignores input
        inputs = StringIO('''1
''')
        outputs = StringIO()
        jqp.run(inputs, outputs, '"a"', raw_output=True)
        self.assertEqual(outputs.getvalue(), 'a\n')

    def test_join_output(self):
        inputs = StringIO('''1
2''')
        outputs = StringIO()
        jqp.run(inputs, outputs, 'j', join_output=True)
        self.assertEqual(outputs.getvalue(), '12')

    def test_ascii(self):
        # This command ignores input
        inputs = StringIO('''1
''')
        outputs = StringIO()
        # This is a Japanese character
        jqp.run(inputs, outputs, u'"\u3042"', ascii_output=True)
        self.assertEqual(outputs.getvalue(), '"\\u3042"\n')

    def test_parse_error(self):
        inputs = StringIO('invalid\n')
        outputs = StringIO()
        with self.assertRaises(SystemExit) as e:
            jqp.run(inputs, outputs, 'j')
        self.assertEqual(e.exception.code, 4)

    def test_execution_error(self):
        inputs = StringIO('1\n')
        outputs = StringIO()
        with self.assertRaises(SystemExit) as e:
            jqp.run(inputs, outputs, 'invalid')
        self.assertEqual(e.exception.code, 3)

    def test_dump_error(self):
        inputs = StringIO('1\n')
        outputs = StringIO()
        with self.assertRaises(SystemExit) as e:
            jqp.run(inputs, outputs, 'lambda: 0')
        self.assertEqual(e.exception.code, 3)

    def test_import_error(self):
        inputs = StringIO('1\n')
        outputs = StringIO()
        with self.assertRaises(SystemExit) as e:
            jqp.run(inputs, outputs, 'j', imports=['unknown_module'])
        self.assertEqual(e.exception.code, 5)
