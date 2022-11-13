from math import prod
from admin.common.header import header

arun = header()

print(arun.head)
print(arun.show())

from admin.common.footer import footer

jimm = footer()
print(jimm.foot)
print(jimm.show())

from admin.service import service

tonny = service()

print(tonny.servie)
print(tonny.show())

from user.product import product

johnny = product()

print(johnny.pro)
print(johnny.show())

