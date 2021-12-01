
with open('2021/1/1-input') as f:
    lines = f.readlines()

count = 0

for i in range(len(lines)):
    if i < len(lines)-3:
        window = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        next_window = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
        if window < next_window:
            count += 1

print(count)