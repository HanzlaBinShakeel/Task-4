# Task 4: General Health Query Chatbot (Prompt Engineering)

## Objective
Answer general health questions using an LLM with engineered prompts and safety filters.

## Tools
- **Default:** Hugging Face `google/flan-t5-small` + curated health knowledge (no API key)
- **Optional:** OpenAI GPT-3.5 (`OPENAI_API_KEY` in `.env`)

## Prompt Engineering
- System role: friendly health **information** assistant (not a doctor)
- Clear guidelines: no diagnosis, no prescriptions, encourage professional care
- Appended **disclaimer** on every response

## Safety Filters
Blocks or redirects:
- Self-harm / overdose requests
- “Diagnose me” / “stop medication” patterns
- Emergency symptoms → call emergency services

## Example Queries
- *What causes a sore throat?*
- *Is paracetamol safe for children?*

## Files
| File | Description |
|------|-------------|
| `health_chatbot.ipynb` | Demo notebook |
| `health_bot.py` | Chatbot module + CLI |
| `.env.example` | Optional OpenAI key template |

## Run
```bash
pip install -r requirements.txt

# Modern web UI (recommended)
streamlit run streamlit_app.py

# Notebook
jupyter notebook health_chatbot.ipynb

# Terminal chat
python health_bot.py
```
