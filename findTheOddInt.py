def find_it(seq):
    count = dict()
    iteration = 0
    current = seq[0]
    previous = None
    return rec_find(seq, iteration, count, current, previous)

def rec_find(seq, iteration, count, current, previous):
    if iteration != len(seq):
        current = seq[iteration]
        if current not in count.keys():
            count[current] = 1
        elif current in count.keys():
            count[current] = count.get(current, 0) + 1
        previous = current
        return rec_find(seq, iteration + 1, count, current, previous)
    else:
        return find_odd_int(count)


def find_odd_int(odd_ints):
    for i in odd_ints.items():
        if i[1] % 2 != 0:
            return i[0]
        


test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5);
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);


'''Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''
