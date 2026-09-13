# -*- coding: utf-8 -*-
"""Part Time Inventory Associate - LG-OSS, Santa Clara, CA 95050.

Varied Bay Area inventory/warehouse employers (Milpitas, Fremont, San Jose).
English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "Santa Clara, CA",
    "target_title": "Inventory Associate",
    "filename": "Brendan_Nforbi_LGOSS_Inventory_Resume.pdf",
    "summary": (
        "Inventory and warehouse associate with 5+ years across Bay Area sites, now targeting the "
        "LG-OSS Part Time Inventory Associate role in Santa Clara. Holds daily coverage at primary "
        "garages and backs up nearby locations, keeping 98%+ scan compliance with FIFO stock "
        "management and ordered task sequences. Completes Garage-101 style readiness daily: correct "
        "signage above product, combined orderly pallets, clean functional desk areas, posted "
        "barcodes, and on-time arrival with reports by deadline. Meets early service requirements "
        "with 5:00am availability Monday through Friday. Acts as a safety advocate for an "
        "accident-free area and joins daily conference calls with upward communication. Skilled with "
        "pallet jacks, scanners, laptops, smartphones, and MS Excel, Word, and Outlook. Holds a high "
        "school diploma, lifts 50+ lbs, works loud warehouse conditions, and can pass a 5-panel drug "
        "screen. Fluent in English with a valid California license for local travel."
    ),
    "competencies": [
        "98%+ Scan Compliance",
        "FIFO Stock Management",
        "Garage-101 Daily Readiness",
        "5:00am Mon-Fri Coverage",
        "Pallet Jack, Scanner & Laptop",
        "MS Excel, Word & Outlook",
        "Safety Advocate, Zero Incidents",
        "Daily Calls & Upward Reporting",
        "Policy & Procedure Adherence",
        "Local Travel Ready",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Inventory Associate",
            "company": "Flex, Milpitas, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Hold daily site coverage and back up nearby garages while meeting early-morning service times",
                "Keep 98%+ scan compliance with FIFO rotation, combined orderly pallets, and correct signage",
                "Run ordered task sequences with on-time arrival and daily reports by deadline",
                "Operate pallet jacks, scanners, laptops, and smartphones with MS Excel, Word, and Outlook updates",
            ],
        },
        {
            "title": "Material Handler",
            "company": "Tesla, Fremont, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Moved inventory with pallet jacks between docks, racking, and staging with safety-first habits",
                "Kept desk and work areas clean, organized, and functional with posted labels and barcodes",
                "Joined daily stand-ups and communicated issues upward between client and company teams",
            ],
        },
        {
            "title": "Warehouse Associate",
            "company": "DHL, San Jose, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Picked, staged, and verified counts with RF scanners in a loud, fast warehouse",
                "Lifted 50+ lbs with bending, twisting, sitting, and standing across full shifts",
                "Trained 5 new associates on inventory accuracy and safety standards",
            ],
        },
    ],
    "certifications": [
        "High School Diploma",
        "Workplace Safety Training",
        "First Aid / CPR Certified",
    ],
}
