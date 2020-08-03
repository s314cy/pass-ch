import argparse
import math


def string_to_float(quotient):
    terms = [float(x) for x in quotient.split('/')]
    r = terms[0]
    for i in range(quotient.count('/')):
        r /= terms[i + 1]
    return r
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--marks', nargs='+', type=str, required=True)
    parser.add_argument('-w', '--weights', nargs='+', type=str, required=True)
    parser.add_argument('-t', '--target', type=str, default='60/100')
    args = parser.parse_args()
    assert len(args.marks) == len(args.weights)

    marks = [string_to_float(m) for m in args.marks]
    weights = [string_to_float(w) for w in args.weights]
    target = string_to_float(args.target)
    assert all(0 <= x <= 1 for x in marks + weights + [target])

    points = sum(mark * weight for mark, weight in zip(marks, weights))
    assert 0 <= points < 1
    final_weight = 1 - sum(weights)
    final_score = abs(target - points) / final_weight

    display_score = math.ceil(final_score * 1000) / 10
    display_target = target * 5 + 1
    print(f'Need to score {display_score:.1f}/100 points on final to reach {display_target:.3f}')
