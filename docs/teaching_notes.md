# Teaching Notes — Discussion Prompts per Notebook

## Notebook 1 — Data Collection

**After Section 4 (quality filter):**
> Every filter is a value judgment. Which filters would you add? Which might
> be too aggressive? What biases could filtering introduce into your training set?

**After Section 5 (long-tail plot):**
> You see the Zipf-like distribution. If you had to choose between: (a)
> training on the 500 most common codes perfectly, or (b) training on 5,000
> codes mediocrely, which would you pick for a production system? Why?

## Notebook 2 — Fine-tuning

**After training completes:**
> Training loss dropped from ~2.1 to ~0.6. What portion of that is the model
> learning the *format* (producing `E11.9`-shaped strings) vs. learning the
> *mapping* (knowing that specific conditions map to specific codes)?
> How would you disentangle these?

## Notebook 3 — Quantization and Benchmarks

**After Q4 accuracy drop:**
> You likely saw a 2-4% accuracy drop going from FP16 to Q4. For which
> applications is this acceptable? For which isn't it? How would you decide
> as a product manager?

**After speed benchmark:**
> Q4 was faster on CPU but possibly slower on GPU. Why? When does this matter
> for deployment decisions?

## Notebook 4 — Agent

**After 5-config eval:**
> The FT+RAG+Tools configuration wins. But which component contributed the
> most? How would you A/B test to isolate each effect?

**After running demo notes:**
> The agent can code individual phrases well, but the *note chunker* is rule-
> based and brittle. How would you improve the chunker? Would a second LLM
> call be worth the added latency?
