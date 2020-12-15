import json
import instabot

config = json.load(open("data/config.json"))

bot = instabot.Bot()
bot.login(username=config["username"], password=config["password"])

bot.upload_photo(config["image_path"], config["description"])
print("###### done ######")
