def analyze_clock_drawing(image_file, target_time):
    # TODO: AI/ML guy replaces this with real Gemini Vision call
    # image_bytes = image_file.read()
    # return gemini_vision_client.analyze(image_bytes, target_time)
    return _mock_cdt_analysis(target_time)

def _mock_cdt_analysis(target_time):
    return {
        "target_time": target_time,
        "scores": {
            "circle_drawn":               True,
            "numbers_present":            True,
            "numbers_correct_position":   True,
            "hands_present":              True,
            "correct_time_shown":         False,
            "spatial_accuracy_score":     7.2,
            "tremor_detected":            False,
        },
        "total_score":    4,
        "concern_level":  "low",
        "clinical_notes": f"Clock targeting {target_time}. Numbers intact. Hands slightly misaligned."
    }