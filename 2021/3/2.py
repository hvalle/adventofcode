
with open('2021/3/1-input') as f:
    lines = f.readlines()


bin_size = len(lines[0])-1

ones = []
zeros = []
oxy_rating_list = lines
co2_rating_list = lines

for x in range(bin_size):
    # First for Oxygen
    gamma_avg = 0
    oxy_rating_list_len = len(oxy_rating_list)
    if oxy_rating_list_len >= 2:
        for y in range(oxy_rating_list_len):
            gamma_avg += int(oxy_rating_list[y][x])

            # Extract lists, we might need them
            if int(oxy_rating_list[y][x]) == 1:
                ones.append(oxy_rating_list[y])
            else:
                zeros.append(oxy_rating_list[y])

        # The average tells the story
        if (gamma_avg/oxy_rating_list_len) >= 0.5:
            oxy_rating_list = ones
        else:
            oxy_rating_list = zeros
        ones = []
        zeros = []

    # Now for CO2
    gamma_avg = 0
    co2_rating_list_len = len(co2_rating_list)
    if co2_rating_list_len >= 2:
        for y in range(co2_rating_list_len):
            gamma_avg += int(co2_rating_list[y][x])

            # Extract lists, we might need them
            if int(co2_rating_list[y][x]) == 1:
                ones.append(co2_rating_list[y])
            else:
                zeros.append(co2_rating_list[y])

        # The average tells the story
        if (gamma_avg/co2_rating_list_len) >= 0.5:
            co2_rating_list = zeros
        else:
            co2_rating_list = ones
    ones = []
    zeros = []

print(int(oxy_rating_list[0],2) * int(co2_rating_list[0],2))