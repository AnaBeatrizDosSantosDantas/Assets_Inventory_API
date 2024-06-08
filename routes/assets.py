from flask import Blueprint, request, jsonify
from create_app import mongo
from bson import ObjectId

assets_bp = Blueprint('assets', __name__)

def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])
    return doc

@assets_bp.route('/<asset_type>/<cpf>', methods=['POST'])
def create_asset(asset_type, cpf):
    data = request.get_json()
    employee = mongo.db.employees.find_one({"cpf": cpf})
    if not employee:
        return jsonify({"message": "Employee not found!"}), 404
    data['asset_type'] = asset_type
    data['employee_cpf'] = cpf
    mongo.db.assets.insert_one(data)
    return jsonify({"message": f"{asset_type} created successfully!"}), 201

@assets_bp.route('/<asset_type>/<cpf>', methods=['PUT'])
def update_asset(asset_type, cpf):
    data = request.get_json()
    result = mongo.db.assets.update_one({"employee_cpf": cpf, "asset_type": asset_type}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"message": f"No {asset_type} found for this employee!"}), 404
    return jsonify({"message": f"{asset_type} updated successfully!"}), 200

@assets_bp.route('/<asset_type>/<cpf>', methods=['DELETE'])
def clear_asset(asset_type, cpf):
    result = mongo.db.assets.delete_one({"employee_cpf": cpf, "asset_type": asset_type})
    if result.deleted_count == 0:
        return jsonify({"message": f"No {asset_type} found for this employee!"}), 404
    return jsonify({"message": f"{asset_type} cleared successfully!"}), 200

@assets_bp.route('/', methods=['GET'])
def get_all_assets():
    assets = list(mongo.db.assets.find())
    assets = [serialize_doc(asset) for asset in assets]
    return jsonify(assets), 200

@assets_bp.route('/<asset_type>/<cpf>', methods=['GET'])
def get_asset_by_employee(asset_type, cpf):
    asset = mongo.db.assets.find_one({"employee_cpf": cpf, "asset_type": asset_type})
    if not asset:
        return jsonify({"message": f"No {asset_type} found for this employee!"}), 404
    return jsonify(serialize_doc(asset)), 200
