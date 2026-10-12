# -*- coding: utf-8 -*-
"""Penske Customer Service Coordinator - Santa Clara branch (2380 Lafayette St).

Shop PM scheduling, outside repairs, workforce plan. English only.
Do not list Penske as a prior employer.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Customer Service Coordinator",
    "filename": "Brendan_Nforbi_Penske_CSC_Resume.pdf",
    "summary": (
        "Customer Service Coordinator targeting Penske Truck Leasing in Santa Clara "
        "(2380 Lafayette St). 5+ years in Bay Area fleet shops: scheduling preventative "
        "maintenance, coordinating outside repairs, and building the daily/weekly work plan "
        "around customer needs, parts, technician skill, and hours. Hands-on diesel "
        "mechanical background plus service-desk administration. Communicates schedule "
        "changes, billing questions, and service issues so customers come back. Follows "
        "DOT, OSHA, and shop safety rules; lifts 50 lbs; available for 2nd shift "
        "(1:00-2:00 p.m. start). High school diploma. Communicates clearly in English. "
        "Lives in Milpitas."
    ),
    "competencies": [
        "Preventative Maintenance Scheduling",
        "Shop Work-Plan & Workforce Planning",
        "Outside Repair / Vendor Coordination",
        "Rental Unit Readiness",
        "Parts Availability",
        "Customer Updates, Billing & Issue Resolution",
        "Service Scheduling Programs",
        "Hands-On Mechanical / Shop Floor",
        "DOT / OSHA / PPE Safety",
        "2nd Shift Availability",
        "Clear English Communication",
    ],
    "experience": [
        {
            "title": "Service Coordinator",
            "company": "Ryder Truck Rental, San Jose, CA",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Build the daily and weekly shop work plan at Ryder San Jose (2481 O'Toole Ave): customer PMs, estimated unscheduled repairs, parts on hand, technician skill, and available hours",
                "Schedule preventative maintenance and communicate updates, schedule changes, billing concerns, and service issues so rental and lease customers stay informed",
                "Keep rental units maintained and prepared for the next customer; confirm parts are on the shelf before a job is dispatched",
                "Hold outside vendors to quality and promised dates; coordinate with district billing clerks on extras and warranty vs. customer-pay",
                "Protect shop productivity by sequencing work and following Ryder / DOT / OSHA safety rules, PPE, and full-shift attendance",
            ],
        },
        {
            "title": "Service Advisor",
            "company": "Coast Counties Peterbilt, San Jose, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Ran service-department administration at 1740 N 4th St: write-ups, PM scheduling, and the shop board so technicians had a clear plan each day",
                "Called customers with status, extra-work approvals, and billing questions; resolved service issues so they returned for the next PM",
                "Ordered and staged parts for scheduled jobs; followed up with vendors on outside repairs until the unit was back on the lot",
                "Used the dealer scheduling system and basic diagnostic notes to assign work to the right technician and hit promised times",
            ],
        },
        {
            "title": "Diesel Technician",
            "company": "TEC Equipment, Oakland, CA",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Hands-on mechanical work at TEC Oakland (8099 S Coliseum Way): PMs, inspections, and unscheduled repairs on Class 6-8 trucks in a dealer shop",
                "Selected the correct tools and PPE, worked around moving trucks, and lifted 50+ lbs; followed shop and OSHA safety practices",
                "Stood, walked, bent, and climbed through the shift; used shop diagnostics under advisor direction",
                "Gave accurate time and parts feedback so the service desk could keep the work plan honest",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
