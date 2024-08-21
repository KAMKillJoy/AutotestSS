import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)


class PracticeForm:

    def __init__(self, driver):
        self.driver = driver
        self.firstname_input = (By.CSS_SELECTOR, "#firstName")
        self.lastname_input = (By.XPATH, "//*[@id='lastName']")
        self.email_input = (By.ID, "userEmail")
        self.gender_male_input = (By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label")
        self.gender_female_input = (By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2) > label")
        self.gender_other_input = (By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3) > label")
        self.mobile_input = (By.CSS_SELECTOR, "#userNumber")
        self.date_of_birth_calendar_input = (By.CSS_SELECTOR, "#dateOfBirthInput")
        self.date_of_birth_day_input = (By.XPATH, "//*[@class='react-datepicker__week']/*[text()='{}']")
        self.date_of_birth_month_input = (By.CSS_SELECTOR, ".react-datepicker__month-select")
        self.date_of_birth_year_input = (By.CSS_SELECTOR, ".react-datepicker__year-select")
        self.subject_input = (By.CSS_SELECTOR, "#subjectsInput")
        self.picture_input = (By.CSS_SELECTOR, "#uploadPicture")
        self.current_address_input = (By.CSS_SELECTOR, "#currentAddress")
        self.state_dropdown_input = (By.XPATH, "//*[@id='state']")
        self.state_option_input = (By.XPATH, "//*[@id='state']/div[2]/div/div[text()='{}']")
        self.city_dropdown_input = (By.ID, "city")
        self.city_option_input = (By.XPATH, "//*[@id='city']/div[2]/div/div[text()='{}']")
        self.submit_input = (By.CSS_SELECTOR, "#submit")
        self.LOCATOR_RESULT_MODAL_STUDENT_NAME = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]')

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname_input).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_input).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_gender(self, gender="other"):
        if gender == "other":
            self.driver.find_element(*self.gender_other_input).click()
        elif gender == "male":
            self.driver.find_element(*self.gender_male_input).click()
        elif gender == "female":
            self.driver.find_element(*self.gender_female_input).click()
        else:
            raise ValueError('Wrong gender option Value!')

    def enter_mobile(self, mobile):
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def enter_date_of_birth(self, day, month, year):
        self.driver.find_element(*self.date_of_birth_calendar_input).click()
        select_year = Select(self.driver.find_element(*self.date_of_birth_year_input))
        select_year.select_by_visible_text(year)
        select_month = Select(self.driver.find_element(*self.date_of_birth_month_input))
        select_month.select_by_visible_text(month)
        self.driver.find_element(self.date_of_birth_day_input[0],
                                 self.date_of_birth_day_input[1].format(day)).click()

    def enter_subject(self, subject):
        for i in subject:
            self.driver.find_element(*self.subject_input).send_keys(i)
            self.driver.find_element(*self.subject_input).send_keys(Keys.RETURN)

    def upload_picture(self, picture):
        self.driver.find_element(*self.picture_input).send_keys(os.getcwd() + picture)

    def enter_current_address(self, current_address):
        self.driver.find_element(*self.current_address_input).send_keys(current_address)

    def enter_state(self, state="NCR"):
        self.driver.find_element(*self.state_dropdown_input).click()
        self.driver.find_element(self.state_option_input[0],
                                 self.state_option_input[1].format(state)).click()

    def enter_city(self, city="Delhi"):
        self.driver.find_element(*self.city_dropdown_input).click()
        self.driver.find_element(self.city_option_input[0],
                                 self.city_option_input[1].format(city)).click()

    def click_submit(self):
        self.driver.find_element(*self.submit_input).click()


class Student:
    def __init__(self, firstname, lastname, email, gender, mobile, dateofbirth, subjects, picture, adress, state, city):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.dateofbirth = dateofbirth
        self.subjects = subjects
        self.picture = picture
        self.adress = adress
        self.state = state
        self.city = city


def ttest_practice_form():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    driver.get('https://demoqa.com/automation-practice-form')

    practice_form = PracticeForm(driver)
    practice_form.enter_firstname("Васисуалий")
    practice_form.enter_lastname("Гваделупа")
    practice_form.enter_email("VasisualiyGvadelupa@mail.ru")
    practice_form.click_gender("female")
    practice_form.enter_mobile("8905452365")
    practice_form.enter_date_of_birth("11", "July", "1988")
    practice_form.enter_subject(["English", "Maths"])
    practice_form.upload_picture("/testimage.jpg")
    practice_form.enter_current_address("ул. Пушкина, д. Колотушкина")
    practice_form.enter_state("Haryana")
    practice_form.enter_city("Karnal")
    practice_form.click_submit()

    print(driver.find_element(*practice_form.LOCATOR_RESULT_MODAL_STUDENT_NAME).text == "Васисуалий Гваделупа")

# driver.quit()


ttest_practice_form()
