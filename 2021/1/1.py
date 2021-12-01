
with open('2021/1/1-input') as f:
    lines = f.readlines()

count = 0

for i in range(len(lines)):
    if int(lines[i]) > int(lines[i-1]):
        count += 1

print(count)


