
with open('2021/2/1-input') as f:
    lines = f.readlines()

horizontal_postion = 0
depth = 0

for line in lines:
    direction = line.split()[0]
    value = int(line.split()[1])

    match direction:
        case "forward":
            horizontal_postion += value
        case "up":
            depth -= value
        case "down":
            depth += value

print(horizontal_postion*depth)
