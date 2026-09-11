# -*- coding: utf-8 -*-
"""Vehicle Data Collection Specialist - Bay Area.

Sensor/mapping fleet history with varied Bay Area employers
(Sunnyvale, Mountain View, Fremont). English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "Milpitas, CA",
    "target_title": "Vehicle Data Collection Specialist",
    "filename": "Brendan_Nforbi_Vehicle_Data_Collection_Resume.pdf",
    "summary": (
        "Reliable professional driver with 4+ years operating sensor, mapping, and delivery fleets "
        "across the Bay Area, now targeting a Vehicle Data Collection Specialist role. Drives "
        "assigned collection routes in manual and supervised modes with strict safety and "
        "operational procedures, monitors onboard data and navigation systems, and captures clean, "
        "complete real-world data. Gives detailed, accurate feedback to engineers, troubleshoots in "
        "real time with dispatch to hit mileage targets, and runs daily pre- and post-mission "
        "inspections with basic vehicle care. Strong with laptops, tablets, smartphones, and "
        "Slack-style tools. Holds a current California license with 3+ years US licensure, a clean "
        "record, and can pass background and drug tests. Fluent in English, punctual, and flexible "
        "on schedules. Able to sit up to 8 hours, bend and lift 25 lbs, and ride through abrupt "
        "braking."
    ),
    "competencies": [
        "Assigned Collection Routes",
        "Manual & Supervised Driving",
        "Sensor & Nav System Monitoring",
        "Clean Data Capture",
        "Detailed Engineer Feedback",
        "Real-Time Troubleshooting & Dispatch",
        "Pre/Post-Mission Inspections",
        "Basic Vehicle Care",
        "Laptops, Tablets & Smartphones",
        "Time Management & Independence",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Mapping Fleet Driver",
            "company": "Apple Maps Operations, Sunnyvale, CA",
            "dates": f"Sep 2023 {EN} Present",
            "bullets": [
                "Drive assigned sensor-collection routes with constant situational awareness and safety-first procedures",
                "Monitor onboard data and navigation systems for clean, complete captures across diverse traffic",
                "Send detailed, accurate daily feedback to engineers and troubleshoot with dispatch to hit targets",
                "Complete pre- and post-mission inspections plus basic care including washing and tire air",
            ],
        },
        {
            "title": "Street Data Driver",
            "company": "Google Street View Ops, Mountain View, CA",
            "dates": f"Aug 2022 {EN} Aug 2023",
            "bullets": [
                "Ran mapped loops with roof and onboard sensors while logging events on laptops and tablets",
                "Coordinated over dispatch chat for reroutes, holds, and quality re-drives",
                "Answered general public questions professionally while protecting test protocols",
            ],
        },
        {
            "title": "Route & Delivery Driver",
            "company": "OnTrac, Fremont, CA",
            "dates": f"Jan 2022 {EN} Jul 2022",
            "bullets": [
                "Completed high-stop commercial routes with GPS, scanning, and proof-of-delivery paperwork",
                "Held DVIR discipline with clean logs, inspections, and strong attendance",
                "Stayed calm and resourceful under pressure in changing daily conditions",
            ],
        },
    ],
    "certifications": [
        "Valid California License, 3+ Yrs US Licensed, Clean Record",
        "DOT Medical Examiner's Certificate (current)",
        "Workplace Safety Training",
    ],
}
