class maxLoops:

    def __init__(self):
        print(self.maxFor([1, 2, 3, 4, 5]))
        print(self.maxFor([57, 62, 5, 26, 550, 9]))
        print(self.maxWhile([1, 2, 3, 4, 5]))
        print(self.maxWhile([57, 62, 5, 26, 550, 9]))

    def maxFor(self, nums):
        bigNum = nums[0]
        for num in nums[1:]:
            if num > bigNum:
                bigNum = num
        return bigNum

    def maxWhile(self, nums):
        bigNum = nums[0]
        counter = 0
        while counter < len(nums):
            if nums[counter] > bigNum:
                bigNum = nums[counter]
            counter += 1
        return bigNum

maxLoops()
