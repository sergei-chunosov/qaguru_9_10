from pages.registration_page import RegistrationPage


def test_add_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_form()

    registration_page.assert_form()
