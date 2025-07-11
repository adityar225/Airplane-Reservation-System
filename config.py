import os

ROWS = int(os.getenv("ROWS", 20))  # Default: 20 - Can change it in the future if needed in the terminal
SEATS_PER_ROW = int(os.getenv("SEATS_PER_ROW", 8))  # Default: 8 - Can change it in the future if needed in the terminal
SEAT_FILE = os.getenv("SEAT_FILE", "seats.json")