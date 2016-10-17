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
