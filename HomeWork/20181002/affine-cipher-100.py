import string

caesaralpha = "abcdefghijklmnopqrstuvwxyz_"

def caesar(input_string, rot):
    output_string = ""
    num = input_string.find(input_string[rot])
    num *= 4
    num += 5
    num %= 27
    output_string = input_string[num]
    # for i in range(len(input_string)):
    #     if input_string[i].isalnum():
    #         idx = (caesaralpha.find(input_string[i]) + rot) % len(caesaralpha)
    #         output_string += caesaralpha[idx]
    #     else:
    #         output_string += input_string[i]
    return output_string

enc = 'ifpmluglesecdlqp_rclfrseljpkq' # encrypt data

for i in range(len(caesaralpha)):
    print caesar(enc, i)
