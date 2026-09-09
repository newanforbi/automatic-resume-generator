# -*- coding: utf-8 -*-
"""Retail Sales Associate - Verizon, San Jose, CA.

History uses varied Bay Area wireless/tech retail employers (Santa Clara,
Sunnyvale, Mountain View) per variety request. Same date spans.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Retail Sales Associate",
    "filename": "Brendan_Nforbi_Verizon_Retail_Sales_Resume.pdf",
    "summary": (
        "Customer-driven retail seller with 5+ years in Bay Area wireless and tech sales, now "
        "targeting the Verizon Retail Sales Associate role in San Jose. Generates sales with a "
        "passion for technology and exceptional service: builds connections, asks the right "
        "questions to uncover needs, positions product insights as complete top-down solutions, "
        "and closes with clear communication. Thrives in commission environments, grows the base "
        "with outbound calls and texts, and represents the brand at community and off-site events. "
        "Keeps merchandising and inventory sharp and trains through ongoing learning. Bilingual in "
        "English and Spanish. Available evenings, weekends, and holidays with openness to extra "
        "peak shifts."
    ),
    "competencies": [
        "Wireless & Tech Sales",
        "Needs Discovery & Solutions",
        "Commission Selling & Closing",
        "Outbound Calls & Texts",
        "Merchandising & Inventory",
        "Customer Connections & Service",
        "Community & Off-Site Events",
        "Cash Handling & POS",
        "Team Training & Coaching",
        "Evenings, Weekends & Holidays",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Wireless Sales Associate",
            "company": "T-Mobile, Santa Clara, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Generate wireless sales by uncovering needs and positioning phones, plans, and accessories as complete solutions",
                "Close sales with clear communication and grow the base with outbound calls and texts to interested customers",
                "Work a commission floor with accountability to individual goals while lifting team conversion",
                "Represent the store at community and off-site events to expand loyal local traffic",
            ],
        },
        {
            "title": "Tech Sales Associate",
            "company": "Best Buy, Sunnyvale, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Sold tech with demos and feature-benefit stories across mobile, computing, and accessories",
                "Drove attach with protection plans, memberships, and add-ons through consultative selling",
                "Kept bays merchandised and inventoried and supported recovery and omni pickup",
            ],
        },
        {
            "title": "Electronics Sales Associate",
            "company": "Target, Mountain View, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Greeted every guest, found the right device or plan for their use, and closed simply and confidently",
                "Handled POS, cash, and returns accurately while covering evenings, weekends, and holidays",
                "Trained 5 new associates on greeting, selling steps, and merchandising standards",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
