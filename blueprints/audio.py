from flask import Blueprint, request
from utils.response  import success_response, error_response
from utils.validators import validate_audio_file
from services.audio_service import analyze_audio

audio_bp = Blueprint("audio", __name__)

@audio_bp.route("/audio-analysis", methods=["POST"])
def audio_analysis():
    valid, msg = validate_audio_file(request)
    if not valid:
        return error_response(msg)

    VALID_TYPES = {"animal_naming", "sentence_repetition", "word_recall"}
    test_type = request.form.get("test_type", "").strip()
    if not test_type:
        return error_response("Missing required field: 'test_type'")
    if test_type not in VALID_TYPES:
        return error_response(f"Invalid test_type. Must be one of: {', '.join(VALID_TYPES)}")

    language = request.form.get("language", "en").strip().lower()
    if language not in ("en", "ur"):
        language = "en"

    result = analyze_audio(request.files["audio"], test_type, language)
    return success_response(data=result, message="Audio analysis complete")