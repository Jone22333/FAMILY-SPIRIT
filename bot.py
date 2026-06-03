# FAMILY-SPIRIT
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
token = 1106898377
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_sessiom)
vk = vk_session.get_api()
def roll_dice():
  """Команда /кубик"""
  return random.randint(1, 6)
  
