from decimal import Decimal


def stay_price(nightly_rate: Decimal, nights: int) -> Decimal:
    return nightly_rate * nights
