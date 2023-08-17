import re
def passwordCheck(password):
    numRegex = re.compile(r'\d+')
    lowRegex = re.compile(r'[a-z]+')
    upRegex = re.compile(r'[A-Z]+')
    lenRegex = re.compile(r'.{8,}')
    num_checker = numRegex.search(password)
    lower_alpha = lowRegex.search(password)
    upper_alpha = upRegex.search(password)
    len_checker = lenRegex.search(password)
    if num_checker and lower_alpha and upper_alpha and len_checker:
        return True
    else:
        return False

check = passwordCheck('Passw0rd')
print(check)