import unittest
import torch
import torch_testing as tt


class TestAssertWithin(unittest.TestCase):

    def test_with_tensor_within_specified_range(self):
        t = torch.tensor([[4.26, 4.261], [4.999, 5]])
        tt.assert_within(t, 4.26, 5)

    def test_with_tensor_with_greater_value(self):
        t = torch.tensor([[4.26, 4.261, 4.5], [4.999, 5, 5.0001]])

        with self.assertRaisesRegex(AssertionError, 'Not equal to tolerance'):
            tt.assert_within(t, 4.26, 5)

    def test_with_tensor_with_smaller_value(self):
        t = torch.tensor([[4.26, 4.261, 4.9], [4.999, 5, 4.25]])

        with self.assertRaisesRegex(AssertionError, 'Not equal to tolerance'):
            tt.assert_within(t, 4.26, 5)

    def test_with_rtol(self):
        t = torch.tensor([[4.26, 4.261, 4.9], [4.999, 5, 5.0001]])
        tt.assert_within(t, 4.26, 5, rtol=0.01)

if __name__ == '__main__':
    unittest.main()
