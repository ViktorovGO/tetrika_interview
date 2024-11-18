import unittest
from unittest.mock import patch
from io import StringIO
import csv
from bs4 import BeautifulSoup

from solution import get_animals_by_page, get_letters_count  

class TestFetchAnimalsCount(unittest.TestCase):
    @patch('solution.requests.get')
    def test_fetch_animals_count(self, mock_get):
        # Пример HTML-страницы для теста
        example_html = """
        <html>
        <body>
        <div class="mw-category mw-category-columns">
            <div class="mw-category-group">
                <h3>А</h3>
                <ul>
                    <li><a href="/wiki/Animal1" title="Аллигатор">Аллигатор</a></li>
                </ul>
                <h3>Б</h3>
                <ul>
                    <li><a href="/wiki/Animal2" title="Бобр">Бобр</a></li>
                </ul>
                <h3>В</h3>
                <ul>
                    <li><a href="/wiki/Animal3" title="Волк">Волк</a></li>
                </ul>
            </div>
        </div>
        <a href="/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Волк" title="Следующая страница">Следующая страница</a>
        </body>
        </html>
        """

        mock_get.return_value.text = example_html

        # Вызываем тестируемую функцию
        animals, next_page = get_animals_by_page("dummy_url")

        self.assertEqual(len(animals), 3)  # Три записи животных
        self.assertEqual(animals[0]['title'], "Аллигатор")  # Проверяем первую запись
        self.assertIsNotNone(next_page)  # Следующая страница должна быть найдена
        self.assertEqual(next_page['href'], "/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=Волк")  # Ссылка на следующую страницу


if __name__ == "__main__":
    unittest.main()
