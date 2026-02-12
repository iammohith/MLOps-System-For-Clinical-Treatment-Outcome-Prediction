"""
Pydantic schemas for API request/response validation.
Shared between training validation and inference.
Enforces exact CSV schema — inference hard-fails on schema violations.
"""

from pydantic import BaseModel, Field, field_validator
from typing import Literal


# --- Valid categorical values (derived from dataset) ---
VALID_GENDERS = ["Female", "Male"]
VALID_CONDITIONS = ["Depression", "Diabetes", "Hypertension", "Infection", "Pain Relief"]
VALID_DRUGS = [
    "Amlodipine", "Amoxicillin", "Azithromycin", "Bupropion", "Ciprofloxacin",
    "Escitalopram", "Glipizide", "Ibuprofen", "Insulin Glargine", "Losartan",
    "Metformin", "Metoprolol", "Paracetamol", "Sertraline", "Tramadol",
]
VALID_SIDE_EFFECTS = [
    "Abdominal pain", "Allergy", "Anxiety", "Back pain", "Constipation",
    "Cough", "Diarrhea", "Dizziness", "Drowsiness", "Dry mouth",
    "Fatigue", "Headache", "Heartburn", "Injection site pain", "Insomnia",
    "Joint pain", "Liver issues", "Low blood sugar", "Low sugar", "Nausea",
    "Rash", "Skin rash", "Sleep issues", "Slow heartbeat", "Stomach pain",
    "Stomach upset", "Sweating", "Swelling", "Tiredness", "Weight gain",
]
VALID_DOSAGES = [50.0, 100.0, 250.0, 500.0, 850.0]


class PredictionRequest(BaseModel):
    """Schema for prediction API request. Matches CSV schema exactly."""

    Patient_ID: str = Field(
        ...,
        description="Pseudonymized unique identifier",
        examples=["P0001"],
    )
    Age: int = Field(
        ...,
        ge=0,
        le=100,
        description="Patient age in years",
    )
    Gender: str = Field(
        ...,
        description="Gender as recorded",
    )
    Condition: str = Field(
        ...,
        description="Medical condition",
    )
    Drug_Name: str = Field(
        ...,
        description="Prescribed drug",
    )
    Dosage_mg: float = Field(
        ...,
        description="Dosage in milligrams",
    )
    Treatment_Duration_days: int = Field(
        ...,
        ge=1,
        description="Duration of treatment in days",
    )
    Side_Effects: str = Field(
        ...,
        description="Reported side effects",
    )

    @field_validator("Gender")
    @classmethod
    def validate_gender(cls, v):
        if v not in VALID_GENDERS:
            raise ValueError(f"Invalid Gender: '{v}'. Must be one of: {VALID_GENDERS}")
        return v

    @field_validator("Condition")
    @classmethod
    def validate_condition(cls, v):
        if v not in VALID_CONDITIONS:
            raise ValueError(
                f"Invalid Condition: '{v}'. Must be one of: {VALID_CONDITIONS}"
            )
        return v

    @field_validator("Drug_Name")
    @classmethod
    def validate_drug(cls, v):
        if v not in VALID_DRUGS:
            raise ValueError(
                f"Invalid Drug_Name: '{v}'. Must be one of: {VALID_DRUGS}"
            )
        return v

    @field_validator("Side_Effects")
    @classmethod
    def validate_side_effects(cls, v):
        if v not in VALID_SIDE_EFFECTS:
            raise ValueError(
                f"Invalid Side_Effects: '{v}'. Must be one of: {VALID_SIDE_EFFECTS}"
            )
        return v

    @field_validator("Dosage_mg")
    @classmethod
    def validate_dosage(cls, v):
        if v not in VALID_DOSAGES:
            raise ValueError(
                f"Invalid Dosage_mg: {v}. Must be one of: {VALID_DOSAGES}"
            )
        return v


class PredictionResponse(BaseModel):
    """Schema for prediction API response."""

    Patient_ID: str = Field(..., description="Patient identifier from request")
    Improvement_Score: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Predicted improvement score (0-10 scale)",
    )
    model_version: str = Field(..., description="Model version identifier")
    disclaimer: str = Field(
        default=(
            "This system predicts patient treatment outcome scores to support "
            "clinical research, quality analysis, and exploratory analytics. "
            "It does not provide diagnostic or treatment recommendations."
        ),
        description="Non-clinical disclaimer",
    )


class HealthResponse(BaseModel):
    """Schema for health check response."""

    status: str = Field(default="healthy")
    model_loaded: bool = Field(default=False)
    model_version: str = Field(default="unknown")


class DropdownValues(BaseModel):
    """Schema for frontend dropdown population."""

    genders: list[str] = VALID_GENDERS
    conditions: list[str] = VALID_CONDITIONS
    drugs: list[str] = VALID_DRUGS
    side_effects: list[str] = VALID_SIDE_EFFECTS
    dosages: list[float] = VALID_DOSAGES
