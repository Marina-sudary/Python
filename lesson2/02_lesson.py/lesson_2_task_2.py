def is_year_leap(year):
    return year % 4 == 0


year_input = input("Введите год: ")


year_to_check = int(year_input)


is_leap = is_year_leap(year_to_check)


print(f"год {year_to_check}: {is_leap}")
