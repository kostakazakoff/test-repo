import os

name = input('What is your name?: ')
place = input('Where are they from?: ')
hobby = input('What hobbies/pastimes do they enjoy?: ')
why = input('Why did you pick SoftUni?: ')
print('========================================================================')

# С + е стария метод. Вече препоръчват с f стринг
info = f"I am {name} from {place}.\n" \
       f"My hobby is {hobby}.\n" \
       f"I picked SoftUni because {why}."

print(info)

ok = False
while not ok:
    path_to_save = input('Where you want to save your txt file? (a/path/you/want/to/save/to): ')
    path_to_save = os.path.join(path_to_save)

    file_name = input('Enter your file name (your_name): ') + '.txt'
    try:
        f = open(os.path.join(path_to_save, file_name), "w")
        f.write(info)
        f.close()
        ok = True
    # Общо except като цяло не се препоръчва.
    except FileNotFoundError:
        print('===============================================================')
        print(f'The path "{path_to_save}" was not found. ')
    except PermissionError:
        print('===============================================================')
        print(f'No permission to save in "{path_to_save}" or file already exists. ')
