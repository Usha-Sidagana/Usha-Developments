import frappe

@frappe.whitelist(allow_guest=True)
def create_todo(description=None):
    if not description:
        frappe.throw("Description is required")

    todo = frappe.get_doc({
        "doctype": "ToDo",
        "description": description
    })
    todo.insert(ignore_permissions=True)

    return {
        "status": "success",
        "todo_id": todo.name,
        "description": description
    }


"""
Post API Testing URL :
    http://localhost:8000/api/method/usha_developments.api.samplepost_api.create_todo


Body Json:
{
	"description": "Learning"
}

"""