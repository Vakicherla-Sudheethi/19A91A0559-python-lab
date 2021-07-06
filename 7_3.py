'''
7.3)
Write a function dups to find all duplicates and unique elements in the list.
'''

def dups(arr):
    table = {}
    for element in arr:
        table[element] = table.get(element,0) + 1
    
    duplicates = [key for key in table.keys() if table[key] > 1]
    unique = [key for key in table.keys() if table[key] == 1]
    
    return (duplicates,unique)

if __name__ == "__main__":
    n = int(input('Enter number of elements: '))
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    info = dups(arr)
    print('Duplicate Elements:',info[0])
    print('Unique Elements:',info[1])

'''
Output:
Enter number of elements: 10
7
5
7
4
5
1
0
8
9
4
Duplicate Elements: [7, 5, 4]
Unique Elements: [1, 0, 8, 9]
'''
