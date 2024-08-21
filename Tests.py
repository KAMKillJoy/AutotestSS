from PracticeForm import StudentRegistrationFormMethods
import testData.Students as Students
from confest import browser


def test_student_registration_form(browser):
    student_registration_form = StudentRegistrationFormMethods(browser)
    student_registration_form.go_to_site()
    student_registration_form.enter_firstname(Students.StudentVasia["firstname"])
    student_registration_form.enter_lastname(Students.StudentVasia["lastname"])
    student_registration_form.enter_email(Students.StudentVasia["email"])
    student_registration_form.click_gender(Students.StudentVasia["gender"])
    student_registration_form.enter_mobile(Students.StudentVasia["mobile"])
    student_registration_form.enter_date_of_birth(*Students.StudentVasia["dateofbirth"])
    student_registration_form.enter_subjects(Students.StudentVasia["subjects"])
    student_registration_form.upload_picture(Students.StudentVasia["picture"])
    student_registration_form.enter_current_address(Students.StudentVasia["address"])
    student_registration_form.enter_state(Students.StudentVasia["state"])
    student_registration_form.enter_city(Students.StudentVasia["city"])
    student_registration_form.click_submit()
    assert (student_registration_form.read_result_modal_student_name() ==
            f"{Students.StudentVasia["firstname"]} {Students.StudentVasia["lastname"]}")
