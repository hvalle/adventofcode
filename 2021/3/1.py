
with open('2021/3/1-input') as f:
    lines = f.readlines()


gamma = ""
epsilon = ""
bin_size = len(lines[0])-1
report_length = len(lines)

for x in range(bin_size):
    gamma_avg = 0
    for y in range(len(lines)):
        gamma_avg += int(lines[y][x])
    if (gamma_avg/report_length) > 0.5:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))