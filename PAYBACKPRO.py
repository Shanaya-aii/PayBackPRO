#Loan interest calculator (Displays Graph and Final result)
import matplotlib.pyplot as plt

def simple_interest(original_amount, years, rate):
    final_amount = original_amount * ( 1 + rate * years)
    return final_amount

def compound_interest(original_amount, years, rate):
    final_amount = original_amount * ((1 + rate) ** years)
    return final_amount

#finding out the increased amount each year to show yearly growth on graphs (list)

def simple_interest_growth(original_amount, years, rate):
    return [original_amount * (1 + rate * y) for y in range(years + 1)]

def compound_interest_growth(original_amount, years, rate):
    return [original_amount * ((1 + rate) ** y) for y in range(years + 1)]


print("Loan Interest Calculator \n ")
original_amount = float(input("Enter the loan amount:"))
rate_percent = float(input("Enter the percentage (%) interest rate: "))
years = int(input("Enter the number of years: "))
choice = input("Is it simple or compound interest?")

#change percentage rate to decimal rate:
rate = rate_percent / 100

#rounding the variable "final" to 2.d.p

if choice.lower() == "simple" :
    final = simple_interest(original_amount, years, rate)
    print("Your final amount after", years, " years is: £" , round(final,2))
    values = simple_interest_growth(original_amount, years, rate)
    

elif choice.lower() == "compound" :
    final = compound_interest(original_amount, years, rate)
    print("Your final amount after", years, " years is: £" , round(final,2))
    values = compound_interest_growth(original_amount, years, rate)
    

else:
    print("Invalid interest type.")
    exit()

# plotting a graph:
# creating a list starting from 0 to the total amount of years for the x axis:

years_list = list(range(years + 1))

#using the year_list as the x axis, the values list with the list of amount each year, and the marker as an "o" to clearly show data points.

plt.plot(years_list, values, marker='o') 
plt.title(f"{choice.capitalize()} Interest Over Time")
plt.xlabel("Time (In Years) ")
plt.ylabel("Amount (£)")
plt.grid(True)
plt.tight_layout()
plt.show()

    


    

