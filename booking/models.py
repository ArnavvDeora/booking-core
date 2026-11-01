from dataclasses import dataclass
from datetime import date

from .config import MAX_STAY_NIGHTS


@dataclass(frozen=True)
class Booking:
    room: str
    guest: str
    check_in: date
    check_out: date

    def __post_init__(self):
        if self.check_out <= self.check_in:
            raise ValueError("check-out must be after check-in")
        if self.nights > MAX_STAY_NIGHTS:
            raise ValueError(f"stays are limited to {MAX_STAY_NIGHTS} nights")

    @property
    def nights(self) -> int:
        return (self.check_out - self.check_in).days
