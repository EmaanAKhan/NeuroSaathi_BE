"""
pydantic_models.py

Pydantic models copied exactly from the AI/ML team's notebook.
These define the exact shape of every AI response in the system.
Do NOT change field names — they must match the notebook exactly.
"""

from pydantic import BaseModel
from typing import List


# ─────────────────────────────────────────────────────────────────────────────
# AUDIO — Animal Naming Test
# ─────────────────────────────────────────────────────────────────────────────

class AudioBiomarkers(BaseModel):
    raw_transcript: str
    animals_named: List[str]
    unique_count: int
    repetitions: int
    hesitation_count: int
    hesitation_words: List[str]
    hesitation_timestamps: List[str]
    avg_pause_ms: int
    longest_pause_ms: int
    pauses_over_5sec: int
    clustering_present: bool
    cluster_groups: List[str]
    word_finding_struggles: int
    word_finding_examples: List[str]
    voice_tremor_detected: bool
    speech_clarity: str


# ─────────────────────────────────────────────────────────────────────────────
# VISION — Clock Drawing Test
# ─────────────────────────────────────────────────────────────────────────────

class ClockFeatures(BaseModel):
    circle_drawn: bool
    circle_quality: str
    circle_size: str
    numbers_present: bool
    numbers_count: int
    numbers_inside_circle: bool
    numbers_correct_sequence: bool
    number_12_at_top: bool
    number_6_at_bottom: bool
    number_3_at_right: bool
    number_9_at_left: bool
    numbers_crowded_one_side: bool
    crowding_direction: str
    hands_drawn: bool
    hand_count: int
    hour_hand_present: bool
    minute_hand_present: bool
    hour_hand_correct: bool
    minute_hand_correct: bool
    correct_time_shown: bool
    spatial_organization: str
    planning_deficit_evident: bool
    tremor_visible: bool
    tremor_severity: str
    cdt_score: int
    concern_level: str
    clinical_pattern: str
    key_findings: List[str]
    positive_signs: List[str]
    interpretation: str
    recommendation: str


# ─────────────────────────────────────────────────────────────────────────────
# PICTURE — Cookie Theft Description
# ─────────────────────────────────────────────────────────────────────────────

class ContentUnits(BaseModel):
    woman_at_sink: bool
    water_overflowing: bool
    boy_stealing_cookies: bool
    girl_reaching_up: bool
    stool_tipping: bool
    window_mentioned: bool
    dishes_mentioned: bool
    kitchen_setting: bool
    total_mentioned: int


class PictureDescription(BaseModel):
    raw_transcript: str
    content_units: ContentUnits
    information_density: str
    total_words_spoken: int
    content_per_100_words: float
    empty_speech_count: int
    empty_speech_examples: List[str]
    hesitation_count: int
    hesitation_words: List[str]
    hesitation_timestamps: List[str]
    avg_pause_ms: int
    longest_pause_ms: int
    word_finding_struggles: int
    word_finding_examples: List[str]
    semantic_errors: int
    semantic_error_examples: List[str]
    discourse_coherence: str
    perseveration_detected: bool
    perseveration_examples: List[str]
    tangential_thinking: bool
    voice_tremor_detected: bool
    speech_clarity: str
    clinical_flag: str
    interpretation: str


# ─────────────────────────────────────────────────────────────────────────────
# MEDGEMMA — Final Report
# ─────────────────────────────────────────────────────────────────────────────

class SimpleScores(BaseModel):
    memory: int
    language: int
    thinking: int
    drawing: int


class PatientReport(BaseModel):
    overall_status: str
    concern_level: str
    simple_scores: SimpleScores
    what_this_means: str
    what_to_do_next: str
    urgency: str


class DiagnosticMarkers(BaseModel):
    semantic_network_status: str
    language_discourse_status: str
    executive_function_status: str
    visuospatial_status: str
    working_memory_status: str
    motor_speech_involvement: bool
    psychomotor_tremor_detected: bool
    cross_test_convergence: str
    convergence_strength: str


class DomainScores(BaseModel):
    semantic_memory: int
    language_fluency: int
    discourse_coherence: int
    visuospatial: int
    executive_function: int
    processing_speed: int
    overall: int


class TestFlag(BaseModel):
    score: int
    flag: str
    top_finding: str


class TestSummary(BaseModel):
    animal_naming: TestFlag
    clock_drawing: TestFlag
    picture_description: TestFlag


class RiskProfile(BaseModel):
    assessment: str
    concern_level: str
    confidence_score: float
    justification: str


class FinalReport(BaseModel):
    clinical_summary: str
    diagnostic_markers: DiagnosticMarkers
    domain_scores: DomainScores
    test_summary: TestSummary
    risk_profile: RiskProfile
    cross_test_findings: List[str]
    key_findings: List[str]
    positive_signs: List[str]
    differential_notes: str
    recommended_battery: List[str]
    urgency: str
    patient_report: PatientReport