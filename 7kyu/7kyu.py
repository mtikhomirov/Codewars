ritual=lambda n:n<2
    """ [Code Golf] An Interesting Ritual.
        https://www.codewars.com/kata/63d6dba199b0cc0ff46b5d8a
        
        Let's say a matrix m exists such that the value of each square is the product of the indices of the rows
        and columns, considering that the indices start at 1 and the first square is in the upper left corner.
        Examples of the matrix:
        n = 1 -> [1] n = 2 -> [1, 2] n = 3 -> [1, 2, 3]
                              [2, 4]          [2, 4, 6]
                                              [3, 6, 9]
        Given n, the size of the square matrix, your task is to create a function,
        ritual, that returns the determinant of the matrix.
        Do not return the matrix; return its determinant
        Input
        You will be given a positive integer n, meaning, don`t worry about input validation.
        Maximum Length
        The length of your code must not exceed 19 characters.
        Random Tests
        There will be a total of 100 random tests.
        They will be separated into 4 categories: small, medium, big, and huge tests, with 25 tests each;
        their range is:
        Small: 1 <= n <= 9
        Medium: 10 <= n <= 1_000
        Big: 100_000 <= n <= 1_000_000
        Huge: 2 ** 32 <= n <= 2 ** 64
    """
    
    
def count_pixels(k):
    """ Asperand pixel counting.
        https://www.codewars.com/kata/63d54b5d05992e0046752389
        
        You can paint an asperand by pixels in three steps:

        First you paint the inner square, with a side of k.
        Then you need to paint one pixel, that's laying diagonally relative to the inner square that you just painted 
        (the bottom-right corner of the inner square is touching the top-left corner of the pixel). 
        Let's call it the "bridge".
        Finally, you will need to paint the outer shape, connected diagonally to the "bridge" 
        ( see the picture for more information ).
        
        Your task is to find the number of pixels that need to be painted, for different k:

        k = 1 => 11
        k = 2 => 18
        k = 3 => 26
        k = 4 => 34

        # Limitations are 1 ≤ k ≤ 1e9
    """
    square = 1
    if k > 1:
        square = (k - 1) * 4
    return 4 * k + 6 + square
    
    
def set_reducer(inp):
    """ Set Reducer.
        https://www.codewars.com/kata/63cbe409959401003e09978b
       
        Description
        Write a function that takes in an array of integers from 0-9, and returns a new array:

        Numbers with no identical numbers preceding or following it returns a 1: 2, 4, 9  => 1, 1, 1
        Sequential groups of identical numbers return their count: 6, 6, 6, 6 => 4
        Example

        [0, 4, 6, 8, 8, 8, 5, 5, 7] => [1, 1, 1, 3, 2, 1]

        Your function should then repeat the process on the resulting array, 
        and on the resulting array of that, until it returns a single integer:

        [0, 4, 6, 8, 8, 8, 5, 5, 7] =>  [1, 1, 1, 3, 2, 1] => [3, 1, 1, 1] => [1, 3] => [1, 1] => [2]

        When your function has reduced the array to a single integer following these rules, 
        it should return that integer.

        [2] => 2

        Rules and assertions
        All test arrays will be 2+ in length
        All integers in the test arrays will be positive numbers from 0 - 9
        You should return an integer, not an array with 1 element
    """  
    
#from itertools import groupby
#
#def set_reducer(inp):
#    while len(inp) > 1:
#        inp = [len(list(b)) for a, b in groupby(inp)]
#    return inp[0]    
    
    
    if len(inp) == 1:
        return inp[0]
    count = 1
    res = []
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    return set_reducer(res)    
    
    
def create_box(m, n):
    """ The 'spiraling' box.
        https://www.codewars.com/kata/63b84f54693cb10065687ae5
        
        Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in the following way:

        (1) All the elements in the first and last row and column are 1.
        (2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
        (3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.

        And so on ...

        Examples
        Create_box(5, 8) should return
        [[1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 2, 1], 
        [1, 2, 3, 2, 1],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]]
        
        create_box(10, 9) should return
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
        [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 
        [1, 2, 3, 4, 4, 4, 4, 3, 2, 1], 
        [1, 2, 3, 3, 3, 3, 3, 3, 2, 1], 
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    """
    return [[min([i + 1, j + 1, m - i, n - j]) for i in range(m)] for j in range(n)]
    
    
from itertools import groupby

def yahtzee_upper(dice):
    """ Yahtzee upper section scoring.
        https://www.codewars.com/kata/63b4758f27f8e5000fc1e427
        
        Introduction
        The game of Yahtzee is played by rolling five 6-sided dice, and scoring the results in a number of ways. 
        For the purpose of this kata, the upper section of Yahtzee gives you six possible ways to score a roll. 
        1 times the number of 1s in the roll, 2 times the number of 2s, 3 times the number of 3s, 
        and so on up to 6 times the number of 6s. For instance, consider the roll [2, 3, 5, 5, 6]. 
        If you scored this as 1s, the score would be 0, since there are no 1s in the roll. If you scored it as 2s, 
        the score would be 2, since there's one 2 in the roll. 
        Scoring the roll in each of the six ways gives you the six possible scores: 0 2 3 0 10 6. 
        The maximum here is 10 (2x5), so your result should be 10.

        You are given a Yahtzee dice roll, represented as a list with k integers from 1 to 10000. 
        Your task is to find the maximum possible score for this roll in the upper section of the Yahtzee score card. 
        Here's what that means.

        Examples
        yahtzee_upper([2, 3, 5, 5, 6]) => 10 #5*2=10 - there is two numbers 5, and that gives as 10
        yahtzee_upper([1, 1, 1, 1, 3]) => 4  #1*4=4, while 3*1=3 - there is four numbers 1, and that gives as 4, while one number 3 gives as 3
        yahtzee_upper([1, 1, 1, 3, 3]) => 6
        yahtzee_upper([15, 9, 9, 8, 9]) => 27
        yahtzee_upper([1654, 1654, 5099, 3086, 1654, 5099, 2274,
            1654, 1654, 1654, 1654, 1654, 3086, 4868, 1654, 4868, 1654,
            3086, 4868, 3086]) => 16540 #1654*10=16540 - large example - there is ten numbers 1654, and that gives as 16540
    """
    
    dice.sort()
    roll = [number * len(list(count)) for number, count in groupby(dice)]
#    return max([i * dice.count(i) for i in set(dice)])
    return max(roll)
    
    
def what_branch(time):
    """ Using Earthly Branches for Time.
        https://www.codewars.com/kata/63b3cebaeb152e12268bdc02
        
        In the traditional system using Earthly Branches, a day is started by 23:00.
        Earthly Branches contain 12 characters:

        子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥
        Not only for the years, it also can be used for the time.
        The day starts with 子, 2 hours later become 丑, then 寅, and so on.

        子: 23:00 - 0:59
        丑: 1:00 - 2:59
        寅: 3:00 - 4:59
        and so on.

        Task:
        Given a time as a string(hh:mm), return the Earthly Branch for that time.
        The string would use 24-hours. It may have leading zero for minute, but no leading zero for hour.

        Examples (input -> output)
        23:00 -> 子
        0:00 -> 子
        1:00 -> 丑
        2:59 -> 丑
        3:00 -> 寅
    """
    earthly_branches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    hours = int(time.split(':')[0])
    return earthly_branches[((hours + 1) // 2) % 12]
    
    
def alphabet(ns):
    """ The alphabet product.
        https://www.codewars.com/kata/63b06ea0c9e1ce000f1e2407
        
        I have four positive integers, A, B, C and D, where A < B < C < D. 
        The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. 
        Your task is to return the value of D.
    """
    ns.sort()
    ns.remove(int(ns[0]*ns[1]))
    return int(ns[6]/ns[2])


from math import isqrt

def max_df(a_n: int) -> int:
    """ Maximum different differences.
        https://www.codewars.com/kata/63adf4596ef0071b42544b9a
        
        Input
        a_n: (int) The maximum/last element of 

        Output
        (int) The maximum possible characteristic based on a_n
​    """
    n = (isqrt(8 * a_n) - 1) // 2
    return n    
