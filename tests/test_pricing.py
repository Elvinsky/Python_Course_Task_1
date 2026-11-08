"""Tests for the pure domain function you implement in domain/pricing.py (AC 4).

These tests are given. Make them pass, then add a second pure function of your own to /domain
and write parametrized tests for it next to this file.

`apply_discount` is imported inside each test on purpose: until /domain exists you get a clear
failure per test instead of a collection error that hides the acceptance tests.
"""

from decimal import Decimal

import pytest


@pytest.mark.parametrize(
    ("price", "percent", "expected"),
    [
        (Decimal("100.00"), 0, Decimal("100.00")),
        (Decimal("19.99"), 10, Decimal("17.99")),
        (Decimal(50), 100, Decimal("0.00")),
    ],
)
def test_apply_discount(price: Decimal, percent: int, expected: Decimal) -> None:
    from domain.pricing import apply_discount

    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize("percent", [-1, 101])
def test_apply_discount_rejects_bad_percent(percent: int) -> None:
    from domain.pricing import apply_discount

    with pytest.raises(ValueError):
        apply_discount(Decimal(10), percent)
