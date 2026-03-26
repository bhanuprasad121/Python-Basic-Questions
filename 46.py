# Richest Customer Wealth

# You are given an m x n integer grid accounts where accounts[i][j] represents the amount of money the i-th customer has in the j-th bank.

# Your task is to return the maximum wealth among all customers.

# A customer's wealth is the sum of all their bank account amounts. The richest customer is the one with the highest total wealth.
def maxwealth():
    account=eval(input("Enter accounts (e.g [[1,2,3],[3,2,1]]): "))
    max_wealth=0
    for customer in account:
        wealth=sum(customer)
        if wealth>max_wealth:
            max_wealth=wealth
    return wealth

print(maxwealth())