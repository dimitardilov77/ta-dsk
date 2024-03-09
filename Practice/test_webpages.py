import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestSimple:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_python_org(self):
        self.driver.get("https://www.python.org")

        print()
        print()

        print(self.driver.title)

        searchbar = self.driver.find_element(By.ID, "id-search-field")
        searchbar.clear()
        searchbar.send_keys("getting started")
        searchbar.send_keys(Keys.ENTER)

        first_link = self.driver.find_element(By.LINK_TEXT, "PyTraining: Getting Started with API Design using Python")
        first_link.click()

        exact_date = self.driver.find_element(By.CLASS_NAME, "single-date").text
        assert exact_date == "16 Sept."

    def test_qa_site(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Consent']").click()

        firstName = "Gábor"
        lastName = "Nyilas"
        email = "gabor.nyilas@codecool.com"
        gender = "Male"

        self.driver.find_element(By.ID, "firstName").send_keys(firstName)
        self.driver.find_element(By.ID, "lastName").send_keys(lastName)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

        self.driver.find_element(By.XPATH, f"//label[normalize-space()='{gender}']").click()



        time.sleep(10)