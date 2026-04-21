# ICD-10 Coding SLM — Teaching Project

An educational pipeline showing how to take a generic small language model and
specialize it for a real healthcare task — **ICD-10-CM diagnosis coding** — then
shrink it, wrap it in a RAG-backed agent, and demo it.

> ⚠️ **Educational use only.** Not a certified coding tool. Not medical advice.
> No real patient data. Fine-tuned on a noisy public dataset; expect label errors.

---

## What you'll actually build and prove

We're deliberate about honest claims. Here's the scope:

| ✅ Provable | ❌ Out of scope for this project |
|---|---|
| Fine-tuning fixes generic model's format errors | Full doctor's note → multi-code (we chunk it) |
| Fine-tuned > base on held-out test data | Works on real-world clinical notes (synthetic demos only) |
| Q4 quantization preserves ~95%+ of FP16 accuracy | Fine-tuning improves tool-calling (we don't train that) |
| Q4 model is smaller (3.4 GB → ~1.1 GB) | Production-grade (it's educational) |
| Q4 model is faster on CPU | |
| Q4 size fits on a Raspberry Pi (theoretical) | |
| Agent + RAG + tools > any single component | |

The demo workflow: pre-crafted doctor's notes are **chunked** into short
phrases, each phrase is coded by the fine-tuned model, the agent validates
each code against the CMS codebook, and the Streamlit app shows the result
side-by-side against the base model.

---

## Architecture

```
     Doctor's note (text)
            │
            ▼
     ┌──────────────┐
     │ Note chunker │   src/note_chunker.py
     │  (phrases)   │
     └──────┬───────┘
            │
      for each phrase:
            ▼
  ┌─────────────────────┐       ┌──────────────┐
  │ Fine-tuned Qwen3-Q4 │◄─────┤ Tool: lookup │
  │   (~1.1 GB GGUF)    │       │ Tool: validate│
  └──────────┬──────────┘       │ Tool: search │
             │                  │ Tool: hierarchy│
             │                  └──────────────┘
             ▼
      ┌──────────────┐
      │ RAG retrieval│   FAISS over 70k ICD codes
      └──────┬───────┘
             │
             ▼
    Deduplicated list of (code, description) pairs
```

---

## Notebook flow

| Notebook | What happens | GPU? |
|---|---|---|
| `00_setup.ipynb`                  | Session bootstrap — git pull, mount Drive, verify env | CPU |
| `01_data_collection.ipynb`        | Download + clean `krishnareddy/icddxdescmap`, EDA, split | CPU |
| `02_finetuning.ipynb`             | QLoRA fine-tune Qwen3-1.7B on 5k codes                | **L4 GPU** |
| `03_quantization_and_benchmarks.ipynb` | Merge adapter → FP16 → Q4 GGUF; benchmark speed/size/accuracy | T4 |
| `04_agent_chatbot.ipynb`          | FAISS index, 4 tools, custom agent loop, note chunking | CPU |

Demo: `streamlit run app/streamlit_app.py` — side-by-side base vs. fine-tuned+agent.

---

## Quick start

### First time: clone from GitHub

```bash
# Replace YOUR-USERNAME with your GitHub handle
git clone https://github.com/YOUR-USERNAME/icd10-slm.git
cd icd10-slm
pip install -r requirements.txt
```

### On Colab

Open `notebooks/00_setup.ipynb` — it handles everything:
1. Mounts Drive
2. Clones/pulls repo into Drive
3. Verifies environment
4. Shows project status dashboard

---

## What you need

| Item | Where to get | Secret name in Colab |
|---|---|---|
| HuggingFace token | https://huggingface.co/settings/tokens | `HF_TOKEN` |
| GitHub PAT (for push) | https://github.com/settings/tokens | `GITHUB_TOKEN` |
| GitHub username | your profile | `GITHUB_USERNAME` |

---

## The core lesson

**No single technique wins alone for knowledge-intensive domain tasks.**

- **Fine-tuning** teaches task *format* (→ valid ICD-10 codes)
- **Retrieval** provides factual *coverage* (→ knows about all 70k codes, not just trained 5k)
- **Quantization** enables *deployment economics* (→ 1.1 GB, CPU-friendly)
- **Tool validation** corrects residual *hallucination* (→ refuses non-existent codes)

You'll prove this quantitatively with an ablation matrix at the end of Notebook 4.

---

## Repository structure

```
icd10-slm/
├── README.md                                 ← this file
├── requirements.txt
├── .gitignore
├── .env.example
├── data/
│   ├── raw/                                  (gitignored)
│   ├── processed/                            (gitignored)
│   └── demo_notes/                           ← 5 hand-crafted clinical notes
├── notebooks/                                ← ALL committed to git
├── app/
│   ├── streamlit_app.py
│   ├── agent.py
│   └── demo_notes.py
├── src/
│   ├── config.py
│   ├── tools.py
│   ├── rag.py
│   ├── note_chunker.py                       ← splits notes → phrases
│   ├── eval.py
│   └── benchmarks.py                         ← size/speed/accuracy measurement
├── models/                                   (gitignored)
├── tests/
└── docs/
    ├── pi_deployment.md                      ← theoretical specs for Pi
    └── teaching_notes.md                     ← discussion prompts per notebook
```

---

## License

MIT. Individual datasets retain their own licenses.
