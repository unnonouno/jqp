try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
import unittest

import jqp


class RunTest(unittest.TestCase):

    def test1(self):
        inputs = StringIO.StringIO('''{"name": "Taro", "age": 10}
''')
        outputs = StringIO.StringIO()
        jqp.run(inputs, outputs, 'j["name"]')
        self.assertEqual(outputs.getvalue(), '"Taro"\n')
