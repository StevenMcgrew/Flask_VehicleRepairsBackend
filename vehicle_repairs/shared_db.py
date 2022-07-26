from flask_sqlalchemy import SQLAlchemy

# db is shared amongst all models via imports, and
# is also imported in the __init__.py file for create_app()
db = SQLAlchemy()
