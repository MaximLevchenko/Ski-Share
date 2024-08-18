from flask_restx import fields


# Create rental post model for the rentals' namespace - endpoint gets it during a new rental creation.
def create_rental_post_model(rentals_namespace):
    return rentals_namespace.model(
        "RentalPost", {
            "date_end": fields.DateTime(),
            "payment_type": fields.String(),
            "base_price": fields.Integer(),

            "employee_id": fields.Integer(),
            "client_id": fields.Integer(),
            "equipments": fields.List(fields.Integer())
        }
    )


# Create rental get model for the rentals' namespace - endpoint returns it to the user with employee and client data.
def create_rental_get_model(rentals_namespace):
    return rentals_namespace.model(
        "RentalGet", {
            "id": fields.Integer(),
            "date_start": fields.DateTime(),
            "date_end": fields.DateTime(),
            "payment_type": fields.String(),
            "base_price": fields.Integer(),
            "is_closed": fields.Boolean(),
            "damage_fee": fields.Integer(),
            "late_return_fee": fields.Integer(),
            "description": fields.String(),

            "employee_id": fields.Integer(),
            "employee_name": fields.String(),
            "employee_surname": fields.String(),
            "client_id": fields.Integer(),
            "client_name": fields.String(),
            "client_surname": fields.String()
        }
    )


# Create rental full model for the rentals' namespace - endpoint returns it to the user with full rental info.
def create_rental_full_model(rentals_namespace):
    return rentals_namespace.model(
        "RentalFull", {
            "id": fields.Integer(),
            "date_start": fields.DateTime(),
            "date_end": fields.DateTime(),
            "payment_type": fields.String(),
            "base_price": fields.Integer(),
            "is_closed": fields.Boolean(),
            "damage_fee": fields.Integer(),
            "late_return_fee": fields.Integer(),
            "description": fields.String(),

            "employee_id": fields.Integer(),
            "client_id": fields.Integer(),
            "equipments": fields.List(fields.Integer())
        }
    )


# Create rental fees model for the rentals' namespace - endpoint gets it during a rental closing.
def create_rental_fees_model(rentals_namespace):
    return rentals_namespace.model(
        "RentalFees", {
            "new_damage_fee": fields.Integer(required=False),
            "new_late_return_fee": fields.Integer(required=False)
        }
    )


# Create rental fees model for the rentals' namespace - endpoint gets it during a rental description registering.
def create_rental_description_model(rentals_namespace):
    return rentals_namespace.model(
        "RentalDescription", {
            "new_description": fields.String()
        }
    )
