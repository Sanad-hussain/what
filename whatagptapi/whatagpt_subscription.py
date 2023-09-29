import frappe
from .whatagpt_functions.data_service import save_data
from .whatagpt_functions.get_doctype_record_client_vise import get_doctype_record_client_vise
from .whatagpt_functions.update_data import update_data

@frappe.whitelist()
def whatagpt_subscription(client_id, subscription):

    check = get_doctype_record_client_vise("Whatagpt Subscription",client_id)
    if check == f"No client exsist":
        payload_request={
            "client_id": client_id,
            "subscription": subscription
        }
        return save_data("Whatagpt Subscription", payload_request)
    
    else:
        params = {
        "Subscription" : subscription
    }
        return update_data("Whatagpt Subscription", "18ef217898", subscription)