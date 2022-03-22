# Secure Passwords Using Python 

SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('i', '1'), ('o', '0'), ('I', "|"))
def secure(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password : ")
    final = secure(password)
    print(f"Your secured password is {final}")