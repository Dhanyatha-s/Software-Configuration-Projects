from flask import Blueprint, request, jsonify
from rules_engine import apply_rules

api_blueprint = Blueprint('api',__name__)

@api_blueprint.route('/apply_rules', methods=['POST'])
def apply_rules_route():
    data = request.get_json()
    config = data.get('config')
    employee = data.get("employee")

    if not config or not employee:
        return jsonify({"error":"Missing 'config' or 'employee'"}), 400
    
    updated = apply_rules(config, employee)
    return jsonify(updated), 200
