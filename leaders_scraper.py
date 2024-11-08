from bs4 import BeautifulSoup as bs
import json
import requests
import re


def get_cookie():
    cookie_url = "https://country-leaders.onrender.com/cookie"
    req_cookie = requests.get(cookie_url)
    return req_cookie.cookies


def get_first_paragraph(wikipedia_url, session):
    print(wikipedia_url)
    first_paragraph = ""
    req_wiki = session.get(wikipedia_url).text
    soup = bs(req_wiki, "html.parser")
    regex_birthdate = r"\d{4}"
    for para in soup.find_all("p"):
        if re.findall(regex_birthdate, para.get_text()):
            first_paragraph = para.get_text()
            break
    first_paragraph = re.sub(r"\[.*?\]", "", first_paragraph)
    first_paragraph = re.sub(r"\n", " ", first_paragraph)
    first_paragraph = re.sub(r"ⓘ", "", first_paragraph)
    first_paragraph = re.sub(r"/.*?/", "", first_paragraph)
    first_paragraph = re.sub(r"\( *;? *Écouter *\)", "", first_paragraph)
    first_paragraph = re.sub(r"Écouter", "", first_paragraph)
    first_paragraph = re.sub(r" +", " ", first_paragraph)
    first_paragraph = re.sub(r" ,", ",", first_paragraph)
    first_paragraph = re.sub(r"\\u[^\s]*", "", first_paragraph)

    return first_paragraph


def get_leaders():
    leaders_dict = {}
    root_url = "https://country-leaders.onrender.com/"
    status_url = "https://country-leaders.onrender.com/status"
    cookie_url = "https://country-leaders.onrender.com/cookie"
    countries_url = "https://country-leaders.onrender.com/countries"
    leaders_url = "https://country-leaders.onrender.com/leaders"
    req_cookie = requests.get(cookie_url)
    cookies = get_cookie()
    req = requests.get(countries_url, cookies=cookies)
    countries = req.json()
    for i in countries:
        req_leaders = requests.get(leaders_url, cookies=cookies, params={"country": i})
        if req_leaders.status_code != 200:
            cookies = get_cookie()
            req_leaders = requests.get(
                leaders_url, cookies=cookies, params={"country": i}
            ).json()
        else:
            req_leaders = requests.get(
                leaders_url, cookies=cookies, params={"country": i}
            ).json()
        leaders_dict[i] = req_leaders
    with requests.Session() as session:
        for i in countries:
            for leader in leaders_dict[i]:
                wikipedia_url = leader["wikipedia_url"]
                first_paragraph = get_first_paragraph(wikipedia_url, session)
                leader["first_paragraph"] = first_paragraph
    return leaders_dict


def save(leaders_per_country):
    with open("leaders_per_country.json", "w", encoding="utf-8") as json_file:
        json.dump(leaders_per_country, json_file, ensure_ascii=False)


leaders_per_country = get_leaders()
save(leaders_per_country)
