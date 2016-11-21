from PIL import Image
import math


def is_prime(a):
    return all(a % i for i in xrange(2, a))


def find_max_factor(a):
    if is_prime(a):
        return a
    else:
        factor_list = [i for i in xrange(2, a) if a % i == 0]
        return factor_list[int(math.floor(len(factor_list) / 2))]

with open('./info.txt', 'r') as myfile:
    txt = myfile.read().replace('\n', '')

while len(txt) % 3 != 0:
    txt += ' '

asc_list = [ord(i) for i in txt]
pixel_list = zip(asc_list[0::3], asc_list[1::3], asc_list[2::3])
max_factor = find_max_factor(len(pixel_list))
im = Image.new('RGB', (max_factor, len(pixel_list) / max_factor))
im.putdata(pixel_list)
im.save('./puzzle.png')
