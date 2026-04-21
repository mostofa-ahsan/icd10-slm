"""Central configuration — all paths, models, prompts live here."""
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
DEMO_NOTES_DIR = DATA_DIR / "demo_notes"
MODELS_DIR = REPO_ROOT / "models"

TRAIN_PATH = PROCESSED_DIR / "train.jsonl"
VAL_PATH = PROCESSED_DIR / "val.jsonl"
TEST_PATH = PROCESSED_DIR / "test.jsonl"
CODEBOOK_PATH = PROCESSED_DIR / "icd10_codebook.parquet"

ADAPTER_DIR = MODELS_DIR / "adapter"
MERGED_DIR = MODELS_DIR / "merged-fp16"
GGUF_PATH = MODELS_DIR / "merged-q4.gguf"
RAG_INDEX_DIR = MODELS_DIR / "rag_index"

# Model
BASE_MODEL = "Qwen/Qwen3-1.7B"

# Data
TRAINING_DATASET = "krishnareddy/icddxdescmap"
MIN_EXAMPLES_PER_CODE = 5
TOP_K_CODES_TO_EXCLUDE = 20
TARGET_NUM_CODES = 5000

# Training
MAX_SEQ_LENGTH = 512
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05

# RAG
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
RAG_TOP_K = 10

# Prompts
SYSTEM_PROMPT = (
    "You are an expert clinical coder. Given a clinical description, "
    "respond with the single most appropriate ICD-10-CM code in the format "
    "LLL.XX (e.g., E11.9, J45.909). Output ONLY the code, no commentary."
)

AGENT_SYSTEM_PROMPT = (
    "You are an expert clinical coder with access to tools for validating "
    "ICD-10-CM codes. For each clinical description:\n"
    "1. Propose a candidate code.\n"
    "2. Use validate_code to confirm it exists.\n"
    "3. If invalid, use icd10_search to find candidates, then pick the best.\n"
    "4. Return the final code with a one-line justification."
)
