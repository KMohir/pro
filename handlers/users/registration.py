import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp, Command
from aiogram.types import ReplyKeyboardRemove

from db import db
from keyboards.default.reply import gender, country, skip
from loader import dp, bot
from states.state import RegStates
from translation import _



import os
from fpdf import FPDF
import fitz  # PyMuPDF
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

from db import db
from translation import _


# Define states for registration process

# Start the document upload process
import os
from fpdf import FPDF
import fitz  # PyMuPDF
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

# Initialize bot and dispatcher

# Define states for registration process

# Start the document upload process
import os
from fpdf import FPDF
import fitz  # PyMuPDF
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import MediaGroup

# Initialize bot and dispatcher

import os
from fpdf import FPDF
import fitz  # PyMuPDF
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import MediaGroup

# Initialize bot and dispatcher

# Start the document upload process
@dp.message_handler(Command("registration"))
async def registration(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    text = (_("Ismingizni kiriting", lang))
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await RegStates.name.set()

@dp.message_handler(state=RegStates.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['name'] = name
    text = (_("Familangizni kiriting", lang))
    await message.answer(text)
    await RegStates.fename.set()

@dp.message_handler(state=RegStates.fename)
async def process_fename(message: types.Message, state: FSMContext):
    fename = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['fename'] = fename
    text = (_("Jinsingizni tanlang", lang))
    await message.answer(text, reply_markup=gender())
    await RegStates.gender.set()

@dp.message_handler(state=RegStates.gender)
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['gender'] = gender
    text = (_("Iltimos, millatingizni ko'rsating", lang))
    await message.answer(text, reply_markup=country())
    await RegStates.nationality.set()

@dp.message_handler(state=RegStates.nationality)
async def process_nationality(message: types.Message, state: FSMContext):
    nationality = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['nationality'] = nationality
    text = (_("Iltimos, tug'ilgan kuningizni kiriting (YYYY-MM-DD)", lang))
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await RegStates.birth.set()

@dp.message_handler(state=RegStates.birth)
async def process_birth(message: types.Message, state: FSMContext):
    birth = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['birth'] = birth
    await message.answer(_("Iltimos, telefon raqamingizni kiriting", lang), reply_markup=ReplyKeyboardRemove())
    await RegStates.phone.set()

@dp.message_handler(state=RegStates.phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['phone'] = phone
    text = (_("Emailingizni yozing", lang))
    await message.answer(text, reply_markup=skip())
    await RegStates.email.set()

@dp.message_handler(state=RegStates.email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['email'] = email
    text = (_("Tug'ilgan joyingiz", lang))
    await message.answer(text, reply_markup=country())
    await RegStates.place.set()

@dp.message_handler(state=RegStates.place)
async def process_place(message: types.Message, state: FSMContext):
    place = message.text
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['place'] = place
    text = (_("Pasport ma'lumotlarini kiriting", lang))
    await message.answer(text)
    await message.answer(_("Iltimos, passportda yozilgan familiyangizni kiriting", lang), reply_markup=ReplyKeyboardRemove())
    await RegStates.passport_surname.set()

# Collect surname
@dp.message_handler(state=RegStates.passport_surname)
async def process_passport_surname(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_surname'] = message.text
    await message.answer(_("Iltimos, passportda yozilgan ismingizni kiriting", lang))
    await RegStates.passport_first_name.set()

# Collect first name
@dp.message_handler(state=RegStates.passport_first_name)
async def process_passport_first_name(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_first_name'] = message.text
    await message.answer(_("Iltimos, ikkinchi ismingizni kiriting", lang))
    await RegStates.passport_middle_name.set()

# Collect middle name
@dp.message_handler(state=RegStates.passport_middle_name)
async def process_passport_middle_name(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_middle_name'] = message.text
    await message.answer(_("Jinsingizni tanlang", lang), reply_markup=gender())
    await RegStates.passport_gender.set()

# Collect gender
@dp.message_handler(state=RegStates.passport_gender)
async def process_passport_gender(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_gender'] = message.text
    await message.answer(_("Iltimos, tug'ilgan kuningizni kiriting (YYYY-MM-DD)", lang), reply_markup=ReplyKeyboardRemove())
    await RegStates.passport_date_of_birth.set()

# Collect date of birth
@dp.message_handler(state=RegStates.passport_date_of_birth)
async def process_passport_date_of_birth(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_date_of_birth'] = message.text
    await message.answer(_("Iltimos, millatingizni ko'rsating", lang), reply_markup=country())
    await RegStates.passport_nationality.set()

# Collect nationality
@dp.message_handler(state=RegStates.passport_nationality)
async def process_passport_nationality(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_nationality'] = message.text
    await message.answer(_("Iltimos, telefon raqamingizni kiriting", lang), reply_markup=ReplyKeyboardRemove())
    await RegStates.passport_phone_number.set()

# Collect phone number
@dp.message_handler(state=RegStates.passport_phone_number)
async def process_passport_phone_number(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['passport_phone_number'] = message.text
    await message.answer(_("Iltimos, universitetingiz nomini kiriting", lang))
    await RegStates.edu_university_name.set()

# Collect university name
@dp.message_handler(state=RegStates.edu_university_name)
async def process_edu_university_name(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['edu_university_name'] = message.text
    await message.answer(_("Iltimos, manzilni kiriting (shahar)",lang))
    await RegStates.edu_address_city.set()

@dp.message_handler(state=RegStates.edu_address_city)
async def process_edu_university_name(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['edu_address_city'] = message.text
    await message.answer(_("Iltimos, o'qish davrini (YYYY-MM) bilan belgilang", lang))
    await RegStates.edu_period_from.set()


@dp.message_handler(state=RegStates.edu_period_from)
async def process_edu_period_from(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['edu_period_from'] = message.text
    await message.answer(_("Iltimos, (YYYY-MM) gacha bo'lgan o'quv davrini ko'rsating", lang))
    await RegStates.edu_period_to.set()


@dp.message_handler(state=RegStates.edu_period_to)
async def process_edu_period_to(message: types.Message, state: FSMContext):
    lang = db.get_lang(message.from_user.id)
    async with state.proxy() as data:
        data['edu_period_to'] = message.text
    await message.answer(_("Iltimos, rasmingizni yuklang", lang))
    await RegStates.photo.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=RegStates.photo)
async def handle_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1]  # Get the highest resolution photo
    file_id = photo.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_name = "photo_" + file_id + ".jpg"

    # Define the path where the file will be saved in the script directory
    save_path = os.path.join(os.path.dirname(__file__), file_name)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Download the photo
    await bot.download_file(file_path, save_path)

    async with state.proxy() as data:
        data['photo'] = save_path

    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Surat muvaffaqiyatli yuklandi! Iltimos, pasport nusxasini yuklang", lang))
    await RegStates.passport_copy.set()


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=RegStates.passport_copy)
async def handle_passport_copy(message: types.Message, state: FSMContext):
    document = message.document
    file_id = document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_name = "passport_copy_" + document.file_name

    save_path = os.path.join(os.path.dirname(__file__), file_name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    await bot.download_file(file_path, save_path)

    async with state.proxy() as data:
        data['passport_copy'] = save_path

    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Pasport nusxasi muvaffaqiyatli yuklandi! Iltimos, diplomingizni yuklang", lang))
    await RegStates.diploma.set()


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=RegStates.diploma)
async def handle_diploma(message: types.Message, state: FSMContext):
    document = message.document
    file_id = document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_name = "diploma_" + document.file_name

    save_path = os.path.join(os.path.dirname(__file__), file_name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    await bot.download_file(file_path, save_path)

    async with state.proxy() as data:
        data['diploma'] = save_path

    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Diplom muvaffaqiyatli yuklandi! Iltimos, qo'shimcha hujjatlarni yuklang", lang))
    await RegStates.additional_documents.set()


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=RegStates.additional_documents)
async def handle_additional_documents(message: types.Message, state: FSMContext):
    document = message.document
    file_id = document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_name = "additional_document_" + document.file_name

    save_path = os.path.join(os.path.dirname(__file__), file_name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    await bot.download_file(file_path, save_path)

    async with state.proxy() as data:
        data['additional_documents'] = save_path

    lang = db.get_lang(message.from_user.id)
    await message.answer(_("Qo'shimcha hujjat muvaffaqiyatli yuklandi! Barcha hujjatlar to'plangan", lang))

    await generate_pdf(state, message.from_user.id)
    await state.finish()


async def generate_pdf(state: FSMContext, user_id: int):
    async with state.proxy() as data:
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=12)
        for key, value in data.items():
            if key not in ['photo', 'passport_copy', 'diploma', 'additional_documents']:
                pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

        if 'photo' in data:
            pdf.image(data['photo'], x=10, y=pdf.get_y(), w=100)

        pdf_output_path = os.path.join(os.path.dirname(__file__), f"output_{user_id}.pdf")
        pdf.output(pdf_output_path)

        new_pdf_output_path = os.path.join(os.path.dirname(__file__), f"final_output_{user_id}.pdf")
        pdf_document = fitz.open(pdf_output_path)

        if any(key in ['passport_copy', 'diploma', 'additional_documents'] for key in data):
            for key in ['passport_copy', 'diploma', 'additional_documents']:
                if key in data:
                    other_doc = fitz.open(data[key])
                    pdf_document.insert_pdf(other_doc)
                    other_doc.close()

            pdf_document.save(new_pdf_output_path)
            pdf_document.close()
        else:
            new_pdf_output_path = pdf_output_path

        media = MediaGroup()
        media.attach_document(types.InputFile(new_pdf_output_path), caption="Collected Data")
        for key in ['passport_copy', 'diploma', 'additional_documents']:
            if key in data:
                media.attach_document(types.InputFile(data[key]), caption=key.replace('_', ' ').capitalize())

        await bot.send_media_group(user_id, media)

