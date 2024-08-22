import os

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class StudentRegistrationFormLocators:
    LOCATOR_FIRSTNAME_TEXTFIELD = (By.CSS_SELECTOR, "#firstName")
    LOCATOR_LASTNAME_TEXTFIELD = (By.XPATH, "//*[@id='lastName']")
    LOCATOR_EMAIL_TEXTFIELD = (By.ID, "userEmail")
    LOCATOR_MAIL_GENDER_RADIO = (By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label")
    LOCATOR_FEMAIL_GENDER_RADIO = (By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2) > label")
    LOCATOR_OTHER_GENDER_RADIO = (By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3) > label")
    LOCATOR_MOBILE_TEXTFIELD = (By.CSS_SELECTOR, "#userNumber")
    LOCATOR_CALENDAR_FORM = (By.CSS_SELECTOR, "#dateOfBirthInput")
    LOCATOR_CALENDAR_DAY_PICK = (By.XPATH, "//*[@class='react-datepicker__week']/*[text()='{}']")
    LOCATOR_CALENDAR_MONTH_DROPDOWN = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    LOCATOR_CALENDAR_YEAR_DROPDOWN = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    LOCATOR_SUBJECT_TEXTFIELD = (By.CSS_SELECTOR, "#subjectsInput")
    LOCATOR_PICTURE_PICKER = (By.CSS_SELECTOR, "#uploadPicture")
    LOCATOR_CURRENT_ADDRESS_TEXTFIELD = (By.CSS_SELECTOR, "#currentAddress")
    LOCATOR_STATE_DROPDOWN = (By.XPATH, "//*[@id='state']")
    LOCATOR_STATE_OPTION = (By.XPATH, "//*[@id='state']/div[2]/div/div[text()='{}']")
    LOCATOR_CITY_DROPDOWN = (By.ID, "city")
    LOCATOR_CITY_OPTION = (By.XPATH, "//*[@id='city']/div[2]/div/div[text()='{}']")
    LOCATOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    LOCATOR_RESULT_MODAL_TITLE = (By.XPATH, '// *[ @ id = "example-modal-sizes-title-lg"]')
    LOCATOR_RESULT_MODAL_STUDENT_NAME = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_EMAIL = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[2]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_GENDER = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[3]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_MOBILE = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_DATE_OF_BIRTH = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[5]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_SUBJECTS = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[6]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_HOBBIES = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[7]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_PICTURE = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[8]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_ADDRESS = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[9]/td[2]')
    LOCATOR_RESULT_MODAL_STUDENT_STATE_AND_CITY = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[10]/td[2]')


class StudentRegistrationFormMethods(BasePage):
    def enter_firstname(self, firstname):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_FIRSTNAME_TEXTFIELD).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_LASTNAME_TEXTFIELD).send_keys(lastname)

    def enter_email(self, email):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_EMAIL_TEXTFIELD).send_keys(email)

    def click_gender(self, gender="other"):
        if gender == "other":
            self.find_element(StudentRegistrationFormLocators.LOCATOR_OTHER_GENDER_RADIO).click()
        elif gender == "male":
            self.find_element(StudentRegistrationFormLocators.LOCATOR_MAIL_GENDER_RADIO).click()
        elif gender == "female":
            self.find_element(StudentRegistrationFormLocators.LOCATOR_FEMAIL_GENDER_RADIO).click()
        else:
            raise ValueError('Wrong gender option Value!')

    def enter_mobile(self, mobile):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_MOBILE_TEXTFIELD).send_keys(mobile)

    def enter_date_of_birth(self, day, month, year):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_CALENDAR_FORM).click()
        select_year = Select(self.find_element(StudentRegistrationFormLocators.LOCATOR_CALENDAR_YEAR_DROPDOWN))
        select_year.select_by_visible_text(year)
        select_month = Select(self.find_element(StudentRegistrationFormLocators.LOCATOR_CALENDAR_MONTH_DROPDOWN))
        select_month.select_by_visible_text(month)
        self.find_element(tuple((StudentRegistrationFormLocators.LOCATOR_CALENDAR_DAY_PICK[0],
                                 StudentRegistrationFormLocators.LOCATOR_CALENDAR_DAY_PICK[1].format(day)))).click()

    def enter_subjects(self, subject):
        for i in subject:
            self.find_element(StudentRegistrationFormLocators.LOCATOR_SUBJECT_TEXTFIELD).send_keys(i)
            self.find_element(StudentRegistrationFormLocators.LOCATOR_SUBJECT_TEXTFIELD).send_keys(Keys.RETURN)

    def upload_picture(self, picture):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_PICTURE_PICKER).send_keys(os.getcwd() + picture)

    def enter_current_address(self, current_address):
        (self.find_element(StudentRegistrationFormLocators.LOCATOR_CURRENT_ADDRESS_TEXTFIELD)
         .send_keys(current_address))

    def enter_state(self, state="NCR"):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_STATE_DROPDOWN).click()
        self.find_element(tuple((StudentRegistrationFormLocators.LOCATOR_STATE_OPTION[0],
                                 StudentRegistrationFormLocators.LOCATOR_STATE_OPTION[1].format(state)))).click()

    def enter_city(self, city="Delhi"):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_CITY_DROPDOWN).click()
        self.find_element(tuple((StudentRegistrationFormLocators.LOCATOR_CITY_OPTION[0],
                                 StudentRegistrationFormLocators.LOCATOR_CITY_OPTION[1].format(city)))).click()

    def click_submit(self):
        self.find_element(StudentRegistrationFormLocators.LOCATOR_SUBMIT_BUTTON).click()

    def read_result_modal_title(self):
        return self.read_element(self.find_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_TITLE))

    def read_result_modal_student_name(self):
        return self.read_element(self.find_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_NAME))

    def read_result_modal_student_email(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_EMAIL)

    def read_result_modal_student_gender(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_GENDER)

    def read_result_modal_student_mobile(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_MOBILE)

    def read_result_modal_student_date_of_birth(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_DATE_OF_BIRTH)

    def read_result_modal_student_subjects(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_SUBJECTS)

    def read_result_modal_student_hobbies(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_HOBBIES)

    def read_result_modal_student_picture(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_PICTURE)

    def read_result_modal_student_address(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_ADDRESS)

    def read_result_modal_state_and_city(self):
        return self.read_element(StudentRegistrationFormLocators.LOCATOR_RESULT_MODAL_STUDENT_STATE_AND_CITY)
