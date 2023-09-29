import frappe
from .whatagpt_functions.save_data import save_data

@frappe.whitelist()
def chat_topic():

  doctype = "Chat Topic"
  payload_request = {
      "topic_name": "hello",
      "system_content":"hi",
      "created_on":"now",
      "client_id":"04b36dd7-c5a2-4b05-906d-7f55b30e7902"
    }
  return save_data(doctype,payload_request)