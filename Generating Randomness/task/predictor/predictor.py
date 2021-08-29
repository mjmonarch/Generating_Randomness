# -------------------------------------------------------------------
# # ------------------------Stage 1------------------------------------
#
# MINIMAL_LENGTH = 100
# APPROPRIATE_INPUT = ['0', '1']
#
# input_string = input("Print a random string containing 0 or 1:")
# general_string = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
# print(general_string)
# while len(general_string) < 100:
#     print("Current data length is ", len(general_string), ", ",
#           100 - len(general_string), " symbols left", sep='')
#     input_string = input("Print a random string containing 0 or 1:")
#     input_string_filtered = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
#     general_string = general_string + input_string_filtered
# print("Final data string:")
# print(general_string)

# ------------------------Stage 2------------------------------------

MINIMAL_LENGTH = 10
APPROPRIATE_INPUT = ['0', '1']
TRIADS_LIST = ['000', '001', '010', '011', '100', '101', '110', '111']

input_string = input("Print a random string containing 0 or 1:")
general_string = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
print(general_string)
while len(general_string) < MINIMAL_LENGTH:
    print("Current data length is ", len(general_string), ", ",
          100 - len(general_string), " symbols left", sep='')
    input_string = input("Print a random string containing 0 or 1:")
    input_string_filtered = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
    general_string = general_string + input_string_filtered

triads_dictionary = dict.fromkeys(TRIADS_LIST, [0, 0])
for i in range(len(general_string) - 3):
    for triad in TRIADS_LIST:
        if triad == general_string[i:i + 3]:
            digit = general_string[i+3]
            triads_dictionary[triad][int(digit)] += 1
            break
print("Final data string:")
print(general_string)
print(triads_dictionary)

