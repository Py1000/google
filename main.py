import time
from datetime import datetime
from telethon import events,TelegramClient

api_id="7993265"
api_hash="d5840e8f57453989ff991acb325f56bd"

bot = TelegramClient("session", api_id , api_hash).start(bot_token="1911791658:AAHeU1vPNJPhfKTWfkD1s22bdsatp03YYq0")
print("Bot online")

@bot.on(events.NewMessage(pattern="/active"))
async def active(event):
	print("Command used : start")
	await event.reply("Hello sir/mam")
	await event.reply("Bot activation done!!!")

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
	id = event.chat_id
	print(id,"messaged bot")
	print("Command used : start")
	await event.reply("Starting bot....")
	time.sleep(2)
	await event.reply("Bot started!!!")
	user_id=replied_user.user.id
	await event.reply(user_id)
	
@bot.on(events.NewMessage(pattern="/ping"))
async def ping(event):
	print("Command used : ping")
	await event.reply("Calculating ping...")
	await event.reply("Unexpected error occured")
	time.sleep(2)
	await event.reply("`Stabalizing bot...`")
	time.sleep(5)
	await event.reply("`Stabalizaed succsefully!!!`")
	await event.reply("Bot online")

@bot.on(events.NewMessage(pattern="\/google"))
async def google(event):
	print("Command used : google")
	id = event.chat_id
	command = event.message.raw_text.split(" ")
	search = command[1]
	url = "https://www.google.com/search?ie=UTF-8&client=mobile-android-vivo-nf-rev1&source=android-browser&q={}".format(search)
	here = "Here"
	result = "Click [{}]({}) to see result".format(here , url)
	await event.reply(result)
	print(id ,"searched for",search)
@bot.on(events.NewMessage(pattern="/for",incoming = True))
async def database(event):
	entity = "-498237028"
	fwd = await bot.forward_messages(entity,event.message)
	print("Command used : for")
		
def main():
	bot.run_until_disconnected()

if __name__=="__main__":
	main()