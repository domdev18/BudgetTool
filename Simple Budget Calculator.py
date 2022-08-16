# Dominic Ferraro
# 6/5/2022
# Peer Programming Assignment
print("Input Pay")
nPay = float(input())
print("Input Rent")
nRent = float(input())
print("Input Utilities")
nUtilities = float(input())
print("Input Groceries")
nGroceries = float(input())
nDiscretionary = nPay - nRent - nUtilities - nGroceries
nTotalBills = nRent + nUtilities + nGroceries
print("Total Bills: " + str(nTotalBills))
print("Discretionary Spending: " + str(nDiscretionary))