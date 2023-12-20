from pages.registration_page import *


def test_add_form():
    registration = RegistrationPage()

    registration.open()

    registration.fill_first_name('Sergei')
    registration.fill_last_name('Chu')
    registration.fill_email('ncrs@example.com')
    registration.choice_gender('Male')
    registration.fill_phone_number(1234567890)
    registration.fill_birthday('October', '1983', '06')
    registration.fill_subjects('English')
    registration.fill_hobbies('Reading')
    registration.picture_upload('bar-h.png')
    registration.fill_address('SPB')
    registration.fill_state('Haryana')
    registration.fill_city('Karnal')
    registration.assert_form(
        'Sergei',
        'Chu',
        'ncrs@example.com',
        'Male',
        '1234567890',
        '06 October,1983',
        'English',
        'Reading',
        'bar-h.png',
        'SPB',
        'Haryana',
        'Karnal'
    )
