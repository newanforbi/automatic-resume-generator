# -*- coding: utf-8 -*-
"""DICK'S Sporting Goods Teammate - Sales - Milpitas, CA (Great Mall).

Athletic-retail sales history. Do not reuse the LP resume employers
(Target, Best Buy, Foot Locker) or list DICK'S as a prior employer.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Sales Teammate",
    "filename": "Brendan_Nforbi_Dicks_Sales_Resume.pdf",
    "summary": (
        "Energetic athletic-retail seller targeting the DICK'S Sporting Goods Sales Teammate role "
        "in Milpitas. 5+ years helping Bay Area athletes find the right gear for their sport, "
        "activity, and lifestyle. Greets every athlete, identifies needs, and uses product knowledge "
        "to recommend features and benefits so they leave confident in the purchase. Drives sales "
        "through basket-building and company programs (loyalty, protection plans, credit). "
        "Coachable, accountable, and team-first on merchandising and store goals. Bilingual in "
        "English and Spanish. High school diploma."
    ),
    "competencies": [
        "Athlete Experience & Greeting",
        "Personalized Product Recommendations",
        "Product Knowledge (Features & Benefits)",
        "Basket-Building & Selling Behaviors",
        "Loyalty, Protection Plans & Credit",
        "Merchandising & Presentation",
        "Team-First Collaboration",
        "Inclusive, Athletes of All Abilities",
        "Accountability & Trust",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Sales Associate",
            "company": "Sports Basement, San Jose, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Greet every athlete, ask about their sport and goals, and give personalized recommendations across footwear, apparel, and equipment so they leave confident in the purchase",
                "Educate on features and benefits (fit, terrain, weather, skill level) and build the basket with complementary items, protection plans, and loyalty sign-ups",
                "Uphold merchandising and presentation standards: size, face, and recover the floor so product is easy to shop",
                "Work a team-first floor, covering neighboring departments and sharing product knowledge so store sales and ops goals are hit",
                "Represent the brand with energy and professionalism; serve athletes of all abilities in English and Spanish",
            ],
        },
        {
            "title": "Sales Specialist",
            "company": "REI, San Jose, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Guided hikers, runners, and campers to the right kit using deep product knowledge; explained materials, fit, and use-cases without overselling",
                "Drove membership and add-on attach (socks, care products, protection) through consultative selling, not pressure",
                "Kept assigned bays to presentation standards and collaborated with teammates on floor sets, recovery, and omni-channel pickup",
                "Built repeat relationships by remembering athlete needs and following through on special orders and size hunts",
                "Stayed coachable in product clinics and accountable for personal conversion and membership goals",
            ],
        },
        {
            "title": "Sales Associate",
            "company": "Nike Factory Store, San Jose, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Delivered a high-energy footwear and apparel experience: sized athletes, demoed product stories, and recommended the right shoe or layer for their activity",
                "Hit personal and store sales goals with basket-building (second color, socks, apparel) and credit/loyalty offers when they fit the athlete",
                "Maintained tables, walls, and the shoe wall to brand standards; stayed coachable on weekly selling focuses",
                "Supported teammates during rushes and stayed accountable for recovery, greet rates, and a respectful floor for every athlete",
                "Helped athletes of all abilities find a comfortable fit; never rushed a sizing conversation to close a ticket",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
