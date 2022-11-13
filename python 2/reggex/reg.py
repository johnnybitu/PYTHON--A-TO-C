import re
txt = "this is rain, a beautiful ramantic day , india"

x = re.search("^this.*india$", txt)
if x:
    print("yes this is true")
else:
    print("no this is fa")


# regex function - :
# findall() - alll values will show
#search()  - any pattern you want to search
#spilit() - after spilit will it match
#sub() - vice versa of spilit


# meta characters

# \d = escape caracter as space u want
# . = any character you want to show 
# ^ - start with
# $ - end with
# * - zero or more occurance
# + - one or more occurance
# ? - zero or one occurance
# {} - exactly specified number of occurance
# | - either or
# () - capture and group


