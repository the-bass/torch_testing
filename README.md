- Written for PyTorch 0.4, Tested with Python 3.6.4 :: Anaconda, Inc.

NOTE: currently all assertion methods are provided by converting the tensors to numpy arrays using `tensor.numpy()` and feeding them into an appropriate `numpy.testing` method.

Usage
```py
import unittest
import torch
import torch_testing as tt


class TestSomeClass(unittest.TestCase):

    def test_some_method(self):
        a = torch.tensor([1, 2])
        b = torch.tensor([1, 2])
        tt.assert_equal(a, b)

if __name__ == '__main__':
    unittest.main()
```
