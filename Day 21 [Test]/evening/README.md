# Question 1
In a traditional forge, a blacksmith faces the challenge of efficiently cutting metal rods to fulfil customer orders of varying lengths. With limited equipment and stock, including a single cutting tool, the objective is to maximize customer satisfaction by fulfilling as many orders as possible while minimizing waste. An algorithm or strategy is needed to optimize the sequence of rod cuts, utilizing available resources effectively. Considerations include minimizing waste, handling unfulfilled orders, Maximize the Profit and streamlining workflow to enhance customer satisfaction and resource utilization.

### Test Cases
| Input | Output |
| ----- | ------ |
| length = [1, 2, 3, 4, 5, 6, 7, 8]<br>price = [1, 5, 8, 9, 10, 17, 17, 20] | 22 |
| length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]<br>price = [3, 5, 8, 9, 10, 17, 17, 20, 22, 25, 30, 35] | 36 |

# Question 2
Mr. X, a faculty member at a prestigious educational institution, has been tasked with preparing a schedule for the upcoming B-Tech batch. The schedule needs to accommodate practical classes for various subjects across different departments. Each department has provided the timings for their practical classes, and Mr. Singh needs to determine how many labs are required to conduct all the classes efficiently.

#### Test cases
| Input |	Output |
| ----- | ------ |
| S: [10:00, 10:30, 11:00, 11:30]<br>E: [10:30, 11:00, 11:30, 12:00] | 1 |
| S: [9:00, 9:30, 11:00, 12:00]<br>E: [10:15, 11:00, 12:15, 13:00] | 2 |
| S: [9:00, 9:15, 9:30, 9:00, 10:15]<br>E: [10:00, 10:30, 10:45, 9:30, 11:30]	| 3 |