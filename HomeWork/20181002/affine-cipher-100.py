import string

text = "abcdefghijklmnopqrstuvwxyz_"

def trans():
    atext = ""
    str(atext)
    for i in range(27):
        i = i * 4 + 15
        i %= 27
        atext += text[i]
    return atext


def caesar(input_string):
    output_string = ""
    str(output_string)
    for i in range(len(input_string)):
        num = trans().find(input_string[i])
        output_string += text[num]
    return output_string

enc = 'ifpmluglesecdlqp_rclfrseljpkq' # encrypt data


print(caesar(enc))
