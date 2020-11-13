import sys
import os
from PIL import Image

# grab first and second argument
# print(sys.argv[1])
# print(sys.argv[2])

# check if new\ exists, if not create
# print(os.listdir('.'))
# print(os.getcwd())

# NÃO                              # curr_dir = './' + sys.argv[1]
# NECESSÁRIO                       # new_dir = './' + sys.argv[2]

curr_dir = sys.argv[1]
new_dir = sys.argv[2]

# print(repr(new_dir))
if not os.path.isdir(new_dir):  # OU os.path.exists
    os.mkdir(new_dir)
    #print('need to create a new dir')
else:
    print('All gooD')

# loop through Pokedex
try:
    for file in os.listdir(curr_dir):
        if file.endswith('jpg'):
            # print(file)
            img = Image.open(f'{curr_dir}{file}')
                # temp = file.split('.')
                # temp[1] = 'png'
                # # print(f'{temp[0]}.{temp[1]}')
                # img.save(f'{new_dir}{temp[0]}.{temp[1]}', 'png')
            clean_name = os.path.splitext(file)[0]
            img.save(f'{new_dir}{clean_name}.png', 'png')
            #print(clean_name)

except FileNotFoundError as err:
    print('File not found...')
# convert images to png
# save to new folder
