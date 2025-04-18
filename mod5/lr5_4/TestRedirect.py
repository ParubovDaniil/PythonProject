import unittest
import io
import sys  # Импортируем модуль sys
from Redirect import Redirect  # Замените это на ваш реальный импорт


class TestRedirect(unittest.TestCase):
    def setUp(self):
        self.test_stdout_file = open('test_stdout.txt', 'w')
        self.test_stderr_file = open('test_stderr.txt', 'w')

    def tearDown(self):
        self.test_stdout_file.close()
        self.test_stderr_file.close()

    def test_redirect_stdout(self):
        with Redirect(stdout=self.test_stdout_file):
            print('Test stdout')

        self.test_stdout_file.flush()
        with open('test_stdout.txt', 'r') as f:
            content = f.read()
            self.assertEqual(content, 'Test stdout\n')

    def test_redirect_stderr(self):
        with Redirect(stderr=self.test_stderr_file):
            print('Test stderr', file=sys.stderr)  # Выводим сообщение в stderr

        self.test_stderr_file.flush()
        with open('test_stderr.txt', 'r') as f:
            content = f.read()
            self.assertIn('Test stderr', content)


if __name__ == '__main__':
    unittest.main()