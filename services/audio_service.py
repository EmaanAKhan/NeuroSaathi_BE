def analyze_audio(audio_file, test_type, language):
    # TODO: AI/ML guy replaces this with real Gemini call
    # audio_bytes = audio_file.read()
    # return gemini_client.analyze(audio_bytes, test_type, language)

    if test_type == "animal_naming":
        return _mock_animal_naming()
    elif test_type == "sentence_repetition":
        return _mock_sentence_repetition()
    elif test_type == "word_recall":
        return _mock_word_recall()
    return _mock_animal_naming()

def _mock_animal_naming():
    return {
        "test_type": "animal_naming",
        "transcript": "Dog, cat, lion, elephant, horse, zebra, monkey, parrot, fish, rabbit, tiger, cow",
        "metrics": {
            "animals_named": ["dog","cat","lion","elephant","horse","zebra","monkey","parrot","fish","rabbit","tiger","cow"],
            "unique_count": 12,
            "clustering_detected": True,
            "hesitation_count": 2,
            "avg_pause_ms": 1800,
            "vocal_jitter_detected": False,
        },
        "concern_level": "low",
        "clinical_notes": "12 unique animals. Good semantic clustering. Within normal range."
    }

def _mock_sentence_repetition():
    return {
        "test_type": "sentence_repetition",
        "transcript": "I only know that John is the one to help today",
        "metrics": {
            "word_accuracy_pct": 92.3,
            "hesitation_count": 1,
            "avg_pause_ms": 600,
            "vocal_jitter_detected": False,
        },
        "concern_level": "low",
        "clinical_notes": "92.3% accuracy. Minor omission. No paraphasias detected."
    }

def _mock_word_recall():
    return {
        "test_type": "word_recall",
        "transcript": "Apple... table... penny",
        "metrics": {
            "words_recalled": 2,
            "words_total": 3,
            "word_accuracy_pct": 66.7,
            "hesitation_count": 3,
            "avg_pause_ms": 2200,
        },
        "concern_level": "moderate",
        "clinical_notes": "2 of 3 words recalled. Retrieval difficulty noted."
    }