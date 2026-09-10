# -*- coding: utf-8 -*-
"""Retail Sales Manager (Store Operations) - CubeSmart, Fremont, CA.

Varied Bay Area storage/property employers (Oakland, Hayward, Union City).
English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "Fremont, CA",
    "target_title": "Retail Sales Manager (Self Storage)",
    "filename": "Brendan_Nforbi_CubeSmart_Retail_Manager_Resume.pdf",
    "summary": (
        "Self-driven storage and retail leader with 5+ years running Bay Area storefronts, now "
        "targeting the CubeSmart Retail Sales Manager role in Fremont. Manages and maintains the "
        "property end to end: builds rapport face to face, identifies storage needs, recommends "
        "solutions, and delivers standout experiences that meet monthly sales goals. Rents spaces, "
        "sells merchandise, runs leasing, POS payments, deposits, and late-payment courtesy calls, "
        "plus invoice review, reports, auction paperwork, and expense and supply control. Walks the "
        "property daily for lock checks and showings and keeps units, doors, restrooms, and grounds "
        "clean and safe. Holds a valid license with personal vehicle, insurance, and US work "
        "authorization plus MS Office skills. Fluent in English, positive and outgoing, available "
        "Saturdays. Able to stand, kneel, crouch, climb ladders, and open doors up to 50 lbs."
    ),
    "competencies": [
        "Property Management & Upkeep",
        "Needs-Based Storage Sales",
        "Face-to-Face Rapport",
        "Monthly Goals & Metrics",
        "Leasing, POS & Deposits",
        "Invoices, Reports & Auctions",
        "Expense & Supply Control",
        "Lock Checks & Showings",
        "Cleaning & Light Maintenance",
        "MS Office & Databases",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Assistant Store Manager",
            "company": "Public Storage, Oakland, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Manage daily storefront: rent spaces, sell merchandise, run leasing, POS payments, and deposits",
                "Build rapport, identify storage needs, and close solutions that meet monthly sales goals",
                "Walk the property for lock checks and showings and handle invoices, reports, and auction paperwork",
                "Keep units, doors up to 50 lbs, restrooms, and grounds clean, safe, and guideline-ready",
            ],
        },
        {
            "title": "Storage Associate",
            "company": "Extra Space Storage, Hayward, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Served diverse customers in person and by phone with late-payment courtesy calls",
                "Controlled expenses and supplies while keeping retail inventory accurate",
                "Maintained facility with mopping, sweeping, bulbs, and cleanouts including ladders",
            ],
        },
        {
            "title": "Customer Service Associate",
            "company": "U-Haul, Union City, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Rented trucks and units with clear contracts and safe handoffs",
                "Drove personal vehicle between sites with valid license and insurance and Saturday coverage",
                "Trained 5 new associates on service, safety, and store standards",
            ],
        },
    ],
    "certifications": [
        "Valid License + Personal Vehicle + Insurance",
        "Workplace Safety Training",
        "First Aid / CPR Certified",
    ],
}
