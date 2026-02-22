"""
picture_service.py

Picture Description (Cookie Theft) — Gemini Audio Analysis.
His exact code from the notebook, adapted for Flask.

The only difference from his notebook:
- audio_file.read() replaces open("/content/recording2.m4a").read()
- mime type is now detected properly from filename (fixing his bug)
- API key comes from .env instead of Colab secrets
"""

import os
from werkzeug.datastructures import FileStorage
from google import genai
from google.genai import types
from models.pydantic_models import PictureDescription

# ── Gemini client ─────────────────────────────────────────────────────────────
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ── Prompt — copied exactly from his notebook ─────────────────────────────────
PICTURE_DESCRIPTION_PROMPT = """
ROLE:
You are a Senior Clinical Neuropsychologist specializing in discourse analysis and vocal biomarkers for neurodegenerative diseases. Your expertise is in detecting subtle acoustic and linguistic indicators of Mild Cognitive Impairment (MCI) and Alzheimer's Disease (AD) through Picture Description Tasks.

TASK:
Perform a high-fidelity Acoustic, Linguistic and Semantic Analysis of the provided audio recording of a patient describing the Cookie Theft Picture.

THE COOKIE THEFT PICTURE CONTAINS THESE KEY ELEMENTS:
1. A woman standing at a kitchen sink (water overflowing, flooding the floor)
2. A boy stealing cookies from a jar while standing on a stool
3. A girl standing below reaching up for cookies
4. The stool is tipping over
5. A window above the sink
6. Dishes on the counter
7. A cabinet with the cookie jar on top
8. Kitchen setting overall

CLINICAL GUIDELINES FOR ANALYSIS:
1. RAW TRANSCRIPT: Transcribe EVERY sound. Log every "um", "uh", "hmm", "err" verbatim.
2. HESITATIONS: Treat every filler as a biomarker. Timestamp the START of each hesitation.
3. PAUSES: Measure silence gaps. >2000ms = search effort. >5000ms = retrieval failure.
4. CONTENT UNITS: Count key elements mentioned. Strict scoring only.
5. INFORMATION DENSITY: Ratio of meaningful content to total words.
6. WORD FINDING: Circumlocution, phonemic groping, long pauses before object names.
7. VOICE QUALITY: Micro-tremors or vocal unsteadiness.
8. DISCOURSE COHERENCE: Logical and spatially organized description?
9. SEMANTIC ERRORS: Misidentifying objects or people.

OUTPUT INSTRUCTIONS:
Return ONLY a valid JSON object. No intro. No markdown. Use this exact schema:

{
  "raw_transcript": "string",
  "content_units": {
    "woman_at_sink": boolean,
    "water_overflowing": boolean,
    "boy_stealing_cookies": boolean,
    "girl_reaching_up": boolean,
    "stool_tipping": boolean,
    "window_mentioned": boolean,
    "dishes_mentioned": boolean,
    "kitchen_setting": boolean,
    "total_mentioned": integer
  },
  "information_density": "string (high/medium/low)",
  "total_words_spoken": integer,
  "content_per_100_words": float,
  "empty_speech_count": integer,
  "empty_speech_examples": ["string"],
  "hesitation_count": integer,
  "hesitation_words": ["string"],
  "hesitation_timestamps": ["string"],
  "avg_pause_ms": integer,
  "longest_pause_ms": integer,
  "word_finding_struggles": integer,
  "word_finding_examples": ["string"],
  "semantic_errors": integer,
  "semantic_error_examples": ["string"],
  "discourse_coherence": "string (organized/mildly_disorganized/severely_disorganized)",
  "perseveration_detected": boolean,
  "perseveration_examples": ["string"],
  "tangential_thinking": boolean,
  "voice_tremor_detected": boolean,
  "speech_clarity": "string (clear/slurred/labored/breathy)",
  "clinical_flag": "string (normal/borderline/concern/high_concern)",
  "interpretation": "string (2 sentence plain English summary)"
}
"""


def analyze_picture_description(audio_file: FileStorage, language: str) -> dict:
    """
    Analyze patient's verbal description of Cookie Theft picture using Gemini.

    Args:
        audio_file: Audio file received from Flask request
        language:   'en' | 'ur'

    Returns:
        dict matching PictureDescription Pydantic model exactly
    """
    # Read bytes from uploaded file (replaces his open() call)
    audio_bytes = audio_file.read()

    # Detect mime type properly (fixes his notebook bug where m4a was sent as wav)
    filename = audio_file.filename.lower()
    if filename.endswith(".m4a"):
        mime_type = "audio/m4a"
    elif filename.endswith(".mp3"):
        mime_type = "audio/mp3"
    elif filename.endswith(".ogg"):
        mime_type = "audio/ogg"
    elif filename.endswith(".webm"):
        mime_type = "audio/webm"
    else:
        mime_type = "audio/wav"

    # Gemini call — exactly from his notebook (with mime type bug fixed)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type=mime_type
            ),
            PICTURE_DESCRIPTION_PROMPT
        ],
        config={
            "temperature": 0.0,
            "response_mime_type": "application/json",
            "response_schema": PictureDescription,
        }
    )

    return response.parsed.model_dump()