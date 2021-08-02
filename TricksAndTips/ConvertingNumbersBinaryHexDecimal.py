###############################################################################
#                            CONVERTING NUMBERS                               #
#                             Decimal, Hex, Bin                               #
###############################################################################

decimal_nums = [56, 10, 0]
hex_nums = [0x38, 0xa, 0x0]
bin_nums = [0b111000, 0b1010, 0b0]

# Decimal to Hex:
dec_to_hex = list(map(lambda x: hex(x), decimal_nums))  # will create new list with hex values in string
print(dec_to_hex)
dec_to_hex = list(map(lambda x: hex(x)[2:], decimal_nums))  # without "0x" prefix
print(dec_to_hex)

# Decimal to Bin:
dec_to_bin = list(map(lambda x: bin(x), decimal_nums))  # will create new list with bin values in string
print(dec_to_bin)
dec_to_bin = list(map(lambda x: bin(x)[2:], decimal_nums))  # without "0b" prefix
print(dec_to_bin)

# Hex to Decimal:
hex_to_dec = list(map(lambda x: int(x), hex_nums))
print(hex_to_dec)

# Bin to Decimal:
bin_to_dec = list(map(lambda x: int(x), bin_nums))
print(bin_to_dec)

# String Hex to Decimal:
hex_string_to_dec = list(map(lambda x: int(x, 16), dec_to_hex))
print(hex_string_to_dec)

# String Bin to Decimal:
bin_string_to_dec = list(map(lambda x: int(x, 2), dec_to_bin))
print(bin_string_to_dec)
