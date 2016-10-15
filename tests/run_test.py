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
