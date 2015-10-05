def centered_average(nums):
    # couting centered_average for given list
    nums = del_1max(nums)
    nums = del_1min(nums)
    total = 0
    for i in range(0,len(nums)-1):
        total += nums[i]
    print total/len(nums)

def del_1min(x):
    # deleting only 1 element with min value from the array
    a = min(x)
    for i in range(0,len(x)-1):
        if x[i] == a:
            del x[i]
            return x

def del_1max(x):
    # deleting only 1 element with max value from the array
    b = max(x)
    for i in range(0,len(x)-1):
        if x[i] == b:
            del x[i]
            print('exit here')
            return x
    print('or exit here')


if __name__ == '__main__':
    print(centered_average([1, 2, 3, 4, 100]))
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))
    print(centered_average([-10, -4, -2, -4, -2, 0]))