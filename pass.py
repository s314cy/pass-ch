import argparse


def string_to_float(quotient):
    if quotient.count('/') > 1:
        raise ValueError
    terms = quotient.split('/')
    if len(terms) == 1:
        return float(terms[0])
    return float(terms[0]) / float(terms[1])


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--marks', nargs='+', type=str, required=True)
    parser.add_argument('-w', '--weights', nargs='+', type=str, required=True)
    parser.add_argument('-t', '--target', type=str, default='60/100')
    #parser.add_argument('-r', '--rounding', type=str, default='')
    args = parser.parse_args()

    assert len(args.marks) == len(args.weights)

    marks = [string_to_float(m) for m in args.marks]
    weights = [string_to_float(w) for w in args.weights]
    target = string_to_float(args.target)
    #factor = 1 / string_to_float(args.rounding)
    assert all([0 <= x <= 1] for x in marks + weights + [target])

    points = sum([mark * weight for mark, weight in zip(marks, weights)])
    final_weight = 1 - sum(weights)
    final_score = abs(target - points) / final_weight
    print(f'Need to score {final_score * 100}/100 points on final to reach {target * 5 + 1}')
