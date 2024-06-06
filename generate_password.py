import random
import string


def generate():
    pws = string.ascii_letters + string.punctuation + string.digits
    pws = ''.join(random.sample(pws, 20))
    return pws



print(generate())