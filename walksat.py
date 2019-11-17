from utils import Dataset, read_file_input
import random


def check_model(dataset: Dataset, model):
    for c in dataset.clauses:
        if not check_clause_true(c, model):
            return False
    return True


def probability(p):
    return random.random() < p


def split_clauses(clauses, model):
    satisfied, unsatisfied = [], []
    for c in clauses:
        if check_clause_true(c, model):
            satisfied.append(c)
        else:
            unsatisfied.append(c)
    return [satisfied, unsatisfied]


def find_max_satisfied(abs_c, clauses, model):
    test_model = model.copy()

    max_satisfy_symbol = -1
    max_clauses_satisfied = -1
    for symbol in abs_c:
        test_model[symbol] = not test_model[symbol]
        satisfied_clauses_counter = 0
        for c in clauses:
            if check_clause_true(c, test_model):
                satisfied_clauses_counter += 1
        if satisfied_clauses_counter > max_clauses_satisfied:
            max_clauses_satisfied = satisfied_clauses_counter
            max_satisfy_symbol = symbol
    return max_satisfy_symbol


def change_max_valid_symbol(c, clauses, model):
    abs_c = map(abs, c)

    max_satisfy_symbol = find_max_satisfied(abs_c, clauses, model)

    model[max_satisfy_symbol] = not model[max_satisfy_symbol]


def change_rand_symbol(c, model):
    rand_symbol = abs(random.choice(c))
    # print(rand_symbol)
    model[rand_symbol] = not model[rand_symbol]


def walkSAT(dataset: Dataset, p=0.5, max_flips=10000):
    # assign random values to the clauses variables
    # model = {bool(random.getrandbits(1)) for s in dataset.symbols}
    model = {s: bool(random.getrandbits(1)) for s in dataset.symbols}
    # print(model)
    if check_model(dataset, model):
        return model, 0

    for i in range(max_flips):
        # split satisfied form unsatisfied clauses
        # satisfied, unsatisfied = [], []
        [satisfied, unsatisfied] = split_clauses(dataset.clauses, model)
        # print(unsatisfied)
        c = random.choice(unsatisfied)
        # print(c)
        if probability(p):
            change_rand_symbol(c, model)
        else:
            change_max_valid_symbol(c, dataset.clauses, model)

        # if unsatisfied is empty found solution
        if check_model(dataset, model):
            return model, i + 1

    return False, max_flips


def check_clause_true(clause, model):
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


def main():
    # d = Dataset(3, 3, [1, 2, 3], [[-3, 1, -2], [-2, -1, 3], [1, -3, 2]])
    d = read_file_input()
    print(d)
    [valid_model, flips] = walkSAT(d)
    print("Valid Model: ")
    print(valid_model)
    print("total flips: ")
    print(flips)


if __name__ == '__main__':
    main()
