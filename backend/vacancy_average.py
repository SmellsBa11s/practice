import sqlite3
import re

def extract_numbers(salary_str):
    # Ищем все числа в строке и возвращаем список найденных чисел
    return [int(num.replace('\xa0', '')) for num in re.findall(r'\d[\d ]*\d', salary_str)]

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def calculate_average_salary_vacancy(keyword):
    conn = sqlite3.connect('bd_vacancy/vacancy.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT salary FROM {keyword}")
    rows = cursor.fetchall()

    salaries = []

    for row in rows:
        salary_str = row[0]
        if "Не указана" in salary_str:
            continue

        numbers = extract_numbers(salary_str)

        if numbers:
            # Если есть два числа, это диапазон, вычисляем среднее значение
            if len(numbers) == 2:
                average_salary = calculate_average(numbers)
                salaries.append(average_salary*1000)
            # Если есть одно число, добавляем его как есть
            elif len(numbers) == 1:
                salaries.append(numbers[0]*1000)

    conn.close()

    # Вычисляем среднее значение зарплат
    if len(salaries) > 0:
        return sum(salaries) / len(salaries)
    else:
        return None
def calculate_average_salary_resume(keyword):
    conn = sqlite3.connect('bd_resume/resume.db')
    cursor = conn.cursor()


    cursor.execute(f"SELECT salary FROM {keyword}")
    rows = cursor.fetchall()


    salaries = []


    for row in rows:
        salary_str = row[0]
        if "Не указана" in salary_str:
            continue

        numbers = extract_numbers(salary_str)

        if numbers:
            # Если есть два числа, это диапазон, вычисляем среднее значение
            if len(numbers) == 2:
                average_salary = calculate_average(numbers)
                salaries.append(average_salary*1000)
            # Если есть одно число, добавляем его как есть
            elif len(numbers) == 1:
                salaries.append(numbers[0])

    conn.close()

    # Вычисляем среднее значение зарплат
    if len(salaries) > 0:
        return sum(salaries) / len(salaries)
    else:
        return None