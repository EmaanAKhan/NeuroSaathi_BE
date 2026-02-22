"""
vision_service.py

Clock Drawing Test — Gemini Vision Analysis.
His exact code from the notebook, adapted for Flask.

The only difference from his notebook:
- image_file.read() replaces open("/content/clock_2.png").read()
- API key comes from .env instead of Colab secrets
"""

import os
from werkzeug.datastructures import FileStorage
from google import genai
from google.genai import types
from models.pydantic_models import ClockFeatures

# ── Gemini client ─────────────────────────────────────────────────────────────
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ── Prompt — copied exactly from his notebook ─────────────────────────────────
CLOCK_DRAWING_PROMPT = """
ROLE:
You are a Senior Clinical Neuropsychologist specializing in visuospatial and executive function assessment for neurodegenerative diseases. Your expertise is in scoring Clock Drawing Tests (CDT) as a validated screening tool for Mild Cognitive Impairment (MCI) and Alzheimer's Disease (AD).

TASK:
Perform a high-fidelity visuospatial and clinical analysis of the provided Clock Drawing Test image. The patient was instructed to draw a clock showing 11:10.

CLINICAL GUIDELINES FOR ANALYSIS:

1. CLOCK FACE (Circle): Is a circle present? Is it closed or open? Is it reasonably round or severely distorted?
2. NUMBERS: Are all 12 numbers present? Are they inside the circle? Are they in correct sequence? Is 12 at the top, 6 at the bottom, 3 on the right, 9 on the left?
3. CLOCK HANDS: Are two hands present? Is there an hour hand pointing near 11? Is there a minute hand pointing near 2?
4. SPATIAL ORGANIZATION: Is the overall layout balanced and centered?
5. TREMOR AND MOTOR: Are lines shaky or wavering?
6. CDT SCORING (Shulman Scale, out of 6): 6=Perfect, 5=Minor errors, 4=Inaccurate time but hands present, 3=Moderate distortion, 2=Severe distortion, 1=No resemblance

OUTPUT INSTRUCTIONS:
Return ONLY a valid JSON object. No intro. No markdown. Use this exact schema:

{
  "circle_drawn": boolean,
  "circle_quality": "string (perfect/nearly_closed/open/missing)",
  "circle_size": "string (appropriate/too_small/too_large)",
  "numbers_present": boolean,
  "numbers_count": integer,
  "numbers_inside_circle": boolean,
  "numbers_correct_sequence": boolean,
  "number_12_at_top": boolean,
  "number_6_at_bottom": boolean,
  "number_3_at_right": boolean,
  "number_9_at_left": boolean,
  "numbers_crowded_one_side": boolean,
  "crowding_direction": "string (left/right/top/bottom/none)",
  "hands_drawn": boolean,
  "hand_count": integer,
  "hour_hand_present": boolean,
  "minute_hand_present": boolean,
  "hour_hand_correct": boolean,
  "minute_hand_correct": boolean,
  "correct_time_shown": boolean,
  "spatial_organization": "string (good/mild_distortion/severe_distortion)",
  "planning_deficit_evident": boolean,
  "tremor_visible": boolean,
  "tremor_severity": "string (none/mild/moderate/severe)",
  "cdt_score": integer,
  "concern_level": "string (low/moderate/high)",
  "clinical_pattern": "string (normal_aging/mild_MCI/alzheimers_pattern/vascular_dementia)",
  "key_findings": ["string"],
  "positive_signs": ["string"],
  "interpretation": "string (2 sentence plain English summary)",
  "recommendation": "string (next steps for the patient)"
}
"""


def analyze_clock_drawing(image_file: FileStorage, target_time: str) -> dict:
    """
    Analyze Clock Drawing Test image using Gemini Vision.

    Args:
        image_file:  Image file received from Flask request
        target_time: Time patient was asked to draw e.g. "11:10"

    Returns:
        dict matching ClockFeatures Pydantic model exactly
    """
    # Read bytes from uploaded file (replaces his open() call)
    image_bytes = image_file.read()

    # Detect mime type from filename
    filename = image_file.filename.lower()
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        mime_type = "image/jpeg"
    elif filename.endswith(".webp"):
        mime_type = "image/webp"
    else:
        mime_type = "image/png"

    # Gemini Vision call — exactly from his notebook
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            ),
            CLOCK_DRAWING_PROMPT
        ],
        config={
            "temperature": 0.0,
            "response_mime_type": "application/json",
            "response_schema": ClockFeatures,
        }
    )

    return response.parsed.model_dump()