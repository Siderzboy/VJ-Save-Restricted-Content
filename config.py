import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8076444237:AAHoWtRkNNumPxQi3t_Rnexzf65di-17u3k")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "11010681"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9b99f4d786c80a9190a24c1dad2ecbec")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7173633741"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://akashh:akash@akash.03unr4p.mongodb.net/?retryWrites=true&w=majority&appName=akash") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
