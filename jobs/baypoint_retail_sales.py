# -*- coding: utf-8 -*-
"""Retail Sales Associate - Baypoint Systems, San Jose, CA 95110.

Varied Bay Area retail employers (Redwood City, Palo Alto, Union City).
English-only per record request.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Retail Sales Associate",
    "filename": "Brendan_Nforbi_Baypoint_Retail_Sales_Resume.pdf",
    "summary": (
        "Outgoing retail associate with 5+ years in fast-paced Bay Area stores, now targeting the "
        "Baypoint Retail Sales Associate role in San Jose. Greets every guest, educates on products, "
        "promotions, and services, and recommends the right fit from needs and preferences. Supports "
        "individual and team sales goals with accurate transactions and professional concern "
        "resolution that protects loyalty. Stays current on promos and policies and collaborates on "
        "creative solutions for niche needs. Reliable, punctual, goal-driven, and team-oriented. "
        "Fluent in English with strong interpersonal skills. Available full time including weekends, "
        "in person."
    ),
    "competencies": [
        "Greeting & Personalized Service",
        "Product & Promo Education",
        "Needs-Based Recommendations",
        "Accurate Transactions",
        "Concern Resolution & Loyalty",
        "Individual & Team Sales Goals",
        "Policy & Promo Knowledge",
        "Creative Niche Solutions",
        "Reliable & Punctual Teamwork",
        "Weekend Availability",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Retail Sales Associate",
            "company": "Apple, Palo Alto, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Greet and assist customers with friendly, professional service and right-fit recommendations",
                "Educate on products, promotions, and services while processing transactions accurately",
                "Support team sales goals and resolve concerns to protect satisfaction and loyalty",
                "Stay current on launches and policies and share creative solutions with the team",
            ],
        },
        {
            "title": "Sales Associate",
            "company": "Best Buy, Redwood City, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Sold tech with demos and attach through consultative, needs-based recommendations",
                "Handled POS, cash, and returns with accuracy during weekend rushes",
                "Kept bays merchandised and ready for high-traffic shopping",
            ],
        },
        {
            "title": "Customer Service Associate",
            "company": "Target, Union City, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Welcomed guests, answered questions, and guided sign-ups with a positive attitude",
                "Collaborated on floor coverage and recovery with reliable attendance",
                "Trained 5 new associates on service and sales standards",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
