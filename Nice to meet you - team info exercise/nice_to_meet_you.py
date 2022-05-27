name = input('What is your name?: ')
place = input('Where are they from?: ')
hobby = input('What hobbies/pastimes do they enjoy?: ')
why = input('Why did you pick SoftUni?: ')
print('========================================================================')
# С + е стария метод. Вече препоръчват с f стринг.
info = f"I am {name} from {place}.\n" \
       f"My hobby is {hobby}.\n" \
       f"I picked SoftUni because {why}."

print(info)

file_name = f"input('Enter your file name (your_name): ').txt"

# Това също се води добра практика. Няма нужда от close.
# Отваря си файла. Върши това в индентацията и затваря.
# Запазва файла в директорията на проекта
with open(file_name, mode="w") as f:
    f.write(info)

print('========================================================================\n')
print("Your file was saved in the project directory")
