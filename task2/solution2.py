import sys
import requests
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(f"__name__ in solution2.py: {__name__}")

def run_script(output_path):
    # Список букв русского алфавита
    russian_letters = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К',
        'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
        'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
    ]

    # Инициализация счетчиков для каждой буквы
    counts = {letter: 0 for letter in russian_letters}

    all_members = []
    cmcontinue = ''
    print("Начинаем получение данных с Википедии...")
    while True:
        params = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': 'Категория:Животные_по_алфавиту',
            'cmlimit': '500',
            'format': 'json',
        }
        if cmcontinue:
            params['cmcontinue'] = cmcontinue
        response = requests.get('https://ru.wikipedia.org/w/api.php', params=params)
        data = response.json()
        all_members.extend(data['query']['categorymembers'])
        if 'continue' in data and 'cmcontinue' in data['continue']:
            cmcontinue = data['continue']['cmcontinue']
        else:
            break
    print(f"Получено {len(all_members)} записей.")

    # Подсчет животных, начинающихся на каждую букву
    for member in all_members:
        title = member['title']
        first_char = title[0].upper()
        if first_char in counts:
            counts[first_char] += 1

    # Вывод результатов в консоль
    print("\nКоличество животных на каждую букву:")
    for letter in russian_letters:
        print(f"{letter}: {counts[letter]}")

    # Убедимся, что директория существует
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Запись результатов в CSV файл
    with open(output_path, 'w', encoding='utf-8') as f:
        for letter in russian_letters:
            f.write(f'{letter},{counts[letter]}\n')
    print(f"\nРезультаты записаны в файл {output_path}")

    return counts  # Возвращаем словарь с подсчетами для тестирования

if __name__ == '__main__':
    # Путь для сохранения файла
    output_path = r'C:\Users\artso\Source\Repos\juniors_interview\task2\beasts.csv'
    run_script(output_path)
