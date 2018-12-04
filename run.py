from utils.create_app.create import app
from app.router.router import Base


if __name__ == '__main__':
    Base.register(app)
    app.run(host='0.0.0.0', port=5000)
