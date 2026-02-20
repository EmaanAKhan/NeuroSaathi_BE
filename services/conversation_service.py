def analyze_conversation(transcript, language):
    # TODO: Aliza / AI team replaces this with real analysis
    # return medgemma_client.analyze_conversation(transcript, language)
    return _mock_conversation_analysis()

def _mock_conversation_analysis():
    return {
        "recent_memory_score":        6.5,
        "remote_memory_score":        8.2,
        "memory_gap":                 1.7,
        "temporal_specificity":       "moderate",
        "confabulation_detected":     False,
        "prospective_memory_success": True,
        "semantic_knowledge_intact":  True,
        "concern_level":              "low",
        "clinical_pattern":           "normal_aging",
        "interpretation":             "Mild recent memory reduction. Remote memory preserved. Normal aging pattern."
    }