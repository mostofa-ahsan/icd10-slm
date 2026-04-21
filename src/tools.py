"""Agent tools for ICD-10-CM validation. Implemented in Notebook 4."""
from __future__ import annotations
from typing import TypedDict


class LookupResult(TypedDict):
    code: str
    short_desc: str
    long_desc: str
    is_valid: bool


class SearchCandidate(TypedDict):
    code: str
    description: str
    score: float


def icd10_lookup(code: str) -> LookupResult:
    """Return the canonical description for a specific ICD-10-CM code."""
    raise NotImplementedError("See Notebook 4, Section 3.1")


def icd10_search(query: str, k: int = 10) -> list[SearchCandidate]:
    """Semantic search over ~70k ICD-10-CM descriptions via FAISS."""
    raise NotImplementedError("See Notebook 4, Section 3.2")


def validate_code(code: str) -> bool:
    """Check whether a string is a real ICD-10-CM code in the codebook."""
    raise NotImplementedError("See Notebook 4, Section 3.3")


def code_hierarchy(code: str) -> dict:
    """Return chapter/block/category for an ICD-10-CM code."""
    raise NotImplementedError("See Notebook 4, Section 3.4")


TOOLS_SCHEMA = [
    {"name": "icd10_lookup",
     "description": "Return canonical description for a specific ICD-10-CM code.",
     "parameters": {"type": "object",
                    "properties": {"code": {"type": "string"}},
                    "required": ["code"]}},
    {"name": "icd10_search",
     "description": "Semantic search over ICD-10-CM descriptions.",
     "parameters": {"type": "object",
                    "properties": {"query": {"type": "string"},
                                   "k": {"type": "integer", "default": 10}},
                    "required": ["query"]}},
    {"name": "validate_code",
     "description": "Check if a string is a real ICD-10-CM code.",
     "parameters": {"type": "object",
                    "properties": {"code": {"type": "string"}},
                    "required": ["code"]}},
    {"name": "code_hierarchy",
     "description": "Get chapter/block/category for a code.",
     "parameters": {"type": "object",
                    "properties": {"code": {"type": "string"}},
                    "required": ["code"]}},
]
