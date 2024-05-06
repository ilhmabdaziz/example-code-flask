from app import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host="192.168.18.37",debug=True)

# flask db init
# flask db migrate
# flask db upgrade
# flask db downgrade
# flask db --help