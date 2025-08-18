        # Given the list nums = [10, 20, 30, 40, 50], write a slice to get the first three elements.

nums = [10, 20, 30, 40, 50]
print(nums[0:3])

        # 2. From the list nums = [1, 2, 3, 4, 5], retrieve all elements except the first one using slicing.

nums = [1, 2, 3, 4, 5]
print(nums[1:5])

        # Given colors = ['red', 'green', 'blue', 'yellow'], slice the list to get only ['green', 'blue'].

colors = ['red', 'green', 'blue', 'yellow']
print(colors[1:3])

            #  From fruits = ['apple', 'banana', 'cherry', 'mango'], use slicing to get ['banana', 'cherry', 'mango'].

fruits = ['apple', 'banana', 'cherry', 'mango']
print(fruits[1:4])

            # Given nums = [5, 10, 15, 20, 25, 30], slice to get the last two elements only.

nums = [5, 10, 15, 20, 25, 30]
print(nums[4:])

            # Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use slicing to get every second element.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[1:10:2])

            # From the list letters = ['a', 'b', 'c', 'd', 'e', 'f'], get the elements from index 2 to the end.
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[2:])

        # Given nums = [10, 20, 30, 40, 50, 60, 70], use slicing to reverse the list.

nums = [10, 20, 30, 40, 50, 60, 70]
length=len(nums)+1
print(nums[::-1])
print(nums[-1:-length:-1])

            # From data = [1, 3, 5, 7, 9, 11, 13], slice the list to get elements starting from index 1 up to index 5 with a step of 2.

data = [1, 3, 5, 7, 9, 11, 13]
print(data[1:5:2])

        # Given nums = [100, 200, 300, 400, 500, 600], use slicing to get [200, 300, 400] without specifying the start index explicitly

nums = [100, 200, 300, 400, 500, 600]
print(nums[1:4:])

        # Given nums = [1, 2, 3, 4, 5], what will be the output of nums[10:]? Explain why.

nums = [1, 2, 3, 4, 5]
print(nums[10:])
# The list nums has a length of 5 (indices 0 to 4).
# The slice nums[10:] attempts to start slicing from index 10.
# Since index 10 is beyond the valid range of indices for nums (which are 0, 1, 2, 3, 4), no elements can be retrieved from that starting point.
# Therefore, the result is an empty list.

            # 2. From nums = [1, 2, 3, 4, 5], slice the list to get [4, 3, 2] using a negative step value.

nums = [1, 2, 3, 4, 5]
print(nums[-2:-5:-1])

        # Given nested = [[1, 2], [3, 4], [5, 6]], slice to get the first two sublists.

nested = [[1, 2], [3, 4], [5, 6]]
print(nums[0:4:])

              # From nums = list(range(1, 21)), use slicing to get the last 5 elements in reverse order.

nums = list(range(1, 21))
print(nums[-1:-6:-1])

            # Given nums = [10, 20, 30, 40, 50], what happens if you slice it as nums[-1:-4]? Explain and fix it to get [50, 40, 30].
nums = [10, 20, 30, 40, 50]
print(nums[-1:-4:-1])