class Earnings:
    def __init__(self, day, earning):
        self.day_of_week = day
        self.earning = earning
        self.list_earnings = []

    def select_earning_day(self):
        self.day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if self.day_of_week.lower() in self.day_list:
            return self.day_of_week.lower()
        else:
            return 'an error occured try entering day of the week in words'

    def all_earnings(self):
        return self.list_earnings.append(self.earning)
        
    def total_earnings(self):
        return sum(self.list_earnings)

class Expenditure:
    def __init__(self, day, spent):
        self.day_of_week = day
        self.spent = spent
        self.list_spent = []

    def select_expense_day(self):
        self.day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if self.day_of_week.lower() in self.day_list:
            return self.day_of_week.lower()
        else:
            return 'an error occured try entering day of the week in words'

    def all_expenses(self):
        return self.list_spent.append(self.spent)
    
    def total_earnings(self):
        return sum(self.list_spent)

class Loans:
    def __init__(self, okoa_jahazi, fuliza):
        self.okoa_jahazi = okoa_jahazi
        self.fuliza = fuliza
        self.list_loans = []

    def all_loans(self):
        self.list_loans.append(okoa_jahazi)
        self.list_loans.append(fuliza)
        return self.list_loans

    def total_loans(self):
        return sum(self.list_loans)

class Networth(Earnings, Expenditure, Loans):
    def __init__(self):
        self.total_earnings = Earnings.total_earnings()
        self.total_expenses = Expenditure.total_earnings()
        self.total_loans = Loans.total_loans()

    def networth_calculator(self):
        return self.total_earnings - (self.total_expense + self.total_loans)

# Networth based on bang system

class Bang(Networth):
    def __init__(self):
        self.networth = Networth.networth_calculator()
        self.list_bangs = []

    def all_bangs(self):
        self.list_bangs = list(range(0, networth, 50))
        return self.list_bangs

class Sets(Bang):
    def __init__(self):
        self.bang_system = []
        self.list_bangs_copy = Bang.list_bangs.copy()
        self.set_decimal = 0

    def sets(self):
        if len(self.list_bangs_copy) >= 10:
            self.bang_system.append(self.list_bangs_copy[0:10])
            del self.list_bangs_copy[0:10]
            self.sets(self.list_bangs_copy)
        else:
            self.bang_system.append(self.list_bangs_copy[0:])
        return self.bang_system

    def stacks(self):
        return [i for i in self.bang_system]

    def decimal_in_sets(self):
        for i in self.bang_system:
            if len(i) < 10:
                self.sets = len(self.bang_system)-1
                self.set_decimal = len(i)

class FileManagement():
    def __init__(self):
        self.day = ''
        self.earnings = {}
        self.spent = {}
        self.loan = {}


    def list_file(self):
        self.file_list = []
        self.f = open('log_file.txt')
        for i in self.f:
            self.file_list.append(i)
        self.f.close()

    def append_log_file(self, item):
        self.f = open('log_file.txt', 'a')
        self.write('\n', item)
        self.f.close()
