def max_profit(jobs):
    # Sort the jobs based on their deadlines
    jobs.sort(key=lambda x: x[2])
    
    max_deadline = max(jobs, key=lambda x: x[2])[2]
    occupied_slots = [False] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        deadline = job[2]
        for i in range(deadline, 0, -1):
            if not occupied_slots[i]:
                total_profit += job[1]
                occupied_slots[i] = True
                break

    return total_profit

# Example usage:
jobs = [
    ("j1", 20, 2),
    ("j2", 30, 4),
    ("j3", 15, 3),
    ("j4", 12, 1),
    ("j5", 35, 3),
    ("j6", 25, 4),
    ("j7", 5, 2)
]

print("Maximum profit:", max_profit(jobs))
