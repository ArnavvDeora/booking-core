from decimal import Decimal

from booking.fees import cancellation_fee


def test_cancelling_well_ahead_is_free():
    assert cancellation_fee(Decimal("100.00"), 72) == Decimal("0.00")


def test_no_show_pays_the_first_night():
    assert cancellation_fee(Decimal("100.00"), 0.5) == Decimal("100.00")
