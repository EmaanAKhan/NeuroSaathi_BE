from flask import jsonify

def success_response(data=None, message="Success", status=200):
    return jsonify({
        "status":  "success",
        "message": message,
        "data":    data or {}
    }), status

def error_response(message, details=None, status=400):
    return jsonify({
        "status":  "error",
        "message": message,
        "details": details
    }), status