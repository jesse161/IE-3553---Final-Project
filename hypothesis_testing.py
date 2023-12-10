import scipy.stats as sci
import numpy as np

n = 200
critical_point = sci.t.ppf(0.95, df = n-1)

#Avg Hourly Casino Profit, Ind Variable: Num of Decks (2, 4, 6)
five_dollar = [1407.43, 1144.12, 1408.48, 779.98, 1411.54, 1035.45]

fifteen_dollar = [4216.37, 8398.3, 4233.92, 10346.46, 4235.52, 6868.37]

twenty_five_dollar = [7023.26, 21672.51, 7036, 23560.48, 7041.67, 22857.12]

# 2 Deck vs 4 Deck
print("2 Deck v 4 Deck")
for i in (five_dollar, fifteen_dollar, twenty_five_dollar):
    t0 = (i[0] - i[2])/np.sqrt((i[1]/n)+(i[3]/n))
    if abs(t0) <= critical_point:
        print("Fail to reject hypothesis")
    else:
        print("Reject")

#4 Deck vs 6 Deck
print("4 Deck v 6 Deck")
for i in (five_dollar, fifteen_dollar, twenty_five_dollar):
    t0 = (i[2] - i[4])/np.sqrt((i[3]/n)+(i[5]/n))
    if abs(t0) <= critical_point:
        print("Fail to reject hypothesis")
    else:
        print("Reject")

#2 Deck vs 6 Deck
print("2 Deck v 6 Deck")
for i in (five_dollar, fifteen_dollar, twenty_five_dollar):
    t0 = (i[0] - i[4])/np.sqrt((i[1]/n)+(i[5]/n))
    if abs(t0) <= critical_point:
        print("Fail to reject hypothesis")
    else:
        print("Reject")

#Avg Hourly Casino Profit, Ind Variable: Blackjack Payouts (3-2, 6-5)
five_dollar1 = [1411.54, 1035.45, 1444.68, 973.69]

fifteen_dollar1 = [4235.52, 6868.37, 4323.52, 8552.6]

twenty_five_dollar1 = [7041.67, 22857.12, 7232.85, 21240.06]

print("3-2 vs 6-5")
for i in (five_dollar1, fifteen_dollar1, twenty_five_dollar1):
    t0 = (i[0] - i[2])/np.sqrt((i[1]/n)+(i[3]/n))
    if abs(t0) <= critical_point:
        print("Fail to reject hypothesis")
    else:
        print("Reject")

#Avg Hourly Casino Profit, Ind Variable: Hand Fee???
print("$2 Table")
t0 = (701.88-563.32)/np.sqrt((153.96/n)+(153.32/n))
if abs(t0) <= critical_point:
    print("Fail to reject hypothesis")
else:
    print("Reject")
