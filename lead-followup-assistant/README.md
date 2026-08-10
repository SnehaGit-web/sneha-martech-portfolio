[README.md](https://github.com/user-attachments/files/30913919/README.md)
# AI Lead Follow-Up Assistant

A working example of building **with** AI, not just using it as a chat assistant. This tool reads a list of CRM leads, autonomously decides which ones need follow-up based on engagement rules, and drafts a personalized outreach email for each qualifying lead by calling Claude's API directly in code.

## What makes this "building with AI" rather than "using AI as a chatbot"

- **Programmatic API usage**: `lead_followup_assistant.py` calls `anthropic.Anthropic().messages.create()` directly in code. No chat interface, no copy-pasting a prompt by hand — the script sends the request and receives the response as part of an automated process.
- **Autonomous decision-making**: the tool doesn't just draft whatever it's told to. It applies real business rules (`needs_followup()`) to decide *which* leads to act on — skipping brand-new leads, flagging cold leads (30+ days) for human review instead of auto-drafting, and only generating emails for leads that genuinely qualify. That decision layer is what separates this from a simple "summarize this text" prompt.
- **Reusable by others**: any marketer could point this script at their own exported lead list (same CSV column structure) and get the same automated triage and drafting — it isn't a one-off, personal-use script.

## How it works

1. Reads a CRM lead export (CSV) with columns for name, company, pipeline stage, days since last contact, stated interest, and last interaction notes.
2. For each lead, applies rule-based logic to classify it as: `follow_up`, `too_new`, or `needs_human_review`.
3. For leads flagged `follow_up`, calls the Claude API to draft a short, context-aware follow-up email referencing that lead's specific interest and last interaction.
4. Prints a summary report: how many emails were drafted, how many leads were flagged for a human to review, and how many were skipped as too new.

## Try it yourself

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
python3 lead_followup_assistant.py sample_leads.csv
```

## Sample data

`sample_leads.csv` contains five fictional leads modeled on the ProShop ERP buyer persona work in the rest of this portfolio (manufacturing/aerospace operations managers), so the drafted emails reflect a realistic B2B context rather than generic placeholder text.

## Possible extensions

- Write drafted emails directly into a CRM via API (HubSpot/Salesforce) instead of printing them, closing the loop from "draft" to "ready to send."
- Add a lightweight web interface (Flask/simple HTML form) so a non-technical marketer could upload a CSV and download drafted emails without touching the command line.
- Chain into a scheduler (cron, or a workflow tool like n8n) to run automatically on a daily/weekly cadence against a live CRM export.
