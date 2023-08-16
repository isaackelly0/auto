import re
dateRegex = re.compile(r'(\d{2})\/(\d{2})\/(\d{4})')
mo = dateRegex.search('DD/MM/YYYY')
day = mo.group(1)
month = mo.group(2)
year = mo.group(3)
if 32 > int(day) > 0 and 13 > int(month) > 0 and 2999 > int(year) > 999:
    if int(day) == 31:
        if int(month) in [1,3,5,7,8,10,12]:
            print("valid date")
        else:
            print('invalid date')
    elif int(day) == 30:
        if int(month) != 2:
            print("valid date")
        else:
            print('invalid date')
    elif int(day) == 29 and int(month) == 2:
        if 0 in [int(year) % 400, int(year) % 100, int(year) % 4]:
            print('valid date')
        else:
            print('invalid date')
    else:
        print('valid date')
else:
    print('invalid date')