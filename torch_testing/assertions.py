import numpy.testing as npt


def assert_equal(actual, expected, **kwargs):
    npt.assert_equal(actual.numpy(), expected.numpy(), **kwargs)

def assert_almost_equal(actual, expected, decimal=7, **kwargs):
    npt.assert_almost_equal(actual.numpy(), expected.numpy(), decimal=decimal, **kwargs)

def assert_allclose(actual, expected, rtol=1e-07, atol=0, equal_nan=True, **kwargs):
    npt.assert_allclose(
        actual.numpy(),
        expected.numpy(),
        rtol=rtol,
        atol=atol,
        equal_nan=equal_nan,
        **kwargs
    )
