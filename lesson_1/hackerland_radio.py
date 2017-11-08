# sample code
N, radio_range = [int(a) for a in input().split()]
x = [int(x_temp) for x_temp in input().strip().split(' ')]


# REVIEW: this can be done without the city list
# a better solution is a sorted list with the positions of the houses
# while iterarting you can skip a lot of empty comparisons
# (their positions is known in advance) therwise the approach is the same
N = max(x)
city = [False] * N

for house in x:
    # this makes them indexes, not positions
    city[house - 1] = True

total_transmitters = 0

current_range = 0
last_house = 0
i = 0

# print(city, N)
while True:
    # city's over and we need a transmitter
    # this might break if no last_house?
    if i > N - 1:
        if current_range > 0:
            total_transmitters += 1
        break

    if current_range == 0:
        if city[i]:
            current_range += 1
            last_house = i
        i += 1
    elif current_range < radio_range:
        if city[i]:
            last_house = i
        current_range += 1
        i += 1
    elif current_range == radio_range:
        total_transmitters += 1
        # if there is a house here, attempt to place a transmitter
        if city[i]:
            # skip the next houses, since they are covered
            i += radio_range + 1  # current_range is the same
        # attempt to put a transmitter at last possible location
        else:
            i = last_house + current_range
        current_range = 0
    # this means, we are out of transmitter range, and need one ASAP
    # this should not happen
    else:
        print('You should not be seeing this')

print(total_transmitters)
