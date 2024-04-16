from googletrans import Translator
import requests


def translate_text_rus_to_eng(text):
    translator = Translator()
    translation = translator.translate(text, src='ru', dest='en')
    return translation.text


def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        country_datas = response.json()
        if country_datas:
            return country_datas[0]
        else:
            print(f"Ошибка {country_name}: не найдена.")
            return None
    else:
        print(f"Не удалось получить данные по стране {country_name}: Код состояния {response.status_code}.")
        return None


def main():
    input_country_name = input("Введите название страны: ")
    translated_text = translate_text_rus_to_eng(input_country_name)
    country_data = get_country_data(translated_text)

    print(f'''Страна: {country_data.get('name', {}).get('common', 'N/A')}, 
        Язык: {', '.join(country_data.get('languages', ['N/A']))}, 
        Столица: {country_data.get('capital', 'N/A')}, 
        Население: {country_data.get('population', 'N/A')},
        Валюта: {', '.join(country_data.get('currencies', ['N/A']))}''')
