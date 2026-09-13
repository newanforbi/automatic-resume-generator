# -*- coding: utf-8 -*-
"""Truck Driver (Food Delivery) - Coast Personnel, Hayward, CA 94544.

Varied Bay Area food/route employers (Hayward, Oakland, San Jose).
English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "Hayward, CA",
    "target_title": "Truck Driver (Food Delivery)",
    "filename": "Brendan_Nforbi_Coast_Truck_Driver_Resume.pdf",
    "summary": (
        "Dependable route driver with 4+ years delivering food and commercial freight across the "
        "Bay Area, now targeting the Coast Truck Driver role in Hayward. Drives 16-ft box trucks "
        "and similar service trucks to retail and restaurant customers across the Bay Area, "
        "Sacramento, and Watsonville with no overnight travel. Loads and unloads product, obtains "
        "signatures on delivery, and runs dispatcher-assigned multi-site routes with professional, "
        "friendly customer service. Uses basic math and English for counts, invoices, and BOLs and "
        "keeps vehicles, equipment, and work areas clean and safe. Holds a valid California license "
        "with a clean record and current DOT medical. Fluent in English, punctual, and available "
        "full time in person."
    ),
    "competencies": [
        "16-Ft Box & Service Trucks",
        "Restaurant & Retail Delivery",
        "Signatures & BOL Paperwork",
        "Dispatcher Multi-Site Routes",
        "Loading & Unloading",
        "Basic Math & English",
        "Safe Vehicle & Equipment Ops",
        "Clean & Safe Work Areas",
        "Food Products Experience",
        "Bay Area + Sacramento Routes",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Route Delivery Driver",
            "company": "US Foods, Oakland, CA",
            "dates": f"Sep 2023 {EN} Present",
            "bullets": [
                "Drive 16-ft service trucks to restaurants on dispatcher-assigned multi-site routes",
                "Load and unload food product safely and keep trucks and work areas clean",
                "Give professional, friendly customer service with clear English communication",
                "Cover Bay Area runs plus Sacramento and Watsonville legs with no overnight travel",
            ],
        },
        {
            "title": "Food Delivery Driver",
            "company": "Keurig Dr Pepper, Modesto, CA",
            "dates": f"Aug 2022 {EN} Aug 2023",
            "bullets": [
                "Ran direct-store-delivery food and beverage routes to grocery and restaurant accounts",
                "Hand-unloaded cases and pallets with pallet jack and hand truck and obtained signatures",
                "Back-stocked and rotated product on-site with accurate counts and invoices",
                "Held DOT compliance and on-time record across Bay Area and Valley routes",
            ],
        },
        {
            "title": "Courier Driver",
            "company": "OnTrac, San Jose, CA",
            "dates": f"Jan 2022 {EN} Jul 2022",
            "bullets": [
                "Completed high-stop commercial routes with scanning and proof-of-delivery paperwork",
                "Operated liftgates and hand trucks with strong safety and attendance",
                "Adapted to traffic and schedule changes while meeting deadlines",
            ],
        },
    ],
    "certifications": [
        "Valid California License, Clean Record",
        "DOT Medical Examiner's Certificate (current)",
        "Workplace Safety Training",
    ],
}
