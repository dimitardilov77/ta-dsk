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
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//button[@aria-label='Consent']").click()

        firstName = "Gábor"
        lastName = "Nyilas"
        email = "gabor.nyilas@codecool.com"
        gender = "Male"
        phoneNumber = "0123456789"
        address1 = "Budapest"
        address2 = "Farkastorki Str"

        self.driver.find_element(By.ID, "firstName").send_keys(firstName)
        self.driver.find_element(By.ID, "lastName").send_keys(lastName)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

        self.driver.find_element(By.XPATH, f"//label[normalize-space()='{gender}']").click()

        self.driver.find_element(By.ID, "userNumber").send_keys(phoneNumber)

        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)

        # self.driver.find_element(By.ID, "dateOfBirthInput").clear()
        # for i in range(11):
        #     self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.BACK_SPACE)

        # self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.COMMAND, "A")
        # self.driver.find_element(By.ID, "dateOfBirthInput").send_keys("11 Oct 1978")

        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        select_element_year = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
        select_year = Select(select_element_year)
        select_year.select_by_visible_text("1978")

        select_element_month = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
        select_month = Select(select_element_month)
        select_month.select_by_visible_text("October")

        self.driver.find_element(By.CLASS_NAME, "react-datepicker__day--011").click()

        self.driver.find_element(By.ID, "subjectsInput").send_keys("Ma")
        self.driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "subjectsInput").send_keys("Comp")
        self.driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)

        elements_sport = (WebDriverWait(self.driver, 10).
                          until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']"))))
        elements_sport.click()

        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Sports']").click()
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Reading']").click()

        self.driver.find_element(By.ID, "currentAddress").send_keys(f"{address1}{Keys.ENTER}{address2}")

        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)

        self.driver.find_element(By.XPATH, "//div[contains(text(),'Select State')]").click()
        self.driver.find_element(By.ID, "react-select-3-input").send_keys("Haryana")
        self.driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

        self.driver.find_element(By.XPATH, "//div[contains(text(),'Select City')]").click()
        self.driver.find_element(By.ID, "react-select-4-input").send_keys("Karnal")
        self.driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

        self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)

        self.driver.find_element(By.ID, "submit").click()

        name_element = self.driver.find_element(By.XPATH,
                                                "//td[normalize-space()='Student Name']//following-sibling::td")
        assert name_element.text == f"{firstName} {lastName}"

        email_element = self.driver.find_element(By.XPATH,
                                                "//td[normalize-space()='Student Email']//following-sibling::td")
        assert email_element.text == email

        gender_element = self.driver.find_element(By.XPATH,
                                                 "//td[normalize-space()='Gender']//following-sibling::td")
        assert gender_element.text == gender

        address_element = self.driver.find_element(By.XPATH,
                                                "//td[normalize-space()='Address']//following-sibling::td")
        assert address_element.text == f"{address1} {address2}"