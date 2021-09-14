# def addDigits(num: int):
#     if num == 0:
#         return 0
#     if num % 9 == 0:
#         return 9
#     return num % 9
# print(f'Value from method 2 is {addDigits(199)}')

# arr = [0,3,2,1]
# a1 = max(arr)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if (arr[i] < a1) and (a1 > arr[j]):
#             out = True
# out

# n =[6,2,6,5,1,2]
# n.sort()
# xc = n[::2]
# print(sum(xc))

# Longest Common Prefix
# s = ["flower","flow","flight"]
# def foo(s):
#     for i in range(len(s[0])):
#         # print(s[0][i])
#         c = s[0][i]
#         for j in range(1,len(s)):
#             if i == len(s[j]) or s[j][i] != c:
#                 return s[0][:i]
#     return s[0]
# print(foo(s))

# Power set of a list
# def powerset(s):
#     ax = []
#     for i in range(1 << len(s)):
#         out = [s[j] for j in range(len(s)) if (i & (1 << j))]
#         ax.append(out)
#     return ax
# print(powerset([1,2,3,4]))

# def maxArea(height):
#       left, right = 0, len(height)-1
#       dummy_value = 0
#       while left < right:
#         dummy_value = max(dummy_value, (right-left) * min(height[left], height[right]))
        
#         if height[left] < height[right]:
#             left+=1
#         else:
#             right-=1
    
#       return dummy_value
# print(maxArea([1,1]))

# # Missing Positive element in a list 
# def missing_element(nums):
#     max_element = max(nums)
#     value = []
#     for j in range(1,max_element):
#         if j not in nums:
#             value.append(j)
#             out = value[0]
#         else:
#             out = max_element + 1
#     # out = value[1]
#     return out
# print(missing_element([1,2,0]))

# Spiral Matrix 
# def spiral_matrix(matrix):
#     start_col,start_row,end_col,end_row = 0,len(matrix),0,len(matrix[0])

#     out = []
#     while start_col < end_col or start_row < end_row:
#     # Right 
#         if start_row < end_row:
#             for i in range(start_col,end_col):
#                 out.extend(matrix[start_row][i])
#         start_row += 1
    
#     # Down 
#         if start_col < end_col:
#             for i in range(start_row,end_row):
#                 out.extend(matrix[i][end_col])
#         end_col -= 1

#     # left
#         if start_row < end_row:
#             for i in range(start_col-1,end_col-1,-1):
#                 out.extend(matrix[end_row][i])
#         end_row -= 1
    
#     # Top
#         if start_col < end_col:
#             for i in range(end_row-1,start_row-1,-1):
#                 out.extend(matrix[i][start_col])
#         start_col += 1


#     return out

# print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))

# First and last of a given element
# def findFirstAndLast(arr, x) :
# 	first = -1
# 	last = -1
# 	for i in range(0, len(arr)) :
# 		if (x != arr[i]) :
# 			continue
# 		if (first == -1) :
# 			first = i
# 		last = i
	
# 	if (first != -1) :
# 		print([first,last])
# 	else :
# 		print("Not Found")
		
		
# # Driver code
# arr = [5,7,7,8,8,10]
# x = 8
# print(findFirstAndLast(arr,x))

# First four max values
# def maxSubArray(nums):
#         best = nums[0]
#         current = nums[0]
#         for i in nums[1:]:
#             current = max(i, current + i)
#             if current > best:
#                 best = current
#         return best
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Product of three numbers
# th = [1,2,3,4]
# for i in range(len(th)):
#     for j in range(i+1,len(th)):
#         out = th[i] * th[j]
#         # print(th[j])
# print(out)

# Largest common prefix
# def LCP1(s):
#     for i in range(len(s[0])):
#         c = s[0][i]
#         for j in range(1,len(s)):
#             if i == len(s[j]) or s[j][i] != c:
#                 return s[0][:i]
#     return s[0]
# print(f'Method 1 output is: {LCP1(["flower","flow","flight"])}')
# def LCP2(s):
#     if len(s) == 0: return ""
#     pref = s[0]
#     for i in range(1,len(s)):
#         while s[i].find(pref)!= 0:
#             pref = pref[:len(pref)-1]
#     return pref
# print(f'Method 2 output is: {LCP2(["flower","flow","flight"])}')

# Product of maximum val 
# def max_prod(nums):
#     nums.sort() # If our list is not sorted
#     return max(nums[-1] *nums[0] * nums[1], nums[-1] *nums[-2] * nums[-3])
# print(f'Method 1 output: {max_prod([-100,-98,-1,2,3,4])}')

# Product of Array without Self
# def aneruth(nums):
#     result = [1] * len(nums)
#     for i in range(len(nums)):
#         result[i] = nums[i-1] * result[i-1]
#     right_prod = 1
#     for i in range(len(nums)-1, -1, -1):
#         result[i] *= right_prod
#         right_prod *= nums[i]
#     return result
# print(aneruth([1,2,3]))

# Three Sum
# def threeSum(aList):
#     aList.sort()
#     res = []
#     setval = set()
#     for i in range(len(aList)):
#         for j in range(i+1,len(aList)):
#             for k in range(j+1,len(aList)):
#                 a,b,c = aList[i],aList[j],aList[k]
#                 if a+b+c == 0 and (a,b,c) not in setval:
#                     res.append([a,b,c])
#                     setval.add((a,b,c))
#     return res
# print(f'Method 1 output: {threeSum([-1,0,1,2,-1,-4])}')

# Word Pattern 
# def wordPattern(pattern, s):
#     s, pattern = s.split(), list(pattern)
#     a = map(s.index, s)
#     b = map(pattern.index, pattern)
#     return a == b
# print(wordPattern("abba", "Aneruth is a man"))

# contiguous Segment of a string
# def contiguousSegment2(astring):
#     return '01' not in astring
# print(f'Method 2 output {contiguousSegment2("110")}')

# Convert to any base
# def str_base(val, base):
#     res = ''
#     while val > 0:
#         res = str(val % base) + res
#         val //= base
#     if res: return sum([int(i) for i in res])
#     return 0
# print(f'Method 1 output is {str_base(10,10)}')

# Count Items Matching a Rule
# items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
# ruleKey = "type"
# ruleValue = "phone"
# def countMatches2(items, ruleKey, ruleValue):
#     if ruleKey == "type":
#         idx = 0
#     elif ruleKey == "color":
#         idx = 1
#     else:
#         idx = 2
#     return sum(1 for i in items if i[idx] == ruleValue)
# print(f'Method 2 Output is: {countMatches2(items, ruleKey, ruleValue)}')

##### Busy Student
# startTime,endTime = [1,2,3],[3,2,7]
# def busyStudent2(startTime, endTime, queryTime):
#         ans=0
#         for i,j in zip(startTime,endTime):
#             if i<=queryTime<=j: 
#                 ans += 1
#         return ans
# print(busyStudent2(startTime,endTime,5))

# temperatures = [73,74,75,71,69,72,76,73]
# def dailyTemperatures(T):
#     ans = [0] * len(T)
#     stack = []
#     for i in range(len(T)):
#         # maintain a monotonically decreasing stack with indices
#         while stack and T[stack[-1]] < T[i]: 
#             index = stack.pop()
#             ans[index] = i - index
#         stack.append(i)
#     return ans
# print(dailyTemperatures(temperatures))


# def minDeletionSize(strs):
#     result = 0
#     for i in range(len(strs[0])):
#         temp = [x[i] for x in strs]
#         result += 0 if temp == sorted(temp) else 1
#     return result
# print(minDeletionSize(["cba","daf","ghi"]))

# def search1(alist,target):
#     for i in alist:
#         if i == target:
#             return alist.index(target) 
#     return -1
# print(f'Method 2 output is: {search1([4,5,6,7,0,1,2],2)}')

# Search in Rotated Sorted Array
# You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [[0,1,2,4,5,6,7]] might become [[4,5,6,7,0,1,2]]).
# If target is found in the array return its index, otherwise, return -1.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
 
# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# def search(alist,target):
#     if target in alist: return alist.index(target)
#     return -1
# print(f'Method 1 output is: {search([4,5,6,7,0,1,2],2)}')

# num = '52'
# oddNums = ['1','3','5','7','9']
# for i in range(len(num)-1,-1,-1):
#     if(num[i] in oddNums):
#         print(num[:i+1])
#     else:
#         print("")

def largeNum(nums):
    out = list(map(lambda x: x*2,nums))
    maxEle = out[len(out)//2]
    for i in out:
        if maxEle < i:
            maxEle = i
            return nums.index(maxEle/2)
    return -1
print(largeNum([1,2,3,2]))