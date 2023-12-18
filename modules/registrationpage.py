from selene import browser, have, command
import os.path


class RegistrationPage:

    def open(self):
        browser.open('automation-practice-form')
        browser.all('[id^=google_ads]').with_(timeout=10).wait_until(
            have.size_less_than_or_equal(3)
        )
        browser.all('[id^=google_ads]').perform(command.js.remove)

    def fill_first_name(self, name):
        browser.element('#firstName').type(name)

    def fill_last_name(self, lastname):
        browser.element('#lastName').type(lastname)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choice_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-dropdown-container').click()
        browser.all('.react-datepicker__month-dropdown-container select option').element_by(
            have.exact_text(month)).click()
        browser.element('.react-datepicker__year-dropdown-container').click()
        browser.all('.react-datepicker__year-select option').element_by(
            have.exact_text(year)).click()
        browser.all(f'.react-datepicker__day--0{day}').first.click()

        browser.element('#dateOfBirthInput').should(have.value('06 Oct 1983'))

    def fill_subjects(self, subjects):
        browser.element('#subjectsInput').type('En')
        browser.element('#react-select-2-option-0').should(have.exact_text(subjects)).click()

    def fill_hobbies(self, hobby):
        (browser.all('.custom-checkbox').
         element_by(have.exact_text(hobby)).
         perform(command.js.scroll_into_view).click())

    def picture_upload(self, picture):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'./resources/{picture}'))

    def fill_state(self, state):
        browser.element('#state').click().element('#react-select-3-option-2').should(have.exact_text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click().element('#react-select-4-option-0').should(have.exact_text(city)).click()
        browser.element('#submit').press_enter()

    def assert_form(self, name, lastname, email, gender, phone,
                    birthday, subjects, hobby, picture, address, state, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            ' '.join([name, lastname]),
            email,
            gender,
            phone,
            birthday,
            subjects,
            hobby,
            picture,
            address,
            ' '.join([state, city])))
