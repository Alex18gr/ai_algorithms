import csv
from datetime import datetime

import walkSat.walksat
import os
import walkSat.utils

"""

This script is used to run the test with the walkSAT algorithm from the walksat.py file.
The test files from the folder test_problems are used for the test. After each test the results are hold to a
list and then exported to a csv file

"""

# the path of the test files
path = 'test_problems'
results = []

# open each file in the given path
for filename in os.listdir(path):
    # print(filename)
    data = walkSat.utils.read_file_input('test_problems/' + filename)
    # print(data)
    # run each test 5 times to reduce error due to random model selections of the algorithm
    for i in range(0, 5):
        result = walkSat.walksat.walkSAT(data)
        print(result)
        results.append(result)

print(results)

# write the results of each test to a csv file named results + timestamp
with open('results' + datetime.now().timestamp().__str__() + '.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for res in results:
        wr.writerow(res)
