import uuid
import requests
import json

def pandora(prompt,parent_message_id,conversation_id):
    message_id = str(uuid.uuid4())
    data = {
            "model": "gpt-3.5-turbo",
            "action": "next",
            "parent_message_id": parent_message_id,
            #"conversation_id": conversation_id,
            "messages": [
                {
                    "content": {
                        "content_type": "text",
                        "parts": [prompt]
                    },

                    "id": message_id,
                    "role": "user"
                }
            ]
        }
    if conversation_id:
        data['conversation_id'] = conversation_id
    elif 'conversation_id' in data:
        del data['conversation_id']



    # 将数据转换为 JSON 格式
    json_data = json.dumps(data)

    # 填入你的 API 密钥
    api_key = "xxxxxxxxxxxxxxxxxxxxx"   #access tocken或session tocken

    # 设置 API 终点
    url = "http://xxxx:8081/<Proxy服务前缀>/backend-api/conversation"

    # 设置请求头
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }



    response = requests.post(url, data=json_data, headers=headers)
    data_stream = str(response.text)

    # Split the data stream by lines
    data_list = data_stream.strip().split('\n\n')

    # Initialize variable to store the last parts generated by ChatGPT
    last_parts = None

    # Iterate through the data in reverse to find the last parts generated
    for data in reversed(data_list):
        # Extract 'parts' section from the 'content' field
        try:
            json_data = json.loads(data.split(': ', 1)[1])
            new_msgid = json_data['message']['id']
            new_conversationid = json_data['conversation_id']
            parts = json_data['message']['content']['parts']
            last_parts = parts[-1] if parts else None
            if last_parts:
                break  # Stop iteration if last parts are found
        except (json.JSONDecodeError, KeyError):
            continue

    # Output the last parts generated by ChatGPT
    return (last_parts,new_msgid,new_conversationid)


prompt = '1+1=?'
parent_message_id = ""  #指定父消息编号
conversation_id = ""    #指定会话编号


coordinates = pandora(prompt,parent_message_id,conversation_id)
last_parts,new_msgid,new_conversationid = coordinates
print("last_parts:", last_parts)
print("new_msgid:", new_msgid)
print("new_conversationid:", new_conversationid)