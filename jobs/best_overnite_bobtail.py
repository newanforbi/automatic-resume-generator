# -*- coding: utf-8 -*-
"""Bobtail P&D Driver - Best Overnite Express, San Jose, CA 95112.

Local P&D history with varied Bay Area employers (San Jose, Oakland,
Fremont). English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Bobtail P&D Driver",
    "filename": "Brendan_Nforbi_Best_Overnite_Bobtail_Resume.pdf",
    "summary": (
        "Local P&D driver with 3+ years on bobtail equipment across the Bay Area, now targeting the "
        "Best Overnite Express Bobtail Driver role in San Jose. Conducts thorough pre-trip and "
        "post-trip inspections, checks fluids, lights, trailer connection, and securement, and reports "
        "repair needs before departure. Follows electronic GPS accurately, runs ELD and in-cab tech to "
        "HOS rules, and makes safe deliveries and pickups with pallet jacks and liftgates plus courteous, "
        "professional service. Secures freight, assists dock loading and unloading, and adapts to traffic "
        "and weather under tight high-volume deadlines. Holds a California license, is fluent in English, "
        "and works independently and as a team. Able to lift and move 99+ lbs, push and pull pallets up "
        "to 1100 lbs, and sit 1.5+ hours driving with frequent lift, twist, stoop, kneel, and climb."
    ),
    "competencies": [
        "Bobtail P&D (3+ Yrs Local)",
        "Pre/Post-Trip Inspections",
        "ELD, HOS & In-Cab Tech",
        "Electronic GPS Routing",
        "Pallet Jack & Liftgate",
        "Freight Securement",
        "Dock Loading & Unloading",
        "Courteous Customer Service",
        "High-Volume Deadlines",
        "California License",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Bobtail P&D Driver",
            "company": "FedEx Freight, San Jose, CA",
            "dates": f"Sep 2023 {EN} Present",
            "bullets": [
                "Run local bobtail pickup and delivery with pre-trip and post-trip inspections and securement checks",
                "Follow electronic GPS and ELD hours-of-service rules while meeting tight high-volume windows",
                "Deliver and pick up with pallet jacks and liftgates, securing freight and assisting dock load and unload",
                "Give professional, courteous service and report equipment repairs to supervisors and mechanics",
            ],
        },
        {
            "title": "P&D Driver",
            "company": "XPO Logistics, Oakland, CA",
            "dates": f"Aug 2022 {EN} Aug 2023",
            "bullets": [
                "Completed local routes with in-cab logs, GPS accuracy, and on-time dock turns",
                "Lifted and moved 99+ lbs and pushed and pulled pallets up to 1100 lbs with safe form",
                "Adapted to traffic and weather while managing multiple priorities and deadlines",
            ],
        },
        {
            "title": "Delivery Driver",
            "company": "OnTrac, Fremont, CA",
            "dates": f"Jan 2022 {EN} Jul 2022",
            "bullets": [
                "Ran multi-stop commercial routes with scanning, counts, and proof-of-delivery paperwork",
                "Sat long drive stretches with frequent lift, twist, stoop, kneel, and climb handling",
                "Held strong attendance as a solo company driver on local routes",
            ],
        },
    ],
    "certifications": [
        "California License (current)",
        "DOT Medical Examiner's Certificate (current)",
        "Workplace Safety Training",
    ],
}
