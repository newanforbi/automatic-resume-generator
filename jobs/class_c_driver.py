# -*- coding: utf-8 -*-
"""Commercial Delivery Driver (Class C) - San Jose, CA.

Polished rebuild of the uploaded Class C resume. All employers, dates,
licenses, and facts preserved; copy tightened for a one-page ATS build.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Commercial Delivery Driver (Class C)",
    "filename": "Brendan_Nforbi_Class_C_Driver_Resume.pdf",
    "summary": (
        "Commercial delivery driver with 4+ years across the San Joaquin Valley and Bay Area, "
        "including OTR long-haul, regional short-haul, yard operations, and dedicated local "
        "heavy-touch delivery. Held a California Class A CDL from January 2022 through March 2026; "
        "currently operate under a California Class C license with a current DOT medical "
        "examiner's certificate. Fluent in English with an on-time delivery record, "
        "clean DOT inspections, and zero damage claims. Available for immediate start including "
        "days, nights, weekends, and split shifts."
    ),
    "competencies": [
        "26-Ft Box Truck Operation",
        "Heavy-Touch Freight (100+ lbs)",
        "Pallet Jack & Hand Truck & Liftgate",
        "Multi-Stop Route Delivery",
        "GPS Routing & Delivery Apps",
        "ELD & HOS Compliance",
        "DVIR Pre-Trip & Post-Trip",
        "BOL Handling & DOT Paperwork",
        "Dock & Yard Operations",
        "Customer-Facing Delivery",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Class A CDL Delivery Driver, Toyota Dedicated Account",
            "company": "Centerline Drivers, LLC, San Jose, CA",
            "dates": f"Sep 2023 {EN} Mar 2026",
            "bullets": [
                "Ran heavy-touch multi-stop routes on a dedicated Toyota parts account from the San Jose terminal into Livermore, Tracy, Manteca, Stockton, and the San Joaquin Valley",
                "Hand-unloaded palletized freight up to 100+ lbs per piece with pallet jack, hand truck, and liftgate with zero damage claims",
                "Completed pre-trip and post-trip DVIRs, ELD logs, and DOT paperwork every shift; verified piece counts, signed BOLs, and resolved shortage or damage issues with receivers",
            ],
        },
        {
            "title": "Class A CDL Delivery Driver",
            "company": "Keurig Dr Pepper, Modesto, CA",
            "dates": f"Aug 2022 {EN} Aug 2023",
            "bullets": [
                "Ran direct-store-delivery routes to grocery, convenience, and food-service accounts across the Central Valley and Bay Area",
                "Performed heavy-touch handling at every stop, hand-unloading cases, kegs, and palletized product and back-stocking and rotating on-site",
                "Held DOT compliance, clean logs, and a reliable on-time delivery record on multi-stop schedules",
            ],
        },
        {
            "title": "Yard Hostler and Spotter",
            "company": "Lazer Spot, Inc., Tracy, CA",
            "dates": f"Apr 2022 {EN} Jul 2022",
            "bullets": [
                "Spotted and positioned trailers between dock doors, staging lanes, and parking areas at a high-volume distribution facility",
                "Coordinated with dock supervisors and shipping teams to prioritize inbound and outbound loads and keep dock throughput on schedule",
            ],
        },
        {
            "title": "Class A CDL Auto Transport Driver",
            "company": "United Road, Nationwide OTR",
            "dates": f"Jan 2022 {EN} Mar 2022",
            "bullets": [
                "Operated tractor-trailer auto transport on interstate long-haul routes; loaded, secured, and unloaded vehicles per DOT and carrier standards",
                "Managed hours-of-service, split-sleeper rest, ELD compliance, and multi-day trip planning across 48-state operations",
            ],
        },
    ],
    "certifications": [
        "California Class C License (current)",
        "DOT Medical Examiner's Certificate (current)",
        "Class A CDL held Jan 2022 through Mar 2026",
        "First Aid / CPR Certified",
    ],
}
