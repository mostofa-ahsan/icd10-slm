"""Hand-crafted sample doctor's notes for the Streamlit demo.

These are SYNTHETIC clinical notes written for educational demos. They do not
describe real patients. Codes annotated are the author's expected mapping, not
clinical gold standard.

All notes follow realistic SOAP / note conventions but keep PHI-free fake names.
"""

DEMO_NOTES = {
    "case_01_t2dm_htn": {
        "title": "Case 1 — T2DM follow-up with HTN",
        "note": """Chief Complaint: 62 yo F here for diabetes follow-up.

HPI: Patient reports home glucose readings running 140-180 fasting. She admits
to skipping metformin doses about twice a week. No polyuria, polydipsia, or
vision changes. No chest pain or shortness of breath. Last A1C 7.8%.

PMH:
  1. Type 2 diabetes mellitus, without complications
  2. Essential hypertension
  3. Mixed hyperlipidemia

Meds: metformin 1000mg BID, lisinopril 20mg daily, atorvastatin 40mg qhs.

Vitals: BP 148/92, HR 78, BMI 31.

Assessment/Plan:
  1. T2DM uncontrolled — increase metformin to 2000mg daily; re-check A1C in 3mo
  2. HTN uncontrolled — add amlodipine 5mg daily
  3. Obesity, class I — dietitian referral""",
        "expected_codes": ["E11.9", "I10", "E78.2", "E66.9"],
    },

    "case_02_copd_exacerbation": {
        "title": "Case 2 — COPD exacerbation, ED presentation",
        "note": """Chief Complaint: 71 yo M with 3 days of worsening dyspnea and productive cough.

HPI: Former smoker (50 pack-year), stopped 2 years ago. Baseline 2L home O2.
Increased sputum, now yellow-green. Denies fever, chest pain, or leg swelling.
Used albuterol inhaler q2h at home with minimal relief.

PMH: COPD, CAD s/p stent 2019, chronic kidney disease stage 3.
Meds: tiotropium, albuterol PRN, aspirin 81mg, atorvastatin.

Exam: wheezing bilaterally, accessory muscle use. SpO2 87% on 2L, up to 94% on 4L.

Assessment/Plan:
  1. Acute exacerbation of COPD — start prednisone 40mg daily x5, azithromycin 500mg
  2. CAD, stable on current regimen
  3. CKD stage 3 — avoid NSAIDs""",
        "expected_codes": ["J44.1", "I25.10", "N18.30"],
    },

    "case_03_low_back_pain": {
        "title": "Case 3 — Acute low back pain, new presentation",
        "note": """Chief Complaint: 44 yo M with acute low back pain x2 days.

HPI: Pain started after lifting heavy boxes at work. Aching, 6/10, worse with
bending. No radiation to legs, no numbness or weakness. No bowel/bladder issues.
Tried ibuprofen with modest relief.

PMH: unremarkable. No prior back problems.
Meds: none regular.

Exam: paraspinal muscle tenderness bilaterally at L4-L5. Straight leg raise
negative. Normal strength and sensation in lower extremities.

Assessment/Plan:
  1. Low back pain, acute, unspecified — consistent with muscular strain
     - ibuprofen 600mg TID with food
     - heat, stretching, avoid heavy lifting
     - follow up in 2 weeks if not improved""",
        "expected_codes": ["M54.5", "S39.012A"],
    },

    "case_04_pneumonia": {
        "title": "Case 4 — Community-acquired pneumonia",
        "note": """Chief Complaint: 29 yo F with 5 days of cough, fever, and chest pain.

HPI: Cough initially dry, now productive of yellow sputum. Subjective fever
with chills. Pleuritic right-sided chest pain. No recent travel, no sick contacts
at home but is a schoolteacher.

PMH: asthma, controlled on albuterol PRN.
Meds: albuterol inhaler.

Exam: T 38.9, RR 22, SpO2 95%. Crackles right lower lobe.
CXR: right lower lobe infiltrate.

Assessment/Plan:
  1. Community-acquired pneumonia, right lower lobe
     - amoxicillin-clavulanate 875/125 BID x7 days
     - return if symptoms worsen or SpO2 drops
  2. Asthma, well controlled""",
        "expected_codes": ["J18.1", "J45.909"],
    },

    "case_05_chest_pain_eval": {
        "title": "Case 5 — Chest pain evaluation",
        "note": """Chief Complaint: 58 yo M with intermittent chest pain x1 week.

HPI: Substernal pressure, comes on with walking up stairs, resolves with rest
within 2-3 minutes. No associated SOB, no radiation. No episodes at rest.
Family history of early CAD (father MI at 55).

PMH: hypertension, hyperlipidemia.
Meds: hydrochlorothiazide 25mg, rosuvastatin 20mg.

Exam: BP 142/88. Heart RRR, no murmurs. Lungs clear.
ECG: normal sinus rhythm, no acute ST changes.

Assessment/Plan:
  1. Chest pain, suspected stable angina pectoris — start aspirin 81mg, metoprolol
     25mg BID, refer to cardiology for stress testing this week
  2. HTN — uncontrolled, consider adding ACE inhibitor
  3. Hyperlipidemia, on statin""",
        "expected_codes": ["I20.9", "I10", "E78.5", "Z82.49"],
    },
}


def list_cases() -> list[str]:
    return list(DEMO_NOTES.keys())


def get_note(key: str) -> dict:
    return DEMO_NOTES[key]
