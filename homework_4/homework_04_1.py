adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(" ", "   ")
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = 0
for letter in adwentures_of_tom_sawer:
    if letter == "h":
     count+=1
print(count)



# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
letter_capilaze = adwentures_of_tom_sawer.split()
for leters in letter_capilaze:
    if leters[0].isupper():
      count+=1
print(count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
count = 0
words = adwentures_of_tom_sawer.split()
for position, word in enumerate(words):
    if word == "Tome":
       count+=1
       if count==2:
        print(f"Слово 'Tom' зустрічається вдруге на позиції {position}")
        break
else:
    print("Слово 'Tom' не зустрічається вдруге")
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
plit_sentences = adwentures_of_tom_sawer.replace(';', '.').split('.')
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in plit_sentences if sentence.strip()]

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.

"""
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3]
    print(fourth_sentence.lower())
else:
    print("Менше ніж чотири речення в тексті.")



# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print("Є речення, яке починається з 'By the time'.")
        found = True
        break
if not found:
    print("Немає речення, яке починається з 'By the time'.")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
if adwentures_of_tom_sawer_sentences:
    last_sentence = adwentures_of_tom_sawer_sentences[-1]
    word_count = len(last_sentence.split())
    print(f"Кількість слів в останньому реченні: {word_count}")
else:
    print("Немає жодного речення в тексті.")