# Given a sorted array of strings, write a recursive function to find the index of the first and last occurrence of a target string. If the target string is not found in the array, report that.
# Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
# Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)
def recursive_target_indexes(arr, target, found = False, indexes=[], i = 0):
    if arr[i] == target:
        indexes.append(i)
        found = True
    if arr[i] != target and found == True:
        found = False
        indexes.append(i - 1)
    if i == len(arr) - 1:
        if len(indexes) == 0:
            return(-1, -1)
        if len(indexes) == 1:
            return(indexes[0], indexes[0])
        return(indexes[0], indexes[-1])
    return recursive_target_indexes(arr, target, found, indexes, i + 1)

# instructors = ["Adriana", "Adriana", "Alan", "Alan", "Alan", "Alan", "Alan", "Braus", "Braus", "Braus", "Braus", "Dan", "Dan", "Dan", "Dan", "Dan", "Dani", "Dani", "Jess", "Meredith", "Milad", "Milad", "Mitchell", "Mitchell", "Mitchell", "Mitchell", "Tina"]
# target = "Jerry"
# print(recursive_target_indexes(instructors, target))
# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, 
# return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

keyboard_dict = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}
def recursive_t9(string_of_nums, possible_strings, builder, index):
    if index == len(string_of_nums):
        possible_strings.append(builder)
        return possible_strings
    
    current_num = int(string_of_nums[index])
    possible_letters = keyboard_dict[current_num]

    for i in range(len(possible_letters)):
        current_letter = possible_letters[i]
        recursive_t9(string_of_nums, possible_strings = possible_strings, builder = builder + current_letter, index = index + 1)

def t9_letters(string_of_nums):
    possible_strings = []
    recursive_t9(string_of_nums, possible_strings, builder = "", index = 0)
    return possible_strings


#  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# print(t9_letters("567"))
