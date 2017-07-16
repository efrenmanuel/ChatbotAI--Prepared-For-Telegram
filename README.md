# ChatbotAI-Telegram

This is a learning AI project made in 5 hours and adapted for telegram (and, after a lot of struggling, unicode).


## Prerequisites

	Python 3.6.1
	numpy module
	
### How to use it

The file AI is the main part of the project, where the magic occurs, it may be imported ( "import AI") in order to use the AI.

It works with two basic functions:

talk(inp, estatus):

	this returns a number output that is the index of the reply chosen in the answ.json file.
	(in the future it may have support for multiple answer storing files).
	
	Variables:
		inp: the text it may reply to.
		estatus: the json file it may search the keys into. (you dont have to put .json) the default file is p1.

Learn(inp, chat, estatus, *args):

It stores the new data in "[estatus].json" (estatus is made so you can have multiple key storing files) and "answ.json" files 
	
	Variables:
		inp: the newest message
		chat: the chat/session name so it can follow a conversation while receiving inputs not fromt the same chat.
		estatus: the json file it may store the keys into. (you dont have to put .json) the default file is p1.
		args: its just in case you want to overwrite the message its replying to. Its optional.
	
The telegram bot file is "chatbot telegram - ntk.py" where you have to write your token and your bot name.

## Author
* **Efrén González** - *Main author*