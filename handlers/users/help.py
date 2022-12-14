from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from utils.pic_for_help import get_info_pic
from loader import dp
from keyboards.inline import my_channel

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer_photo(photo=get_info_pic(), caption="Инлайн бот для поиска видео из YouTube. Также бот способен скачивать видео оттуда если отправить ему ссылку. Но видео скачается если оно небольшого размера.\n\nСоздатель: @frogy_cat\nБлагодарю за использование моего бота!)", reply_markup=my_channel.Channel)
