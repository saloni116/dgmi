
stream = input("Enter binary string: ")

buckets = []

# Process each 1 and form DGIM buckets
for i, bit in enumerate(stream):

    if bit == '1':
        # New bucket of size 1
        buckets.append([1, i])

        # Merge buckets if more than 2 of same size exist
        while True:
            size_groups = {}

            for bucket in buckets:
                size = bucket[0]

                if size not in size_groups:
                    size_groups[size] = []

                size_groups[size].append(bucket)

            merged = False

            for size in sorted(size_groups.keys()):
                if len(size_groups[size]) > 2:
                    same_buckets = sorted(
                        size_groups[size],
                        key=lambda x: x[1]
                    )

                    # Merge two oldest buckets
                    b1 = same_buckets[0]
                    b2 = same_buckets[1]

                    buckets.remove(b1)
                    buckets.remove(b2)

                    # New merged bucket
                    buckets.append([size * 2, b2[1]])
                    buckets.sort(key=lambda x: x[1])

                    merged = True
                    break

            if not merged:
                break

# Print buckets from RIGHT SIDE
buckets.sort(key=lambda x: x[1], reverse=True)

print("\nDGIM Buckets from Right Side:\n")

powers = []
values = []

for number, bucket in enumerate(buckets, start=1):
    size = bucket[0]

    power = 0
    temp = size

    while temp > 1:
        temp = temp // 2
        power += 1

    print(f"Bucket {number} = 2^{power} = {size}")
    powers.append(f"2^{power}")
    values.append(size)

print("\nTotal number of 1's =", " + ".join(powers))
print("           =", " + ".join(map(str, values)))
print("           =", sum(values))


#sample output-101101101011