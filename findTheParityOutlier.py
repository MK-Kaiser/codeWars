def find_outlier(integers):
    if integers[0] % 2 == 0 and integers[1] %2 ==0 and integers[2] %2 ==0: # handles even
        for i in range(0, len(integers)):
            if integers[i] %2 != 0:
                return integers[i]
    if integers[0] % 2 != 0 and integers[1] %2 !=0 and integers[2] %2 !=0: # handles odd
        for i in range(0, len(integers)):
            if integers[i] %2 == 0:
                return integers[i]
    else:
        if integers[0]%2 == integers[2]%2:
            return integers[1]
        if integers[0]%2 == integers[1]%2:
            return integers[2]
        if integers[1]%2 == integers[2]%2:
            return integers[0]
    
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
Examples

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)

'''
