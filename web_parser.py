
import file_operations as fop
from selenium import webdriver
from selenium.webdriver.common.by import By


def SeleniumSetup():  # Selenium driver setup with headless option

    driverOptions = webdriver.FirefoxOptions()
    driverOptions.headless = True
    driver = webdriver.Firefox(options=driverOptions)
    return driver


def parse_link(url):
    driver = SeleniumSetup()
    driver.get(url)
    extracted_content = []

    target_element = driver.find_elements(
        By.XPATH, "//div[@class='category-page__member-left']/a[@title]")

    for items in target_element:
        titles = items.get_attribute("title")
        extracted_content.append(titles)
        # print(titles)

    fop.WriteToFile("files/raw_vault_data.txt", extracted_content)


def RUN():
    parse_link("https://warframe.fandom.com/wiki/Category:Vaulted")
