"""Custom tool-calling agent. Implemented in Notebook 4."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentStep:
    role: str
    content: str | None = None
    tool_name: str | None = None
    tool_args: dict[str, Any] | None = None
    tool_result: Any = None


@dataclass
class AgentResult:
    final_code: str
    justification: str
    steps: list[AgentStep] = field(default_factory=list)
    total_tokens: int = 0
    latency_ms: float = 0.0


class ICD10CodingAgent:
    def __init__(self, model_path: str, max_iterations: int = 5):
        self.model_path = model_path
        self.max_iterations = max_iterations

    def _load(self) -> None:
        raise NotImplementedError("See Notebook 4, Section 4.1")

    def code(self, clinical_description: str) -> AgentResult:
        raise NotImplementedError("See Notebook 4, Section 4.2")
