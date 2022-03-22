#  Password Generator 

import string as s
import random as r

if __name__ == "__main__":
    lower = s.ascii_lowercase
    upper = s.ascii_uppercase
    digits = s.digits
    punc = s.punctuation
    
    plen = int(input("Enter password length : "))
    s = []
    s.extend(list(lower))
    s.extend(list(upper))
    s.extend(list(digits))
    s.extend(list(punc))

    r.shuffle(s)

    pw = "".join(s[:plen])
    print(f'Your password is {pw}')