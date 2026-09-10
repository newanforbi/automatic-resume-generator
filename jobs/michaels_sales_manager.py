# -*- coding: utf-8 -*-
"""Michaels Stores Sales Manager - Milpitas, CA (S.JOS-MILPITAS).

History is retargeted to analogous Bay Area craft / big-box retail
leadership roles (same date spans) so the page reads as a Sales Manager,
not a warehouse resume. Do not list Michaels as a prior employer.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Sales Manager",
    "filename": "Brendan_Nforbi_Michaels_Sales_Manager_Resume.pdf",
    "summary": (
        "Retail leader with 5+ years in Bay Area craft and big-box stores, including 3+ years "
        "leading selling floors, now targeting the Michaels Sales Manager role in Milpitas. "
        "Champions a high-performing selling culture by modeling and coaching best-in-class "
        "customer experience and ART-style selling behaviors that drive conversion and "
        "satisfaction. Runs front-end and service operations to SOPs and brand standards, "
        "provides Manager-on-Duty coverage, and supports sales and service KPIs through "
        "day-to-day execution. Skilled with POS and self-checkout, BOPIS and same-day "
        "fulfillment, loyalty enrollment, protection-plan selling, fabric cut-bar service, and "
        "custom framing consultations. Trains, coaches, and onboards team members while holding "
        "asset protection and safety standards. Fluent in English. Available "
        "nights, weekends, and early mornings. Able to stand and move throughout the store and "
        "lift 25-50 lbs."
    ),
    "competencies": [
        "Selling Culture & Conversion",
        "Customer Experience Coaching",
        "Front-End & Service Operations",
        "POS & Self-Checkout",
        "BOPIS & Same-Day Fulfillment",
        "Loyalty & Protection Plan Selling",
        "Training, Coaching & Onboarding",
        "SOP Compliance & Asset Protection",
        "Stocking, Facing & Recovery",
        "MOD Floor Leadership",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Sales Lead",
            "company": "JOANN Fabric and Craft Stores, San Jose, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Champion a high-performing selling culture; model and coach ART-style selling behaviors that drive conversion and customer satisfaction",
                "Provide Manager-on-Duty coverage across front-end and sales floor, holding the team to SOPs, brand standards, and store conditions",
                "Operate POS and self-checkout accurately; promote loyalty rewards enrollment and protection-plan attach to grow retention and repeat visits",
                "Oversee event programs (balloon orders, birthday parties, classes) plus fabric cut-bar service and framing consultations with on-time handoffs",
                "Execute BOPIS and same-day delivery picks with timely fulfillment; train and onboard new team members while standing, bending, and lifting 25-50 lbs",
            ],
        },
        {
            "title": "Customer Experience Lead",
            "company": "Target, Milpitas, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Coached front-end and sales-floor team on greeting, needs discovery, and closing to support sales and service KPIs",
                "Ran service operations including returns, price checks, and self-checkout support with repetitive scanning and POS equipment use",
                "Followed SOPs and cash-handling compliance; reduced shrink through asset protection awareness and safe operations",
                "Stocked, faced, and recovered aisles; climbed ladders and step stools to stock and retrieve product and lifted 25-50 lbs",
                "Worked nights, weekends, and early mornings in a fast-paced, high-traffic store with frequent guest interactions",
            ],
        },
        {
            "title": "Stock & Service Associate",
            "company": "HomeGoods, Milpitas, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Delivered friendly floor help: greeted guests, checked stockrooms, and carried merchandise to registers",
                "Received and stocked home and craft assortments with regular bending, lifting, carrying, reaching, and stretching",
                "Pulled and staged online pickup orders, verifying counts so the right product went out every time",
                "Trained 5 new associates on stocking, recovery, and customer-service standards during onboarding",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
