import csv


def read_csv_results(file_name):
    """
    read the data from the csv file with the given name and fix the value types and
    :param file_name:
    :return: the m/n values and the normalized data from the csv file
    """
    data = []
    values = set()

    # open the csv file
    with open(file_name, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # manipulate the data for each row based on the variable type
        for row in readCSV:
            row[0] = int(row[0])
            row[1] = int(row[1])
            row[2] = float(row[2])
            row[3] = int(row[3])
            row[4] = bool(row[4])
            # remove the last row that holds the model and we do not need it for the calculations
            row = row[:-1]
            # append to the end of the list the m/n value
            row.append(row[0] / row[1])
            # print(row)
            values.add(row[5])

            data.append(row)

    return values, data
