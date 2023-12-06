from os import getenv
from dotenv import load_dotenv
load_dotenv()
API_KEY = getenv("WORDNIK_API_KEY")


class WordNik:
    def __init__(self):
        print("init")

    def text_generate(self, d):
        text = f'# {d["word"].upper()}\n## Definitions\n_from {d["definitions"][0]["source"]}_\n'
        for i in d["definitions"]:
            text += f'_**{i["partOfSpeech"]}:**_ {i["text"]}\n'
        text += f'\n## Examples\n'
        for i in d["examples"]:
            text += i["text"] + "\n_**Source:**_" + f' [{i["title"]}]({i["url"]})\n\n'
        text += f'## Note\n{d["note"]}'
        print(text)
        return text

    def get_WOTD(self, date_iso):
        from resources.variables import WORDNIK_ENDPOINT
        url = f'{WORDNIK_ENDPOINT}/words.json/wordOfTheDay?date={date_iso}&api_key={API_KEY}'
        from requests import get
        response = get(url, headers={}, data={})
        print("WOTD Response:", response.text)
        response_json = response.json()
        template = self.text_generate(response_json)
        return template


if __name__ == "__main__":
    from datetime import date
    cur_date = date.today()
    date_iso = cur_date.isoformat()
    x = WordNik().get_WOTD(date_iso)
    print(x)

