import unittest
import torch_testing as tt


class TestPackaging(unittest.TestCase):

    def test_name(self):
        self.assertEqual(tt.name, 'torch_testing')

if __name__ == '__main__':
    unittest.main()
