count=0
with open('log_files/201811123005.log',encoding='utf8') as lines:
    for line in lines:
        id = line.split(',')[1]
        id = id[4:]
        if id=='201811123005':
            count+=1
print(count)  