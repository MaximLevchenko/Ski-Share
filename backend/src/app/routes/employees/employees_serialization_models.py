from flask_restx import fields


# Create employee post model for the employees' namespace - endpoint gets it during a new employee creation.
def create_employee_post_model(employees_namespace):
    return employees_namespace.model(
        "EmployeePost", {
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "password": fields.String(),
            "phone": fields.String(),
            "salary": fields.Integer(),
            "position": fields.String()
        }
    )


# Create employee get model for the employees' namespace - endpoint returns it during get request.
def create_employee_get_model(employees_namespace):
    return employees_namespace.model(
        "EmployeeGet", {
            "id": fields.Integer(),
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "phone": fields.String(),
            "salary": fields.Integer(),
            "position": fields.String()
        }
    )


# Create client update model for the employees' namespace - endpoint gets it during an employee update.
def create_employee_update_model(employees_namespace):
    return employees_namespace.model(
        "EmployeeUpdate", {
            "new_phone": fields.String(required=False),
            "new_salary": fields.Integer(required=False),
            "new_position": fields.String(required=False)
        }
    )


# Create employee profile model for the employees' namespace - endpoint returns it during a get request
# to the employee by id, includes the latest rental ids for own profile.
def create_employee_profile_model(employees_namespace):
    return employees_namespace.model(
        "EmployeeProfile", {
            "id": fields.Integer(),
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "phone": fields.String(),
            "salary": fields.Integer(),
            "position": fields.String(),
            "latest_rentals": fields.List(fields.Integer())
        }
    )