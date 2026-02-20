from flask import Blueprint, request
from utils.response   import success_response, error_response
from utils.validators  import validate_image_file
from services.vision_service import analyze_clock_drawing

vision_bp = Blueprint("vision", __name__)

@vision_bp.route("/vision-analysis", methods=["POST"])
def vision_analysis():
    valid, msg = validate_image_file(request)
    if not valid:
        return error_response(msg)

    target_time = request.form.get("target_time", "").strip()
    if not target_time:
        return error_response("Missing required field: 'target_time' (e.g. '10:10')")

    result = analyze_clock_drawing(request.files["image"], target_time)
    return success_response(data=result, message="Clock drawing analysis complete")