from flask import Blueprint, request, jsonify, make_response, current_app
from flask_cors import CORS

collector_routes = Blueprint('collector_routes', __name__)
CORS(collector_routes)


@collector_routes.route('/historical', methods=['GET'])
def get_historical():
    pass


@collector_routes.route('/latest-listings', methods=['GET'])
def get_latest_listings():
    coin_market_cap_service = current_app.coin_market_cap_service
    start = request.args.get('start')
    limit = request.args.get('limit')
    convert = request.args.get('convert')

    if not start or not limit or not convert:
        return jsonify({'error': 'Invalid request'}), 400

    response_data = coin_market_cap_service.get_latest_listings(start, limit, convert)

    return jsonify(response_data), 200
