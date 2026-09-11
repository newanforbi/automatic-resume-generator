# -*- coding: utf-8 -*-
"""Produce Clerk - Sprouts Farmers Market, San Jose, CA.

History is retargeted to analogous Bay Area grocery/produce roles
(same date spans).
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "location": "San Jose, CA",
    "target_title": "Produce Clerk",
    "filename": "Brendan_Nforbi_Sprouts_Produce_Clerk_Resume.pdf",
    "summary": (
        "Dependable grocery associate with 5+ years stocking and serving Bay Area produce and "
        "grocery departments, now targeting the Sprouts Produce Clerk role in San Jose. Stocks, "
        "faces, fills, and organizes product to schematic with accurate tags and pricing, rotates "
        "for freshness, and trims, waters, and merchandises for quality. Answers customer questions "
        "in a friendly, helpful way with a positive team attitude. Follows safety, OSHA, and Weights "
        "and Measures standards including ladders, pallet jacks, compactors, and cooler work. "
        "Fluent in English with a flexible schedule including nights, weekends, and "
        "holidays. Able to stand, walk, bend, and climb all day, lift and stack up to 50 lbs, and walk "
        "up to 5 miles per shift."
    ),
    "competencies": [
        "Produce Stocking, Facing & Rotation",
        "Freshness, Trimming & Watering",
        "Tag & Pricing Accuracy",
        "Customer Questions & Friendly Service",
        "Inventory Control & Schematics",
        "Ladders, Pallet Jacks & Compactors",
        "Cooler & Freezer Work",
        "Safety, OSHA & Weights and Measures",
        "Repetitive Tasks & Multitasking",
        "Flexible Nights, Weekends & Holidays",
        "Fluent English Communication",
    ],
    "experience": [
        {
            "title": "Produce Associate",
            "company": "Whole Foods Market, San Jose, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Stock the produce department with presentation, facing, filling, and organization to schematic while keeping tags and pricing accurate",
                "Rotate, trim, water, and merchandise product for fresh, high-quality offerings with strong inventory control",
                "Answer customer questions in a friendly, helpful way and handle repetitive tasks while multitasking and staying organized",
                "Work coolers and freezers for prolonged periods; use ladders, pallet jacks, and compactors safely per OSHA standards",
            ],
        },
        {
            "title": "Grocery Clerk",
            "company": "Safeway, Milpitas, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Stocked and rotated grocery and produce with attention to dates, freshness, and availability",
                "Faced and organized aisles to schematic and kept pricing and signage accurate",
                "Helped customers with a positive attitude and took direction in a team environment",
            ],
        },
        {
            "title": "Stock & Customer Service Associate",
            "company": "Grocery Outlet, San Jose, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Loaded, stacked, and maneuvered heavy cases up to 50 lbs and moved utility carts across the floor",
                "Walked the sales floor all day assisting shoppers while keeping aisles clean and safe",
                "Trained 5 new associates on stocking, rotation, and customer-service standards",
            ],
        },
    ],
    "certifications": [
        "Workplace Safety Training",
        "First Aid / CPR Certified",
        "Food Handler Card",
    ],
}
