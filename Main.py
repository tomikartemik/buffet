import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard
import requests

session = requests.Session()

LOGIN = '+79179321974'
PASSWORD = 'sokolbond007'

vk_session = vk_api.VkApi(LOGIN, PASSWORD)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

# try:
#     vk_session.auth(token_only=True)
# except vk_api.AuthError as error_msg:
#     print(error_msg)

keyboard = VkKeyboard(one_time=False, inline=True)
keyboard.add_callback_button(label="Open URL",
                             payload={"type": "open_link", "link": "https://vk.com/dev/bots_docs_5"})
