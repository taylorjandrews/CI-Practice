"""
Tests for HelloWorld program
"""

from HelloWorld import run
import unittest

class TestHelloWorld(unittest.TestCase):
    def test_text_match(self):
        expected = 'Hello World!'
        self.assertEqual(expected, run())

if __name__ == '__main__':
    unittest.main()
