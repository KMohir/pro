from aiogram.dispatcher.filters.state import StatesGroup, State
class RegStates(StatesGroup):

    name=State()
    fename=State()
    gender=State()
    nationality=State()
    birth=State()
    phone = State()
    email = State()
    place=State()
    passport_surname = State()
    passport_first_name = State()
    passport_middle_name = State()
    passport_gender = State()
    passport_date_of_birth = State()
    passport_nationality = State()
    passport_phone_number = State()
    edu_university_name = State()
    edu_address_city = State()
    edu_period_from = State()
    edu_period_to = State()
    photo = State()
    passport_copy = State()
    diploma = State()
    additional_documents = State()


    end = State()
    number=State()
    help = State()


class answer(StatesGroup):
    A1 = State()
    A2 = State()

class language(StatesGroup):
    lang = State()

class questions(StatesGroup):
    answer = State()
class RegistrationStates(StatesGroup):

    start=State()
    lang=State()
    name = State()
    phone = State()
    end = State()
    number=State()
    help = State()

