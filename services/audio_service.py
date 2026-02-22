"""
audio_service.py

Animal Naming Test — Gemini Audio Analysis.
His exact code from the notebook, adapted for Flask.

The only difference from his notebook:
- audio_file.read() replaces open("/content/recording.wav").read()
- API key comes from .env instead of Colab secrets
"""

import os
from werkzeug.datastructures import FileStorage
from google import genai
from google.genai import types
from models.pydantic_models import AudioBiomarkers


# ── Gemini client (key loaded from .env file) ─────────────────────────────────
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ── Prompt — copied exactly from his notebook ─────────────────────────────────
ANIMAL_NAMING_PROMPT = """
ROLE:
You are a Senior Clinical Neuropsychologist specializing in vocal biomarkers for neurodegenerative diseases. Your expertise is in detecting subtle acoustic and linguistic indicators of Mild Cognitive Impairment (MCI) and Alzheimer's Disease (AD) through Verbal Fluency Tests.

TASK:
Perform a high-fidelity Acoustic and Semantic Analysis of the provided 60-second audio recording (Animal Naming Test).

CLINICAL GUIDELINES FOR ANALYSIS:
1. RAW TRANSCRIPT: Transcribe EVERY sound. Do not normalize. If the patient says "Gira... Giraffe," include the "Gira...". Log every "um", "uh", "hmm", and filler.
2. HESITATIONS: Treat every "um", "uh", and breathy "err" as a significant biomarker of retrieval cost. Precisely timestamp the START of each hesitation.
3. PAUSES (IEIs): Measure the silence between the end of one animal and the start of the next.
   - A pause > 2000ms indicates a search effort.
   - A pause > 5000ms indicates a "Switching" failure in the semantic network.
4. CLUSTERING: Analyze if animals are retrieved via semantic nodes (e.g., Pet -> Farm -> African Safari).
5. VOICE QUALITY: Listen for "Micro-tremors" or "Vocal Unsteadiness" (markers for Parkinsonian or motor-speech involvement).
6. WORD FINDING: Identify "Tip-of-the-tongue" phenomena, false starts, or verbalized frustration.

OUTPUT INSTRUCTIONS:
Return ONLY a valid JSON object. No intro. No markdown. Use this exact schema:

{
  "raw_transcript": "string (verbatim including every filler/stutter)",
  "animals_named": ["string"],
  "unique_count": integer,
  "repetitions": integer,
  "hesitation_count": integer,
  "hesitation_words": ["string"],
  "hesitation_timestamps": ["string (e.g., 12s)"],
  "avg_pause_ms": integer,
  "longest_pause_ms": integer,
  "pauses_over_5sec": integer,
  "clustering_present": boolean,
  "cluster_groups": ["string"],
  "word_finding_struggles": integer,
  "word_finding_examples": ["string"],
  "voice_tremor_detected": boolean,
  "speech_clarity": "string (clear/slurred/labored/breathy)"
}
"""


def analyze_audio(audio_file: FileStorage, test_type: str, language: str) -> dict:
    """
    Analyze audio from Animal Naming Test using Gemini.

    Args:
        audio_file: Audio file received from Flask request
        test_type:  'animal_naming'
        language:   'en' | 'ur'

    Returns:
        dict matching AudioBiomarkers Pydantic model exactly
    """
    # Read bytes from uploaded file (replaces his open() call)
    audio_bytes = audio_file.read()

    # Detect mime type from filename
    filename = audio_file.filename.lower()
    if filename.endswith(".mp3"):
        mime_type = "audio/mp3"
    elif filename.endswith(".m4a"):
        mime_type = "audio/m4a"
    elif filename.endswith(".ogg"):
        mime_type = "audio/ogg"
    elif filename.endswith(".webm"):
        mime_type = "audio/webm"
    else:
        mime_type = "audio/wav"

    # Gemini call — exactly from his notebook
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type=mime_type
            ),
            ANIMAL_NAMING_PROMPT
        ],
        config={
            "temperature": 0.0,
            "response_mime_type": "application/json",
            "response_schema": AudioBiomarkers,
        }
    )

    # Returns clean dict — exactly like his model_dump()
    return response.parsed.model_dump()