class Dataset:
    def __init__(self, nbvar, nbclauses, symbols, clauses):
        self.nbvar = nbvar
        self.nbclauses = nbclauses
        self.symbols = symbols
        self.clauses = clauses

    def __str__(self):
        return "number of variables: {self.nbvar}, number of clauses: {self.clauses}, symbols: {self.symbols}".format(
            self=self)


def read_file_input(url):
    f = open(url, 'r')
    # print(f.readlines())

    line = f.readline().strip().split(' ')
    while line[0] == 'c':
        line = f.readline().strip().split(' ')

    # print(line)

    if line[0] != 'p':
        return False

    n_values = int(line[2])
    n_clauses = int(line[3])

    clauses = []

    for i in range(n_clauses):
        c_line = [int(x) for x in f.readline().strip().split(' ')[0:-1]]
        clauses.append(c_line)
        # print(c_line)

    symbols = [x for x in range(1, n_values + 1)]
    # print(symbols)
    ds = Dataset(n_values, n_clauses, symbols, clauses)
    # print(ds)
    return ds
