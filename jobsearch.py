def job_sequencing(job_code, profit, deadline):
    n = len(profit)
    max_deadline = max(deadline)
    
    jobs = [(job_code[i], profit[i], deadline[i]) for i in range(n)]
    
    jobs.sort(key=lambda x: x[1], reverse=True)

    result = [None] * max_deadline
    slots = [False] * max_deadline

    for job in jobs:
        for i in range(min(max_deadline - 1, job[2] - 1), -1, -1):
            if slots[i] is False:
                result[i] = job[0]
                slots[i] = True
                break

    max_profit = 0
    job_sequence = []
    for i in range(max_deadline):
        if result[i] is not None:
            max_profit += job[1]  # Corrected line
            job_sequence.append(result[i])

    return max_profit, job_sequence

# Given data
job_code = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7']
profit = [20, 30, 15, 12, 35, 25, 5]
deadline = [2, 4, 3, 1, 3, 4, 2]

max_profit, job_sequence = job_sequencing(job_code, profit, deadline)
print("Maximum Profit:", max_profit)
print("Job Sequence:", job_sequence)
