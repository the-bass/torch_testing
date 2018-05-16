import numpy.testing as npt


def assert_equal(actual, desired, **kwargs):
    npt.assert_equal(actual.numpy(), desired.numpy(), **kwargs)

def assert_almost_equal(actual, desired, decimal=7, **kwargs):
    npt.assert_almost_equal(actual.numpy(), desired.numpy(), decimal=decimal, **kwargs)

def assert_allclose(actual, desired, rtol=1e-07, atol=0, equal_nan=True, **kwargs):
    npt.assert_allclose(
        actual.numpy(),
        desired.numpy(),
        rtol=rtol,
        atol=atol,
        equal_nan=equal_nan,
        **kwargs
    )
