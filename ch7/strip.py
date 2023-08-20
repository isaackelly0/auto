import re
def strip(string, thing):
    if thing:
        notThisRegex = re.compile(r'') #TODO
    else:
        notThisRegex = re.compile(r'[^\s]+')
    pole = notThisRegex.search(string)
    print(pole.group())
strip("    poo    ", False)