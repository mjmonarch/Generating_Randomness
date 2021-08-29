# -------------------------------------------------------------------
# ------------------------Stage 1------------------------------------

MINIMAL_LENGTH = 100
APPROPRIATE_INPUT = ['0', '1']
general_string = ""

input_string = input("Print a random string containing 0 or 1:")
general_string = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
print(general_string)
while len(general_string) < 100:
    print("Current data length is ", len(general_string), ", ",
          100 - len(general_string), " symbols left", sep='')
    input_string = input("Print a random string containing 0 or 1:")
    input_string_filtered = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
    general_string = general_string + input_string_filtered
print("Final data string:")
print(general_string)
