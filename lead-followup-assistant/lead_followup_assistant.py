"""
AI Lead Follow-Up Assistant
----------------------------
A tool that reads a list of CRM leads, autonomously decides which ones
need follow-up based on engagement rules, and drafts a personalized
follow-up email for each one by calling the Claude API programmatically.

This demonstrates:
  1. Programmatic AI API usage (no chat interface — the script calls
     Claude directly in code).
  2. Lightweight agentic decision-making (the script decides WHICH
     leads to act on, not just what to say, based on business rules).
  3. A reusable tool other marketers could run against their own
     exported CRM lead lists.

Usage:
  export ANTHROPIC_API_KEY="your-key-here"
  python3 lead_followup_assistant.py sample_leads.csv
"""

import csv
import os
import sys
from datetime import datetime
import anthropic

# ---------------------------------------------------------------------
# STEP 1: Decision rules (the "agentic" part — deciding WHO gets acted on)
# ---------------------------------------------------------------------
# A lead qualifies for automated follow-up if:
#   - It's been more than 3 days since last contact, AND
#   - The lead is not already "New" (those get a different, faster-touch flow)
#   - The lead has NOT gone cold (more than 30 days = needs a human decision,
#     not an automated touch, so we skip those and flag them instead)

FOLLOW_UP_MIN_DAYS = 3
COLD_LEAD_THRESHOLD_DAYS = 30


def needs_followup(lead):
    """Returns 'follow_up', 'too_new', or 'needs_human_review'."""
    days = int(lead["last_contact_days_ago"])
    stage = lead["stage"].strip().lower()

    if days > COLD_LEAD_THRESHOLD_DAYS:
        return "needs_human_review"
    if stage == "new" and days < FOLLOW_UP_MIN_DAYS:
        return "too_new"
    if days >= FOLLOW_UP_MIN_DAYS:
        return "follow_up"
    return "too_new"


# ---------------------------------------------------------------------
# STEP 2: The actual AI call — this is the programmatic API usage piece
# ---------------------------------------------------------------------

def draft_followup_email(client, lead):
    """Calls the Claude API directly (no chat UI) to draft a follow-up email."""

    prompt = f"""You are a marketing operations assistant drafting a short,
professional follow-up email on behalf of a B2B software company (ProShop,
an ERP/MES/QMS platform for metalworking and aerospace machine shops).

Lead details:
- Name: {lead['name']}
- Job title: {lead['job_title']}
- Company: {lead['company']}
- Pipeline stage: {lead['stage']}
- Days since last contact: {lead['last_contact_days_ago']}
- Stated interest: {lead['interest']}
- Last interaction: {lead['last_interaction_note']}

Write a short (under 120 words), warm, non-pushy follow-up email.
Reference their specific stated interest and last interaction naturally.
Include one clear, low-friction next step (e.g., a quick call or a
relevant resource), not a hard sell.
Output ONLY the email body text, no subject line, no preamble."""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


# ---------------------------------------------------------------------
# STEP 3: Orchestration — read leads, apply rules, call AI, report results
# ---------------------------------------------------------------------

def main(csv_path):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Set the ANTHROPIC_API_KEY environment variable first.")
        print('  export ANTHROPIC_API_KEY="your-key-here"')
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    with open(csv_path, newline="") as f:
        leads = list(csv.DictReader(f))

    print(f"Loaded {len(leads)} leads from {csv_path}\n")
    print("=" * 70)

    drafted_count = 0
    flagged_count = 0
    skipped_count = 0

    for lead in leads:
        decision = needs_followup(lead)
        print(f"\n{lead['name']} ({lead['company']}) — {lead['stage']}, "
              f"{lead['last_contact_days_ago']} days since contact")

        if decision == "follow_up":
            print("  -> DECISION: Draft automated follow-up email")
            email = draft_followup_email(client, lead)
            print("  -> DRAFTED EMAIL:")
            print("  " + "-" * 50)
            for line in email.split("\n"):
                print(f"  {line}")
            print("  " + "-" * 50)
            drafted_count += 1

        elif decision == "needs_human_review":
            print("  -> DECISION: Lead is cold (30+ days) — flagged for "
                  "human review, not auto-drafted")
            flagged_count += 1

        else:
            print("  -> DECISION: Too new for automated touch yet — skipped")
            skipped_count += 1

    print("\n" + "=" * 70)
    print(f"Summary: {drafted_count} emails drafted | "
          f"{flagged_count} flagged for human review | "
          f"{skipped_count} skipped (too new)")


if __name__ == "__main__":
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "sample_leads.csv"
    main(csv_file)
