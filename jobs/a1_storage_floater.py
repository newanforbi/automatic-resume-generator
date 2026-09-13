# -*- coding: utf-8 -*-
"""Self Storage Store Associate (District Floater) - A1 Self Storage, San Jose, CA.

Varied Bay Area property/service employers (Oakland, Concord, Fremont).
English-only per record request (posting lists Spanish as a plus only).
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Self Storage Store Associate (District Floater)",
    "filename": "Brendan_Nforbi_A1_Storage_Floater_Resume.pdf",
    "summary": (
        "Customer-focused associate with 5+ years in Bay Area retail, service, and property-front "
        "roles, now targeting the A1 Self Storage District Floater role. Shows and rents units, "
        "completes paperwork accurately, and follows up on tenant questions in person, online, and "
        "by phone. Mixes office work with grounds walks and tenant interaction plus routine "
        "janitorial care. Holds a valid California Class C license with reliable transportation, "
        "insurance, and a clean DMV record and rotates daily between San Jose, Oakland, and Concord "
        "with mileage. Detail-oriented, organized, and strong with MS Word, Excel, and Outlook. "
        "Fluent in English with excellent written and verbal communication. Available full time 5 "
        "days including weekends for Mon-Fri 9-6 and Sat-Sun 9-5 coverage. Able to sit, stand, and "
        "walk all shift and pass an alcohol and drug screening."
    ),
    "competencies": [
        "Unit Showings & Rentals",
        "In-Person, Online & Phone Service",
        "Paperwork & Follow-Up",
        "Grounds Walks & Inspections",
        "Routine Janitorial Care",
        "Daily Multi-Site Rotation",
        "Valid CA Class C + Clean DMV",
        "MS Word, Excel & Outlook",
        "Detail, Organized & Multitasking",
        "Independent, Minimal Supervision",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Leasing Associate",
            "company": "Greystar Apartments, Oakland, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Show and lease units to new tenants in person, online, and by phone with accurate paperwork and follow-up",
                "Walk grounds daily for readiness, safety, and curb appeal plus light janitorial care",
                "Track leads, occupancies, and tenant issues with detail in MS Word, Excel, and Outlook",
                "Rotate coverage between nearby communities with reliable transportation and clean DMV record",
            ],
        },
        {
            "title": "Store Associate",
            "company": "Public Storage, Concord, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Rented storage units, collected payments, and completed move-in paperwork per policy",
                "Answered phones, solved tenant questions, and kept offices and grounds clean and professional",
                "Worked independently with minimal supervision across full-time schedules including weekends",
            ],
        },
        {
            "title": "Customer Service Associate",
            "company": "Home Depot, Fremont, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Helped customers with friendly service while standing, walking, and lifting across the shift",
                "Kept aisles stocked, faced, and safe with strong multitasking and organization",
                "Trained 5 new associates on service, safety, and store standards",
            ],
        },
    ],
    "certifications": [
        "Valid California Class C License, Clean DMV + Insurance",
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
