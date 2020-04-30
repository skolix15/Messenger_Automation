# Messenger_Automation
Sending automated messages using messenger chat platform

This project was written with language "Python" in platform "PyCharm" and with the use of a web automation framework named "Selenium".
In order to run this program, it will be needed the "Selenium" driver for the web browser "Firefox". The driver exists in the file "geckodriver.exe".

When this source code runs, the web browser "Firefox" will open and the "Messenger" platform will be appeared in the screen.
Then, the source code will automate fill the user's data and will press the "Log in" button. 
After this, the source code will search in the area of all the messages to find the conversation with the name of a specific user.
When the conversation been found, the source code will automate write in the text-message area a specific message and then the "Enter" button of messenger will be clicked.

More details:

In lines 5-6 the user of this source code will add the path of the driver (geckodriver.exe)

In lines 9-11 the user of this source code will add the email and the password of his/her account.

In line 39 the user of this source code will write the name of the contact that he or she wants to send a message.

In line 50 the user of this source code will write the whole message that he or she wants to send. 


Some Notes:

This program works only for the first 21 contacts that exist in the recently messages.
In order to work for a person that exists in the messages further down, the contact area must be scrolled.

