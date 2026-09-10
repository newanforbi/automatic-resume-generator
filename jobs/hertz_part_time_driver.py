# -*- coding: utf-8 -*-
"""Part Time Driver - Hertz, San Jose, CA ($18.70/hr).

Airport-focused driving history with varied Bay Area employers
(Burlingame/SFO, Oakland, San Jose) per variety request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Part Time Driver",
    "filename": "Brendan_Nforbi_Hertz_Part_Time_Driver_Resume.pdf",
    "summary": (
        "Safe, high-energy driver with 4+ years moving vehicles and parcels across the Bay Area, "
        "now targeting the Hertz Part Time Driver role in San Jose. Transports vehicles safely "
        "within airport and service areas and between on- and off-airport locations while providing "
        "outstanding customer service with a courteous, professional appearance. Follows all safety "
        "policies to protect company assets and works with minimal supervision at a fast pace. Holds "
        "a valid California Class C license with a clean record and current DOT medical, is over 21, "
        "and is bilingual in English and Spanish with flexibility for weekends and holidays."
    ),
    "competencies": [
        "Airport & Service-Area Driving",
        "On/Off-Airport Vehicle Moves",
        "Outstanding Customer Service",
        "Courteous Professional Appearance",
        "Safety Policies & Asset Protection",
        "Minimal-Supervision Reliability",
        "GPS, Maps & Lot Coordination",
        "Vehicle Inspection & Fuel Checks",
        "Paperwork & Key Control",
        "Weekends & Holidays Flexibility",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Airport Shuttle Driver",
            "company": "Park N Fly, Burlingame, CA",
            "dates": f"Sep 2023 {EN} Present",
            "bullets": [
                "Transport passengers and vehicles safely around SFO-area lots and service areas with on-time loops",
                "Move vehicles between airport and off-airport locations while following all safety policies",
                "Provide outstanding customer service with courteous, professional behavior and appearance",
                "Inspect vehicles, track keys, and protect company assets with minimal supervision",
            ],
        },
        {
            "title": "Lot Attendant & Driver",
            "company": "Enterprise Rent-A-Car, Oakland, CA",
            "dates": f"Aug 2022 {EN} Aug 2023",
            "bullets": [
                "Shuttled rental vehicles between branches and service bays with GPS routing and clean record",
                "Prepped, fueled, and staged cars while keeping lots organized and secure",
                "Helped customers with directions and handoffs in a fast, high-energy operation",
            ],
        },
        {
            "title": "Courier Driver",
            "company": "OnTrac, San Jose, CA",
            "dates": f"Jan 2022 {EN} Jul 2022",
            "bullets": [
                "Ran multi-stop routes with phone scanning and proof-of-delivery paperwork",
                "Lifted packages up to 50 lbs with safe carries and strong attendance",
                "Covered weekend and holiday shifts during peak volume",
            ],
        },
    ],
    "certifications": [
        "Valid California Class C License, Clean Record",
        "DOT Medical Examiner's Certificate (current)",
        "Workplace Safety Training",
    ],
}
