import time
import requests

from selenium.webdriver.common.by import By
from seleniumwire import webdriver

driver = webdriver.Chrome()
driver.get("https://www.vivriticapital.com/pdf/Digital%20Lending/Smartcoin%20-%20LSP%20and%20DLA.pdf")

links = driver.find_elements(By.TAG_NAME, 'a')
l = []
for i in links:
    href = i.get_attribute("href")
    l.append(href)
print(l)
print(len(l))
link_details = {"400 Client Error or Server Error": [],
                "404 Not Found": [],
                "200 OK": [],
                "Others": []
                }
for url in l:
    try:
        response = requests.get(url)
        if response.status_code == 400:
            print(f"Broker link found and link is {url} and status code=400")

            link_details[f'{response.status_code} Client Error or Server Error'].append(url)
        elif response.status_code == 404:
            print(f"Link Not found and link is {url} and status code=404")
            link_details[f'{response.status_code} Not Found'].append(url)

        elif response.status_code == 200:
            print(f"Link is OK and url is {url}")
            link_details[f"{response.status_code} OK"].append(url)

        else:
            print(f"Link is not proper")
            link_details["Others"].append(f"{response.status_code} : {url}")

    except requests.exceptions.RequestException as e:
        print("exception occurs", e)
print(link_details)
