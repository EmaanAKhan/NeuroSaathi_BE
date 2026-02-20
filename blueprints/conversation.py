from flask import Blueprint, request
from utils.response   import success_response, error_response
from utils.validators  import validate_json_field
from services.conversation_service import analyze_conversation

conversation_bp = Blueprint("conversation", __name__)

@conversation_bp.route("/conversation-analysis", methods=["POST"])
def conversation_analysis():
    data = request.get_json(silent=True)
    if not data:
        return error_response("Request body must be valid JSON")

    valid, msg = validate_json_field(data, "transcript", str)
    if not valid:
        return error_response(msg)
    if len(data["transcript"]) < 50:
        return error_response("Transcript too short. Minimum 50 characters.")

    language = data.get("language", "en").strip().lower()
    if language not in ("en", "ur"):
        language = "en"

    result = analyze_conversation(data["transcript"], language)
    return success_response(data=result, message="Conversation analysis complete")