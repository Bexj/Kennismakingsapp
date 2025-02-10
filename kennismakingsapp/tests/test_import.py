"""Test Kennismakingsapp."""

import kennismakingsapp


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(kennismakingsapp.__name__, str)
