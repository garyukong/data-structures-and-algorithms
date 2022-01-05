def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    def sqrt_recursive(number, lower, upper):
        # Case 0: number is less than or equal to 1
        if number <= 1:
            return number

        # Find midpoint and squared value of midpoint
        mid = (lower + upper) // 2
        mid_squared = mid * mid

        # Case 1: midpoint squared equals number -> return midpoint
        if mid_squared == number:
            return mid

        # Case 2: midpoint is less than 1 -> take lower value as floored square root
        elif mid - lower < 1:
            return lower

        # Case 3: midpoint squared is greater than number -> recur on the left side
        elif mid_squared > number:
            return sqrt_recursive(number, lower, mid)

        # Case 4: midpoint squared is less than number -> recur on the right side
        elif mid_squared < number:
            return sqrt_recursive(number, mid, upper)

    return sqrt_recursive(number, 0, number)

# Test cases
if __name__ == "__main__":

    # Cases which have an integer square root
    print ("Pass" if (0 == sqrt(0)) else "Fail")
    print ("Pass" if (1 == sqrt(1)) else "Fail")
    print ("Pass" if (3 == sqrt(9)) else "Fail")
    print ("Pass" if (4 == sqrt(16)) else "Fail")

    # Cases which do not have an integer square root
    print ("Pass" if (5 == sqrt(27)) else "Fail")
    print ("Pass" if (6 == sqrt(37)) else "Fail")
    print ("Pass" if (7 == sqrt(52)) else "Fail")

    # Cases with very large numbers
    print ("Pass" if (1000 == sqrt(1000000)) else "Fail")
    print ("Pass" if (3162 == sqrt(9999999)) else "Fail")

    # Cases with empty number and string - both should return an error
    sqrt()
    sqrt('')