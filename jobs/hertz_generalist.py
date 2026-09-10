# -*- coding: utf-8 -*-
"""Generalist Hertz resume covering Manager Trainee, Automotive Sales
Consultant, Sales and Service Specialist, and Part Time Driver roles
(Fremont, Mountain View, Santa Clara, Hayward, San Jose).

History uses varied Bay Area customer service, sales, and driving roles.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "Milpitas, CA",
    "target_title": "Sales & Service Associate (Manager Trainee Track)",
    "filename": "Brendan_Nforbi_Hertz_Generalist_Resume.pdf",
    "summary": (
        "Service-driven associate with 5+ years across Bay Area sales, customer service, and "
        "driving roles, targeting Hertz openings in Fremont, Mountain View, Santa Clara, Hayward, "
        "and San Jose. Delivers friendly counter and phone service, uncovers needs, recommends "
        "vehicles and protection options, and closes with clear paperwork. Prepares and coordinates "
        "vehicles, keeps lots and records organized, and drives safely on local routes "
        "and shuttles. Coaches new team members and welcomes a manager-trainee growth path. Holds a "
        "valid California Class C license with a clean record and current DOT medical, is over 21, "
        "and is bilingual in English and Spanish with flexible availability."
    ),
    "competencies": [
        "Counter & Phone Customer Service",
        "Vehicle & Protection Sales",
        "Needs Discovery & Closing",
        "Reservations & Paperwork Accuracy",
        "Vehicle Prep & Lot Coordination",
        "Safe Local Driving & Shuttles",
        "GPS, Maps & Route Apps",
        "Cash, Credit & Till Balancing",
        "Coaching & Trainee Leadership",
        "Valid CA Class C, Clean Record",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Sales & Service Associate",
            "company": "Enterprise Rent-A-Car, Fremont, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Serve counter and phone customers on rentals, reservations, vehicle choice, and protection options with friendly closing",
                "Inspect, prep, and coordinate vehicles on the lot and complete paperwork accurately for on-time handoffs",
                "Drive local shuttles and swaps safely with GPS routing and a clean driver record",
                "Coach new hires on greeting, selling steps, and safety while covering peak days and weekends",
            ],
        },
        {
            "title": "Automotive Sales Associate",
            "company": "Carmax, Santa Clara, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Guided buyers through vehicle needs, features, and financing paths with consultative selling",
                "Drove attach with protection plans and add-ons and kept CRM notes and paperwork exact",
                "Coordinated with service and lot teams so vehicles were ready for demos and delivery",
            ],
        },
        {
            "title": "Courier & Service Driver",
            "company": "OnTrac, Hayward, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Ran multi-stop Bay Area routes with phone scanning, customer contact, and 50-lb stair carries",
                "Completed DVIRs, logs, and proof-of-delivery paperwork with strong attendance",
                "Helped cover Mountain View and San Jose zones during peak volume",
            ],
        },
    ],
    "certifications": [
        "Valid California Class C License, Clean Record",
        "DOT Medical Examiner's Certificate (current)",
        "Workplace Safety Training",
    ],
}
