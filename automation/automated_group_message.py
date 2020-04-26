from skpy import Skype
from settings import SKYPE_USERNAME, SKYPE_PASSWORD


# Initiate skype object with username/email/phone_number and password
# Keep your username and password in .env
# I will recommend you to keep them encrypted
skype_object = Skype(SKYPE_USERNAME, SKYPE_PASSWORD)


def recent_chat_info():
    """
    Send a message to your target group from your skype account.
    Then run this function to see recent chat. where you will get something at
    the beginning like:

    19:********************************@thread.skype

    This is your targeted group
    Save this id in your .env file's TARGET_GROUP variable
    """
    recent_chats = skype_object.chats.recent()
    print(recent_chats)


def send_automated_group_message(channel_id: str, message: str):
    """
    Send message to targeted group using the decoded channel id

    :param message: str
    :param channel_id: str
    :return:
    """
    try:
        channel = skype_object.chats.chat(channel_id)
        channel.sendMsg(message)
    except Exception as e:
        print(e)

