import unittest
from io import StringIO
import sys
from decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_single_dot(self):
        test_cases = [
            ('абра-кадабра.', 'абра-кадабра'),
            ('абр......a.', 'a'),
            ('.', ''),
            ('1.2.3', '123')
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                self.assertEqual(decrypt(input_str), expected)

    def test_double_dots(self):
        test_cases = [
            ('абраа..-кадабра', 'абра-кадабра'),
            ('абра--..кадабра', 'абра-кадабра'),
            ('1..2.3', '23'),
            ('абр......a', 'a')
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                self.assertEqual(decrypt(input_str), expected)

    def test_combined_dots(self):
        test_cases = [
            ('абраа..-.кадабра', 'абра-кадабра'),
            ('абрау...-кадабра', 'абра-кадабра'),
            ('1...2..3.', '3')
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                self.assertEqual(decrypt(input_str), expected)

    def test_multiple_dots(self):
        test_cases = [
            ('абра........', ''),
            ('1.......................', ''),
            ('абр..........', '')
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                self.assertEqual(decrypt(input_str), expected)

    def test_empty_string(self):
        self.assertEqual(decrypt(''), '')

    def test_stdin_handling(self):
        original_stdin = sys.stdin
        try:
            test_cases = [
                ('абра-кадабра.', 'абра-кадабра'),
                ('абраа..-кадабра', 'абра-кадабра'),
                ('.', '')
            ]
            for input_str, expected in test_cases:
                with self.subTest(input=input_str, expected=expected):
                    sys.stdin = StringIO(input_str)
                    self.assertEqual(decrypt(sys.stdin.read()), expected)
        finally:
            sys.stdin = original_stdin

if __name__ == '__main__':
    unittest.main()