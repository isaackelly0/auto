def printTable(arr):
    colWidths = [0] * len(arr)
    count = 0
    for table in arr:
        for item in table:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1
    for item in range(len(arr[0])):
        for table in range(len(arr)):
            print(arr[table][item].rjust(colWidths[table]), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)