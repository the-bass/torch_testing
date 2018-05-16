import unittest
import torch
from assertions import assert_almost_equal


class TestAssertAlmostEqual(unittest.TestCase):

    def test_with_only_just_almost_equal_one_value_tensors(self):
        a = torch.tensor([1, 2, 23.65727169])
        b = torch.tensor([1, 2, 23.65727160])
        assert_almost_equal(a, b)

    def test_with_only_just_not_almost_equal_one_value_tensors(self):
        a = torch.tensor([1, 2, 23.73298])
        b = torch.tensor([1, 2, 23.732979])

        with self.assertRaisesRegex(AssertionError, 'Arrays are not almost equal'):
            assert_almost_equal(a, b)

if __name__ == '__main__':
    unittest.main()
