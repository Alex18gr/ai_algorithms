import csv
from datetime import datetime

from walkSat import csv_results
import matplotlib.pyplot as plt

[values, data] = csv_results.read_csv_results('results1574607831.166307.csv')

values_list = list(values)
values_list.sort()

# this dictionary holds the calculated satisfiable probability for each m/n value
values_dict = dict.fromkeys(values_list, 0.0)

for val in values_list:
    total = 0
    total_trues = 0
    for d in data:
        if d[5] == val:
            total += 1
            # the satisfied condition is the max fips
            if d[3] < 10000:
                total_trues += 1
    # how the probability is calculated
    values_dict[val] = total_trues / total

# print(values_dict)

# creating the plot using the matplot lib
plt.plot(list(values_dict.keys()), list(values_dict.values()))
plt.scatter(x=list(values_dict.keys()), y=list(values_dict.values()))
plt.xlabel('clauses / Symbols ratio m/n')
plt.ylabel('P(Satisfiable)')
plt.xticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
plt.show()

# # write the results of each test to a csv file named results + timestamp
# with open('results_prob_' + datetime.now().timestamp().__str__() + '.csv', 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     for i in range(0, len(list(values_dict.keys()))):
#         wr.writerow([list(values_dict.keys())[i], list(values_dict.values())[i]])
