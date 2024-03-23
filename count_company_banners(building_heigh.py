def count_company_banners(building_heights):
    x = building_heights[0]
    count = 1
    for height in building_heights[1:]:
        if height > x:
            x = height
            count += 1
    return count

# Provided test cases
test_cases = [
    [10, 15, 20, 10, 12],
    [8, 8, 8, 8, 8],
    [5, 10, 5, 15, 5, 20],
    [25, 15, 30, 20, 25]
]

# Iterate through each test case and print the result
for i, buildings in enumerate(test_cases, 1):
    print(f"Test case {i}: {count_company_banners(buildings)}")
