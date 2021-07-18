# Required Packages
from collections import Counter
from itertools import combinations
import textwrap as wp
# import numpy as np
import itertools,re
class hacerRank():
    def __init__(self) -> None:
        pass

    # Sales by Match
    # There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
    # Example 
    # n = 7
    # arr = [[1,2,1,2,1,3,2]]
    # There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
    # Function Description
    # Complete the sockMerchant function in the editor below.
    # sockMerchant has the following parameter(s):
    # int n: the number of socks in the pile
    # int arr[[n]]: the colors of each sock
    # Returns 
    # int: the number of pairs
    @staticmethod
    def salesMatch(self,arr):
        c = 0
        for i in Counter(self.arr).values():
            c += int(i/2)
        return c
    # print(f'Method 1 solution is: {salesMatch1([1,2,1,2,1,3,2])}')

    # Left Rotation
    # A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
    # For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. 
    # Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
    # Given an array a of n integers and a number,d , perform d left rotations on the array. 
    # Return the updated array to be printed as a single line of space-separated integers.
    def leftRotation(self,alist,n):
        return self.alist[self.n:] + self.alist[:self.n]
    # print(f'Left rotation array is {leftRotation([1,2,3,4,5],3)}')

    # Minimum Swaps 2 
    # You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
    # You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
    # Example : arr = [7,1,3,2,4,5,6] Number of swaps: 5 --> output
    # using bubble sort we can count the number of swaps required
    # Partial output solves 3/15 test cases 
    @staticmethod
    def minSwaps(self,alist):
        counter = 0
        for j in range(len(self.alist)):
            for i in range(len(self.alist)-1):
                if self.alist[i] > self.alist[i+1]:
                    self.alist[i],self.alist[i+1]  = self.alist[i+1],self.alist[i]
                    counter += 1
        return self.alist,counter
    # print(minSwaps([7,1,3,2,4,5,6]))

    # Hash Tables: Ransom Note
    # Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. 
    # He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. 
    # The words in his note are case-sensitive and he must use only whole words available in the magazine. 
    # He cannot use substrings or concatenation to create the words he needs.
    # Given the words in the magazine and the words in the ransom note, 
    # print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
    # Example
    # magazine = "attack at dawn"; note = "Attack at dawn"

    # Method 1
    @staticmethod
    def ransome1(self,mag,note):
        counter = 0
        for m in range(len(self.mag.split(" "))):
            for n in range(1,len(self.note.split(" "))):
                if self.note.split(" ")[n] == self.mag.split(" ")[m]:
                    counter += 1
        
        if counter == len(self.note.split(" ")):
            return 'Yes'
        return 'No'
    # print(f'Can we replicate the Magazine: {ransome1("two times three is not four","two times two is four")}')

    # Method 2 (#bettermethod)
    @staticmethod
    def ransome2(self,mag,note):
        return (Counter(self.note) - Counter(self.mag)) == {}
    # print(f'Can we replicate the Magazine: {ransome2("two times three is not four","two times two is four")}')

    # Two Strings
    # Given two strings, determine if they share a common substring. A substring may be as small as one character.
    # Example: s1: 'and'; s2: 'art' common substring 'a'.
    @staticmethod
    def twoStrings1(self,s1,s2):
        return (set(self.s1).intersection(set(self.s2)),len(set(self.s1).intersection(set(self.s2))) >= 1)
    # print('Is there any common susbstring present {1} and the string is {0}'.format(twoStrings1("hello","world")[0],twoStrings1("hello","world")[1]))

    # Alternating Characters
    # You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. 
    # To do this, you are allowed to delete zero or more characters in the string.
    # Your task is to find the minimum number of required deletions.
    # Example s = AABAAB requires two deletions to make s = ABAB 
    # Loop through the string and if we find the next immediate string similar to the first one then we increment the counter value.
    @staticmethod
    def alterChar(self,string):
        count = 0
        for i in range(len(self.string)-1):
            if self.string[i] == self.string[i+1]:
                count += 1
        return count
    # print(f'Number fo deletions required to make the array alternative: {alterChar("AAAA")}')

    # Triple sum
    # Given 3 arrays a,b,c of different sizes, find the number of distinct triplets (p,q,r) where p is an element of a and p<=q ,q>=r.
    # Example: a = [3,5,7]; b = [3,6]; c = [4,6,9] output: 4 (4 different triplets)
    @staticmethod
    def threeSum(self,a,b,c):
        return list(set([(i,j,k) for i in self.a for j in self.b for k in self.c if i<=j and j>=k]))
    # print(f'Distinct triplets is: {threeSum([3,5,7],[3,6],[4,6,9])} and its length is {len(threeSum([3,5,7],[3,6],[4,6,9]))}')

    # Merge the Tools!
    @staticmethod
    def mergeTools(self,string,k):
        out = [''.join(list(set(i))) for i in wp.wrap(self.string,self.k)]
        print("\n".join(out))
    # mergeTools("ABBABSCD",4)

    # Common Child
    # A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. 
    # Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
    # Example: s1 --> "ABCD" s2 --> "ABDC" otuput: 3 (Returns the length of the common child present in both strings)
    # Yet to see this
    @staticmethod
    def commonChild(self,s1, s2):
        # Function to fetch all the substring
        def Sub_Sequences(string):
            combs = []
            for l in range(1, len(string)+1):
                combs.append(list(itertools.combinations(string, l)))
            ts = [''.join(t) for c in combs for t in c]
            return ts
        s1List = Sub_Sequences(self.s1)
        s2List = Sub_Sequences(self.s2)
        counter = [len(i) for i in s1List for j in s2List  if i == j]
        return max(counter)
    # print(f'Maximum length of common child is: {commonChild("ABCD","ABDC")}')

    # Capitalize!
    # You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
    # For example, alison heck should be capitalised correctly as Alison Heck.
    # Given a full name, your task is to capitalize the name appropriately.

    # Method 1 using lambda function
    @staticmethod
    def solve1(self,s):
        dum = lambda name: name.title()   
        return dum(self.s) 
    # print(f'{solve1("aneruth mohanasundaram")}')

    # Method 2 using for loop
    @staticmethod
    def solve2(self,s):
        return ' '.join([i.title() for i in self.s.split(' ')])
    # print(f'{solve2("aneruth mohanasundaram")}')    

    # Time Delta
    # When users post an update on social media,such as a URL, image, status update etc., 
    # other users in their network are able to view this new post on their news feed. 
    # Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
    # Since sometimes posts are published and viewed in different time zones, this can be confusing. 
    # You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
    # Day dd Mon yyyy hh:mm:ss +xxxx
    # Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
    # See this later
    @staticmethod
    def timeDelta(self,s1,s2):
        return

    # Sherlock and the Valid String
    # Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
    # Example
    # s = abc | This is a valid string because frequencies are {a:1,b:1,c:1}
    @staticmethod
    def isvalid(self,s):
        hash_map = Counter(self.s)
        freq_map = Counter(hash_map.values())
        if len(freq_map) == 1: return 'YES'
        if len(freq_map) >= 2: return 'NO'
        if 1 in freq_map and (freq_map[min(freq_map.keys())] == 1 or (min(freq_map.keys()) - max(freq_map.keys())) == 1 ):
            return 'YES'
        else:
            return 'NO'
    # print(f'This string is valid? {isvalid("abcdefghhgfedecba")}')

    # Compare the Triplets 
    # Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
    # The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
    # The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
    # If a[i] > b[i], then Alice is awarded 1 point.
    # If a[i] < b[i], then Bob is awarded 1 point.
    # If a[i] = b[i], then neither person receives a point.
    # Comparison points is the total points a person earned. Given a and b, determine their respective comparison points.
    # Function Description
    # Complete the function compareTriplets in the editor below.
    # compareTriplets has the following parameter(s):
    # int a[3]: Alice's challenge rating
    # int b[3]: Bob's challenge rating
    # Return
    # int[2]: Alice's score is in the first position, and Bob's score is in the second.
    @staticmethod
    def compareArr(self,alist,blist):
        dic = {"Alice":0,"Bob":0}    
        for i,j in zip(self.alist,self.blist):
            if i>j:
                dic['Alice'] += 1
            elif i < j:
                dic['Bob'] += 1
        return list(dic.values())
    # print(f'Alice and Bob score is: {compareArr([17,28,30],[99,16,8])}')

    # Diagonal Difference
    # For example, the square matrix arr is shown below:
    #     1 2 3
    #     4 5 6
    #     9 8 9  
    # The left-to-right diagonal = 1 + 5 + 9 = 15.  
    # The right to left diagonal = 3 + 5 + 9 = 17. 
    # Their absolute difference is |15 -17| = 2.
    @staticmethod
    def diagonalDifference(self,arr):
        row = len(self.arr[0])
        sum_diag1 = sum([self.arr[i][i] for i in range(row)])
        sum_diag2 = sum([self.arr[row-1-i][i] for i in range(row-1,-1,-1)])
        return abs(sum_diag1 - sum_diag2)

    # Plus Minus
    # Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
    # Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
    # Example: 
    # arr = [1,1,0,-1,-1] | output = [0.400000,0.400000,0.200000]
    @staticmethod
    def plusMinus(self,alist):
        val = Counter(self.alist).values()
        res = [i/sum(val) for i in val]
        return res
    # print(f'Final value is {plusMinus([1,1,0,-1,-1])}')

    # Mini-Max Sum
    # Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
    # Example: 
    # arr = [1,3,5,7,9] | output = [16,24] 
    # Explaination: 
    # The minimum sum is 1 + 3 + 5 + 7 = 16 and 3 + 5 + 7 + 9 = 24

    # Method 1
    @staticmethod
    def miniMax1(self,ar):
        out = [sum(j) for i in range(1,len(self.ar)) for j in combinations(self.ar,i) if len(j) == len(self.ar)-1]
        return out
    # print(f'Output from method 1 is: {miniMax1([1,3,5,9])}')

    # Method 2
    @staticmethod
    def miniMax2(self,ar):
        resultList = [[self.ar[i],self.ar[i+1],self.ar[j],self.ar[j+1]] for i in range(len(self.ar)-1) for j in range(i,len(self.ar)-1)]
        output = [i for i in resultList if len(list(set(i))) != 2 and len(list(set(i))) != 3]
        return [max(output),min(output)]
    # print(f'Output from method 2 is: {miniMax2([1,3,5,9])}')

    # Words Score
    # Consider that vowels in the alphabet are a, e, i, o, u and y.
    # Function score_words takes a list of lowercase words as an argument and returns a score as follows:
    # The score of a single word is 2 if the word contains an even number of vowels. Otherwise, the score of this word is 1. The score for the whole list of words is the sum of scores of all words in the list.
    # Debug the given function score_words such that it returns a correct score.
    # Your function will be tested on several cases by the locked template code.

    # Sample Input: 
    # hacker book

    # Sample Output: 
    # 4
    # Method 1
    @staticmethod
    def wordsScore1(self,words):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        score = 0
        wordsList = self.words.split(' ')
        for word in wordsList:
            hash_map = Counter(word)
        out = [hash_map[i] for i in vowels if i in hash_map.keys()]
        if sum(out) % 2 == 0:  score = sum(out) + 2
        else:score += 1 
        return score
    # print(f'Method 1 output is: {wordsScore1("hacker book")}')

    # Method 2
    @staticmethod
    def wordsScore2(self,words):
        score = 0
        for word in self.words:
            score+= len(re.findall("[aeiouy]",word))%2 or 2          
        return score
    # print(f'Method 2 output is: {wordsScore2(["hacker","book"])}')

    # Yet to see this
    # Validating Credit Card Numbers
    # You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
    # A valid credit card from ABCD Bank has the following characteristics: 
    # ► It must start with a 4 or 5 or 6
    # ► It must contain exactly 16 digits. 
    # ► It must only consist of digits (0-9). 
    # ► It may have digits in groups of 4, separated by one hyphen "-".
    # ► It must NOT use any other separator like ' ' , '_', etc. 
    # ► It must NOT have 4 or more consecutive repeated digits.

    # Examples:
    # Valid Credit Card Numbers
    # 4253625879615786 
    # 4424424424442444  
    # 5122-2368-7954-3214

    # Invalid Credit Card Numbers
    # 42536258796157867       #17 digits in card number → Invalid 
    # 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
    # 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
    # 44244x4424442444        #Contains non digit characters → Invalid
    # 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
    @staticmethod
    def validCard(self,card):
        return
    # print(validCard("42536258796157867"))

    # Grading Students
    # HackerLand University has the following grading policy:
    # Every student receives a grade in the inclusive range from 0 to 100.
    # Any grade less than 40 is a failing grade.
    # Sam is a professor at the university and likes to round each student's grade according to these rules:
    # If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
    # If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
    @staticmethod
    def studentGrade(self,alist):
        return [i+(5-(i%5)) if(i>37 and i%5 != 0 and i%5>=3) else i for i in self.alist]
    # print(f'Method 1 output is: {studentGrade([73,67,38,33])}')

    # Encryption
    # An English text needs to be encrypted using the following encryption scheme. 
    # First, the spaces are removed from the text. Let L be the length of this text. 
    # Then, characters are written into a grid, whose rows and columns have the following constraints:
    # [Check the ipynb for following constraints]

    # Method 1 using numpy package
    @staticmethod
    def encrypt(self,string):
        sqaureRootL = str((len(self.string))**0.5) 
        row,col = list(map(int,sqaureRootL[:3].split('.')))[0],list(map(int,sqaureRootL[:3].split('.')))[1]
        stringList = [i for i in string]
        wordMatrix = np.matrix(stringList).reshape((row,col))
        return wordMatrix
    # print(f'Method 1 output is: \n {encrypt("haveaniceday")}')

    # Bigger is Greater
    # Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
    # Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
    #  - It must be greater than the original word
    #  - It must be the smallest word that meets the first condition
    # Example 
    # Input: w = abcd | otuput: abdc



if __name__ == '__main__':
    # Calling our class
    hr = hacerRank()

    # Accessing our sub classes from our base class

    ###### Sales by match ######
    # print(f'Total count of pair is: {hr.salesMatch([1,2,1,2,1,3,2])}')

    ###### Left Rotation ######
    print(f'\nLeft rotation array is {hr.leftRotation([1,2,3,4,5],3)}')

    ###### Minimum Swaps 2 ######
    # Yet to see this logic
    print(f'\nMinimum swaps required is: {hr.minSwaps([7,1,3,2,4,5,6])}')

    ###### Ransom Note ######
    print('\n Method 1 Ransom Note')
    print(f'Can we replicate the Magazine: {hr.ransome1("two times three is not four","two times two is four")}')
    print('\n')
    print('Method 2 Ransom Note')
    print(f'\nCan we replicate the Magazine: {hr.ransome2("two times three is not four","two times two is four")}')
    ###### Sales by match ######


    ###### Sales by match ######