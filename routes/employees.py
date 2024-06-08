from flask import Blueprint, request, jsonify
from create_app import mongo
from bson import ObjectId

employees_bp = Blueprint('employees', __name__)

def serialize_doc(doc):
    """Converte o ObjectId para string em documentos MongoDB"""
    doc['_id'] = str(doc['_id'])
    return doc

@employees_bp.route('/', methods=['POST'])
def add_employee():
    data = request.get_json()
    if mongo.db.employees.find_one({"cpf": data['cpf']}):
        return jsonify({"message": "Employee already exists!"}), 400
    mongo.db.employees.insert_one(data)
    return jsonify({"message": "Employee added successfully!"}), 201

@employees_bp.route('/<cpf>', methods=['DELETE'])
def delete_employee(cpf):
    employee = mongo.db.employees.find_one({"cpf": cpf})
    if not employee:
        return jsonify({"message": "Employee not found!"}), 404
    if mongo.db.assets.find_one({"employee_cpf": cpf}):
        return jsonify({"message": "Cannot delete employee with assigned assets!"}), 400
    mongo.db.employees.delete_one({"cpf": cpf})
    return jsonify({"message": "Employee deleted successfully!"}), 200

@employees_bp.route('/', methods=['GET'])
def get_employees():
    employees = list(mongo.db.employees.find())
    employees = [serialize_doc(employee) for employee in employees]
    return jsonify(employees), 200

@employees_bp.route('/<cpf>', methods=['GET'])
def get_employee_inventory(cpf):
    employee = mongo.db.employees.find_one({"cpf": cpf})
    if not employee:
        return jsonify({"message": "Employee not found!"}), 404
    assets = list(mongo.db.assets.find({"employee_cpf": cpf}))
    employee['assets'] = [serialize_doc(asset) for asset in assets]
    return jsonify(serialize_doc(employee)), 200

@employees_bp.route('/<cpf>', methods=['PUT'])
def update_employee(cpf):
    data = request.get_json()
    result = mongo.db.employees.update_one({"cpf": cpf}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"message": "Employee not found!"}), 404
    return jsonify({"message": "Employee updated successfully!"}), 200
