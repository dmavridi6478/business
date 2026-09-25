---
name: kesha-voice-kit
description: Lightweight voice interaction toolkit for AI agents — wraps speech-to-text (STT) and text-to-speech (TTS) into a simple Python interface. Use when you want to add voice I/O to a chatbot, Claude tool, or automation script without wiring multiple STT/TTS libraries separately.
---

# Kesha Voice Kit — Voice I/O Toolkit for AI Agents

A Python toolkit that bundles speech recognition and speech synthesis for fast voice-first agent prototyping.

## What it replaces

Hand-rolling the STT + TTS plumbing when all you need is voice in/out on top of a language model.

## Key capabilities

- **Speech-to-text**: Microphone capture → text via Whisper or cloud STT
- **Text-to-speech**: Agent response → audio playback
- **Agent integration**: Drop-in voice layer for any Python chatbot or Claude tool use loop
- **Configurable backends**: Swap STT/TTS providers through config

## When to reach for it

- You want a talking agent demo in under an hour
- Building accessibility tooling that needs voice I/O
- Prototyping a voice interface for a Claude-based assistant
- Teaching voice AI integration without writing audio pipeline boilerplate

## Stack

Python · Whisper (or cloud STT) · pyttsx3 / ElevenLabs (TTS)

## Clone

```bash
git clone https://github.com/drakulavich/kesha-voice-kit
```

## Quickstart

```bash
pip install -r requirements.txt
python main.py
```
