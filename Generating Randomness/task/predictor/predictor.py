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

# MINIMAL_LENGTH = 100
# APPROPRIATE_INPUT = ['0', '1']
# TRIADS_LIST = ['000', '001', '010', '011', '100', '101', '110', '111']
#
# input_string = input("Print a random string containing 0 or 1:")
# general_string = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
# print(general_string)
# while len(general_string) < MINIMAL_LENGTH:
#     print("Current data length is ", len(general_string), ", ",
#           100 - len(general_string), " symbols left", sep='')
#     input_string = input("Print a random string containing 0 or 1:")
#     input_string_filtered = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
#     general_string = general_string + input_string_filtered
#
# # triads_dictionary = dict.fromkeys(TRIADS_LIST, [0, 0])
# triads_dictionary = dict.fromkeys(TRIADS_LIST, None)
# for triad in triads_dictionary.keys():
#     triads_dictionary[triad] = [0, 0]
#
# for i in range(len(general_string) - 3):
#     for triad in triads_dictionary.keys():
#         if triad == general_string[i:i + 3]:
#             digit = int(general_string[i+3])
#             if digit == 0:
#                 (triads_dictionary[triad])[0] += 1
#             elif digit == 1:
#                 (triads_dictionary[triad])[1] += 1
#             break
#
# print("Final data string:")
# print(general_string)
# print()
# for triad in triads_dictionary.keys():
#     print(triad, ": ", triads_dictionary[triad][0], ",", triads_dictionary[triad][1], sep='')

# ------------------------Stage 3------------------------------------
# import random
#
# MINIMAL_LENGTH = 100
# APPROPRIATE_INPUT = ['0', '1']
# TRIADS_LIST = ['000', '001', '010', '011', '100', '101', '110', '111']
#
# input_string = input("Print a random string containing 0 or 1:")
# general_string = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
# print(general_string)
# while len(general_string) < MINIMAL_LENGTH:
#     print("Current data length is ", len(general_string), ", ",
#           100 - len(general_string), " symbols left", sep='')
#     input_string = input("Print a random string containing 0 or 1:")
#     input_string_filtered = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
#     general_string = general_string + input_string_filtered
#
# # triads_dictionary = dict.fromkeys(TRIADS_LIST, [0, 0])
# triads_dictionary = dict.fromkeys(TRIADS_LIST, None)
# for triad in triads_dictionary.keys():
#     triads_dictionary[triad] = [0, 0]
#
# for i in range(len(general_string) - 3):
#     for triad in triads_dictionary.keys():
#         if triad == general_string[i:i + 3]:
#             digit = int(general_string[i+3])
#             if digit == 0:
#                 (triads_dictionary[triad])[0] += 1
#             elif digit == 1:
#                 (triads_dictionary[triad])[1] += 1
#             break
#
# print("Final data string:")
# print(general_string)
# print()
#
# # generate first three chars in predicted string based on frequency of 0 and 1 in the base string
# predicted_string = ""
# for i in range(3):
#     predicted_string += random.choice(general_string)
# print(predicted_string)
#
# test_string = input("Please enter a test string containing 0 or 1:")
# general_string = "".join([x for x in test_string if x in APPROPRIATE_INPUT])
# print("\n", general_string, sep='')
#
# for i in range(len(general_string) - 3):
#     triad = general_string[i:i + 3]
#     if (triads_dictionary[triad])[1] < (triads_dictionary[triad])[0]:
#         predicted_string += '0'
#     else:
#         predicted_string += '1'
# print("prediction:\n", predicted_string, "\n", sep='')
#
# guesses = 0
# for i in range(3, len(general_string)):
#     if general_string[i] == predicted_string[i]:
#         guesses += 1
# print("Computer guessed right {0:d} out of {1:d} symbols ({2:.2f} %)".format(guesses, len(general_string) - 3,
#                                                                          (guesses / (len(general_string) - 3)) * 100))

# ------------------------Stage 4------------------------------------
import random

MINIMAL_LENGTH = 100
APPROPRIATE_INPUT = ['0', '1']
TRIADS_LIST = ['000', '001', '010', '011', '100', '101', '110', '111']


def education():
    print("Please give AI some data to learn...\n"
          "The current data length is 0, {0:d} symbols left\n"
          "Print a random string containing 0 or 1:".format(MINIMAL_LENGTH))
    input_string = input()
    base_string = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
    # print(base_string)
    while len(base_string) < MINIMAL_LENGTH:
        print("Current data length is ", len(base_string), ", ",
              MINIMAL_LENGTH - len(base_string), " symbols left", sep='')
        input_string = input("Print a random string containing 0 or 1:")
        input_string_filtered = "".join([x for x in input_string if x in APPROPRIATE_INPUT])
        base_string = base_string + input_string_filtered

    add_educational_info(base_string)

    print("Final data string:")
    print(base_string)
    print()
    return base_string


def add_educational_info(string):
    for i in range(len(string) - 3):
        for triad in triads_dictionary.keys():
            if triad == string[i:i + 3]:
                digit = int(string[i + 3])
                if digit == 0:
                    (triads_dictionary[triad])[0] += 1
                elif digit == 1:
                    (triads_dictionary[triad])[1] += 1
                break


def make_prediction(base_string, test_string):
    # generate first three chars in predicted string based on frequency of 0 and 1 in the base string
    predicted_string = ""
    for i in range(3):
        predicted_string += random.choice(base_string)

    base_string = "".join([x for x in test_string if x in APPROPRIATE_INPUT])
    # print(base_string)

    for i in range(len(base_string) - 3):
        triad = base_string[i:i + 3]
        if (triads_dictionary[triad])[1] < (triads_dictionary[triad])[0]:
            predicted_string += '0'
        else:
            predicted_string += '1'
    if len(base_string) > 3:
        add_educational_info(base_string)
    print("prediction:\n", predicted_string, "\n", sep='')

    guesses = 0
    for i in range(3, len(base_string)):
        if base_string[i] == predicted_string[i]:
            guesses += 1
    print("Computer guessed right {0:d} out of {1:d} symbols ({2:.2f} %)".format(guesses, len(base_string) - 3,
                                                                                 (guesses / (
                                                                                         len(base_string) - 3)) * 100))
    return guesses - (len(base_string) - 3 - guesses) if len(base_string) > 3 else 0


# triads_dictionary = dict.fromkeys(TRIADS_LIST, [0, 0])
triads_dictionary = dict.fromkeys(TRIADS_LIST, None)
for triad in triads_dictionary.keys():
    triads_dictionary[triad] = [0, 0]
general_string = education()
player_balance = 1000
print("You have ${0:d}. Every time the system successfully predicts your next press, you lose $1.\n"
      "Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!\n".format(player_balance))
while True:
    decision = input("Print a random string containing 0 or 1:\n")
    if decision.__eq__("enough"):
        break
    player_balance -= make_prediction(general_string, decision)
    print("Your balance is now ${0:d}\n".format(player_balance))
print("Game over!")
