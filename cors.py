
from flask_cors import CORS
from abovl.app import create_app

application = create_app()
cors = CORS(application, allow_headers=('Content-Type', 'Accept', 'Credentials', 'Authorization', 'X-BB-Api-Client-Version'), supports_credentials=True, origins=['http://localhost:8000'])

if __name__ == '__main__':
    application.run('0.0.0.0', port=5000, debug=True)
