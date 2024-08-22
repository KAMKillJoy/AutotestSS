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

    assert student_registration_form.check_modal_result()
    assert (student_registration_form.read_result_modal_student_name().casefold() ==
            f"{Students.StudentVasia["firstname"]} {Students.StudentVasia["lastname"]}".casefold())
    assert (student_registration_form.read_result_modal_student_email().casefold() ==
            Students.StudentVasia["email"].casefold())
    assert (student_registration_form.read_result_modal_student_gender().casefold() ==
            Students.StudentVasia["gender"].casefold())
    assert (student_registration_form.read_result_modal_student_mobile().casefold() ==
            Students.StudentVasia["mobile"].casefold())
    assert (student_registration_form.read_result_modal_student_date_of_birth().casefold() ==
            f"{Students.StudentVasia['dateofbirth'][0]} {Students.StudentVasia['dateofbirth'][1]},"
            f"{Students.StudentVasia['dateofbirth'][2]}".casefold())
    assert (student_registration_form.read_result_modal_student_subjects().casefold() ==
            ", ".join(Students.StudentVasia['subjects']).casefold())
    assert (student_registration_form.read_result_modal_student_picture().casefold() ==
            Students.StudentVasia["picture"].casefold())
    assert (student_registration_form.read_result_modal_student_address().casefold() ==
            Students.StudentVasia["address"].casefold())
    assert (student_registration_form.read_result_modal_state_and_city().casefold() ==
            f"{Students.StudentVasia['state']} {Students.StudentVasia['city']}".casefold())