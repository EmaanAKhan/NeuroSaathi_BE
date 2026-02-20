from flask import Blueprint
from utils.response import success_response

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health_check():
    from flask import current_app
    return success_response(
        data={
            "server": "online",
            "version": "1.0.0",
            "ai_services": {
                "gemini":   "configured" if current_app.config.get("GEMINI_API_KEY")   else "not configured (using mock)",
                "medgemma": "configured" if current_app.config.get("MEDGEMMA_API_KEY") else "not configured (using mock)",
            }
        },
        message="NeuroSaathi API is running"
    )