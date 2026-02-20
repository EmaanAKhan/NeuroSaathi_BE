from flask import Blueprint, request
from utils.response import success_response, error_response
from services.medgemma_service import combined_reasoning
import json

reasoning_bp = Blueprint("reasoning", __name__)

REQUIRED_RESULTS = ["audio_result", "vision_result", "picture_result", "conversation_result"]

@reasoning_bp.route("/combined-reasoning", methods=["POST"])
def combined_reasoning_endpoint():
    data = request.get_json(silent=True)
    if not data:
        return error_response("Request body must be valid JSON")

    patient_info = data.get("patient_info")
    if not patient_info or not isinstance(patient_info, dict):
        return error_response("Missing or invalid 'patient_info'")

    try:
        age = int(patient_info["age"])
        if not (40 <= age <= 110):
            return error_response("patient_info.age must be between 40 and 110")
    except (ValueError, TypeError, KeyError):
        return error_response("patient_info.age is required and must be a number")

    missing = [k for k in REQUIRED_RESULTS if k not in data]
    if missing:
        return error_response(f"Missing result fields: {', '.join(missing)}")

    result = combined_reasoning(
        patient_info         = patient_info,
        audio_result         = data["audio_result"],
        vision_result        = data["vision_result"],
        picture_result       = data["picture_result"],
        conversation_result  = data["conversation_result"],
    )
    return success_response(data=result, message="Clinical reasoning complete")