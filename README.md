# Messenger_Automation
"Sending automated messages using messenger chat platform"

This project was written with language "Python" in platform "PyCharm" and with the use of a web automation framework named "Selenium".
In order to run this program, it will be needed the "Selenium" driver for the web browser "Firefox". The aforementioned driver exists in the current repository and is named as "geckodriver.exe".

When this source code runs, the web browser "Firefox" will open and the "Messenger" platform will be appeared in the screen.
Then, the source code will automate fill the user's data and will press the "Log in" button. 
After this, the source code will search in the area of all the messages to find the conversation with the name of a specific account (the one that the user wants).
When the conversation of the give account will be found, the source code will automate write in the text-message area a specific message (the one that the user wants) and then the "Enter" button of messenger will be clicked.

More details:

- In lines 9-11 the user needs to insert his/her credentials.

- In line 39 the user needs to write the name of the contact that he or she wants to send a message.

- In line 50 the user needs to write the message that he or she wants to send. 


Some Notes:

This program works only for the first 21 contacts that exist in the recently messages.
In order to work for a person that exists in the messages further down, the contact area must be scrolled down.

👉 If you need any further information for the current project feel free to contact by sending me an email: **skolix15@gmail.com**

