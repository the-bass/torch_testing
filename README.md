# Torch Testing

A collection of assertion methods to compare PyTorch Tensors in tests.

Tested with
 - PyTorch 0.4
 - Python 3.6.4 :: Anaconda, Inc.

NOTE: Currently all assertion methods are provided by converting the tensors to numpy arrays and feeding them into an appropriate `numpy.testing` method. That way, on failure, detailed information is provided as to why it failed.

## Usage example
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

## Assertions

### `assert_equal(actual, expected, **kwargs)`
Currently this assertion method is provided by converting the tensors to `numpy` arrays using `tensor.numpy()` and feeding them to [numpy.testing.assert_equal](https://docs.scipy.org/doc/numpy/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal).

### `assert_allclose(actual, expected, rtol=1e-07, atol=0, equal_nan=True, **kwargs)`
Currently this assertion method is provided by converting the tensors to `numpy` arrays using `tensor.numpy()` and feeding them to [numpy.testing.assert_allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose).
