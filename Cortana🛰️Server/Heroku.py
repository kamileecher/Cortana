#|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
#|🛸|      (𝐜)𝐂𝐨𝐫𝐭𝐚𝐧𝐚𝐀𝐈 | 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!       |`;
#|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
import math
import heroku3
import requests
from os import getenv
HEROKU = getenv("HEROKU")
herokuHttp = "https://api.heroku.com"
HEROKU_APP_NAME  =   str(getenv("HEROKU_APP_NAME"))  
HEROKU_API_KEY   =   str(getenv("HEROKU_API_KEY"))  
HERO = heroku3.from_key(HEROKU_API_KEY)
#|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
#|🛸|      (𝐜)𝐂𝐨𝐫𝐭𝐚𝐧𝐚𝐀𝐈 | 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!       |`;
#|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
try:
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = HERO.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(herokuHttp + path, headers=headers)
    if r.status_code != 200:
        print("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")
        text_file = open("./ʍɨʐʊӄɨ🗑️ȶɛʍք/𝐇𝐞𝐫𝐨𝐤𝐮.txt", "w")
        text_file.write("Try Again Later")
        text_file.close()
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    #|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
    #|🛸|      (𝐜)𝐂𝐨𝐫𝐭𝐚𝐧𝐚𝐀𝐈 | 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!       |`;
    #|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    #|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
    #|🛸|      (𝐜)𝐂𝐨𝐫𝐭𝐚𝐧𝐚𝐀𝐈 | 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!       |`;
    #|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    text_file = open("./ʍɨʐʊӄɨ🗑️ȶɛʍք/𝐇𝐞𝐫𝐨𝐤𝐮.txt", "w")
    text_file.write(
    f"""
╔═══════◇🌿𝐓𝐨𝐩𝐢𝐜: Heroku_Usage
║🛸 𝐀𝐩𝐩 𝐍𝐚𝐦𝐞: _{HEROKU_APP_NAME}_
║💀 𝐃𝐲𝐧𝐨 𝐔𝐬𝐞𝐝: _{AppHours}ʜᴏᴜʀꜱ {AppMinutes}ᴍɪɴꜱ_ = *{AppPercentage}%*
║⏰ 𝐃𝐲𝐧𝐨 𝐑𝐞𝐦𝐚𝐢𝐧𝐢𝐧𝐠: _{hours}ʜᴏᴜʀꜱ {minutes}ᴍɪɴꜱ_ = *{percentage}%*
╚════════════╝"""
    )
    text_file.close()
except Exception as e:
    text_file = open("./ʍɨʐʊӄɨ🗑️ȶɛʍք/𝐇𝐞𝐫𝐨𝐤𝐮.txt", "w")
    text_file.write("Try Again Later")
    text_file.close()
#|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;
#|🛸|      (𝐜)𝐂𝐨𝐫𝐭𝐚𝐧𝐚𝐀𝐈 | 𝐢𝐬 𝐚 𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐌𝐮𝐥𝐭𝐢𝐏𝐮𝐫𝐩𝐨𝐬𝐞-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐌𝐨𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧,𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝟏𝟎𝟎+ 𝐦𝐨𝐫𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬!       |`;
#|🛸|======================================================================================================⬡  𝐊𝐫𝐚𝐤𝐢𝐧𝐳𝐋𝐚𝐛™`;