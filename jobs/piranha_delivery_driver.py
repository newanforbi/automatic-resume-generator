# -*- coding: utf-8 -*-
"""Parcel Delivery Driver - Piranha Ops, Milpitas, CA.

History uses varied Bay Area delivery employers (Fremont, Sunnyvale,
Hayward) per variety request. Same date spans.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "Milpitas, CA",
    "target_title": "Parcel Delivery Driver",
    "filename": "Brendan_Nforbi_Piranha_Delivery_Driver_Resume.pdf",
    "summary": (
        "Delivery driver with 4+ years running residential and commercial parcel routes across "
        "the Bay Area, now targeting the Piranha Ops Parcel Delivery Driver role in Milpitas. "
        "Safely operates step vans, Sprinters, Transits, and 26-ft box trucks with phones for "
        "routes, customer contact, and package scanning plus GPS navigation. Lifts packages up to "
        "50 lbs up and down stairs with an on-time, clean-driving record. Shows up on time, works "
        "hard, and welcomes overtime, 5th and 6th day opportunities, and 9:35am to 7:15pm coverage "
        "4 to 6 days a week. Holds a valid California Class C license with a clean history, is over "
        "21, and can pass a pre-employment drug screen. Fluent in English."
    ),
    "competencies": [
        "Step Van, Sprinter & Transit Operation",
        "Residential & Commercial Routes",
        "Phone Scanning & Route Apps",
        "GPS Navigation",
        "Packages up to 50 lbs + Stairs",
        "Safe Driving & Clean Record",
        "On-Time Attendance",
        "Overtime & 5th/6th Day Availability",
        "Customer Delivery Contact",
        "Paid Training Ready",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Parcel Delivery Driver",
            "company": "OnTrac, Fremont, CA",
            "dates": f"Sep 2023 {EN} Present",
            "bullets": [
                "Run high-stop residential and commercial parcel routes from 9:35am coverage, using phone for route info, customer delivery, and package scanning",
                "Safely operate delivery vans with GPS navigation and lift packages up to 50 lbs up and down stairs",
                "Show up on time as scheduled and volunteer for overtime at 1.5x plus 5th and 6th day opportunities",
                "Keep a clean driver history with zero at-fault incidents across the tenure",
            ],
        },
        {
            "title": "Delivery Driver, Sprinter / Transit",
            "company": "Amazon DSP, Sunnyvale, CA",
            "dates": f"Aug 2022 {EN} Aug 2023",
            "bullets": [
                "Delivered 150+ parcels per shift across Sunnyvale and Mountain View with on-time station returns",
                "Navigated apartments, businesses, and gated stops with GPS plus customer calls and texts",
                "Handled heavy-touch handoffs with pallet jack, hand truck, and safe stair carries",
            ],
        },
        {
            "title": "Courier & Route Driver",
            "company": "Medline Transport, Hayward, CA",
            "dates": f"Jan 2022 {EN} Jul 2022",
            "bullets": [
                "Ran multi-stop medical supply routes with DVIRs, BOLs, and piece-count verification",
                "Coordinated with dock teams to prioritize loads and keep throughput on schedule",
                "Managed hours-of-service and ELD compliance with clean logs and inspections",
                "Passed pre-employment and ongoing drug screening with excellent attendance",
            ],
        },
    ],
    "certifications": [
        "Valid California Class C License, Clean Record",
        "DOT Medical Examiner's Certificate (current)",
        "Workplace Safety Training",
    ],
}
