from decimal import Decimal

FREE_CANCELLATION_HOURS = 48
LATE_CANCELLATION_HOURS = 2
LATE_FEE_SHARE = Decimal("0.5")


def cancellation_fee(first_night_price: Decimal, hours_before_check_in: float) -> Decimal:
    if hours_before_check_in >= FREE_CANCELLATION_HOURS:
        return Decimal("0.00")
    if hours_before_check_in >= LATE_CANCELLATION_HOURS:
        return first_night_price * LATE_FEE_SHARE
    return first_night_price
