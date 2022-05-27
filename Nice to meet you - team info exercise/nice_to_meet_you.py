import os

name = input('What is your name?: ')
place = input('Where are they from?: ')
hobby = input('What hobbies/pastimes do they enjoy?: ')
why = input('Why did you pick SoftUni?: ')
print('========================================================================')

info = 'I am ' + name + ' from ' + place + '. My hobby is ' + hobby + '. I picked SoftUni because ' + why + '.'
print(info)

ok = False
while not ok:
    path_to_save = input('Where you want to save your txt file? (a/path/you/want/to/save/to): ')
    file_name = input('Enter your file name (your_name): ') + '.txt'
    try:
        with open(os.path.join(path_to_save, file_name), "w") as f:
            f.write(info)
            f.close()
            ok = True
            print(f'Your file is saved as {path_to_save}\\{file_name}')
    except:
        print('===============================================================')
        print('Something is wrong! Try again to enter the file name and path: ')
