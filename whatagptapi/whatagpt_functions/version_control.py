import frappe

@frappe.whitelist()
def version_control(version, doctype=None, client_id=None):
    if float(version) > 1.0:
        return f"1"
    else:
        return f"1002"