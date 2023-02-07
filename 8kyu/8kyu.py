import math
import sys


def distance_between_points(a, b):
    """ Geometry Basics: Distance between points in 2D
        https://www.codewars.com/kata/58dced7b702b805b200000be

        This series of katas will introduce you to basics of doing geometry with computers.
        Point objects have attributes x and y.
        Write a function calculating distance between Point a and Point b.
        Tests compare expected result and actual answer with tolerance of 1e-6.
        :param a: Point a
        :param b: Point a
        :return: distance between points a and b
    """
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def even_or_odd(number):
    """ Even or Odd
        https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

        Create a function that takes an integer as an argument and returns "Even" for even numbers
        or "Odd" for odd numbers.
        :param number: integer number
        :return: "Even" for even numbers or "Odd" for odd numbers
        """
    return 'Even' if number % 2 == 0 else 'Odd'


def mystery():
    """ Return to Sanity
        https://www.codewars.com/kata/514a7ac1a33775cbb500001e

        This function should return an object, but it's not doing what's intended. What's wrong?
    """
    results = {'sanity': 'Hello'}
    return results


def quarter_of(month):
    """ Quarter of the year
        https://www.codewars.com/kata/5ce9c1000bab0b001134f5af

        Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
        For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
        and month 11 (November), is part of the fourth quarter.

        Constraint:
        1 <= month <= 12

        :param month: number of month
        :return: Quarter of the year
    """
    return (month - 1) // 3 + 1


def total_bytes(obj):
    """ Byte me!
        https://www.codewars.com/kata/636f26f52aae8fcf3fa35819

        In this kata, you need to return the number of bytes (aka. memory size) a given object takes up.
        Different variable types will be given, but they will all be valid.
        Also, random generation for strings takes out of Unicode, not the regular 255 ascii letters.
        p.s: Don't be afraid to use the internet. It "byte" come in handy :)
        :param obj:
        :return: number of bytes
    """
    return sys.getsizeof(obj)


def flip(d, a):
    """ Gravity Flip.
        https://www.codewars.com/kata/5f70c883e10f9e0001c89673

        If you've completed this kata already and want a bigger challenge, here's the 3D version

        Bob is bored during his physics lessons, so he's built himself a toy box to help pass the time.
        The box is special because it has the ability to change gravity.

        There are some columns of toy cubes in the box arranged in a line.
        The i-th column contains a_i cubes. At first, the gravity in the box is pulling the cubes downwards.
        When Bob switches the gravity, it begins to pull all the cubes to a certain side of the box,
        d, which can be either 'L' or 'R' (left or right).
        Below is an example of what a box of cubes might look like before and after switching gravity.

    :param d: direction 'L' or 'R'
    :param a: list
    """
    a.sort(reverse=(d == 'L'))
    return a


def quadratic(x1, x2):
    """ Quadratic Coefficients Solver.
        https://www.codewars.com/kata/5d59576768ba810001f1f8d6

        In this Kata you are expected to find the coefficients of quadratic equation of the given two roots (x1 and x2).
        Equation will be the form of ax^2 + bx + c = 0
        Return type is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in the order
        (a, b, c).
        Since there are infinitely many solutions to this problem, we fix a = 1.
        Remember, the roots can be written like (x-x1) * (x-x2) = 0

        Example
        quadratic(1,2) = (1, -3, 2)
        This means (x-1) * (x-2) = 0; when we do the multiplication this becomes x^2 - 3x + 2 = 0

        Example 2
        quadratic(0,1) = (1, -1, 0)
        This means (x-0) * (x-1) = 0; when we do the multiplication this becomes x^2 - x + 0 = 0

        Note
        Inputs will be integers.
        When x1 == x2, this means the root has the multiplicity of two
    """
    return 1, -(x1 + x2), x2 * x1


def same_case(a, b):
    """ Check same case.
        https://www.codewars.com/kata/5dd462a573ee6d0014ce715b

        Write a function that will check if two given characters are the same case.

        If either of the characters is not a letter, return -1
        If both characters are the same case, return 1
        If both characters are letters, but not the same case, return 0
        Examples
        'a' and 'g' returns 1
        'A' and 'C' returns 1
        'b' and 'G' returns 0
        'B' and 'g' returns 0
        '0' and '?' returns -1
    """
    if a.isalpha() and b.isalpha():
        return int(a.isupper() == b.isupper())
    else:
        return -1


def warn_the_sheep(queue):
    """ A wolf in sheep's clothing.
        https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15

        Wolves have been reintroduced to Great Britain.
        You are a sheep farmer, and are now plagued by wolves which pretend to be sheep.
        Fortunately, you are good at spotting them.

        Warn the sheep in front of the wolf that it is about to be eaten.
        Remember that you are standing at the front of the queue which is at the end of the array:

        [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
           7      6      5      4      3            2      1
        If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep".
        Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!"
        where N is the sheep's position in the queue.

        Note: there will always be exactly one wolf in the array.

        Examples
        Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
        Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

        Input: ["sheep", "sheep", "wolf"]
        Output: "Pls go away and stop eating my sheep"
    """
    if queue[len(queue) - 1] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    for i in range(len(queue) - 1, -1, -1):
        if queue[i] == 'wolf':
            return f'Oi! Sheep number {len(queue) - i - 1}! You are about to be eaten by a wolf!'


def approx_equals(a, b):
    """ Floating point comparison.
        https://www.codewars.com/kata/5f9f43328a6bff002fa29eb8

        You have:

        a float value that comes from a computation and may have accumulated errors up to ±0.001
        a reference value
        a function approx_equals that compare the two values taking into account loss of precision;
        the function should return True if and only if the two values are close to each other,
        the maximum allowed difference is 0.001
        The function is bugged and sometimes returns wrong results.

        Your task is to correct the bug.

        Note
        This kata uses fixed tolerance for simplicity reasons, but usually relative tolerance is better.
        Fixed tolerance is useful for comparisons near zero or when the magnitude of the values is known.
    """
    return abs(a - b) < 0.001


def elevator(left, right, call):
    """ Closest elevator.
        https://www.codewars.com/kata/5c374b346a5d0f77af500a5a

        Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2),
        write a function elevator accepting 3 arguments (in order):

        left - The current floor of the left elevator
        right - The current floor of the right elevator
        call - The floor that called an elevator
        It should return the name of the elevator closest to the called floor ("left"/"right").

        In the case where both elevators are equally distant from the called floor, choose the elevator to the right.

        You can assume that the inputs will always be valid integers between 0-2.

        Examples:

        elevator(0, 1, 0) # => "left"
        elevator(0, 1, 1) # => "right"
        elevator(0, 1, 2) # => "right"
        elevator(0, 0, 0) # => "right"
        elevator(0, 2, 1) # => "right"
    """
    return 'left' if abs(call - left) < abs(call - right) else 'right'
