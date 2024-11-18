import requests
import time
import csv
from bs4 import BeautifulSoup

def get_animals_by_page(url):
    """
    Получшение всех животных и адреса следующей страницы
    """
    rp = requests.get(url=url)
    soup = BeautifulSoup(rp.text, 'lxml')
    animal_groups = soup.find('div', {'class': 'mw-category mw-category-columns'}).find_all('div', {'class': 'mw-category-group'})
    animals = []
    for group in animal_groups:
        animals.extend(group.find_all('a'))  # Собираем всех животных

    # Ищем ссылку на следующую страницу
    next_page = soup.find('a', string="Следующая страница")
    return animals, next_page

def get_letters_count():
    """
    Подсчёт количества животных на каждую букву алфавита
    """
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letters_count = dict()
    
    while(url):
        # print(f'Обработка {url}')
        # Получаем животных и адрес следующей страницы
        animals, next_page = get_animals_by_page(url)
        
        # Проходимся по каждому животному
        for animal in animals:
            letter = animal.get('title')[0]
            if len(letter) > 0 and letter.isalpha():
                letter = letter.upper()
                letters_count[letter] = letters_count.get(letter,0) + 1

        # Обновляем url
        if next_page:
            # time.sleep(0.5)
            url = "https://ru.wikipedia.org" + next_page['href']
        
        else:
            url = None

    with open("beasts.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for letter, count in sorted(letters_count.items()):
            writer.writerow([letter, count])
    


if __name__ == "__main__":
    get_letters_count()