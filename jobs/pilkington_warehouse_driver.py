# -*- coding: utf-8 -*-
"""Warehouse Associate / Some Driving (Days) - Pilkington, San Jose, CA.

Hybrid warehouse + delivery history using real warehouse employers and the
candidate's driving credentials. Same date spans as the base resume.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Warehouse Associate / Delivery Driver",
    "filename": "Brendan_Nforbi_Pilkington_Warehouse_Driver_Resume.pdf",
    "summary": (
        "Warehouse and delivery associate with 5+ years in distribution plus 4+ years commercial "
        "driving, now targeting the Pilkington Warehouse Associate / Some Driving role in San Jose. "
        "Receives and unpacks trucks, locates and pulls parts, inspects and loads delivery trucks "
        "accurately, unloads and processes returns, stocks racks, and keeps inventory accurate with "
        "cycle counts. Operates forklifts, order pickers, pallet jacks, hand trucks, liftgates, and "
        "basic hand tools with strong safety compliance. Delivers to customers with friendly client "
        "interaction, reads maps and GPS routes, and completes will-call paperwork. Holds a valid "
        "California Class C license with a current DOT medical and good driving record. Proficient in "
        "English, with excellent attendance. Able to lift 35-45 lbs frequently "
        "and up to 70-100 lbs on occasion and work in outdoor-like temperatures. Available Mon-Fri "
        "8:30am-5pm days."
    ),
    "competencies": [
        "Receiving, Unpacking & Returns",
        "Picking, Pulling & Will-Call",
        "Loading & Delivery Driving",
        "Forklift & Order Picker",
        "Pallet Jack, Hand Truck & Hand Tools",
        "Inventory & Cycle Counts",
        "Maps, GPS & Delivery Routes",
        "Customer Relations & Proof of Pick-Up",
        "Safety Compliance & Inspections",
        "Valid CA Class C + DOT Medical",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Warehouse Associate",
            "company": "HD Supply, Pleasanton, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Receive shipments and unpack trucks; locate parts in racks, pull stock, and visually inspect before accurate truck loading",
                "Pick, pack, and stage 200+ orders per shift and process returns daily with 99.4% accuracy",
                "Operate sit-down and reach forklifts plus pallet jacks and hand tools to replenish and load safely",
                "Run cycle counts with RF scanners and WMS to keep inventory accurate and support delivery routes",
            ],
        },
        {
            "title": "Material Handler",
            "company": "Medline Industries, Lathrop, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Received, inspected, and put away inbound freight and stocked assigned racks in a high-volume facility",
                "Moved product with electric pallet jacks and stand-up forklifts between docks, racking, and staging",
                "Processed 80+ orders per shift with voice-pick and RF scanners while meeting rate and safety targets",
            ],
        },
        {
            "title": "Warehouse Worker",
            "company": "Ferguson Enterprises, Stockton, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Loaded and unloaded trucks carrying product up to 75 lbs per piece and handled will-call style pickups with paperwork",
                "Delivered friendly client interaction on pickups and shortage or damage questions with good customer relations",
                "Trained 5 new associates on equipment, accuracy, and safety with excellent attendance over the tenure",
            ],
        },
    ],
    "certifications": [
        "Valid California Class C License + DOT Medical",
        "OSHA Forklift Certified (Sit-Down, Stand-Up, Reach)",
        "First Aid / CPR Certified",
    ],
}
