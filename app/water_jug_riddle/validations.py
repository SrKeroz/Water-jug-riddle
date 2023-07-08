def validations(x, y, z):
    """
    Validates all parameters to ensure that certain conditions are met.

    Args:
        x (int): First integer parameter to validate.
        y (int): Second integer parameter to validate.
        z (int): Third integer parameter to validate.

    Returns:
        if all parameters are valid return a tuple with two values bool: True and string: confirmation message
        if any parameter is invalid rerunt a tuple with two values bool: False and string: error message
    """

    if isinstance(x, str) or isinstance(y, str) or isinstance(z, str):

        # If any of the parameters is a string (letter, sign), it returns False
        return False, "Values can't be signs or letters"  
        
    if x <= 0 or y <= 0 or z <= 0:
        # If any of the parameters is less than or equal to zero, it returns False
        return False, "Values must be greater than 0"
    
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        # If any of the parameters is not an integer, return False
        return False, "Values can't be decimals or fractions"
    
    if z > x and z > y:
        # If Z is greater than X or greater than Y, return False
        return False, "Water to measure can't be greater than x_gallon and y_gallon"
    
    return True, "OK"  # If it passes all validations, it returns True
