class ROI:

    def __init__ (self, income=-77, expense=-77,  invest=-77): #-77 being used as 'undeclared'
        self.income=income
        self.expense=expense
        self.invest=invest

    def incomes(self):
        total=float(input("What is your monthly rental income?: ")) #These assume good input (some sort of number, which can be made into a float)
        total+=float(input("What is your monthly laundry income?: ")) #anything else including none break via error
        total+=float(input("What is your monthly storage income?: "))
        total+=float(input("What is your monthly misc income?: "))
        print(f"Your monthly income is ${round(total,2)}.")
        self.income=total

    def incFast(self,inc): #3 ways to declare things, in class declaration, in prompted inputs, or with the 'fast' options
        self.income=inc


    def expenses(self):
        total=float(input("What is your monthly tax expense?: "))
        total+=float(input("What is your monthly insurance expense?: "))
        total+=float(input("What is your monthly utility expense?: "))
        total+=float(input("What is your monthly home owners association expense?: "))
        total+=float(input("What is your monthly expense for lawn or snow mowers?: "))
        total+=float(input("How much monthly are you setting aside for vacancy?: "))
        total+=float(input("How much monthly are you setting aside for repairs?: ")) 
        total+=float(input("How much monthly are you setting aside for capital expenses?: "))
        total+=float(input("What are you paying your property manager: "))
        total+=float(input("What is the mortgage cost?: "))
        print(f"Your monthly expense is ${round(total,2)}.")
        self.expense=total

    def expFast(self,exp):
        self.expense=exp

    def cashFlow(self): #Worth noting if you go to expense/income after cash flow, it won't auto
        if self.income==-77:
            self.incomes()
        if self.expense==-77:
            self.expenses()

        print(f"Your monthly cash flow is ${round((self.income-self.expense),2)}")


    def invested(self):
        total=float(input('How much was down payment? '))
        total+=float(input('How much was down closing cost? '))
        total+=float(input('How much was budgeted for rehab? '))
        total+=float(input('What was the cost of other misc expenditures? '))
        print(f"The total invested is ${round(total,2)}.")
        self.invest=total

    def invFast(self,inv):
        self.invest=inv

    def cashOnCashROI(self):
        if self.income==-77 or self.expense==-77:
            self.cashFlow()
        if self.invest==-77:
            self.invested()
        
        print(f"Cash on cash ROI is {round((self.income-self.expense)*12/self.invest*100,2)}%") #12 to make it annual, forgot it initially



#testing all methods
test1=ROI(2000,1610)
test1.cashFlow()
test1.invFast(50000)
test1.cashOnCashROI()
print('\n')
# test2=ROI()
# test2.cashOnCashROI()#should use all the 'manual' functions
test3=ROI()#testing fast methods
test3.incFast(2000)
test3.expFast(1610)
test3.invFast(50000)
test3.cashFlow()
test3.cashOnCashROI()