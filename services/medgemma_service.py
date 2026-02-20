def combined_reasoning(patient_info, audio_result, vision_result, picture_result, conversation_result):
    # TODO: AI/ML guy replaces this with real MedGemma call
    # prompt = build_prompt(patient_info, audio_result, vision_result, picture_result, conversation_result)
    # return medgemma_client.reason(prompt)
    return _mock_combined_reasoning(patient_info)

def _mock_combined_reasoning(patient_info):
    age = patient_info.get("age", 68)
    return {
        "domain_scores": {
            "memory":       62.0,
            "language":     74.0,
            "executive":    80.0,
            "attention":    85.0,
            "visuospatial": 78.0,
        },
        "overall_concern_level": "moderate",
        "clinical_pattern":      "aMCI",
        "summary": f"Results show early memory and language changes slightly below expected for age {age}. See a doctor within 2-4 weeks.",
        "recommendations": [
            "See a neurologist within 2-4 weeks",
            "Start daily brain training exercises",
            "Ensure 7-8 hours sleep nightly",
            "30 minutes walking daily",
            "Return for follow-up screening in 7 days",
        ],
        "next_screening_days":  7,
        "refer_to_neurologist": True,
        "full_clinical_report": "Pattern consistent with amnestic MCI. Memory-predominant deficits with preserved executive function. Neurologist referral advised."
    }