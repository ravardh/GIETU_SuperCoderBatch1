import sys

class Solution:
    def lemonadeChange(self, bills):
        fives = 0
        tens = 0
        twenties = 0

        for bill in bills:
           
            if bill == 5:
                fives += 1

            
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1

            
            elif bill == 20:
                
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                    fives += 1

               
                elif fives >= 3:
                    fives -= 3

               
                else:
                    return False

        return True

def main(bill):
    sol = Solution()
    print("Can Ninja return the correct change to all the customers? ", sol.lemonadeChange(bill))

if __name__ == "__main__":
    bill_size = int(input())
    bill_arr = list(map(int, input().split()))

    if bill_size != len(bill_arr):
        raise ValueError("The length of the list does not match the size of the array")

    main(bill_arr)