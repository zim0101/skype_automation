# skype_automation

```
Project Tree:
--------------------------------------------------------------------------------
.
├── automation
│   ├── automated_group_message.py
│   ├── __init__.py
│   └── utils.py
├── README.md
├── requirements.txt
├── run.py
└── settings.py
└── .env


```
```
Steps to install

1. lets make a new directory somewhere in your computer. You know, just to make 
things clean. Run:

$ mkdir skype_automation && cd skype_automation

2. Assure you have python3, pip and venv. There is tons of resource to install 
those. Go get your tigers

3. now run this command bellow to make a virtualenv for your project.

$ python3 -m venv skype_automation_env

4. Activate your venv

$ . skype_automation_env/bin/activate

5. Lets get into our venv 
 
$ cd skype_automation_env

6. Clone the repo and Install all dependencies from our requirements.txt file

$ pip3 install -r requirements.txt

7. create .env file and set this variables:
SECRET_KEY=
SKYPE_USERNAME=
SKYPE_PASSWORD=

EXAMPLE_GROUP=
TARGET_GROUP=

# these are the group channel id which you can find by these steps:
a) send a message to the group 
b) run recent_chat_info() method's code to get the recent skype group id.


And, please, encrypt these variable's value from your python console using jwt, except 
the SECRET_KEY

8. Run run.py with this command:
python3 run.py

Enjoy your automated life now!!!