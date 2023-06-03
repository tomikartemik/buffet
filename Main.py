import asyncio
from vkbottle import API
from vkbottle.bot import Bot, Message

TOKEN = 'vk1.a.QaAOGk5zvMqtcWTiA5V2_QHI8JtmIi3q5ZIFUknAgIDETz1i-tAXNAmhH4d4uOWkcEx8wn6mjF6875E1QfV22WREf0360PEKUIwtRIMubuxY491y9Ub-9_skdrIMPG9TGjjzd66hgb8YOlAZgkVVtdGhPmYHsCUojm8F4PfxuHUM2uC8kSKSUUVIOy3SWQhzL7tEF4I6_il94IQ9gxlyAg'


bot = Bot(token=TOKEN)

@bot.on.message(text="Привет")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))

bot.run_forever()
