import unittest
import torch
from assertions import assert_equal


class TestAssertEqual(unittest.TestCase):

    def test_with_empty_tensors(self):
        a = torch.tensor([])
        b = torch.tensor([])
        assert_equal(a, b)

    def test_with_equal_one_value_tensors(self):
        a = torch.tensor([23.65])
        b = torch.tensor([23.65])
        assert_equal(a, b)

    def test_with_equal_1_dimensional_tensors(self):
        a = torch.tensor([23.65, 8.2])
        b = torch.tensor([23.65, 8.2])
        assert_equal(a, b)

    def test_with_equal_2_dimensional_tensors(self):
        a = torch.tensor([
            [23.65, 9.3, 5.2],
            [8.2, 1.1, 9],
        ])
        b = torch.tensor([
            [23.65, 9.3, 5.2],
            [8.2, 1.1, 9],
        ])
        assert_equal(a, b)

    def test_with_equal_tensors_of_different_type(self):
        a = torch.tensor([4], dtype=torch.int32)
        b = torch.tensor([4.0], dtype=torch.float16)
        assert_equal(a, b)

    def test_with_unequal_one_value_tensors(self):
        a = torch.tensor([23.65])
        b = torch.tensor([23.66])

        with self.assertRaisesRegex(AssertionError, 'Arrays are not equal'):
            assert_equal(a, b)

    def test_with_tensors_of_different_dimension(self):
        a = torch.tensor([23.65, 1])
        b = torch.tensor([23.66])

        with self.assertRaisesRegex(AssertionError, 'Arrays are not equal'):
            assert_equal(a, b)

    def test_with_unequal_2_dimensional_tensors(self):
        a = torch.tensor([
            [23.65, 9.3, 5.2],
            [8.2, 1.1, 9],
        ])
        b = torch.tensor([
            [23.65, 9.3, 5.2],
            [8.2, 1.2, 9],
        ])

        with self.assertRaisesRegex(AssertionError, 'Arrays are not equal'):
            assert_equal(a, b)

if __name__ == '__main__':
    unittest.main()
