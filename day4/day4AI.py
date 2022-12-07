with open("input") as infile:
    pairs = [line[:-1] for line in infile.readlines()]


# Split each pair into two ranges and store them in a list
ranges = [pair.split(",") for pair in pairs]

# Keep track of the number of pairs where one range fully contains the other
count = 0

# Iterate over the list of ranges
for i in range(len(ranges)):
    # Get the first range in the current pair
    r1 = ranges[i]

    # Compare the current range to every other range
    for j in range(i+1, len(ranges)):
        # Get the second range in the current pair
        r2 = ranges[j]

        # Check if one range fully contains the other
        if (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r1[0] >= r2[0] and r1[1] <= r2[1]):
            # Increment the counter if one range fully contains the other
            count += 1

# Print the number of pairs where one range fully contains the other
print(count)