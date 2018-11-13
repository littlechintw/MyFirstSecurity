import string

text = "xyzqc{t3_qelrdeq_t3_k33a3a_lk3_lc_qe3p3}"
letter = "abcdefghijklmnopqrstuvwxyz"

def caesar(input):
    output = ""
    str(output)
    for i in range(len(text)):
      if(letter.find(text[i]) >= 0):
        if(letter.find(text[i])+input >= 26):
          output += letter[letter.find(text[i])+input-26]
        else:
          output += letter[letter.find(text[i])+input]
      else:
        output += text[i]
    return output

for n in range(26):
  print(caesar(n))

# http://120.114.62.89/challenges#ABCTF%202016%20:%20ceasar-salad-10
