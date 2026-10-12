# -*- coding: utf-8 -*-
"""Aramark Cashier Lead - San Jose, CA.

Look-up-able Bay Area FOH / cash-lead roles (North Bay + South Bay).
Do not list Aramark as a prior employer.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Cashier Lead",
    "filename": "Brendan_Nforbi_Aramark_Cashier_Lead_Resume.pdf",
    "summary": (
        "Guest-focused Cashier Lead targeting Aramark in San Jose. 5+ years running registers, "
        "cash and credit, and the front of house across the Bay Area: Costco "
        "Wholesale on Coleman Ave in Santa Clara, Starbucks on Fourth Street in San Rafael, "
        "and IKEA in East Palo Alto. Trains cashiers, delegates tasks, balances drawers, "
        "verifies bag deposits, and stocks the outlet to par. Works independently, follows "
        "open/close and cash-handling SOPs, and keeps the station clean and guest-ready. "
        "Food Handler certified; ready to complete alcohol-service training. Communicates "
        "clearly in English. Lives in Milpitas."
    ),
    "competencies": [
        "POS / Register Accuracy",
        "Cash & Credit Handling",
        "Drawer Balance & Deposits",
        "Training & Delegating Cashiers",
        "Front-of-House Leadership",
        "Guest Service & Anticipating Needs",
        "Opening & Closing Procedures",
        "Inventory & Restocking",
        "Sanitation & Station Cleanup",
        "Independent Shift Ownership",
        "Clear Verbal & Written English",
    ],
    "experience": [
        {
            "title": "Front End Supervisor",
            "company": "Costco Wholesale, Santa Clara, CA (Coleman Ave)",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Lead the front of house at Costco #129 (1601 Coleman Ave): schedule and delegate cashier assignments, keep lines moving, and own the guest experience from greeting to exit",
                "Train new cashiers on POS, cash/credit handling, membership tender, and Costco cash-handling policy; make change for cashiers and verify bag deposits at close",
                "Count, organize, and balance drawers; complete cashier slips and deposits with limited supervision and clean over/shorts",
                "Follow opening and closing procedures; restock front-end inventory (bags, sundries, impulse) and keep the area clean and shoppable through standing, lifting, and recovery",
                "Anticipate member needs, resolve tender issues on the spot, and communicate clearly in English",
            ],
        },
        {
            "title": "Shift Supervisor",
            "company": "Starbucks, San Rafael, CA (Fourth Street)",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Ran independent shifts at the downtown store (1100 Fourth St): opened/closed, assigned barista and register tasks, and trained partners on guest service, POS, and cash procedures",
                "Operated the register for cash and card, balanced the till, prepared deposits, and followed company cash-handling and dress-code standards every shift",
                "Kept pastry, retail, and cup inventory at par; replenished and faced product during service and after close",
                "Delivered a memorable, guest-first experience on a high-traffic North Bay block; handled written and verbal handoffs in the daily log",
            ],
        },
        {
            "title": "Retail Cashier and Customer Service",
            "company": "IKEA, East Palo Alto, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Processed high-volume cash and credit checkouts at IKEA East Palo Alto (1700 E Bayshore Rd) with accurate counts and few voids",
                "Greeted guests, anticipated needs (bags, Family card, delivery), and kept the cash lane stocked, clean, and ready",
                "Supported open/close recovery: sanitation, cart returns, and facing impulse at the exit",
                "Built the cash-handling and guest-service foundation later used to train and lead other cashiers",
            ],
        },
    ],
    "certifications": [
        "Food Handler Card",
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
