from PIL import Image

txt = 'Congratulations you solved the puzzle! Please reach us in bpan@northern.co'

while len(txt) % 3 != 0:
    txt += ' '

asc_list = [ord(i) for i in txt]
pixel_list = zip(asc_list[0::3], asc_list[1::3], asc_list[2::3])
im = Image.new('RGB', (len(pixel_list), 1))
im.putdata(pixel_list)
im.save('./puzzle.png')
