# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print (f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples*4


# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
print("У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.")
print("Скільки всього дерев посадили в саду?" )
apples_1 = 4
pear_1 = apples_1 + 5
plam_1 = apples_1 - 2
tree_1 = apples_1 + pear_1 +plam_1
print( "Відповідь:"  , tree_1 ,"дерев посадили в саду" )
print()



"""

# task 08
"""
print("До обіда температура повітря була на 5 градусів вище нуля.")
print("Після обіду температура опустилася на 10 градусів.")
print('Надвечір потепліло на 4 градуси. Яка температура надвечір?')
temp_1= 0 + 5
temp_2 = temp_1 - 10
temp_3 = temp_2 + 4
print("Відповідь:" , temp_3 , "температура надвечір")
print()

"""

# task 09
"""
print("Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.")
print("1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.")
print("Скількі сьогодні дітей у театральному гуртку?")
girl_1 = int(24 / 2 )
boy_1 = 24 - 1
girl_2 = girl_1 - 2
print("Відповідь: Сьогодні у театральному гуртку було", boy_1 ,"хлопчика і", girl_2, "дівчаток")
print()


"""

# task 10
"""
print("Перша книжка коштує 8 грн., друга - на 2 грн. дороже,")
print("а третя - як половина вартості першої та другої разом.")
print("Скільки будуть коштувати усі книги, якщо купити по одному примірнику?")
book_1 = 8
book_2 = book_1 + 2
book_3 = int((book_1 + book_2)/2)
book_all = book_1 + book_2 + book_3
print ("Відповідь:", book_all, "гривень будуть коштувати усі книги, якщо купити по одному примірнику.")
