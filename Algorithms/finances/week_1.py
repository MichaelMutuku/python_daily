# period Monday 11 to Friday 15

########################################################################################################################
# Earnings
earn_mon = 200

earn_tue = 200

earn_wed = 100

earn_thu = 200

earn_fri = 200

list_earnings = [earn_mon, earn_tue, earn_wed, earn_thu, earn_fri]

total_earnings = sum(list_earnings)

print(f'The total amount you have earned this week is: {total_earnings}')

########################################################################################################################
# expediture
spent_mon = 200

spent_tue = 200

spent_wed = 100

spent_thu = 200

spent_fri = 200

list_expense = [spent_mon, spent_tue, spent_wed, spent_thu, spent_fri]

total_expense = sum(list_expense)

print(f'The total amount you have spent this week is: {total_expense}')

########################################################################################################################
# loans
okoa_jahazi = 100

fuliza = 400

list_loans = [okoa_jahazi, fuliza]

total_loans = sum(list_loans)

########################################################################################################################
#Networth

def networth(total_earnings = total_earnings, total_expense = total_expense, total_loans = total_loans):
    return total_earnings - (total_expense + total_loans)

print(f'Your networth is {networth()}')

########################################################################################################################
# Networth based on bang system
list_bangs = list(range(0, networth(), 50))
print(list_bangs)

temporary = []
def sets(list_bangs = list_bangs):
    if len(list_bangs) >= 10:
        temporary.append(list_bangs[0:10])
        del list_bangs[0:10]
        sets(list_bangs)
    else:
        temporary.append(list_bangs[0:])

sets()    
print(temporary)

# bangs = len(temporary)
for i in temporary:
    if len(i) < 10:
        bangs = len(temporary) - 1

sets = len([x for i in temporary for x in i])

print(f'According the bang system you have {bangs} bangs and {sets} sets')