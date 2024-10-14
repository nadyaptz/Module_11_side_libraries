import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# сначала познакомимся с Pandas. Для этого прочитаем данные из файлов:

student_names = []
with open('list_of_students.txt', 'r', encoding='UTF-8') as file:
    line = file.readlines()
    student_names.extend(line)

for i in range(len(student_names)):
    student_names[i] = str(student_names[i]).replace("\n", '')

student_dates_of_birth = []
with open('dates_of_birth.txt', 'r', encoding='UTF-8') as file:
    line = file.readlines()
    student_dates_of_birth.extend(line)

for i in range(len(student_dates_of_birth)):
    student_dates_of_birth[i] = str(student_dates_of_birth[i]).replace("\n", '')

# создадим табличку из данных
table = pd.DataFrame(
    {
        "A": '11B',
        "B": pd.Series(student_names, dtype=str),
        "C": pd.Series(student_dates_of_birth),
        "D": np.array([3] * 28, dtype="int32"),
        "E": pd.Categorical(["соц-эконом", "хим-био", "мат", "соц-эконом", "соц-эконом", "хим-био", "мат", "соц-эконом",
                             "соц-эконом", "хим-био", "мат", "соц-эконом",
                             "соц-эконом", "хим-био", "мат", "соц-эконом",
                             "соц-эконом", "хим-био", "мат", "соц-эконом",
                             "соц-эконом", "хим-био", "мат", "соц-эконом",
                             "соц-эконом", "хим-био", "мат", "соц-эконом"]),
    })
#
print(table)

# добавим пол студента
table2 = table.copy()
table2['D'] = ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'F', 'F',
               'F', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'M', 'F', 'F']

print(table2)

# отберем всех девушек
table3 = table2[table2['D'].isin(['F'])]  # all female students
print(table3)

# теперь поработаем с матрицами:

first_line = np.linspace(0, 7, num=5)
print(np.array(first_line))
second_line = np.zeros(5)
print(np.array(second_line))
third_line = np.ones(5)
print(np.array(third_line))
forth_line = np.arange(5)
print(np.array(forth_line))
fifth_line = np.arange(10, 20, 2)
print(fifth_line)
# создадим матрицу из строк:
matrix = np.array([first_line, second_line, third_line, forth_line, fifth_line])
print(matrix)

# создадим единичную матрицу:
a = np.eye(5)
print("Единичная матрица:\n", a)

# сложим наши две матрицы:
result = matrix + a
print("Результат сложения двух матриц:\n", result)

# а теперь начертим график (обратимся к первому примеру - возьмем данные из таблички про студентов)

# посчитаем, сколько детей родилось в каких месяцах

my_months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Month = lambda x: x[3:5]

for i in range(len(student_dates_of_birth)):
    index = int(Month(student_dates_of_birth[i])) - 1
    my_months[index] += 1
print(my_months)

month_titles = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
                'декабрь']
plt.pie(my_months, labels=month_titles, counterclock=False)
plt.title('Пример круговой диаграммы: Кол-во родившихся по месяцам студентов')

plt.show()
