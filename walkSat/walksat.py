import time

from walkSat.utils import Dataset, read_file_input
import random


def check_model(dataset: Dataset, model):
    """
    This function checks whether the model is valid for the given dataset
    :param dataset:
    :param model:
    :return:
    """
    for c in dataset.clauses:
        if not check_clause_true(c, model):
            return False
    return True


def probability(p):
    """
    helper function, return a boolean value with the given probability
    :param p:
    :return:
    """
    return random.random() < p


def split_clauses(clauses, model):
    """
    Splits the given clauses in 2 lists based on the given model if they are satisfied or unsatisfied from it and return
    the 2 lists
    :param clauses:
    :param model:
    :return:
    """
    satisfied, unsatisfied = [], []
    for c in clauses:
        if check_clause_true(c, model):
            satisfied.append(c)
        else:
            unsatisfied.append(c)
    return [satisfied, unsatisfied]


def find_max_satisfied(abs_c, clauses, model):
    """
    Finds the symbol of the abs_c clause which when its value is changed, the most clauses of the list clauses
    are satisfied based on the given model
    :param abs_c:
    :param clauses:
    :param model:
    :return:
    """

    test_model = model.copy()

    max_satisfy_symbol = -1
    max_clauses_satisfied = -1
    # test every symbol in the abs_c symbols array
    for symbol in abs_c:
        # flip the value of that symbol in the model
        test_model[symbol] = not test_model[symbol]
        # counter for the satisfied clauses for that symbol flip
        satisfied_clauses_counter = 0
        for c in clauses:
            # check how many clauses are satisfied with that flip
            if check_clause_true(c, test_model):
                satisfied_clauses_counter += 1
        # check if we have a new max in satisfied clauses
        if satisfied_clauses_counter > max_clauses_satisfied:
            max_clauses_satisfied = satisfied_clauses_counter
            max_satisfy_symbol = symbol
    return max_satisfy_symbol


def change_max_valid_symbol(c, clauses, model):
    """
    changes the value of the symbol of the clause c which when its value is changed, the most clauses are satisfied
    of the list clauses based on the given model
    :param c:
    :param clauses:
    :param model:
    :return:
    """
    abs_c = map(abs, c)

    max_satisfy_symbol = find_max_satisfied(abs_c, clauses, model)

    model[max_satisfy_symbol] = not model[max_satisfy_symbol]


def change_rand_symbol(c, model):
    """
    changes the value of a random symbol of the clause c
    :param c:
    :param model:
    :return:
    """
    rand_symbol = abs(random.choice(c))
    # print(rand_symbol)
    model[rand_symbol] = not model[rand_symbol]


def walkSAT(dataset: Dataset, p=0.5, max_flips=10000):
    start_time = time.time()
    # assign random values to the clauses variables
    model = {s: bool(random.getrandbits(1)) for s in dataset.symbols}

    # check if the random generated model is solution
    while check_model(dataset, model):
        model = {s: bool(random.getrandbits(1)) for s in dataset.symbols}

    # start of the algorithm
    for i in range(max_flips):
        # split satisfied form unsatisfied clauses
        [satisfied, unsatisfied] = split_clauses(dataset.clauses, model)

        # select a random unsatisfied clause
        c = random.choice(unsatisfied)

        if probability(p):
            change_rand_symbol(c, model)
        else:
            change_max_valid_symbol(c, dataset.clauses, model)

        # if unsatisfied is empty found solution
        if check_model(dataset, model):
            return [dataset.nbclauses, dataset.nbvar, time.time() - start_time, i + 1, True, model]

    # here is the case that we dont find any solution after the max flips done
    return [dataset.nbclauses, dataset.nbvar, time.time() - start_time, max_flips, False, model]


def check_clause_true(clause, model):
    """
    checks if a clause is satisfied based on the given model
    :param clause:
    :param model:
    :return:
    """
    for c in clause:
        # print(c)
        # print(model[1])
        if c < 0:
            value = not model[abs(c)]
        else:
            value = model[abs(c)]
        if value:
            return True
    return False


# This main is for test purposes
def main():
    # d = Dataset(3, 3, [1, 2, 3], [[-3, 1, -2], [-2, -1, 3], [1, -3, 2]])
    for i in range(0, 6):
        d = read_file_input('walkSat/sat_275_50_1_.dimacs')
        print(d)
        print(walkSAT(d))


if __name__ == '__main__':
    main()
