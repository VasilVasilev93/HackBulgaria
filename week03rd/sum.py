# sum.py
import sys


def main():
    nums = []
    sums = 0
    arg = sys.argv[1]
    file = open(arg, "r")
    nums.append(file.read().split(" "))
    for k in range(0, len(nums[0]) - 1):
        sums += int(nums[0][k])
    file.close()
    print (sums)

if __name__ == '__main__':
    main()
