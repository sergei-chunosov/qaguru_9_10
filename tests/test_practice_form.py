from modules.registrationpage import RegistrationPage


def test_add_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Sergei')
    registration_page.fill_last_name('Chu')
    registration_page.fill_email('ncrs@example.com')
    registration_page.choice_gender('Male')
    registration_page.fill_phone_number(1234567890)
    registration_page.fill_birthday('October', '1983', '06')
    registration_page.fill_subjects('English')
    registration_page.fill_hobbies('Reading')
    registration_page.picture_upload('bar-h.png')
    registration_page.fill_address('SPB')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')
    registration_page.assert_form(
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
