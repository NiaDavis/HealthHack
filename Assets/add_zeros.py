with open('JHU_Data_2020.02.07_PM.csv', 'r') as file:
    for line in file:
        newline = line[0]
        for i in range(1,len(line)):
            if line[i] == ',' and line[i-1] == ',':
                newline += '0,'
            else:
                newline += line[i]
        print(newline, end='')