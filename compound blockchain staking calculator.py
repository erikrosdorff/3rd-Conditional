#lets make a calucator that shows our ROI in crypto staking
'''
V1
Insert coins manually

#convert to currency (e.g. usd -> $ etc.)

v2
See history of "would have been" investments

v3
Connect through API (VPN?)

Looks at your current shares:
1) Shows how much you have in Currency and USD (or any other variant of your choosing)
2) If you stake a coin, what will be the return in coin currency and in fiat currency
3) Shows minium and maximuim return estamates per week, month, and year.
4) Finds your target, and suggests how much you need to invest based on the current price
5) Shows changes in price and how much you should invest to make your target
6) Shows how much you would have needed to invest based on previous prices

#a = p(1 + (r/n))**(n*t)

n = number of times per t (e.g. 1 time a week is 52)
returns_per_week = (amount_staked * .04)/12)/4) #p
interest_rate = reward_percentage #kraken #r
def number_of_times_per_period(times) #n
if 1 time per week:
    num_of_times_per_period = 12/4
else: #twice a week
    num_of_times_per_period = (12/4)/2
t = length_of_time

staked_interest = returns_per_week(1 + (interest_rate/number_of_times_per_week))**(number_of_times_per_week/t) )



Select Coin
Select Currency
Select Compouded or Returned
#Connect Kraken account somehow?
See price history


{Coin}  {Symbol}    Price per {currency}   Staking     Staking ROI Percentage     Min ROI Per Week {Coin}   Max ROI Per Week {Coin}      Min ROI Per Week {Currency}   Max ROI Per Week {Currency}     

    Estimated ROI Per Month #average    Min ROI Per Month{coin}   Max ROI Per Month{coin}   Min ROI Per month based on {price per{currency}}    Max ROI Per month based on {price per{currency}}

    Estimated ROI per year #average     Min ROI in 1 year{coin}   Max ROI in 1 year{coin}   Min ROI Per year based on {price per{currency}}    Max ROI Per year based on {price per{currency}}

    Min max rewards earned      min max rewards earned


'''

#a = p*(1 + (r/n))**(n,t) 
#A = the future value of the investment/loan, including interest
#P = the principal investment amount (the initial deposit or loan amount)
#r = the annual interest rate (decimal)
#n = the number of times that interest is compounded per unit t
#t = the time the money is invested or borrowed for
#[staked_interest = returns_per_week(1 + (interest_rate/number_of_times_per_week))**(number_of_times_per_week/t) )]
#If an amount of $5,000 is deposited into a savings account at an annual interest rate of 5%, 
#compounded monthly, the value of the investment after 10 years can be calculated as follows...
#P = 5000.
#r = 5/100 = 0.05 (decimal).
#n = 12.
#t = 10.
#If we plug those figures into the formula, we get the following:
#A = 5000 (1 + 0.05 / 12) (12 * 10) = 8235.05.
#So, the investment balance after 10 years is $8,235.05.

import math
import time

#This section only takes in the coin's value
coin = input("Enter name of the coin: ")
symbol = input("Enter coin Symbol: ")
price_input = float(input("Enter current price of coin USD: "))
price = float(price_input)
staking = float(input("Enter how many coins are being staked: "))
min_reward_input = input("Enter minimuim reward percentage, e.g. 12: ")
min_reward = f'{float(min_reward_input) / 100:.1%}' #fstring converts to percentage

def max_reward_fun(max):
    if max == 'None' or 'none' or 0:
        return None 
    else:
        return max
max = input("Enter maximuim reward percentage (If there is only one, simply write 'none'): ")
max_reward_input = max
max_reward = f'{float(max) / 100:.1%}'

time_period = input("Enter time period: either Y M W: ")

def time_period_conversion(time_period):
    time = 0
    if time_period == 'Y' or 'y':
        time = 365
        print("365 Days")
    elif time_period == 'M' or 'm':
        time = 30 #find for different months
        print("30 Days")
    elif time_period == 'W' or 'w':
        time = 7
        print("7 Days")
    else:
        print("Not a valid time period.")
    return time

num_times_interest_compounded = str(input("Enter number of times interest is compounded: ")) #Daily Weekly Monthly Yearly

#t = time period = year? month? week? day? hour?


#def num_investments (n):


#def amount_time(time):
#n = amount of times in a certain period you invest (t)
#t = time period (Year, day, month, etc.)

#a = p*(1 + (r/n))**(n*t) 

min_reward_input = int(min_reward_input)
max_reward_input = int(max_reward_input)
min_returns_per_week = (staking * min_reward_input/52) #p = the principal investment amount (the initial deposit or loan amount) /12 months /4 weeks
max_returns_per_week = (staking * max_reward_input/52)

min_compound_interest = min_returns_per_week*(1 + (min_reward_input/52))**(52*1) #1 = 1 year need to figure out the time calculation// (n*t) n = amount of times done // t = time period
max_compound_interest = max_returns_per_week*(1 + (max_reward_input/52))**(52*1)

min_compound_interest_USD = price * min_compound_interest
max_compound_interest_USD = price * max_compound_interest
symbol_upper = symbol.upper()
coin_capitalize = coin.capitalize()


print('Coin: ', coin_capitalize, "\n"
     'Symbol: ' , symbol_upper, '\n'
     'Price: $' , price , '\n'
     'Staking: ', staking, '\n'
     'Minimuim Reward: ', min_reward, '\n'
     'Maximuim Reward: ', max_reward, '\n' 
     "Minimuim Compound Staking Interest: ", min_compound_interest, symbol_upper, '\n'
     "Maximuim Compound Staking Interest: ", max_compound_interest, symbol_upper, '\n'
     "Min USD: ", "${:.2f}".format(min_compound_interest_USD), '\n'
     "Max USD: ", "${:.2f}".format(max_compound_interest_USD))