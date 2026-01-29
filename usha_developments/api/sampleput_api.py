import frappe
@frappe.whitelist(allow_guest=True)
def update_todo(name,description):
    if not name:
        frappe.throw("Name is Required")
    
    todo=frappe.get_doc("ToDo", name)
    todo.description=description
    todo.save(ignore_permissions=True)

    return {
        "status":"success",
        "todo_id":todo.name,
        "updated_description":description
    }


"""
Put API Testing URL :
http://localhost:8000/api/method/usha_developments.api.sampleput_api.update_todo


json:
{
  "name": "n3vd8hpqqr",
  "description": "Updated Description using PUT API"
}
"""