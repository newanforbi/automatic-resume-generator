# -*- coding: utf-8 -*-
"""Lowe's Part Time Cashier - Union City, CA (store 1132).

Look-up-able East Bay home-improvement cashier roles. Do not list Lowe's
or the Union City Home Depot as a prior employer.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Part Time Cashier",
    "filename": "Brendan_Nforbi_Lowes_Cashier_Resume.pdf",
    "summary": (
        "Accurate, friendly cashier targeting the part-time Cashier role at Lowe's Union City "
        "(32040 Union Landing Blvd). 5+ years on East Bay home-improvement checkstands: "
        "The Home Depot Hayward #1017, Ace Hardware of Fremont, and Harbor Freight Hayward. "
        "Runs POS for cash and credit, processes returns, keeps the front end clean, and greets "
        "every customer. Available for part-time evenings, weekends, and flexible hours. "
        "Bilingual in English and Spanish. Lives in Milpitas; reliable commute to Union City."
    ),
    "competencies": [
        "POS / Register Accuracy",
        "Cash & Credit Handling",
        "Returns & Exchanges",
        "Customer Greeting",
        "Front-End Recovery",
        "Part-Time Flexibility",
        "Home Improvement Product Basics",
        "Drawer Balance",
        "Team Support",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Cashier",
            "company": "The Home Depot, Hayward, CA (#1017)",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Operate POS for cash, debit, credit, and gift cards at Home Depot #1017 (21787 Hesperian Blvd); keep drawers balanced and transactions accurate",
                "Greet every customer, process returns and exchanges, and offer the store credit card when it fits the project",
                "Keep the checkstand stocked and clean; call for loading help and stay on my feet through evening and weekend volume",
                "Answer basic product and location questions, then walk or radio a specialist so the guest leaves with what they came for",
                "Available part-time including evenings and weekends; reliable on the Union City / Hayward 880 corridor",
            ],
        },
        {
            "title": "Cashier",
            "company": "Ace Hardware of Fremont, Fremont, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Ran the register at Ace Hardware of Fremont (3700 Thornton Ave): cash, cards, house charges, and rainchecks with few voids",
                "Delivered helpful, neighbor-style service; found fasteners and paint supplies when customers were unsure what they needed",
                "Faced impulse and bag supplies; counted the drawer at open and close per store SOP",
                "Worked a flexible part-time schedule including nights and weekends in a small, team-run hardware store",
                "Helped neighbors load bags and small project materials to the car when the lot was busy",
            ],
        },
        {
            "title": "Retail Sales Cashier",
            "company": "Harbor Freight, Hayward, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Processed high-volume tool and hardware checkouts at Harbor Freight #494 (24022 Hesperian Blvd) with accurate cash and card handling",
                "Greeted guests, scanned coupons and Inside Track Club offers, and kept the front lane recovered and shoppable",
                "Supported fellow associates on the floor when lines were short; stood and lifted through freight and recovery as needed",
                "Built the cash-handling and customer-service habits used on every later home-improvement checkstand",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
