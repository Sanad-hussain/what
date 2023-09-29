import frappe
import os
import requests
from .whatagpt_functions.version_control import version_control
from .whatagpt_functions.append_user_content import *
from .whatagpt_functions.get_previous_response import get_previous_response
from .whatagpt_functions.chatgpt_api_calling import chatgpt_api_calling
from .whatagpt_functions.time_stamp import time_stamp
from .whatagpt_functions.data_service import *
from .whatagpt_subscription import whatagpt_subscription

#userid , user_content, system_role , system_content
@frappe.whitelist()
def get(client_id, user_content, version,chat_topic, language=None):
    # currten date , 
    
    additional_content= ","
    #check version
    check_version=version_control(version)
    if check_version != f"1":
        return check_version  
    
    if language != None:
        additional_content = append_language(additional_content, language)

    if chat_topic == "0":
        previous_content=""
    else:
        previous_content=get_previous_response(client_id,chat_topic)

    gpt_user_content=str(user_content)+str(additional_content)
    # calling chatgpt api to get response
    completion=chatgpt_api_calling(gpt_user_content, previous_content)

    if chat_topic == "0":
        chat_topic=append_title(completion)
        chat_topic=chatgpt_api_calling(chat_topic)
        #system_content=append_system_content(completion)
        #system_content=chatgpt_api_calling(system_content)
        doctype = "Chat Topic"
        payload_request = {
           "topic_name": chat_topic,
            "system_content":"system_content",
            "created_on":time_stamp(),
            "client_id":client_id
        }
        chat_topic=save_data(doctype,payload_request)

    doctype = "Chat History" 
    payload_request = {
        "client_id": client_id,
        "time_stamp": time_stamp(),
        "message_type": "Request",
        "message": user_content,
        "chat_topic": chat_topic
    }
    payload_response = {
        "client_id": client_id,
        "time_stamp": time_stamp(),
        "message_type": "Response",
        "message": completion,
        "chat_topic": chat_topic
    }
    save_chat(doctype, payload_request, payload_response)

    return completion
