# -*- coding: utf-8 -*-
"""Truck Rental Agent - Monarch Truck Center, San Jose, CA 95133.

Varied Bay Area truck/rental employers (Oakland, Hayward, Redwood City).
English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Truck Rental Agent",
    "filename": "Brendan_Nforbi_Monarch_Rental_Agent_Resume.pdf",
    "summary": (
        "Service-minded rental associate with 5+ years across Bay Area vehicle rental, truck, and "
        "counter operations, now targeting the Monarch Truck Rental Agent role in San Jose. Works "
        "the rental counter daily: answers phones, quotes rates, takes reservations, explains "
        "insurance and verifies coverage, opens and closes contracts, checks trucks in and out, "
        "processes long-term invoices, collects payments, and calls customers for service and "
        "inspections. Handles filing, copying, scanning, and faxing with MS Outlook and Excel and "
        "sells during slow periods to grow business. Holds a valid California license with a good "
        "record and can pass a drug screen. Fluent in English, climbs in and out of larger trucks, "
        "lifts up to 25 lbs, and is available full-time day shift in person."
    ),
    "competencies": [
        "Rental Counter & Reservations",
        "Rate Quotes & Contracts",
        "Insurance Verification",
        "Truck Check-In & Check-Out",
        "Invoices & Payment Collection",
        "Service & Inspection Scheduling",
        "Phones & Team Communication",
        "MS Outlook & Excel Admin",
        "Filing, Copying & Scanning",
        "Upselling & Business Growth",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Truck Rental Agent",
            "company": "Penske Truck Rental, Oakland, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Work the rental counter: quote rates, take reservations, and open and close contracts accurately",
                "Explain insurance requirements, verify customer coverage, and check trucks in and out",
                "Process monthly long-term invoices, collect payments, and call customers for service and inspections",
                "Climb in and out of larger trucks and handle admin filing, scanning, and MS Outlook and Excel work",
            ],
        },
        {
            "title": "Rental Counter Associate",
            "company": "Enterprise Truck Rental, Hayward, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Answered high-volume phones and booked reservations with friendly, professional communication",
                "Verified licenses and insurance and kept contract paperwork exact for audit-ready files",
                "Sold add-ons during slow periods to grow branch revenue",
            ],
        },
        {
            "title": "Customer Service Associate",
            "company": "Ryder, Redwood City, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Supported drivers and walk-ins with check-ins, directions, and service coordination",
                "Kept office admin sharp with copying, faxing, and organized records",
                "Trained 5 new associates on counter standards and safety",
            ],
        },
    ],
    "certifications": [
        "Valid California License, Good Record",
        "Workplace Safety Training",
        "First Aid / CPR Certified",
    ],
}
