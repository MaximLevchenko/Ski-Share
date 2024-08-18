from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, Namespace

from .equipments_serialization_models import create_equipment_post_model, create_equipment_get_model, \
    create_equipment_update_model
from ...controllers import ControllerException, EquipmentsController, EquipmentsSortController, EquipmentController


equipments_namespace = Namespace("equipments", description="Equipments related operations.")

equipment_post_model = create_equipment_post_model(equipments_namespace)
equipment_get_model = create_equipment_get_model(equipments_namespace)
equipment_update_model = create_equipment_update_model(equipments_namespace)


@equipments_namespace.route('/')
class EquipmentsRouter(Resource):
    """
    Router for handling operations related to equipment.

    Provides handlers for HTTP GET and POST requests made to the '/equipments' endpoint.
    """

    @equipments_namespace.marshal_list_with(equipment_get_model)
    @jwt_required()
    def get(self):
        """
        Retrieves a list of all equipment.

        This endpoint requires authentication (JWT token).

        :return: A list of all equipment along with HTTP status code 200.
        :rtype: tuple[list[dict[str, Any]], int]
        """
        equipments_controller = EquipmentsController()

        return equipments_controller.create_response_with_equipments_data()

    @equipments_namespace.expect(equipment_post_model)
    @equipments_namespace.response(400, "Invalid equipment data.")
    @jwt_required()
    def post(self):
        """
        Creates a new equipment entry.

        This endpoint requires authentication (JWT token) and the equipment data as JSON in the request body.

        The equipment data should match the structure of the `equipment_post_model`.

        :raises ControllerException: If the provided data is invalid.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, Any], int]
        """
        equipments_controller = EquipmentsController(request.get_json())

        try:
            equipments_controller.create_equipment()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return equipments_controller.create_response_with_successful_create_message()


@equipments_namespace.route('/sort')
class EquipmentsSortRouter(Resource):
    """
    Router for handling operations related to sorting equipment.

    Provides a handler for HTTP GET requests made to the '/equipments/sort' endpoint.
    """

    @equipments_namespace.response(400, "Invalid sort QUERY parameters.")
    @equipments_namespace.marshal_list_with(equipment_get_model)
    @jwt_required()
    def get(self):
        """
        Fetches a list of equipment sorted based on given QUERY parameters.

        This method requires a JWT token. It creates an `EquipmentsSortController` instance and attempts to sort the
        equipment using the provided QUERY parameters. If sorting is successful, it returns a response containing the
        sorted equipment data.

        :return: A response object containing sorted equipment data or an error message if an error occurs.
        :rtype: tuple[list[dict[str, Any]], int]

        :raises ControllerException: If an error occurs while sorting the equipment.
        """
        equipments_sort_controller = EquipmentsSortController(request.args.to_dict())

        try:
            equipments_sort_controller.sort_equipments()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return equipments_sort_controller.create_response_with_sorted_equipments_data()


@equipments_namespace.route('/equipment/<int:inventory_number>')
class EquipmentRouter(Resource):
    """
    Router for handling operations related to a specific piece of equipment.

    Provides handlers for HTTP GET, PUT, and DELETE requests made to the '/equipments/equipment/{inventory_number}'
    endpoint, where `{inventory_number}` is the inventory number of the specific equipment.
    """

    @equipments_namespace.response(404, "Equipment not found.")
    @equipments_namespace.marshal_with(equipment_get_model)
    @jwt_required()
    def get(self, inventory_number):
        """
        Fetches the data for a specific piece of equipment.

        This method requires a JWT token. It creates an `EquipmentController` instance, validates the equipment,
        and if the equipment is valid, it returns a response containing the equipment data.

        :param inventory_number: The inventory number of the specific piece of equipment.
        :type inventory_number: int

        :return: A response object containing the equipment data or an error message if an error occurs.
        :rtype: tuple[dict[str, Any], int]

        :raises ControllerException: If an error occurs while fetching or validating the equipment data.
        """
        equipment_controller = EquipmentController(inventory_number)

        try:
            equipment_controller.validate_equipment()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return equipment_controller.create_response_with_equipment_data()

    @equipments_namespace.expect(equipment_update_model)
    @equipments_namespace.response(400, "Invalid equipment update data.")
    @equipments_namespace.response(404, "Equipment not found.")
    @jwt_required()
    def put(self, inventory_number):
        """
        Updates the data for a specific piece of equipment.

        This method requires a JWT token. It creates an `EquipmentController` instance, validates the equipment,
        and if the equipment is valid, it updates the equipment data.

        :param inventory_number: The inventory number of the specific piece of equipment.
        :type inventory_number: int

        :return: A response object containing a success message or an error message if an error occurs.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If an error occurs while updating or validating the equipment data.
        """
        equipment_controller = EquipmentController(inventory_number, request.get_json())

        try:
            equipment_controller.validate_equipment()
            equipment_controller.update_equipment()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return equipment_controller.create_response_with_successful_update_message()

    @equipments_namespace.response(201, "Equipment deleted successfully.")
    @equipments_namespace.response(404, "Equipment not found.")
    @jwt_required()
    def delete(self, inventory_number):
        """
        Deletes a specific piece of equipment.

        This method requires a JWT token. It creates an `EquipmentController` instance, validates the equipment,
        and if the equipment is valid, it deletes the equipment.

        :param inventory_number: The inventory number of the specific piece of equipment.
        :type inventory_number: int

        :return: A response object containing a success message or an error message if an error occurs.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If an error occurs while deleting or validating the equipment.
        """
        equipment_controller = EquipmentController(inventory_number)

        try:
            equipment_controller.validate_equipment()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        equipment_controller.delete_equipment()

        return equipment_controller.create_response_with_successful_delete_message()


@equipments_namespace.route('/equipment/<int:inventory_number>/damaged')
class EquipmentDamagedRouter(Resource):
    """
    Router for handling operations related to a specific piece of equipment that has been marked as damaged.

    Provides a handler for HTTP GET requests made to the '/equipments/equipment/{inventory_number}/damaged'
    endpoint, where `{inventory_number}` is the inventory number of the specific piece of equipment.
    """

    @equipments_namespace.response(201, "Equipment updated successfully.")
    @equipments_namespace.response(404, "Equipment not found.")
    @jwt_required()
    def get(self, inventory_number):
        """
        Marks a specific piece of equipment as damaged.

        This method requires a JWT token. It creates an `EquipmentController` instance, validates the equipment,
        and if the equipment is valid, it updates the status of the equipment as damaged.

        :param inventory_number: The inventory number of the specific piece of equipment.
        :type inventory_number: int

        :return: A response object containing a success message or an error message if an error occurs.
        :rtype: tuple[dict[str, str], int]

        :raises ControllerException: If an error occurs while updating the equipment status or validating the equipment.
        """
        equipment_controller = EquipmentController(inventory_number)

        try:
            equipment_controller.validate_equipment()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        equipment_controller.update_equipment_status_as_damaged()

        return equipment_controller.create_response_with_successful_update_message()
