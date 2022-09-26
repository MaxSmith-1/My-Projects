import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

count = 0

session = vk_api.VkApi(token="4e224d5ac7d0c48f910eff3d639486a3da8c2e31c956c256086f61e351882a213b7af9912b74afbf3eef1")

def send_message(user_id, message):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    })


for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text =="hello":
            send_message(user_id, "Awlright")
            count += 1
            print(str(count))