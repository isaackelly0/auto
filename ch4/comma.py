def comma(arr):
    try:
        if len(arr) > 0:
            sentence = ''
            for i in range(len(arr)):
                if i == len(arr)-1:
                    sentence += "and " + str(arr[i])
                else:
                    sentence += str(arr[i]) + ', '
            return sentence
        else:
            return "Do not enter an empty list"
    except TypeError:
        print("Please enter a list")

print(comma(['puss','n','boots','donkey']))