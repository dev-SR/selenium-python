# pipenv install selenium pandas webdriver-manager rich
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.setup import WebDriverSetup

class LinkGrabber(WebDriverSetup):
    def __init__(self, headless=False):
        super().__init__(headless=headless)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def collect_links(self, url):
        self.get(url)
        try:
            WebDriverWait(self, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "t404__showmore")))
            show_more_button = self.find_element(By.CLASS_NAME, "t404__showmore")
            while show_more_button.is_displayed():
                show_more_button.click()
        except TimeoutException:
            print("Timeout while waiting for show more button")
        links = self.find_elements(By.CLASS_NAME, "t404__link")
        headers = self.find_elements(By.CLASS_NAME, "t404__title.t-heading.t-heading_xs")
        links_data = []
        for i in range(len(links)):
            link_data = {"href": links[i].get_attribute("href"), "header": headers[i].text}
            links_data.append(link_data)
        df = pd.DataFrame(links_data)
        df.to_csv("links_data.csv", index=False)
        print(f"Collected {len(links_data)} links")
