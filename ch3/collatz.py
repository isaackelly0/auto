import sys
def collatz():
    try:
        while True:
            print("Enter number:")
            num = input()
            try:
                if int(num):
                    num = int(num)
                    while num != 1:
                        if num % 2 == 0:
                            num = num//2
                            print(num)
                        elif num % 2 == 1:
                            num = 3*num+1
                            print(num)
            except:
                print('Use integers only')
    except KeyboardInterrupt:
        sys.exit()
collatz()