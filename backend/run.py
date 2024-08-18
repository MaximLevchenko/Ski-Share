from src.app.main import create_app
from src.configurations import DevConfig

# Create a Flask application instance using the development configuration.
app = create_app(DevConfig)


if __name__ == '__main__':
    """
    Entry point of the application when run as a script. 

    The Flask development server is run if the script is executed directly.
    """
    # Run the application.
    app.run()
