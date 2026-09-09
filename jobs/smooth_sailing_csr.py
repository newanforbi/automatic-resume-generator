# -*- coding: utf-8 -*-
"""Customer Service Representative (Nonprofit Outreach) - San Jose, CA 95112.

History is retargeted to analogous Bay Area community outreach, event,
and customer service roles (same date spans).
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Customer Service Representative (Community Outreach)",
    "filename": "Brendan_Nforbi_Community_Outreach_CSR_Resume.pdf",
    "summary": (
        "Friendly, people-focused service associate with 5+ years engaging Bay Area customers "
        "in person, now targeting the nonprofit outreach Customer Service Representative role in "
        "San Jose. Creates a welcoming experience at busy event and retail sites: greets every "
        "guest, shares clear program information, answers questions, and helps with sign-ups and "
        "contributions following set guidelines. Upbeat on my feet for full day shifts indoors and "
        "outdoors, tracks outreach numbers, and keeps set-up, breakdown, and site standards sharp. "
        "Bilingual in English and Spanish with reliable transportation and a valid California Class C "
        "license. Available for full-time day shift, in person."
    ),
    "competencies": [
        "In-Person Community Engagement",
        "Donor & Customer Service",
        "Sign-Ups & Contribution Support",
        "Mission & Program Storytelling",
        "De-Escalation & Problem Solving",
        "Outreach Tracking & Team Updates",
        "Event Set-Up & Breakdown",
        "Day-Shift Reliability",
        "Valid CA Class C License",
        "Outdoor & Indoor Event Stamina",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Community Outreach Associate",
            "company": "Goodwill of Silicon Valley, San Jose, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Engage community members at busy in-person sites, creating a welcoming experience and connecting supporters to programs and giving options",
                "Share simple, accurate mission information and answer questions on services, sign-ups, and contributions following clear guidelines",
                "Track daily outreach counts and communicate updates to the team lead while holding set-up, breakdown, and site professionalism standards",
                "Stay upbeat on my feet across full day shifts indoors and outdoors in English and Spanish",
            ],
        },
        {
            "title": "Customer Service Associate",
            "company": "Target, Milpitas, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Greeted every guest, answered product and service questions, and guided sign-ups for loyalty and registry with a customer-first attitude",
                "Resolved concerns calmly at the service desk and kept accurate transaction and account records",
                "Supported weekend rushes and team coverage while standing and walking the full shift",
            ],
        },
        {
            "title": "Event Support Associate",
            "company": "SAP Center Event Staff, San Jose, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Welcomed large crowds, gave directions, and kept entry and concourse areas safe and professional",
                "Assisted with booth set-up and breakdown and answered event questions for first-time visitors",
                "Trained 5 new associates on greeting standards, site rules, and customer care",
            ],
        },
    ],
    "certifications": [
        "Valid California Class C License",
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
