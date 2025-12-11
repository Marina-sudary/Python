from smartphone import Smartphone

catalog = []

catalog = [
    Smartphone("Apple", "iPhone 14", "+7-123-456-78-90"),
    Smartphone("Samsung", "Galaxy S22", "+7-234-567-89-01"),
    Smartphone("Xiaomi", "Mi 11", "+7-345-678-90-12"),
    Smartphone("OnePlus", "9 Pro", "+7-456-789-01-23"),
    Smartphone("Google", "Pixel 6", "+7-567-890-12-34")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

