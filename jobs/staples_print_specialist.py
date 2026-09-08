# -*- coding: utf-8 -*-
"""Staples Retail Print Specialist - Milpitas, CA (95035). Print training provided.

History is retargeted to analogous Bay Area print, copy, and shipping retail
roles (same date spans) so the page reads as a Print Specialist, not a warehouse resume.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Retail Print Specialist",
    "filename": "Brendan_Nforbi_Print_Specialist_Resume.pdf",
    "summary": (
        "Customer-focused Print Associate with 5+ years in Bay Area copy, print, and shipping retail, "
        "now targeting the Staples Print Specialist role in Milpitas. Greets customers, asks open-ended "
        "questions to understand copy and print needs, and uses order intake tools to capture a complete "
        "print solution. Produces professionally finished work with visual inspection and defect detection. "
        "Skilled with Microsoft Word and desktop applications to open, save, and send electronic files, and "
        "comfortable helping customers at self-service copiers and PC rentals. De-escalates issues in a calm, "
        "cooperative way. Bilingual in English and Spanish. Available immediately for flexible part-time hours, "
        "including evenings and weekends. Able to stand and walk continuously and lift 10-50 lbs."
    ),
    "competencies": [
        "Customer Service & Consultation",
        "Print & Copy Production",
        "Visual Inspection & Quality Control",
        "Defect Detection",
        "Microsoft Word & Desktop Applications",
        "Order Intake Tools",
        "Self-Service Copiers & PC Rentals",
        "Conflict De-escalation",
        "Shipping Support",
        "Flexible Part-Time Scheduling",
        "Bilingual: English & Spanish",
    ],
    "experience": [
        {
            "title": "Print Associate",
            "company": "FedEx Office, Milpitas, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Greet customers as they enter the print center and ask open-ended questions to understand copy, print, finishing, and turnaround needs",
                "Use order intake tools to capture project details and recommend a total print solution, including copies, color output, binding, posters, and business cards",
                "Produce professionally finished products on print and production equipment; perform visual inspection and defect detection before customer handoff (99.5% reprint-free)",
                "Assist customers at self-service copiers and PC rentals; open, save, and send electronic files in Microsoft Word and similar desktop applications",
                "Cover packing and shipping as assigned; de-escalate service issues in a calm, nonconfrontational way while standing and lifting 10-50 lbs throughout the shift",
            ],
        },
        {
            "title": "Copy & Print Associate",
            "company": "Office Depot, Fremont, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Consulted walk-in and small-business customers on copy and print projects, asking qualifying questions to size jobs and suggest finishing that completed the solution",
                "Operated copiers, printers, and finishing equipment in a high-paced retail print center; inspected output for quality issues, color defects, and incomplete sets",
                "Handled customer files on desktop applications, including Microsoft Word, to open, save, and send work for same-day and next-day production",
                "Collaborated with a team-oriented retail crew during peak hours and resolved complaints cooperatively without confrontation",
                "Trained 5 new associates on greeting standards, order intake, and quality checks during onboarding",
            ],
        },
        {
            "title": "Retail Print & Shipping Associate",
            "company": "The UPS Store, Milpitas, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Greeted customers and captured packing, shipping, and print-copy orders, then produced copies and simple print jobs with a keen eye for quality issues",
                "Helped customers with shipping, mailbox, and self-serve tasks; regularly lifted boxes and supplies in the 10-50 lb range and walked the floor continuously",
                "Managed delayed-package and order conflicts in a reasonable, cooperative manner while protecting customer and business information with honesty and integrity",
                "Worked a flexible retail schedule based on store needs, including evenings and weekends, in a fast, sometimes stressful neighborhood location",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
