from flask_restx import fields


# Create login post model for the authentication namespace - endpoint gets it during employee authentication.
def create_login_post_model(auth_namespace):
    return auth_namespace.model(
        "LoginPost", {
            "email": fields.String(),
            "password": fields.String()
        })


# Create login get model for the authentication namespace - endpoint returns it after successful authentication.
def create_login_get_model(auth_namespace):
    return auth_namespace.model(
        "LoginGet", {
            "id": fields.Integer(),
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "phone": fields.String(),
            "salary": fields.Integer(),
            "position": fields.String(),
            "latest_rentals": fields.List(fields.Integer()),

            "access_token": fields.String(),
            "refresh_token": fields.String()
        }
    )


# Create refresh get model for the authentication namespace - endpoint returns it after /refresh request.
def create_refresh_get_model(auth_namespace):
    return auth_namespace.model(
        "RefreshGet", {
            "access_token": fields.String()
        }
    )


# Create current employee get model for the authentication namespace
# - endpoint returns it after /current_employee request.
def create_current_user_get_model(auth_namespace):
    return auth_namespace.model(
        "CurrentEmployeeGet", {
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
