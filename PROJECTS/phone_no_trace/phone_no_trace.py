import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('this is number')

phone_no = phonenumbers.parse(number)

timezone_area = timezone.time_zones_for_number(phone_no)

company_name = carrier.name_for_number(phone_no, "en")

reggistration= geocoder.description_for_number(phone_no, "en")


print(phone_no)
print(timezone_area)
print(company_name)
print(reggistration)
