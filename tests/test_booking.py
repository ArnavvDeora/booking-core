from datetime import date
from decimal import Decimal

import pytest

from booking import Booking, BookingConflict, RoomCalendar
from booking.pricing import stay_price


def b(room, guest, start, end):
    return Booking(room, guest, date(2026, 6, start), date(2026, 6, end))


def test_nights():
    assert b("101", "Ana", 1, 4).nights == 3


def test_rejects_zero_or_negative_stays():
    with pytest.raises(ValueError):
        b("101", "Ana", 4, 4)


def test_rejects_stays_over_the_limit():
    with pytest.raises(ValueError):
        Booking("101", "Ana", date(2026, 1, 1), date(2026, 2, 15))


def test_overlapping_bookings_conflict():
    cal = RoomCalendar()
    cal.add(b("101", "Ana", 1, 5))
    with pytest.raises(BookingConflict):
        cal.add(b("101", "Ben", 3, 7))


def test_different_rooms_never_conflict():
    cal = RoomCalendar()
    cal.add(b("101", "Ana", 1, 5))
    cal.add(b("102", "Ben", 1, 5))
    assert len(cal.bookings_for("102")) == 1


def test_back_to_back_bookings_conflict():
    cal = RoomCalendar()
    cal.add(b("101", "Ana", 1, 5))
    with pytest.raises(BookingConflict):
        cal.add(b("101", "Ben", 5, 8))


def test_stay_price():
    assert stay_price(Decimal("80.00"), 3) == Decimal("240.00")
