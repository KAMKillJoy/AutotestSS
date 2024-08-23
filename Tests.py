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

    student_registration_form = StudentRegistrationFormMethods(browser)  # выбор студента из модуля Students
    student = Students.StudentVasia

    with allure.step("Открытие сайта"): student_registration_form.go_to_site()
    with allure.step("Введение имени"): student_registration_form.enter_firstname(student["firstname"])
    with allure.step("Введение фамилии"): student_registration_form.enter_lastname(student["lastname"])
    with allure.step("Введение email"): student_registration_form.enter_email(student["email"])
    with allure.step("Выбор гендера"): student_registration_form.click_gender(student["gender"])
    with allure.step("Введение номера телефона"): student_registration_form.enter_mobile(student["mobile"])
    with allure.step("Введение даты рождения"): student_registration_form.enter_date_of_birth(*student["dateofbirth"])
    with allure.step("Введение дисциплин"): student_registration_form.enter_subjects(student["subjects"])
    with allure.step("Выбор изображения"): student_registration_form.upload_picture(student["picture"])
    with allure.step("Введение адреса"): student_registration_form.enter_current_address(student["address"])
    with allure.step("Введение штата"): student_registration_form.enter_state(student["state"])
    with allure.step("Введение города"): student_registration_form.enter_city(student["city"])
    with allure.step("Отправка формы"): student_registration_form.click_submit()

    with allure.step("Проверка наличия окна с результатами"):
        assert student_registration_form.check_modal_result()
    with allure.step("Проверка корректного имени"):
        assert (student_registration_form.read_result_modal_student_name().casefold() ==
            f"{student["firstname"]} {student["lastname"]}".casefold())
    with allure.step("Проверка корректного email"):
        assert (student_registration_form.read_result_modal_student_email().casefold() ==
            student["email"].casefold())
    with allure.step("Проверка корректного гендера"):
        assert (student_registration_form.read_result_modal_student_gender().casefold() ==
            student["gender"].casefold())
    with allure.step("Проверка корректного мобильного номера"):
        assert (student_registration_form.read_result_modal_student_mobile().casefold() ==
            student["mobile"].casefold())
    with allure.step("Проверка корректной даты рождения"):
        assert (student_registration_form.read_result_modal_student_date_of_birth().casefold() ==
            f"{student['dateofbirth'][0]} {student['dateofbirth'][1]},"
            f"{student['dateofbirth'][2]}".casefold())
    with allure.step("Проверка корректных дисциплин"):
        assert (student_registration_form.read_result_modal_student_subjects().casefold() ==
            ", ".join(student['subjects']).casefold())
    with allure.step("Проверка корректного изображения"):
        assert (student_registration_form.read_result_modal_student_picture().casefold() ==
            student["picture"].casefold())
    with allure.step("Проверка корректного адреса"):
        assert (student_registration_form.read_result_modal_student_address().casefold() ==
            student["address"].casefold())
    with allure.step("Проверка корректных штата и города"):
        assert (student_registration_form.read_result_modal_state_and_city().casefold() ==
            f"{student['state']} {student['city']}".casefold())