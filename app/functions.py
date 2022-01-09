from riotwatcher import LolWatcher, ApiError
from dotenv import load_dotenv, dotenv_values

ENVVALUES = dotenv_values('.env')
REGION = ENVVALUES['REGION']
APIKEY = ENVVALUES['RIOT_API']

lolWatcher = LolWatcher(APIKEY)
summoner = lolWatcher.summoner.by_name(REGION,"pathrix")
def getId(summonerName):
    return summoner['id']