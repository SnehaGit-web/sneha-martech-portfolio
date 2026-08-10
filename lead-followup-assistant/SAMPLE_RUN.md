[SAMPLE_RUN.md](https://github.com/user-attachments/files/30913954/SAMPLE_RUN.md)
# Sample Run Output

Below is unedited output from an actual run of `lead_followup_assistant.py` against `sample_leads.csv`, using a live Claude API call. This confirms the tool works end to end: reading lead data, applying autonomous decision rules, and generating contextually accurate drafts via a programmatic API call (not a chat interface).

```
Loaded 5 leads from sample_leads.csv
======================================================================
Maria Santos (Precision AeroFab) — Marketing Qualified Lead, 9 days since contact
  -> DECISION: Draft automated follow-up email
  -> DRAFTED EMAIL:
  --------------------------------------------------
  Hi Maria,
  I hope the AS9100 audit readiness guide has been helpful as you explore ways to streamline quality documentation at Precision AeroFab.
  Since audit readiness is top of mind for you, I thought you might find value in seeing how other quality managers have used ProShop to cut audit prep time and maintain continuous compliance — rather than the usual scramble before each audit.
  Would a brief 15-minute call work for you this week or next? Happy to walk through a couple of specific examples relevant to your situation, or just answer any questions that came up while reviewing the guide.
  Either way, no pressure — just here if helpful.
  Best,
  --------------------------------------------------
David Chen (Ironworks Manufacturing) — Sales Qualified Lead, 4 days since contact
  -> DECISION: Draft automated follow-up email
  -> DRAFTED EMAIL:
  --------------------------------------------------
  Hi David,
  Thanks again for joining our live demo last week. I enjoyed your questions about ERP integration—it's clear you're thinking carefully about how this would work alongside your existing systems.
  Since you mentioned wanting better real-time production visibility, I thought you might find value in a quick 15-minute call to walk through how ProShop handles data synchronization with other ERPs. We can also discuss what a phased integration might look like for Ironworks Manufacturing specifically.
  Would sometime this week or early next work for a brief conversation? No pressure—just want to make sure you have what you need to evaluate if we're a good fit.
  Best,
  [Your name]
  --------------------------------------------------
Rachel Nowak (Northstar Machining Co.) — Marketing Qualified Lead, 21 days since contact
  -> DECISION: Draft automated follow-up email
  -> DRAFTED EMAIL:
  --------------------------------------------------
  Hi Rachel,
  I wanted to follow up since you joined our newsletter a few weeks ago. I hope you've found the content helpful.
  I know reducing manual work and administrative overhead was top of mind for you at Northstar Machining. We've helped similar shops cut their admin time by 40-60% by eliminating duplicate data entry and automating routine processes.
  I'd be happy to share a brief example of how a few aerospace shops have tackled this—no pressure, just a 15-minute conversation to see if there's anything relevant to your situation.
  Would sometime next week work for a quick call?
  Best regards,
  [Name]
  --------------------------------------------------
James Johnson (Apex Precision Metalworks) — New, 2 days since contact
  -> DECISION: Too new for automated touch yet — skipped
Tom Reilly (Reilly Fabrication) — Marketing Qualified Lead, 15 days since contact
  -> DECISION: Draft automated follow-up email
  -> DRAFTED EMAIL:
  --------------------------------------------------
  Hi Tom,
  I wanted to follow up since you'd opened a couple of our recent emails about audit compliance. I know staying ready for AS9100 or NADCAP audits without drowning in paperwork is a constant challenge for fabrication shops.
  If you're still exploring ways to streamline your audit trail and documentation, I'd be happy to send over a brief guide that shows how shops like yours are cutting audit prep time in half—or we could schedule a quick 15-minute call if that's more helpful.
  Either way, no pressure. Just wanted to make sure you had what you needed.
  Best regards,
  [Your name]
  --------------------------------------------------
======================================================================
Summary: 4 emails drafted | 0 flagged for human review | 1 skipped (too new)
```

## What this run demonstrates

- **Correct autonomous triage**: the tool correctly skipped James Johnson (2 days since contact, stage "New") while drafting for the four leads that met the follow-up criteria — a real decision, not a fixed template applied to everyone.
- **Context-aware drafting, not generic templating**: each email reflects the specific lead's stated interest and last interaction (Maria's audit-readiness guide download, David's ERP integration question from a live demo, Rachel's dormant newsletter signup, Tom's opened-but-unclicked emails) — pulled directly from the input data into the prompt sent to the API.
- **Stage-appropriate tone**: David (further along, post-demo) received a more advanced, integration-focused email; Rachel (cold, 21 days, newsletter-only engagement) received a lower-pressure, value-reintroduction email. This variation came from the model reasoning over the lead's actual stage and history, not from hardcoded logic.
