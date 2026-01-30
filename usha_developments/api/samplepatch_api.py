import frappe

@frappe.whitelist(allow_guest=True)
def patch_todo(name, status=None, description=None):
    if not name:
        frappe.throw("Name Required")

    todo = frappe.get_doc("ToDo", name)

    if status is not None:
        todo.status = status

    if description is not None:
        todo.description = description

    todo.save(ignore_permissions=True)

    return {
        "status": "success",
        "todo_id": todo.name,
        "updated_fields": {
            "status": status,
            "description": description
        }
    }