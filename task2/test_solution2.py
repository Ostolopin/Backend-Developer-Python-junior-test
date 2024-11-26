import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
import requests_mock
from solution2 import run_script

class TestSolution2(unittest.TestCase):
    def test_api_response(self):
        with requests_mock.Mocker() as m:
            url = 'https://ru.wikipedia.org/w/api.php'
            m.get(url, json={
                'query': {
                    'categorymembers': [
                        {'title': 'Аист'},
                        {'title': 'Бобр'},
                        {'title': 'Волк'},
                        {'title': 'Воробей'},
                        {'title': 'Гусь'}
                    ]
                }
            })

            expected_counts = {
                'А': 1,
                'Б': 1,
                'В': 2,
                'Г': 1,
                # Остальные буквы по нулям
            }

            output_path = r'C:\Users\artso\Source\Repos\juniors_interview\task2\test_beasts.csv'
            counts = run_script(output_path)

            for letter, expected_count in expected_counts.items():
                self.assertEqual(counts.get(letter, 0), expected_count)

    def test_file_creation(self):
        with requests_mock.Mocker() as m:
            url = 'https://ru.wikipedia.org/w/api.php'
            m.get(url, json={
                'query': {
                    'categorymembers': []
                }
            })

            output_path = r'C:\Users\artso\Source\Repos\juniors_interview\task2\test_beasts.csv'
            if os.path.exists(output_path):
                os.remove(output_path)
            run_script(output_path)
            self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()
