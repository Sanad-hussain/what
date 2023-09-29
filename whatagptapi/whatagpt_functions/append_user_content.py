import frappe
from ..whatagpt_functions.get_doctype_record_client_vise import get_doctype_record_client_vise

@frappe.whitelist()
def append_user_content(user_content=None, append_content=None, system_content=None, chat_topic=None):

    if chat_topic == None:
        user_content=str(user_content)+","+str(append_content)
    return user_content


@frappe.whitelist()
def append_language(user_content=None, language=None):
     return append_user_content(user_content, " respond in "+language)

@frappe.whitelist()
def append_title(user_content=None):
     return append_user_content("create title in 5 words for , ", user_content)

@frappe.whitelist()
def append_system_content(user_content=None):
     return append_user_content("Create system content for  ", user_content)