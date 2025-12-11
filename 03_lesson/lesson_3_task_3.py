from address import Address
from mailing import Mailing

to_addr = Address("123456", "Дремучено", "Лешего", "10", "5")
from_addr = Address("456789", "Болотино", "Водяного", "13", "9")

mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=450.30, track="AB123456789RU")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")

