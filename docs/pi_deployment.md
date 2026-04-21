# Raspberry Pi Deployment (Theoretical)

## Scope

This document shows that the Q4-quantized fine-tuned Qwen3-1.7B model is
**feasible** on a Raspberry Pi 4 or Pi 5. We do not include actual Pi
benchmark numbers — only a theoretical feasibility analysis from CPU
measurements in Notebook 3.

## Model size on disk

| Artifact | Size (MB) |
|---|---|
| Base Qwen3-1.7B (FP16)      | ~3,400 |
| Fine-tuned + merged (FP16)  | ~3,400 |
| **Fine-tuned Q4_K_M GGUF**  | **~1,100** |

## Memory requirements at inference

| Component | Approx |
|---|---|
| Model weights (memory-mapped) | 1,100 MB |
| KV cache @ 2048 context       | ~150 MB |
| llama.cpp runtime overhead    | ~100 MB |
| **Total**                     | **~1,350 MB** |

## Pi platform feasibility

| Platform | RAM | Verdict |
|---|---|---|
| Raspberry Pi 3B+  | 1 GB | ❌ Insufficient |
| Raspberry Pi 4 (2 GB) | 2 GB | ⚠️ Tight — swap risk |
| **Raspberry Pi 4 (4 GB)** | 4 GB | ✅ Fits comfortably |
| Raspberry Pi 5 (4 GB) | 4 GB | ✅ Better performance per watt |
| Raspberry Pi 5 (8 GB) | 8 GB | ✅ Plenty of headroom |

## Expected throughput (extrapolated from Colab CPU)

Based on tokens/sec measurements in Notebook 3 running on Colab's CPU:

| Platform | Est. tokens/sec |
|---|---|
| Colab CPU (Intel Xeon) | *see Notebook 3 measurement* |
| Raspberry Pi 4 | ~40-60% of Colab CPU |
| Raspberry Pi 5 | ~70-90% of Colab CPU |

For a ~5 word ICD-10 code output (~8 tokens), expect **1-2 second latency**
on Pi 4 and **under 1 second** on Pi 5.

## What we did NOT verify

- Actual tokens/sec on real Pi hardware
- Thermal throttling under sustained load
- Storage I/O impact from mmap on SD card vs. USB SSD

Running on a real Pi is left as an exercise. The ingredients are:

```bash
# On the Pi
pip install llama-cpp-python
python -c "
from llama_cpp import Llama
llm = Llama(model_path='merged-q4.gguf', n_ctx=2048)
print(llm('Patient with shortness of breath. ICD-10:', max_tokens=16))
"
```
