import random
import string

for i in range(1, 10):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print(salt)