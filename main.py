from datetime import datetime
import json
from contacts import get_contacts
from news import get_news


def get_all_information():
    dict_res = {
        "CONTACTS of VC": get_contacts(),
        "NEWS from visa.vfsglobal.com": get_news(),
    }
    return dict_res


def save_to_json(information):
    with open("news_" + str(datetime.now()).replace(' ', '').replace(':', '-') + ".json", "w", encoding="utf-8") as f:
        json.dump(information, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    res = get_all_information()
    save_to_json(res)
