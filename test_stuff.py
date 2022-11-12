#a = p*(1 + (r/n))**(n*t)

a = 2119.11*(1 + (.04/52))**(52*1)
print(a)



'''
Money balance equation
robertson's cash-balance equation
p = m/kt

quantity theory of money formula
m*v = p*t
m = money supply
v = velocity of money
p = general price of goods
t = all transactions

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

round_compound = round(num_of_compound, 10)
#print(round_compound)
#round_compound = float(round_compound)
min_reward_input = float(min_reward_input)
max_reward_input = float(max_reward_input)
min_returns_per_week = (staking * min_reward_input/round_compound) #p = the principal investment amount (the initial deposit or loan amount) /12 months /4 weeks
max_returns_per_week = (staking * max_reward_input/round_compound)

min_compound_interest = min_returns_per_week*(1 + (min_reward_input/num_of_compound))**(round_compound*time_conversion) #1 = 1 year need to figure out the time calculation// (n*t) n = amount of times done // t = time period
max_compound_interest = max_returns_per_week*(1 + (max_reward_input/num_of_compound))**(round_compound*time_conversion)

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
'''