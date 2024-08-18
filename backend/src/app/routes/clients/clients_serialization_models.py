from flask_restx import fields


# Create client post model for the clients' namespace - endpoint gets it during a new client creation.
def create_client_post_model(clients_namespace):
    return clients_namespace.model(
        "ClientPost", {
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "phone": fields.String(),
            "passport_number": fields.String(),
            "address": fields.String(),
            "birth_date": fields.Date()
        }
    )


# Create client get model for the clients' namespace - endpoint returns it to the user after a new client creation.
def create_client_get_model(clients_namespace):
    return clients_namespace.model(
        "ClientGet", {
            "id": fields.Integer(),
            "name": fields.String(),
            "surname": fields.String(),
            "email": fields.String(),
            "phone": fields.String(),
            "passport_number": fields.String(),
            "address": fields.String(),
            "birth_date": fields.Date(),
            "registration_date": fields.Date()
        }
    )


# Create client update model for the clients' namespace - endpoint gets it during a client update.
def create_client_update_model(clients_namespace):
    return clients_namespace.model(
        "ClientUpdate", {
            "new_email": fields.String(required=False),
            "new_phone": fields.String(required=False),
            "new_passport_number": fields.String(required=False),
            "new_address": fields.String(required=False)
        }
    )