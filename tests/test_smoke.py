"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import lumenify


def test_version_is_set() -> None:
    assert lumenify.__version__
