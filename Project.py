class RentalProperty():
    def __init__(self):
        self.expense = {}
        self.income = {}
        self.investment = {}
        self.ROI = None
        self.cash_flow = None
    
    def incomeROI(self):
        while True:
            incomeinput = input('First you will have to add income sources. Would you like to add, delete, or calculate total income amount? Please type add, delete, or total.')
            if incomeinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "add":
                while True:
                    incomekey = input('What income source would you like to add? Type "Finish" when finished.')
                    if incomekey.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "finish":
                        print(self.income)
                        break
                    incomevalue = input(f'Please type the amount in dollars of {incomekey}.')
                    try: 
                        self.income[incomekey.strip(" .,/!?@#$%^&*-=\;':<>").lower()] = float(incomevalue)
                        print(self.income)
                    except:
                        print(f'{incomevalue} is not a valid number. No punctuations. Please try again.')
            elif incomeinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "delete":
                print(self.income)
                while True:
                    incometypedelete = input('Please enter the name of the income type saved that you wish to change. Type "Finish" when finished.')
                    if incometypedelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "finish":
                        print(self.income)
                        break
                    elif incometypedelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") in self.income:
                        incomekeydelete = input('Would you like to delete/modify the income type? Please type "delete" or "modify"')
                        if incomekeydelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == 'modify':
                            incomemodify = input('Please enter the new value in dollars.')
                            try:
                                self.income[incometypedelete.lower().strip(" .,/!?@#$%^&*-=\;':<>")] = float(incomemodify)
                                print(self.income)
                            except:
                                print(f'{incomemodify} is not a valid number. Please try again.')                
                        elif incomekeydelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == 'delete':
                            del self.income[incometypedelete]
                            print(self.income)
                    else:
                        print(f'{incometypedelete} is not a saved income type. Please try again.')
            elif incomeinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "total":
                print(f'Your total income amount is ${sum(self.income.values())}')
                return self.income
            else: 
                print(f'{incomeinput} is not a valid action. Please try again.')
            
    
    def expenseROI(self):
         while True:
            expenseinput = input('Next, add expense sources. Would you like to add, delete, or calculate total expense amount? Please type add, delete, or total.')
            if expenseinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "add":
                while True:
                    expensekey = input('What expense source would you like to add? Type "Finish" when finished.')
                    if expensekey.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "finish":
                        print(self.expense)
                        break
                    expensevalue = input(f'Please type the amount in dollars of {expensekey}.')
                    try: 
                        self.expense[expensekey.strip(" .,/!?@#$%^&*-=\;':<>").lower()] = float(expensevalue)
                        print(self.expense)
                    except:
                        print(f'{expensevalue} is not a valid number. No punctuations. Please try again.')
            elif expenseinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "delete":
                print(self.expense)
                while True:
                    expensetypedelete = input('Please enter the name of the expense type saved that you wish to change. Type "Finish" when finished.')
                    if expensetypedelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "finish":
                        print(self.expense)
                        break
                    elif expensetypedelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") in self.expense:
                        expensekeydelete = input('Would you like to delete/modify the income type? Please type "delete" or "modify"')
                        if expensekeydelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == 'modify':
                            expensemodify = input('Please enter the new value in dollars.')
                            try:
                                self.expense[expensetypedelete.lower().strip(" .,/!?@#$%^&*-=\;':<>")] = float(expensemodify)
                                print(self.expense)
                            except:
                                print(f'{expensemodify} is not a valid number. Please try again.')                
                        elif expensekeydelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == 'delete':
                            del self.expense[expensetypedelete]
                            print(self.expense)
                    else:
                        print(f'{expensetypedelete} is not a saved expense type. Please try again.')
            elif expenseinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "total":
                print(f'Your total expense amount is ${sum(self.expense.values())}')
                return self.expense
            else: 
                print(f'{expenseinput} is not a valid action. Please try again.')
    
    def cashflow(self):
        cashf = sum(self.income.values())-sum(self.expense.values())
        print(f'Your total cash flow is ${cashf} monthly or ${cashf*12} annually.')
        self.cash_flow = cashf*12
        
    
    def investmentROI(self):
        while True:
            ROIinput = input('Finally, please input your investments into this property. Would you like to add, delete, or calculate total investments? Please type add, delete, or total.')
            if ROIinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "add":
                while True:
                    ROIinputkey = input('What investment source would you like to add? Type "Finish" when finished.')
                    if ROIinputkey.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "finish":
                        print(self.investment)
                        break
                    ROIinputvalue = input(f'Please type the amount in dollars of {ROIinputkey}.')
                    try: 
                        self.investment[ROIinputkey.strip(" .,/!?@#$%^&*-=\;':<>").lower()] = float(ROIinputvalue)
                        print(self.investment)
                    except:
                        print(f'{ROIinputvalue} is not a valid number. No punctuations. Please try again.')
            elif ROIinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "delete":
                print(self.investment)
                while True:
                    ROIinputdelete = input('Please enter the name of the investment type saved that you wish to change. Type "Finish" when finished.')
                    if ROIinputdelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "finish":
                        print(self.investment)
                        break
                    elif ROIinputdelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") in self.investment:
                        ROIinputdelete = input('Would you like to delete/modify the income type? Please type "delete" or "modify"')
                        if ROIinputdelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == 'modify':
                            ROIinputmodify = input('Please enter the new value in dollars.')
                            try:
                                self.investment[ROIinputdelete.lower().strip(" .,/!?@#$%^&*-=\;':<>")] = float(ROIinputmodify)
                                print(self.investment)
                            except:
                                print(f'{ROIinputmodify} is not a valid number. Please try again.')                
                        elif ROIinputdelete.lower().strip(" .,/!?@#$%^&*-=\;':<>") == 'delete':
                            del self.investment[ROIinputdelete]
                            print(self.investment)
                    else:
                        print(f'{ROIinputdelete} is not a saved investment type. Please try again.')
            elif ROIinput.lower().strip(" .,/!?@#$%^&*-=\;':<>") == "total":
                print(f'Your total investment amount is ${sum(self.investment.values())}')
                return self.investment
            else: 
                print(f'{ROIinput} is not a valid action. Please try again.')
    def cashROI(self):
        cashf = sum(self.income.values())-sum(self.expense.values())
        try:
            print(f'Your ROI for this property is {(cashf*12)/sum(self.investment.values())*100}%.')
            self.ROI = f'{(cashf*12)/sum(self.investment.values())*100}%'
            
        except:
            print(f'Unable to calculate ROI. Investment values are not inputted. Please try again.')
            self.investmentROI()
            self.cashROI()
            
        
        
        
def calculateROI(item):
    calculateinput = input('What would you like to do? Calculate cash flow or ROI? Please type cash or ROI.')
    if calculateinput.lower().strip() == "cash" or calculateinput.lower().strip() == "cash flow":    
        item.incomeROI()
        item.expenseROI()
        item.cashflow()
    elif calculateinput.lower().strip() == "roi":
        item.incomeROI()
        item.expenseROI()
        item.cashflow()
        item.investmentROI()
        item.cashROI()
    else: 
        print(f'{calculateinput} is an invalid input. Please try again.')
House1 = RentalProperty()    
House2 = RentalProperty()
calculateROI(House2)
