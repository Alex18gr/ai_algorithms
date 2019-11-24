import csv
from datetime import datetime

import walkSat.csv_results as csv_results
import matplotlib.pyplot as plt

# read the data from the csv results
[values, data] = csv_results.read_csv_results('walkSat/results1574607831.166307.csv')

values_list = list(values)
values_list.sort()

print(values_list)

# create a dictionary to hold the mean time value for the total tries of each m/n value
values_dict = dict.fromkeys(values_list, 0.0)

for d in data:
    if d[5] in values_dict:
        values_dict[d[5]] = (d[2] + values_dict[d[5]]) / 2



# print(list(values_dict.keys()))
# print(list(values_dict.values()))

# creating the plot using the matplot lib
plt.scatter(x=list(values_dict.keys()), y=list(values_dict.values()))
plt.plot(list(values_dict.keys()), list(values_dict.values()))
plt.xlabel('clauses / Symbols ratio m/n')
plt.ylabel('Runtime')
plt.xticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
plt.show()

# # write the results of each test to a csv file named results + timestamp
# with open('results_time_' + datetime.now().timestamp().__str__() + '.csv', 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     for i in range(0, len(list(values_dict.keys()))):
#         wr.writerow([list(values_dict.keys())[i], list(values_dict.values())[i]])