from flask import current_app

def allowed_audio(filename):
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    return ext in current_app.config["ALLOWED_AUDIO_EXTENSIONS"]

def allowed_image(filename):
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    return ext in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]

def validate_audio_file(request):
    if "audio" not in request.files:
        return False, "No audio file provided. Expected field name: 'audio'"
    file = request.files["audio"]
    if file.filename == "":
        return False, "Audio file has no filename"
    if not allowed_audio(file.filename):
        allowed = ", ".join(current_app.config["ALLOWED_AUDIO_EXTENSIONS"])
        return False, f"Invalid audio format. Allowed: {allowed}"
    return True, ""

def validate_image_file(request):
    if "image" not in request.files:
        return False, "No image file provided. Expected field name: 'image'"
    file = request.files["image"]
    if file.filename == "":
        return False, "Image file has no filename"
    if not allowed_image(file.filename):
        allowed = ", ".join(current_app.config["ALLOWED_IMAGE_EXTENSIONS"])
        return False, f"Invalid image format. Allowed: {allowed}"
    return True, ""

def validate_json_field(data, field, field_type=str):
    if field not in data:
        return False, f"Missing required field: '{field}'"
    if not isinstance(data[field], field_type):
        return False, f"Field '{field}' must be type {field_type.__name__}"
    if field_type == str and not data[field].strip():
        return False, f"Field '{field}' cannot be empty"
    return True, ""