name=input("Enter client name: ")
loan = float(input("Enter amount of loan: "))
days=int(input("Enter days taken with loan: "))

total= loan + (0.1 * loan) 

"""for days less than or equal to 30"""

if days <=30: 
    print("Total amount from ",name, "is: ", total)
#for days greater than 30
elif days >30:
    extra_days= days-30
    real_total= total+(0.01*loan*extra_days)
    print("total amount from",name,"is: ",real_total)










