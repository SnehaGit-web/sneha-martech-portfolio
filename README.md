# Sneha Ann George — Marketing Technology Portfolio

Hands-on samples of marketing automation, CRM, and lifecycle email work, built to demonstrate practical skills alongside my HubSpot certifications (HubSpot Marketing Hub Software Certified, HubSpot Inbound Marketing Certified).

**Contact:** snehaanngeorge.ca@gmail.com · [LinkedIn](https://linkedin.com/in/sneha-ann-george)

---

## Case Study: Loopwork — Email Marketing & Lead Capture

A self-directed sample project: coded responsive HTML emails, lifecycle/behavioral email strategy, and a lead-capture research form.

**Loopwork** is a fictional B2B SaaS product used here purely as a design and copy vehicle — no real company, client data, or brand assets are used. All code, copy, and design decisions are original.

### What's in this case study

| File | Purpose | Buyer/customer stage |
|---|---|---|
| [`emails/email-01-welcome.html`](emails/email-01-welcome.html) | Day-0 onboarding email | New signup |
| [`emails/email-02-feature-announcement.html`](emails/email-02-feature-announcement.html) | Product/feature launch email | Active customer |
| [`emails/email-03-reengagement.html`](emails/email-03-reengagement.html) | Behavioral win-back email (21-day inactivity trigger) | Lapsed/at-risk customer |
| [`forms/survey-form.html`](forms/survey-form.html) | Product research / sales-enablement survey | Lead generation |

### Why these four pieces together

This is modeled as a small lifecycle marketing program rather than four disconnected samples:

- The **survey form** represents the kind of market-research capture used to inform segmentation and messaging — the same pattern used for structured lead data collection from sales agents in a past role.
- The **welcome email** covers the acquisition/onboarding trigger.
- The **feature announcement** covers ongoing lifecycle engagement for active users.
- The **re-engagement email** covers behavioral remarketing — re-targeting based on inactivity, a technique used in production for SendGrid-based customer journeys.

### Screenshots

<table>
<tr>
<td><img src="screenshots/email-01-welcome.png" width="260"><br><sub>Welcome email</sub></td>
<td><img src="screenshots/email-02-feature-announcement.png" width="260"><br><sub>Feature announcement</sub></td>
<td><img src="screenshots/email-03-reengagement.png" width="260"><br><sub>Re-engagement email</sub></td>
</tr>
</table>

<img src="screenshots/survey-form.png" width="320"><br><sub>Survey form</sub>

### Technical notes

**Emails** are built as production-style HTML email, not modern web HTML:
- Table-based layout (`role="presentation"` tables), not flexbox/grid — required for consistent rendering across Outlook, Gmail, and Apple Mail
- Inline and embedded styles with MSO conditional comments for Outlook compatibility
- Hidden preheader text for inbox preview lines
- "Bulletproof" button technique (padded table cell, not just a styled `<a>` tag) for reliable rendering in Outlook
- Mobile-responsive via media queries, with a 600px max-width container
- Every CTA link includes UTM parameters (`utm_source`, `utm_medium`, `utm_campaign`) for campaign attribution

**Survey form** uses semantic HTML (`fieldset`/`legend` grouping, required-field indicators) for accessibility, and modern CSS since it's a standard web page rather than an email client target.

### How to view

Open any `.html` file directly in a browser, or view the screenshots above.
