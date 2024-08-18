from flask_restx import fields


# Create equipment post model for the equipments' namespace - endpoint gets it during a new equipment creation.
def create_equipment_post_model(equipments_namespace):
    return equipments_namespace.model(
        "EquipmentPost", {
            "category": fields.String(),
            "manufacturer": fields.String(),
            "model": fields.String(),
            "size": fields.String(),
            "price_per_hour": fields.Integer(),
            "description": fields.String()
        }
    )


# Create client get model for the equipments' namespace - endpoint returns it to the user after
# a new equipment creation.
def create_equipment_get_model(equipments_namespace):
    return equipments_namespace.model(
        "EquipmentGet", {
            "inventory_number": fields.Integer(),
            "category": fields.String(),
            "manufacturer": fields.String(),
            "model": fields.String(),
            "size": fields.String(),
            "price_per_hour": fields.Integer(),
            "description": fields.String(),
            "registration_date": fields.Date(),
            "status": fields.String()
        }
    )


# Create equipment update model for the equipments' namespace - endpoint gets it during a equipment update.
def create_equipment_update_model(equipments_namespace):
    return equipments_namespace.model(
        "EquipmentUpdate", {
            "new_price_per_hour": fields.Integer(required=False),
            "new_description": fields.String(required=False),
        }
    )
