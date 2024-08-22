import allure

from PracticeForm import StudentRegistrationFormMethods
import testData.Students as Students
from confest import browser


def test_student_registration_form(browser):
    allure.dynamic.title("Тест формы регистрации студента")
    allure.dynamic.description("Тест заполняет форму, отправляет, "
                               "проверяет что появилось окно с результатами отправки формы и что "
                               "данные в окне соответствуют введённым в форму")
    allure.dynamic.tag("GUI_test", "Simbirsoft", "StudentForm")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    allure.dynamic.link("https://demoqa.com/automation-practice-form", name="Website")
    student_registration_form = StudentRegistrationFormMethods(browser)
    with allure.step("Открытие сайта"): student_registration_form.go_to_site()
    with allure.step("Введение имени"): student_registration_form.enter_firstname(Students.StudentVasia["firstname"])
    with allure.step("Введение фамилии"): student_registration_form.enter_lastname(Students.StudentVasia["lastname"])
    with allure.step("Введение email"): student_registration_form.enter_email(Students.StudentVasia["email"])
    with allure.step("Выбор гендера"): student_registration_form.click_gender(Students.StudentVasia["gender"])
    with allure.step("Введение номера телефона"): student_registration_form.enter_mobile(Students.StudentVasia["mobile"])
    with allure.step("Введение даты рождения"): student_registration_form.enter_date_of_birth(*Students.StudentVasia["dateofbirth"])
    with allure.step("Введение дисциплин"): student_registration_form.enter_subjects(Students.StudentVasia["subjects"])
    with allure.step("Выбор изображения"): student_registration_form.upload_picture(Students.StudentVasia["picture"])
    with allure.step("Введение адреса"): student_registration_form.enter_current_address(Students.StudentVasia["address"])
    with allure.step("Введение штата"): student_registration_form.enter_state(Students.StudentVasia["state"])
    with allure.step("Введение города"): student_registration_form.enter_city(Students.StudentVasia["city"])
    with allure.step("Отправка формы"): student_registration_form.click_submit()

    with allure.step("Проверка наличия окна с результатами"):
        assert student_registration_form.check_modal_result()
    with allure.step("Проверка корректного имени"):
        assert (student_registration_form.read_result_modal_student_name().casefold() ==
            f"{Students.StudentVasia["firstname"]} {Students.StudentVasia["lastname"]}".casefold())
    with allure.step("Проверка корректного email"):
        assert (student_registration_form.read_result_modal_student_email().casefold() ==
            Students.StudentVasia["email"].casefold())
    with allure.step("Проверка корректного гендера"):
        assert (student_registration_form.read_result_modal_student_gender().casefold() ==
            Students.StudentVasia["gender"].casefold())
    with allure.step("Проверка корректного мобильного номера"):
        assert (student_registration_form.read_result_modal_student_mobile().casefold() ==
            Students.StudentVasia["mobile"].casefold())
    with allure.step("Проверка корректной даты рождения"):
        assert (student_registration_form.read_result_modal_student_date_of_birth().casefold() ==
            f"{Students.StudentVasia['dateofbirth'][0]} {Students.StudentVasia['dateofbirth'][1]},"
            f"{Students.StudentVasia['dateofbirth'][2]}".casefold())
    with allure.step("Проверка корректных дисциплин"):
        assert (student_registration_form.read_result_modal_student_subjects().casefold() ==
            ", ".join(Students.StudentVasia['subjects']).casefold())
    with allure.step("Проверка корректного изображения"):
        assert (student_registration_form.read_result_modal_student_picture().casefold() ==
            Students.StudentVasia["picture"].casefold())
    with allure.step("Проверка корректного адреса"):
        assert (student_registration_form.read_result_modal_student_address().casefold() ==
            Students.StudentVasia["address"].casefold())
    with allure.step("Проверка корректных штата и города"):
        assert (student_registration_form.read_result_modal_state_and_city().casefold() ==
            f"{Students.StudentVasia['state']} {Students.StudentVasia['city']}".casefold())