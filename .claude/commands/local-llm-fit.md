---
description: Check whether a very large local model (such as a 125B split across GPU, RAM and SSD) fits your hardware and is worth it
argument-hint: <GPU and VRAM, RAM, free SSD, task>
---

Use skill `buildwithneej-5-repos-oct9`. For "$ARGUMENTS" estimate whether a 125B-parameter model compressed for GPU plus RAM plus SSD offloading would run: memory and disk needed (the slides say about 70 GB download and 32 to 64 GB RAM), likely tokens per second (the maker reports 53 to 94 on an RTX 5070 12 GB at different compression levels), and the quality loss to expect. Compare with a smaller local model and a hosted API for the same task, and recommend one test to run first. Remind me to bind any local API to 127.0.0.1.
