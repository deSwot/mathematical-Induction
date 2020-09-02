import string     
import random     

def generator(in_list):
    x = string.ascii_lowercase
    random_ = ''.join(list((random.choice(x) for num in range(1))))
    while random_ in in_list:
        random_ = ''.join(list((random.choice(x) for num in range(1))))
    return random_
          

