ritual=lambda n:n<2
    """ [Code Golf] An Interesting Ritual.
        https://www.codewars.com/kata/63d6dba199b0cc0ff46b5d8a/train/python

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
