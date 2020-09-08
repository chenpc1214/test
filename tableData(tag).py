"""import pprint

def printable():

    tableData = [["apple","orange","cherries","banana"],
             ["alice","bob","card","david"],
             ["dogs","cats","moose","goose"]]
    
    new = [[],[],[],[]]

    for i in range(0,len(tableData)):
        new[0].append(tableData[i][0])
        new[1].append(tableData[i][1])
        new[2].append(tableData[i][2])
        new[3].append(tableData[i][3])
        
    result =" ".join(new)
    print(result)"""


#解答:

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David',],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for w in range(len(table[0])):
        for z in range(len(table)):
            if len(table[z][w]) > colWidths[z]:
                colWidths[z] = len(table[z][w])
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y] + 1), end='')
        print()
   
printTable(tableData)

