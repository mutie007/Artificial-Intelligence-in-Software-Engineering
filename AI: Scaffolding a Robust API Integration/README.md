# AI: Scaffolding a Robust API Integration

## Description
This task demonstrates the use of Contextual Prompting to improve a Python API client by adding secure API key handling and better error handling.

## Files
- `initial_sentiment_analyzer.py` → Original code before AI refinement
- `refined_sentiment_analyzer.py` → Final code after AI refinement

## AI Tool Used
Claude (Contextual Prompting)

## Key Improvements
- API key loaded from environment variable `TEXT_PROCESSING_API_KEY`
- Authorization header using Bearer token
- Explicit handling of `Timeout` and `ConnectionError` exceptions
