# Torch Testing

A collection of assertion methods to compare PyTorch Tensors in tests.

Currently all assertion methods are provided by converting the tensors to numpy arrays and feeding them into an appropriate `numpy.testing` method. That way, on failure, detailed information is provided as to why the test failed.

Last tested with **Python 3.6.4 :: Anaconda, Inc.** and **PyTorch 0.4**.

## Installation

Clone this repository and run

```py
pip install .
```

inside the root directory to make the module available as `torch_testing`.

## Usage example

You can assert the equality of two `torch.tensor`s like

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

## Assertion methods

### `assert_equal(actual, expected, **kwargs)`
Currently this assertion method is provided by converting the tensors to `numpy` arrays using `tensor.numpy()` and feeding them to [numpy.testing.assert_equal](https://docs.scipy.org/doc/numpy/reference/generated/numpy.testing.assert_equal.html#numpy.testing.assert_equal).

### `assert_allclose(actual, expected, rtol=1e-07, atol=0, equal_nan=True, **kwargs)`
Currently this assertion method is provided by converting the tensors to `numpy` arrays using `tensor.numpy()` and feeding them to [numpy.testing.assert_allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose).

### `assert_within(tensor, min_val, max_val, rtol=0)`
Ensures that all values of the given `tensor` are greater than or equal to `min_val` and less than or equal to `max_val`. Allows to specify a relative tolerance `rtol`, which behaves as in [numpy.testing.assert_allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose).

*NOTE: Uses `assert_allclose` under the hood, hence the fail message might currently be a little confusing.*

## Development

*Unless noted otherwise, all commands are expected to be executed from the root directory of this repository.*

### Building the package for local development

To make the package available locally while making sure changes to the files are reflected immediately, run

```sh
pip install -e .
```

### Test suite

Run all tests using

```sh
python -m unittest discover tests
```
