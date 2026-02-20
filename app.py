from flask import Flask
from flask_cors import CORS
import os
from config import config_map

def create_app(env=None):
    app = Flask(__name__)

    env = env or os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_map.get(env, config_map["development"]))

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from blueprints.health       import health_bp
    from blueprints.audio        import audio_bp
    from blueprints.vision       import vision_bp
    from blueprints.picture      import picture_bp
    from blueprints.conversation import conversation_bp
    from blueprints.reasoning    import reasoning_bp

    app.register_blueprint(health_bp,       url_prefix="/api/v1")
    app.register_blueprint(audio_bp,        url_prefix="/api/v1")
    app.register_blueprint(vision_bp,       url_prefix="/api/v1")
    app.register_blueprint(picture_bp,      url_prefix="/api/v1")
    app.register_blueprint(conversation_bp, url_prefix="/api/v1")
    app.register_blueprint(reasoning_bp,    url_prefix="/api/v1")

    from utils.response import error_response

    @app.errorhandler(404)
    def not_found(e):
        return error_response("Endpoint not found", status=404)

    @app.errorhandler(405)
    def method_not_allowed(e):
        return error_response("Method not allowed", status=405)

    @app.errorhandler(413)
    def file_too_large(e):
        return error_response("File too large. Maximum size is 50MB.", status=413)

    return app
app = create_app()
if __name__ == "__main__":
    app = create_app()
    print("\n" + "="*50)
    print("  NeuroSaathi Backend Starting...")
    print("="*50)
    print("  Base URL : http://localhost:5000/api/v1")
    print("  Health   : http://localhost:5000/api/v1/health")
    print("="*50 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=True)