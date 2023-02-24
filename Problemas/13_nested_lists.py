"""
Given the names and grades for each student in a class of x students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    num = []
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        arr.append([name,score])
        num.append(score)
        num.sort()
    second_min = 0
    mini = num[0]
    arr.sort()
    for i in num:
        if i != mini:
            second_min = i
            break
    
    for i in arr:
        if i[1] == second_min:

            print(i[0])