from flask import request
from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from flask_restx import Resource, Namespace

from .auth_serialization_models import create_login_post_model, create_login_get_model, create_refresh_get_model, \
    create_current_user_get_model
from ...controllers import ControllerException, LoginController, LogoutController, RefreshController, \
    CurrentUserController


auth_namespace = Namespace("auth", description="Authentication related operations.")

login_post_model = create_login_post_model(auth_namespace)
login_get_model = create_login_get_model(auth_namespace)
refresh_get_model = create_refresh_get_model(auth_namespace)
current_user_get_model = create_current_user_get_model(auth_namespace)


@auth_namespace.route('/login')
class LoginRouter(Resource):
    """
    This router handles the user login operation.

    It validates the received user credentials and if valid, generates and returns an access token.
    """

    @auth_namespace.expect(login_post_model)
    @auth_namespace.response(401, "Invalid email or password.")
    # @auth_namespace.marshal_with(login_get_model)
    def post(self):
        """
        Validates user credentials and provides a JWT token if valid.

        This method expects user email and password in the request's body.
        If the credentials are valid, it returns a JWT token for the user to authenticate further requests.

        :raises ControllerException: If the user credentials are invalid.

        :return: A dictionary with JWT access and refresh tokens, and the HTTP status code 200.
        """
        login_controller = LoginController(request.get_json())

        try:
            login_controller.validate_user()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return login_controller.create_response()


@auth_namespace.route('/logout')
class LogoutRouter(Resource):
    """
    This router handles the user logout operation.

    It revokes the JWT token associated with the current session.
    """

    @jwt_required()
    def get(self):
        """
        Revokes the current JWT token.

        This method revokes the JWT token associated with the current session, effectively logging out the user.

        :return: A dictionary with a success message and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        logout_controller = LogoutController(get_jwt()["jti"])

        logout_controller.revoke_user_jti()

        return logout_controller.create_response()


@auth_namespace.route('/refresh')
class RefreshRouter(Resource):
    """
    This router handles the token refresh operation.

    It validates the refresh token and if valid, generates a new access token.
    """

    @auth_namespace.marshal_with(refresh_get_model)
    # @jwt_required(refresh=True)
    def get(self):
        """
        Validates the refresh token and provides a new JWT access token if valid.

        This method expects a JWT refresh token. If the token is valid, it returns a new JWT access token.

        :raises ControllerException: If the refresh token is invalid.

        :return: A dictionary with a new JWT access token and the HTTP status code 200.
        :rtype: tuple[dict[str, str], int]
        """
        refresh_controller = RefreshController(request.cookies.get("refresh_token"))

        try:
            refresh_controller.validate_user_refresh_token()

        except ControllerException as e:
            return {"message": e.message}, e.http_code

        return refresh_controller.create_response()


@auth_namespace.route('/current-employee')
class CurrentEmployeeRouter(Resource):
    """
    This router returns the data of the currently authenticated user.
    """

    @auth_namespace.marshal_with(current_user_get_model)
    @jwt_required()
    def get(self):
        """
        Returns the data of the currently authenticated user.

        This method returns the details of the currently authenticated user based on the JWT token.

        :return: A dictionary with the data of the currently authenticated user and the HTTP status code 200.
        :rtype: tuple[dict[str, any], int]
        """
        current_user_controller = CurrentUserController(get_jwt_identity())

        current_user_controller.find_user_by_identity()

        return current_user_controller.create_response()


