# morse dict
morse = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-':'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'}

# input validation
check = 1
while(check):
    print("Input a sequence of dashes (-) and dots (.) with no spaces.")
    str_morse = input()
    check = 0
    for i in range((len(str_morse))):
        if str_morse[i] == '.':
            pass
        elif str_morse[i] == '-':
            pass
        else:
            check += 1
            print('Incorrect character detected.')
            break

# this function starts from the beginning of the morse string and converts the first i (4/3/2/1) dots and dashes to a letter
# str is the remaining morse characters that have yet to be converted
# ans is the morse characters that have been converted to letters, and gets appended with the newly converted letter during recursive calls
def demorse(str, ans):
    for i in [4,3,2,1]:
        # if we are selecting more morse characters than there are left in the string, skip through this iteration of i
        if len(str) < i:
            continue
        # char_morse is the first i morse characters of the string; we will convert this to a letter
        char_morse = str[:i]
        # not all morse strings of length 4 are in the a-z dictionary
        if i == 4:
            if char_morse not in morse:
                continue
        # convert char_morse to a letter (char)
        char = morse.get(char_morse)
        # if we have reached the end of the string, print what we have for ans so far with the new char
        if len(str) == i:
                print(ans+char)
        # otherwise, recursively call demorse() with the remaining string of morse characters (from i onwards), and add char to ans
        else:
            demorse(str[i:], ans+char)
    return 'Done!'

print(demorse(str_morse, ''))

