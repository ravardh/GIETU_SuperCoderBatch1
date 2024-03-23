def min_labs_needed(start_times, end_times):
    if not start_times or not end_times:
        return 0

    n = len(start_times)
    sorted_timings = sorted(zip(start_times, end_times), key=lambda x: x[1])

    labs = []
    for start, end in sorted_timings:
        allocated = False
        for lab in labs:
            if lab <= start:
                lab = end
                allocated = True
                break
        if not allocated:
            labs.append(end)
    return len(labs)

# Test cases
test_cases = [
    (["10:00", "10:30", "11:00", "11:30"], ["10:30", "11:00", "11:30", "12:00"]),
    (["9:00", "9:30", "11:00", "12:00"], ["10:15", "11:00", "12:15", "13:00"]),
    (["9:00", "9:15", "9:30", "9:00", "10:15"], ["10:00", "10:30", "10:45", "9:30", "11:30"])
]

for i, (start_times, end_times) in enumerate(test_cases, 1):
    print(f"Test case {i}: Number of labs required: {min_labs_needed(start_times, end_times)}")
