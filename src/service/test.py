import requests
import json

# 设置 API URL 和 API 密钥
url = "https://api2.aigcbest.top/v1/chat/completions"
api_key = "sk-igzJkocZvGiw0AfnQT3zyrjOCLDC6FfCkbTPd274UDcJiCRO"  # 替换为你的实际 API 密钥

# 设置请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# 设置请求体
data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "詹梓聪是谁？"}],
    "temperature": 0.7,
    "max_tokens": 2048,  # 设置最大 tokens 数量，可以根据需要调整
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查响应状态
if response.status_code == 200:
    # 打印响应内容
    print(response.json()['choices'][0]['message']['content'])
else:
    print("Error:", response.status_code, response.text)
