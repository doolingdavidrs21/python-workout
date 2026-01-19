def hex_output(hex_num: int):
    """
    Docstring for hex_output

    :param hex_num: takes in a hex integer (powers of 16 instead of 100)
    and returns the corresponding decimal integer, prints it to the screen
    :return: integer representation of the hexadecimal string
    """
    hex_string = str(hex_num)
    reversed_hex_string = hex_string[::-1]
    decimal_value = 0
    for i, digit in enumerate(reversed_hex_string):
        if digit.isdigit():
            decimal_value += int(digit, base=16) * (16 ** i)

    print(f"The decimal value of hexadecimal {hex_string} is {decimal_value}")
    return decimal_value




