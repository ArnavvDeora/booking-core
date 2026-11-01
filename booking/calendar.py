from .models import Booking


class BookingConflict(Exception):
    pass


def overlaps(a: Booking, b: Booking) -> bool:
    # Check-out day may equal the next check-in day (rooms turn over 11:00 -> 15:00).
    return a.check_in < b.check_out and b.check_in < a.check_out


class RoomCalendar:
    def __init__(self):
        self._bookings = []

    def add(self, booking: Booking) -> None:
        for existing in self._bookings:
            if existing.room == booking.room and overlaps(existing, booking):
                raise BookingConflict(f"{booking.room} is taken by {existing.guest}")
        self._bookings.append(booking)

    def bookings_for(self, room: str) -> list:
        return [b for b in self._bookings if b.room == room]
