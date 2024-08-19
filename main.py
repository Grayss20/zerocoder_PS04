from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random
import pprint


def initial_search():
    browser.get(
        "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    first_choice = input("Данная программа осуществляет поиск по статьям русской Википедии. "
                         "\nЧто вы хотите найти? ")
    browser.find_element(By.ID, "searchInput").send_keys(first_choice, Keys.ENTER)
    if browser.find_element(By.ID, "firstHeading").get_attribute("textContent") == "Результаты поиска":
        browser.find_element(By.CLASS_NAME, "mw-search-result-heading").find_element(By.TAG_NAME, "a").click()


def scroll_article():
    print("Нажимайте Enter для листания параграфов.")
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


def get_hatnotes():
    hh = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hh.append(element)
    return hh


browser = webdriver.Chrome()
initial_search()
hatnotes = get_hatnotes()

print(f"Ваш поиск вернул статью с {len(hatnotes)} связанными с ней статьями."
      f"\nВы можете: \n1) листать параграфы текущей статьи, \n2) перейти на одну из "
      f"связанных страниц или \n3) выйти из программы.")
while True:
    try:
        choice = int(input("Ваш выбор 1, 2 или 3: "))
        if choice not in [1, 2, 3]:
            raise ValueError
        break
    except ValueError:
        print("Неверное значение. Попробуйте ещё раз.")

if choice == 1:
    scroll_article()
elif choice == 2:
    link = hatnotes[0].find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    scroll_article()
elif choice == 3:
    browser.quit()


hatnote = random.choice(hatnotes)

input("Нажмите Enter. ")

link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
input("Нажмите Enter. ")
time.sleep(10)
browser.quit()
