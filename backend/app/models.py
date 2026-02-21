from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict, Any

# -----------------------------
# Existing Profile Models
# -----------------------------

class ProfessionalProfile(BaseModel):
    full_name: str
    contact_info: Dict[str, str]
    professional_summary: str

class Education(BaseModel):
    degree: str
    institution: str
    timeline: str
    specialization: str
    relevant_coursework: List[str]

class Experience(BaseModel):
    role: str
    organization: str
    timeline: str
    mentors: Optional[str] = None
    responsibilities: Optional[List[str]] = None
    achievements: Optional[List[str]] = None

class TechnicalSkills(BaseModel):
    languages: List[str]
    frameworks_and_libraries: List[str]
    tools_and_platforms: List[str]
    architectures_and_models: List[str]
    specialized_domains: List[str]

class Project(BaseModel):
    project_title: str
    role: str
    context: Optional[str] = None
    description: str

    technical_architecture: Optional[Dict[str, Any]] = None
    methodology: Optional[Dict[str, Any]] = None
    outcomes: Optional[Dict[str, Any]] = None
    impact: Optional[List[str]] = None

class Publication(BaseModel):
    title: str
    venue: str
    role: str
    summary: str

class Profile(BaseModel):
    professional_profile: ProfessionalProfile
    education: Education
    experience: List[Experience]
    technical_skills: TechnicalSkills
    projects: List[Project]
    publications: List[Publication]


# ---------------------------------------------------
# NEW: Full Research Project Page Model (IMPORTANT)
# ---------------------------------------------------

class ProjectPage(BaseModel):
    """
    Represents a full standalone project page
    (e.g. VREyeSAM, SEG-U-Sclera / SSBC 2025)
    """

    slug: str                 # "vreyesam", "ssbc"
    title: str
    subtitle: str
    description: str

    architecture: List[str]
    methodology: List[str]

    metrics: Dict[str, str]
    impact: List[str]
