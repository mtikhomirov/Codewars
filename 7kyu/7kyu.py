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
