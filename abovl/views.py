
from flask import current_app, request, Blueprint, jsonify
import json

bp = Blueprint('abovl', __name__)



@bp.route('/token', methods=['GET'])
def token(date=None):
    """Will either create a new OAuth token
            - subordinate to the API_TOKEN
       Or retrieve stored token
           - based on a cookie
    """

    resp = current_app.make_response(staus=200, mimetype='application/json')
    
    token = request.cookies.get('token')
    
    # verify it was created by us
    t = current_app.load_client(token)
    
    # if not, obtain a new token
    if t is not None:
        t = current_app.create_client()
        current_app.logger.info('Create a new OAuth Client/Token: {}', t)
    
    resp.response = json.dumps(t)
    resp.set_cookie('token', token)
    return resp        

