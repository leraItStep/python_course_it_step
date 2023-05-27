#### Lesson 9 For loop

### Task 1
Написать программу, которая на вход принимает целое число N. Вывести в консоль число Фибоначчи, равное N
~~~
Input: 3
Output: 2
~~~

### Task 2
Создайте любую переменную строку и поместите туда любой текст. Сделайте так, чтобы все нечетные по порядку слева на право символы стали “_”, а все символы, местоположение которых четное и которые равны “a” - стали “b”. 
~~~
Input: “Ham is tasty” 
Output: “_b _s_t_s_y”
~~~
### Task 3
Пройтись по диапазону чисел от 0 до 100 и вывести только те из них, которые делятся на 3

### Task 4
Дано натуральное число N. Используя операции // и %, следует перевернуть данное число.
~~~
Input: 123 
Output: 321
~~~

### Task 5
Дано натуральное число N. Если оно является простым, то следует вывести 1, иначе - 0. Простым называется число, которое делится без остатка на себя и 1. 

### Task 6
Пройтись по диапазону чисел от 0 до 100, выводить все числа, при этом пропустить число 4 и, как только цикл достигнет числа 18 - выйти из цикла

### Task 7**
Вы ведете счет в бейсбольном матче по странным правилам. Игра состоит из нескольких раундов,
где результаты прошлых раундов могут повлиять на результаты будущих раундов.
В начале игры вы начинаете с пустой записью. Вам дан список строк `ops`, где `ops[i]` — это i-я операция, которую вы должны применить к записи, и она является одной из следующих:
- Целое число x. Запишите новую оценку x.
- "+" - Запишите новую оценку, которая является суммой двух предыдущих оценок. Гарантируется, что всегда будет два предыдущих результата. 
- "D" - Запишите новый счет, который в два раза превышает предыдущий. Гарантируется, что всегда будет предыдущий счет.
- "C" - аннулировать предыдущий счет, удаляя его из записи. Гарантируется, что всегда будет предыдущий счет.

вернуть сумму всех баллов записи

~~~
Input: ["5", "-2", "4", "C", "D", "9", "+", "+"]
Output: 27
~~~