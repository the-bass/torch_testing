import torch
import numpy.testing as npt


def assert_equal(actual, expected, **kwargs):
    npt.assert_equal(
        __np_array_from_torch__(actual),
        __np_array_from_torch__(expected),
        **kwargs
    )

def assert_almost_equal(actual, expected, decimal=7, **kwargs):
    npt.assert_almost_equal(
        __np_array_from_torch__(actual),
        __np_array_from_torch__(expected),
        decimal=decimal,
        **kwargs
    )

def assert_allclose(actual, expected, rtol=1e-07, atol=0, equal_nan=True, **kwargs):
    npt.assert_allclose(
        __np_array_from_torch__(actual),
        __np_array_from_torch__(expected),
        rtol=rtol,
        atol=atol,
        equal_nan=equal_nan,
        **kwargs
    )

def assert_within(tensor, min_val, max_val, rtol=0):
    half_interval_length = (max_val - min_val) / 2

    assert_allclose(
        tensor,
        torch.full(tensor.shape, min_val + half_interval_length),
        rtol=rtol,
        atol=half_interval_length
    )

def __np_array_from_torch__(torch):
    return torch.detach().numpy()
