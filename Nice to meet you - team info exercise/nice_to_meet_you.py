import os

name = input('What is your name?: ')
place = input('Where are they from?: ')
hobby = input('What hobbies/pastimes do they enjoy?: ')
why = input('Why did you pick SoftUni?: ')
print('===============================================')

info = name + ' from ' + place + ' with a ' + hobby + ' hobby' + ' pick SoftUni because ' + why + ' :)'
print(info)

ok = False
while not ok:
    dir_to_save = input('Where you want to save your txt file? (a/path/you/want/to/save/to): ')
    file_name = input('Enter your file name: ') + '.txt'
    try:
        f = open(os.path.join(dir_to_save, file_name), "w")
        f.write(info)
        f.close()
        ok = True
    except:
        print('Something is wrong! Try again to enter the file name and path: ')
