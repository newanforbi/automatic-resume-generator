# -*- coding: utf-8 -*-
"""Lowe's Part Time Cashier - Union City, CA (store 1132 / Union Landing Blvd).

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
        "Fast, friendly cashier targeting the part-time Cashier role at Lowe's Union City "
        "(32040 Union Landing Blvd). 5+ years of retail customer service on East Bay "
        "home-improvement registers: Home Depot Hayward #1017, Ace Hardware of Fremont, "
        "and Harbor Freight Hayward. Delivers a professional checkout: scan and bag, "
        "payments and exchanges, self-checkout help, and a clean, safe workstation. "
        "Uses a computer POS to input, access, and output transaction data. Stands for "
        "the shift, lifts 10-15+ lbs, and jumps in to stock, move carts, and help other "
        "departments. Bilingual English/Spanish. Lives in Milpitas; reliable commute to "
        "Union City. Available part-time evenings and weekends."
    ),
    "competencies": [
        "Fast, Friendly, Professional Checkout",
        "Scan & Bag Accuracy",
        "Self-Checkout Assistance",
        "Payments & Exchanges",
        "POS / Computer Transaction Entry",
        "Basic Arithmetic & Cash Handling",
        "Clean, Safe Workstation",
        "Stocking, Carts & Other Duties",
        "Stand for Prolonged Periods",
        "Lift 10-15+ lbs",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Cashier",
            "company": "The Home Depot, Hayward, CA (#1017)",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Deliver a fast, friendly, professional checkout at Home Depot #1017 (21787 Hesperian Blvd): scan and bag accurately, take cash/debit/credit, and process payments and exchanges",
                "Proactively assist customers in the self-checkout area when the front end is busy so every guest leaves satisfied",
                "Input, access, and modify transactions on POS computers; use basic arithmetic to count change and verify totals",
                "Keep a clean, safe workstation; stand the full shift and lift 10-15+ lbs (team lift on heavier project materials)",
                "Complete other duties as assigned: help neighboring departments, stock shelves, and move carts on the lot",
            ],
        },
        {
            "title": "Cashier",
            "company": "Ace Hardware of Fremont, Fremont, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Managed the register at Ace Hardware of Fremont (3700 Thornton Ave): scanned, bagged, and solved checkout problems in a fast-paced neighborhood store",
                "Answered customer questions on fasteners, paint, and aisle location so they got the best value and left on a high note",
                "Maintained a clean, safe checkstand; counted the drawer with addition and subtraction at open and close",
                "Worked part-time nights and weekends; stocked shelves and recovered carts when the register was slow",
            ],
        },
        {
            "title": "Retail Sales Cashier",
            "company": "Harbor Freight, Hayward, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Processed high-volume checkouts at Harbor Freight #494 (24022 Hesperian Blvd) on a computer POS: scan, bag, coupons, cash and card",
                "Greeted guests, answered tool questions, and kept the front lane clean and safe through constant standing and light lifting",
                "Helped other departments with stocking and cart runs so the store stayed shoppable during rushes",
                "Built the retail customer-service foundation used on every later home-improvement register",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
