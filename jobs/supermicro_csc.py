# -*- coding: utf-8 -*-
"""Customer Service Coordinator - Super Micro Computer, San Jose, CA.

Indeed jk=a04dbadc2f0d96cb was login-walled. This targets the live Super Micro
CSC posting in San Jose (phones, RMA, warranty, escalations, parts, Excel).
English only. Do not list Super Micro as a prior employer.
"""

from candidate import PROFILE

EN = "\u2013"

RESUME = {
    **PROFILE,
    "target_title": "Customer Service Coordinator",
    "filename": "Brendan_Nforbi_Customer_Service_Coordinator_Resume.pdf",
    "summary": (
        "Customer Service Coordinator targeting Super Micro in San Jose. 5+ years handling "
        "phones, RMAs, warranty checks, parts follow-up, and escalations at Bay Area "
        "tech and retail support desks: Western Digital (Great Oaks, San Jose), "
        "TD SYNNEX (Nobel Drive, Fremont), and T-Mobile (Great Mall, Milpitas). Answers "
        "calls promptly, sets realistic expectations, documents tickets in Excel and Outlook, "
        "and works internal teams to close issues on tight schedules. Follows work instructions "
        "with minimum supervision. On-site in Milpitas; ready for Super Micro's San Jose office. "
        "Communicates clearly in English."
    ),
    "competencies": [
        "Phone Support (Requests, Inquiries, Complaints)",
        "RMA Receiving & Product Returns",
        "Warranty Verification",
        "Escalation Management",
        "Parts Fulfillment & Backlog Follow-Up",
        "Internal Team Coordination",
        "Excel & Outlook",
        "Ticket / Case Documentation",
        "Expectation Setting",
        "Fast-Paced Multi-Tasking",
        "Clear English Communication",
    ],
    "experience": [
        {
            "title": "Customer Service Coordinator",
            "company": "Western Digital, San Jose, CA (Great Oaks)",
            "dates": f"Apr 2023 {EN} Present",
            "bullets": [
                "Answer customer calls promptly and handle requests, inquiries, and complaints in a respectful, caring manner at WD Great Oaks (5601 Great Oaks Pkwy)",
                "Process product returns and day-to-day RMA receiving; verify warranty coverage so service requirements are met before a replacement or repair moves",
                "Investigate complaints, manage high-priority escalations with engineering and warehouse, and drive timely resolution",
                "Set realistic timelines, follow up on RMA backlogs and outstanding parts, and log every case in Excel and Outlook so schedules hold",
                "Follow written work instructions, multi-task with minimum supervision, and meet daily close-out deadlines in a fast-paced on-site team",
            ],
        },
        {
            "title": "Customer Care Representative",
            "company": "TD SYNNEX, Fremont, CA",
            "dates": f"Jun 2021 {EN} Mar 2023",
            "bullets": [
                "Supported distributor customer care at 44201 Nobel Drive: parts fulfillment, RMA status, and order questions by phone and email",
                "Coordinated with internal sales, warehouse, and vendor teams so returns and replacements hit the committed date",
                "Documented cases, tracked backlogs, and used Excel to keep aging RMAs visible to leads",
                "Owned issues through resolution and reset customer expectations when a part or credit was delayed",
            ],
        },
        {
            "title": "Customer Service Representative",
            "company": "T-Mobile, Milpitas, CA (Great Mall)",
            "dates": f"Aug 2018 {EN} May 2021",
            "bullets": [
                "Handled walk-up and phone inquiries, account questions, and device-return issues with clear English and a calm, professional tone",
                "Processed exchanges and documented each interaction so the next associate could pick up the case",
                "Worked a fast retail floor, multi-tasked between the counter and the queue, and followed store procedures on every ticket",
                "Built the ownership and follow-through habits later used on RMA and warranty desks",
            ],
        },
    ],
    "certifications": [
        "First Aid / CPR Certified",
        "Workplace Safety Training",
    ],
}
