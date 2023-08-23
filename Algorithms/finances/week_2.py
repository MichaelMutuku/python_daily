# period Monday 18 to Friday 22

########################################################################################################################
# Earnings
earn_mon = 200

earn_tue = 200

earn_wed = 200

earn_thu = 200

earn_fri = 200

list_earnings = [earn_mon, earn_tue, earn_wed, earn_thu, earn_fri]

total_earnings = sum(list_earnings)

print(f'The total amount you have earned this week is: {total_earnings} \n')

########################################################################################################################
# expediture
spent_mon = 200

spent_tue = 170

spent_wed = 230

spent_thu = 200 

spent_fri = 200

list_expense = [spent_mon, spent_tue, spent_wed, spent_thu, spent_fri]

total_expense = sum(list_expense)

print(f'The total amount you have spent this week is: {total_expense} \n')

########################################################################################################################
# loans
okoa_jahazi = 90

fuliza = 120

list_loans = [okoa_jahazi, fuliza]

total_loans = sum(list_loans)

########################################################################################################################
#Networth

def networth_calculator(total_earnings = total_earnings, total_expense = total_expense, total_loans = total_loans):
    return total_earnings - (total_expense + total_loans)

networth = networth_calculator()

print(f'Your networth is {networth} \n')

########################################################################################################################
# Networth based on bang system
list_bangs = list(range(0, networth, 50))
print('All Bangs:')
print(list_bangs, end="\n\n")

bang_system = []
list_bangs_copy = list_bangs.copy()
def sets(list_bangs = list_bangs_copy):
    if len(list_bangs) >= 10:
        bang_system.append(list_bangs_copy[0:10])
        del list_bangs_copy[0:10]
        sets(list_bangs_copy)
    else:
        bang_system.append(list_bangs_copy[0:])

sets()  

print("Stacks:")
for i in bang_system:
    print(i, end='\n')

# bangs = len(temporary)
decimal_in_sets = 0
for i in bang_system:
    if len(i) < 10:
        sets = len(bang_system) - 1
        decimal_in_sets = len(i)

bangs = len(list_bangs)

band = 200 * sets

print(f'\n According the bang system you have {sets}.{decimal_in_sets} sets and {bangs} bangs\n')