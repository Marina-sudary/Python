def is_year_leap(year):
    return year % 4 == 0


year = 1988

year = 2023


if is_year_leap:
    print(f"год {year}: True")
else:
    print(f"год {year}: False")
