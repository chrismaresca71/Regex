import re

regex = open('Regex_Project.txt')

lst = []
for line in regex:
    x = re.findall('[0-9]+', line)
    if x != []:
        for num in x:
            num = int(num)
            lst.append(num)

y = 0
for x in lst:
        y = y + x
print(y)




