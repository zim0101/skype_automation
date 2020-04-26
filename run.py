from automation.automated_group_message import send_automated_group_message
from settings import TARGET_GROUP_ID, EXAMPLE_GROUP_ID


if __name__ == '__main__':
    message = "Hello everyone"
    send_automated_group_message(EXAMPLE_GROUP_ID, message)
    # send_automated_group_message(TARGET_GROUP_ID, message)

