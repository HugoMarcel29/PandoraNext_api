import requests
import json

def get_chat_completion(prompt):

    url = 'http://xxx.xx.xx.xx:8081/<Proxy服务前缀>/v1/chat/completions' #自架设的PandoraNext的服务器地址

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # 转换数据为JSON格式
    json_data = json.dumps(data)

    # 自定义头部信息
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'pk-xxxxxxxxxxxxxxxxxxx',  # 替换为实际的访问令牌，pool tocken或share tocken
        # 可以添加其他需要的头部信息
    }

    # 发送POST请求，包括头部信息
    response = requests.post(url, data=json_data, headers=headers)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        content = json_response['choices'][0]['message']['content']
    else:
        content = f"Failed with status code:{response.status_code}"

    # 返回响应内容
    return content

#调用ChatGPT
prompt = '1+1=?'
content = get_chat_completion(prompt)
print(content)