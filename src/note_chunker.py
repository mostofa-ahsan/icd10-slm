"""Split a doctor's note into short, codable phrases.

This is our answer to the "document-level coding" gap: we trained on short
phrases, so we chunk notes into phrases before coding. Simple rule-based
splitter — no model call, just section headers + punctuation.
"""
from __future__ import annotations
import re


# Common section headers in clinical notes. We split before each.
_SECTION_HEADERS = [
    "chief complaint", "history of present illness", "hpi",
    "past medical history", "pmh", "medications", "meds",
    "allergies", "social history", "family history",
    "review of systems", "ros", "physical exam", "pe",
    "assessment", "plan", "impression", "diagnosis", "diagnoses",
    "vitals", "labs", "imaging", "problem list",
]


def chunk_note(note: str, min_len: int = 4, max_len: int = 200) -> list[str]:
    """Split a doctor's note into codable phrases.

    Strategy:
      1. Normalize whitespace
      2. Split on section headers and bullet markers (`-`, `*`, numbered)
      3. Split each chunk on sentence-ending punctuation
      4. Filter: drop too-short (<min_len) and too-long (>max_len) chunks

    Returns a deduplicated list of phrase strings.
    """
    text = re.sub(r"\s+", " ", note).strip()

    # Split on headers (case insensitive)
    header_pattern = r"(?i)\b(" + "|".join(re.escape(h) for h in _SECTION_HEADERS) + r")\s*:"
    parts = re.split(header_pattern, text)

    phrases: list[str] = []
    for part in parts:
        if part.lower() in _SECTION_HEADERS:
            continue  # skip header tokens themselves
        # Split on bullets and numbered list markers
        for sub in re.split(r"(?:(?:^|\s)[-*•]\s+|\s*\d+[\.\)]\s+|;|\n)", part):
            # Split on sentence enders
            for s in re.split(r"(?<=[.!?])\s+", sub):
                s = s.strip().strip(",.:;-").strip()
                if min_len <= len(s) <= max_len:
                    phrases.append(s)

    # Dedupe while preserving order
    seen, out = set(), []
    for p in phrases:
        key = p.lower()
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


if __name__ == "__main__":
    sample = """
    Chief Complaint: 55yo M with 2 days of chest pain radiating to left arm.
    HPI: Pain is crushing, 8/10, worse with exertion.
    PMH: Hypertension, Type 2 Diabetes, hyperlipidemia.
    Meds: metoprolol 50mg BID, metformin 1000mg BID, atorvastatin 40mg.
    Assessment:
      1. Acute coronary syndrome, rule out MI
      2. HTN, controlled
      3. T2DM without complications
    """
    for i, p in enumerate(chunk_note(sample)):
        print(f"{i+1}. {p}")
