def analyze_picture_description(audio_file, language):
    # TODO: AI/ML guy replaces this with real Gemini call
    # audio_bytes = audio_file.read()
    # return gemini_client.analyze_picture(audio_bytes, language)
    return _mock_picture_analysis()

def _mock_picture_analysis():
    return {
        "transcript": "I can see a woman washing dishes, water overflowing. Two children stealing cookies from a jar on a tipping stool.",
        "content_units":          9,
        "information_density":    0.68,
        "empty_word_count":       3,
        "filled_pause_count":     4,
        "avg_pause_ms":           1200,
        "semantic_errors":        0,
        "mean_utterance_length":  14.2,
        "word_finding_struggles": 1,
        "coherence_score":        7.8,
        "concern_level":          "low",
        "clinical_interpretation": "9 of 15 content units identified. Coherent description. Normal range."
    }