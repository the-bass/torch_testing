import unittest
import torch
from assertions import assert_allclose


class TestAssertAllclose(unittest.TestCase):

    def test_with_allclose_tensors(self):
        a = torch.tensor([1, 2, 23.65799, 0])
        b = torch.tensor([1, 2, 23.657989, 0])
        assert_allclose(a, b)

    def test_with_not_allclose_tensors(self):
        a = torch.tensor([1, 2, 23.6579, 0])
        b = torch.tensor([1, 2, 23.65789, 0])

        with self.assertRaisesRegex(AssertionError, 'Not equal to tolerance'):
            assert_allclose(a, b)

    def test_atol_param_with_allclose_tensors(self):
        a = torch.tensor([0, 0, 0])
        b = torch.tensor([-1, 0, 1])
        assert_allclose(a, b, atol=1, rtol=0)

    def test_atol_param_with_not_allclose_tensors(self):
        a = torch.tensor([0])
        b = torch.tensor([-1.001])

        with self.assertRaisesRegex(AssertionError, 'Not equal to tolerance'):
            assert_allclose(a, b, atol=1, rtol=0)

if __name__ == '__main__':
    unittest.main()
