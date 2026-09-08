# Automatic Resume Generator

Paste a job posting. This repo stores Brendan Ngwa Nforbi's identity facts and renders a **one-page, ATS-friendly PDF** targeted at that role.

```bash
python3 generate_resume.py jobs.staples_print_specialist
```

- `candidate.py` — name, contact, education, languages. These stay stable.
- `jobs/` — one module per application. Rewrite titles, Bay Area employers, and bullets to analogous work for that specific job. Keep the same date spans. Do not reuse a warehouse history on a retail/print posting (or the reverse).
- `generate_resume.py` — Helvetica, navy headers, letter size, one page.
