"""FAISS retriever over ICD-10-CM descriptions. Implemented in Notebook 4."""
from __future__ import annotations
from pathlib import Path


class ICDRetriever:
    def __init__(self, embedding_model: str, index_dir: Path):
        self.embedding_model_name = embedding_model
        self.index_dir = Path(index_dir)

    def build_index(self, codebook) -> None:
        raise NotImplementedError("See Notebook 4, Section 2.1")

    def load_index(self) -> None:
        raise NotImplementedError("See Notebook 4, Section 2.2")

    def query(self, text: str, k: int = 10) -> list[dict]:
        raise NotImplementedError("See Notebook 4, Section 2.3")
