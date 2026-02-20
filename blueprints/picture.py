from flask import Blueprint, request
from utils.response   import success_response, error_response
from utils.validators  import validate_audio_file
from services.picture_service import analyze_picture_description

picture_bp = Blueprint("picture", __name__)

@picture_bp.route("/picture-description", methods=["POST"])
def picture_description():
    valid, msg = validate_audio_file(request)
    if not valid:
        return error_response(msg)

    language = request.form.get("language", "en").strip().lower()
    if language not in ("en", "ur"):
        language = "en"

    result = analyze_picture_description(request.files["audio"], language)
    return success_response(data=result, message="Picture description analysis complete")