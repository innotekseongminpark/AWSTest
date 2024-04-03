# import requests
#
# url = 'http://<3.141.26.126>:5000/api'  # EC2 인스턴스의 IP 주소로 변경하세요.
# data = {'key1': 'value1', 'key2': 'value2'}  # 전송할 데이터
#
# response = requests.post(url, json=data)
# print(response.json())

# receive_data.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/receive_data", methods=["POST"])
def receive_data():
    data = request.get_json()
    message = data.get("message")
    print("Received message:", message)
    return "Data received successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)  # 외부에서 접근 가능한 포트로 설정