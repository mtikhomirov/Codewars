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
        All integers in the test arrays will be positive numbers from 0 to 9
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


def can_escape(walls):
    """ Hurry up, the walls are closing in!.
        https://www.codewars.com/kata/63ab271e96a48e000e577442

        Task
        "Given a list walls closing in at you, can you make it past those walls without being hit?"
        Input
        walls: an array of 2-ples, each 2-ple storing non-negative numbers representing the distance
        of the walls closing in at you from each side respectively to the center of the room.
        Output
        return a boolean indicating whether it is possible to run past the walls without being hit.
        Specification
        You are at the left side in the center of the room
        You want to reach the right side in the center of the room
        You can only move in a straight line across the room
        Walls are closing in at you from both sides of the room
        Walls stop once they hit the center of the room
        You and the walls move at the same speed
        You get hit by a wall if you are on the same tile as a wall
        If a wall reaches a tile ahead of you, you cannot make it past that wall anymore
        Input Constraints
        50 tests with 1 <= number of walls <= 4
        50 tests with 5 <= number of walls <= 15
        50 tests with 16 <= number of walls <= 50
        50 tests with 51 <= number of walls <= 100
        0 <= starting distance of walls to center of room <= 120
        Examples
        In the examples below, you start on tile A and want to reach tile B.
        You have to walk across the center of the room -.
        Walls W are closing in on you from the north and south.
    """

    for i in range(len(walls)):
        if min(walls[i]) <= i+1:
            return False
    return  True


def to_imparfait(verb_phrase):
    """ French Imparfait Conjugation.
        https://www.codewars.com/kata/6394c1995e54bd00307cf768
        
        Task
        Given a simple French phrase, consisting of a subject and a verb in its infinitive form, 
        you need to turn it into L'imparfait, using the table below. 
        To conjugate a sentence in l'imparfait, drop the last two letters of the verb and 
        replace it with the correct ending based on the subject.

        Here are the endings to replace the verb with:

        Subject	Verb Ending
        Je (I)	-ais
        Tu (You)	-ais
        Il/Elle/On (He/She/It or We)	-ait
        Nous (We)	-ions
        Vous (You or Y'all)	-iez
        Ils/Elles (They)	-aient
        Let's say you want to translate I was walking to French:

        Take the subject + infinitive: Je marcher
        Remove the last two letters: Je march
        Apply the correct ending: Je marchais
        You get Je marchais, which can be checked with our handy dandy google translate.
    """
    france_dict = {
        'Je': 'ais',
        'Tu': 'ais',
        'Il': 'ait',
        'Elle': 'ait',
        'On': 'ait',
        'Nous': 'ions',
        'Vous': 'iez',
        'Ils': 'aient',
        'Elles': 'aient'
    }
    return verb_phrase[:-2]+france_dict[verb_phrase.split()[0]]


def perpendicular(n):
    """ Perpendicular lines.
        https://www.codewars.com/kata/6391fe3f322221003db3bad6
        
        You are given an input (n) which represents the amount of lines you are given, 
        your job is to figure out what is the maximum amount of perpendicular bisectors 
        you can make using these lines.

        Note: A perpendicular bisector is one that forms a 90 degree angle

        n will always be greater than or equal to 0
    """
    return (n // 2) * (n - n // 2)


import socket
def socket_client():
    """ Simple Socket Client.
        https://www.codewars.com/kata/639107e0df52b9cb82720575
        
        There is a socket listening on port 1111 of local host.

        The socket either belongs to a server that sends back anything you send to it, 
        or to a server that reverses anything you send to it.

        Create a function that does the following:

        Connects to the socket on port 1111.
        Sends one packet to the server.
        Receives one packet from the server.
        Returns True if the server is the regular type (i.e., it sends back the same packet that was sent to it), 
        or False if the server is the reversing type (i.e., it reverses the packet that was sent to it).
        Make sure to close the socket after you are done using it. 
        If you time out while trying to connect, it is likely that you did not connect, send, receive, 
        and close the socket in the correct order.
    """
    HOST = 'localhost'
    PORT = 1111
    SEND_TEXT = b'sample tests'
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.send(SEND_TEXT)
        response = sock.recv(1024)
        sock.close()
    return response == SEND_TEXT


def cube(n):
    """ Rubik's Cube Art.
        https://www.codewars.com/kata/6387ea2cf418c41d277f3ffa
        
        To complete this kata you will have to finish a function that returns a string 
        of characters which when printed resemble a Rubik's cube. 
        The function is named cube, and it has one integer parameter (formal argument) n, 
        for the dimensions of the cube.
    """
    string = ''
    for i in range(n):
        string +=' ' * (n - 1 - i) + '/\\' * (i + 1) + '_\\' * n + '\n'
    for i in range(n):
        string +=" " * i + '\\/' * (n - i) + '_/' * n + '\n'
    return string.rstrip('\n')


def get_sum(n):
    """ Summation Triangle #1.
        https://www.codewars.com/kata/6357825a00fba284e0189798
        
        The task
        You have to make a program capable of returning the sum of all the elements 
        of a triangle with side of size n+1.

        The problem
        . Brute-forcing will not work!

        The definition
        A triangle element aij where is the column and j is the row can be defined as 
        aij = 2j + i + 1 where 0≤ i ≤ j ≤ n
    """
    return (n + 1) * (n + 2) * (4 * n + 3) // 6


def contact(hallway):
    """ Walking in the hallway.
        https://www.codewars.com/kata/6368426ec94f16a1e7e137fc
        
        You are a security guard at a large company, your job is to look over the cameras. 
        Finding yourself bored you decide to make a game from the people walking in a hallway on one of the cameras. 
        As many people walk past the hallway you decide to figure out the minimum steps it will take before 2 people 
        cross or come into contact with each other (assuming every person takes a step at the same time).

        People are represented as arrows, < for a person moving left and > for a person moving right and - for an empty space

        A step represents a person moving forward one -, each person moves 1 step at the same time

        in this example the first people to come in contact with each other do it after 1 step
        ---><----
        in this example the first people to come in contact with each other do it after 1 step
        --->-<------->----<-
        in the case that no people come in contact return -1
        ----<----->----
    """
#    left = [i for i in range(len(hallway)) if hallway[i] == '<']
#    right = [i for i in range(len(hallway)) if hallway[i] == '>']
#    dist = -1
#    for i in range(len(left)):
#        for j in range(len(right)):
#            d = left[i] - right[j]
#            if d > 0 and (d < dist or dist == -1):
#                dist = d
#    if dist < 0:
#        return -1
#    cont = (dist + 1) // 2
#    return cont

#def contact(hallway):
#    left = [i for i in range(len(hallway)) if hallway[i] == '<']
#    right = [i for i in range(len(hallway)) if hallway[i] == '>']
#    d = [(left[i] - right[j] + 1) // 2 for i in range(len(left)) for j in range(len(right)) if left[i] - right[j] > 0]
#   return -1 if not d else min(d)
#
#def contact(hallway):
#    d = 0
#    flag = False
#    for index, sym in enumerate(hallway):
#        if sym == '>':
#            left = index
#            flag = True
#        elif sym =='<' and flag:
#            right = index
#            flag = False
#            if not d or right - left < d:
#                d = right - left
#    return -1 if not d else (d + 1) // 2

#def contact(hallway):
#    d = 0
#    right = 0
#    while right > -1:
#        right = hallway.find('<')
#        left = hallway.rfind('>', 0, right)
#        if (not d or right - left < d) and left > -1 and right > -1:
#            d = right - left
#        hallway = hallway[right+1:]
#    return -1 if not d else (d + 1) // 2


import re

#def contact(hallway):
    pairs = re.findall('>-*<', hallway)
    return min(map(len, pairs)) // 2 if pairs else -1


def movie_times(open, close, length):
    """ Movie Showtimes.
        https://www.codewars.com/kata/6376bbc66f2ae900343b7010
        
        You just started working at a local cinema, 
        and your first task is to write a function that returns the showtimes of a specific movie, 
        given its length. In order to make your job easier, 
        you will work with 24-hour format throughout this kata.

        Your function receives three parameters, all of them being integers:

        open - Hour at which the cinema opens.
        close - Hour at which the cinema closes.
        length - Length of the movie, in minutes.
        It must return an array of times, with each time being in the format (hour, minute). 
        For example, (19, 30) means 19:30, and (2, 0) means 02:00. 
        The last session in the array cannot end after the cinema closes. 
        Also, the times in the array must be sorted from earliest to latest.

        There's also a 15-minute window between a session's end and the beginning of the following one, 
        in order to give enough time for users to take a seat.

        For example, for a cinema opening at 13:00 and closing at 23:00 showing a 60-minute movie, 
        your function must return the following array:

        >>> movie_times(13, 23, 60)
        [(13, 0), (14, 15), (15, 30), (16, 45), (18, 0), (19, 15), (20, 30), (21, 45)]
        Note that the cinema might close at times such as 02:00 or 03:00, meaning examples like this must also work:

        >>> movie_times(16, 3, 75)
        [(16, 0), (17, 30), (19, 0), (20, 30), (22, 0), (23, 30), (1, 0)]
        IMPORTANT: For languages other than Python, just return an array of arrays. 
        See sample test cases for more info on how to return the list of times.

        NOTE: This kata isn't meant to be too challenging, so opening times for all tests will be 12:00 or later, 
        and closing times will always be 6:00 or earlier.

        NOTE 2: Midnight will be represented as (0, 0) or 0:00 in this kata, instead of 24:00.
    """
    gap = 15
    open, close = open * 60, (close + 24 * (close < 12)) * 60
    return list(map(convert_to_hours, range(open, close - length + 1, length + gap)))

def convert_to_hours(time):
    hours, minuts = divmod(time, 60)
    return hours % 24, minuts
