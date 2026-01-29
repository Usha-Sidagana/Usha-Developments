import frappe

@frappe.whitelist(allow_guest=True)
def hello_api(name="API"):
    return{
        "status":"success",
        "message":f"Hello {name or 'World'}"
    }


"""
GET API URL for Testing : http://localhost:8000/api/method/usha_developments.api.sample_api.hello_api
"""