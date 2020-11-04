# Requirements and password should pass all below test cases:
# 1. Password must be at least 8 characters
# 2. Password must be at least 1 upper case
# 3. Password must be at least 1 lower case
# 3. Password must be at least 1 number
# 5. Password must be at least 1 special character

import random
import re
def password_gen():
    random_uppercase = list(map(chr,range(65,91)))
    random_lowercase = list(map(chr,range(97,123)))
    random_chars = ['@','#','$','%','^','&','*']

    password1 = random.choice(random_uppercase) + random.choice(random_lowercase) + random.choice(random_chars) + str(random.randrange(1,9))
    password2 = random.choice(random_uppercase) + random.choice(random_lowercase) + random.choice(random_chars) + str(random.randrange(1,9))

    password = password1 + password2

    return password

test_case = re.fullmatch("((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,20})",password_gen())
if test_case != None:
    print("Password is strong: ", password_gen())
else:
    print("Password is week: ", password_gen())

