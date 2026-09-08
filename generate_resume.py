#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render a one-page, ATS-friendly resume matching the existing template."""

from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

NAVY = Color(0.121569, 0.305882, 0.47451)
GRAY = Color(0.2, 0.2, 0.2)
LEFT = 49.2
WIDTH = 513.6
PAGE_W, PAGE_H = letter
BODY_SIZE = 9.5
BODY_LEADING = 12.0
BULLET_LEADING = 11.5
# Helvetica WinAnsi bullet (matches the warehouse template)
BULLET = chr(149)


def pdf_text(text: str) -> str:
    """Map common Unicode punctuation to Helvetica WinAnsi glyphs."""
    return (
        text.replace("\u2013", chr(150))
        .replace("\u2014", chr(151))
        .replace("\u2022", chr(149))
        .replace("\u00e9", chr(233))
        .replace("\u00a0", chr(160))
    )


def wrap_text(text: str, font: str, size: float, max_width: float) -> list[str]:
    # Split on regular spaces only so non-breaking spaces keep phrases together.
    words = text.split(" ")
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if stringWidth(trial, font, size) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def wrap_phrases(phrases: list[str], font: str, size: float, max_width: float, sep: str) -> list[str]:
    """Wrap a list of phrases without splitting inside a phrase."""
    lines: list[str] = []
    current = ""
    for phrase in phrases:
        trial = phrase if not current else f"{current}{sep}{phrase}"
        if stringWidth(pdf_text(trial), font, size) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = phrase
    if current:
        lines.append(current)
    return lines or [""]


class ResumeCanvas:
    def __init__(self, path: str):
        self.c = canvas.Canvas(path, pagesize=letter)
        self.y = PAGE_H - 50.4
        self.c.setTitle("")
        self.c.setAuthor("")

    def set_meta(self, data: dict) -> None:
        self.c.setTitle(f"{data['name'].title()} - {data['target_title']}")
        self.c.setAuthor(data["name"].title())

    def hline(self, y: float, weight: float = 1) -> None:
        self.c.setStrokeColor(NAVY)
        self.c.setLineWidth(weight)
        self.c.setLineCap(1)
        self.c.line(LEFT, y, LEFT + WIDTH, y)

    def section(self, title: str) -> None:
        self.y -= 8
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(LEFT, self.y, title)
        self.y -= 2
        self.hline(self.y)
        self.y -= 14

    def header(self, data: dict) -> None:
        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica-Bold", 16)
        name = data["name"]
        name_w = stringWidth(name, "Helvetica-Bold", 16)
        self.c.drawString(LEFT + (WIDTH - name_w) / 2.0, self.y, pdf_text(name))
        self.y -= 14

        self.c.setFillColor(NAVY)
        self.c.setFont("Helvetica-Bold", 11)
        title = data["target_title"]
        title_w = stringWidth(title, "Helvetica-Bold", 11)
        self.c.drawString(LEFT + (WIDTH - title_w) / 2.0, self.y, pdf_text(title))
        self.y -= 13

        contact = f"{data['phone']}  |  {data['email']}  |  {data['location']}"
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", BODY_SIZE)
        contact_w = stringWidth(contact, "Helvetica", BODY_SIZE)
        self.c.drawString(LEFT + (WIDTH - contact_w) / 2.0, self.y, pdf_text(contact))
        self.y -= 6
        self.hline(self.y, weight=1.5)
        self.y -= 4

    def summary(self, text: str) -> None:
        self.section("PROFESSIONAL SUMMARY")
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", BODY_SIZE)
        for line in wrap_text(text, "Helvetica", BODY_SIZE, WIDTH):
            self.c.drawString(LEFT, self.y, pdf_text(line))
            self.y -= BODY_LEADING
        self.y += 2

    def competencies(self, items: list[str]) -> None:
        self.section("CORE COMPETENCIES")
        sep = f"  {BULLET}  "
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", BODY_SIZE)
        for line in wrap_phrases(items, "Helvetica", BODY_SIZE, WIDTH, sep):
            self.c.drawString(LEFT, self.y, pdf_text(line))
            self.y -= BODY_LEADING
        self.y += 2

    def experience(self, jobs: list[dict]) -> None:
        self.section("PROFESSIONAL EXPERIENCE")
        indent = 14
        bullet_width = WIDTH - indent
        for i, job in enumerate(jobs):
            if i:
                self.y -= 3
            title = job["title"]
            rest = f"  |  {job['company']}"
            self.c.setFillColor(GRAY)
            self.c.setFont("Helvetica-Bold", BODY_SIZE)
            self.c.drawString(LEFT, self.y, pdf_text(title))
            title_w = stringWidth(title, "Helvetica-Bold", BODY_SIZE)
            self.c.setFont("Helvetica", BODY_SIZE)
            self.c.drawString(LEFT + title_w, self.y, pdf_text(rest))
            dates = pdf_text(job["dates"])
            date_w = stringWidth(dates, "Helvetica", BODY_SIZE)
            self.c.drawString(LEFT + WIDTH - date_w, self.y, dates)
            self.y -= 13
            for bullet in job["bullets"]:
                lines = wrap_text(bullet, "Helvetica", BODY_SIZE, bullet_width - 10)
                self.c.setFont("Helvetica", BODY_SIZE)
                self.c.drawString(LEFT + indent, self.y, BULLET)
                self.c.drawString(LEFT + indent + 10, self.y, pdf_text(lines[0]))
                self.y -= BULLET_LEADING
                for cont in lines[1:]:
                    self.c.drawString(LEFT + indent + 10, self.y, pdf_text(cont))
                    self.y -= BULLET_LEADING
                self.y -= 1
            self.y -= 2

    def certifications(self, items: list[str]) -> None:
        self.section("CERTIFICATIONS")
        joined = f"  {BULLET}  ".join(items)
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica", BODY_SIZE)
        for line in wrap_text(joined, "Helvetica", BODY_SIZE, WIDTH):
            self.c.drawString(LEFT, self.y, pdf_text(line))
            self.y -= BODY_LEADING
        self.y += 2

    def education(self, edu: dict) -> None:
        self.section("EDUCATION")
        self.c.setFillColor(GRAY)
        self.c.setFont("Helvetica-Bold", BODY_SIZE)
        self.c.drawString(LEFT, self.y, pdf_text(edu["credential"]))
        cred_w = stringWidth(edu["credential"], "Helvetica-Bold", BODY_SIZE)
        self.c.setFont("Helvetica", BODY_SIZE)
        dash = "  " + chr(151) + "  "  # em dash in WinAnsi
        self.c.drawString(LEFT + cred_w, self.y, dash + pdf_text(edu["school"]))

    def save(self) -> float:
        if self.y < 36:
            raise SystemExit(f"Resume overflowed one page (y={self.y:.1f}). Tighten copy.")
        self.c.save()
        return self.y


def load_job(module_name: str) -> dict:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    mod = importlib.import_module(module_name)
    return mod.RESUME


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a one-page targeted resume PDF.")
    parser.add_argument(
        "job",
        nargs="?",
        default="jobs.staples_print_specialist",
        help="Python module path containing RESUME (default: jobs.staples_print_specialist)",
    )
    args = parser.parse_args()
    data = load_job(args.job)
    out = Path(__file__).resolve().parent / data["filename"]
    renderer = ResumeCanvas(str(out))
    renderer.set_meta(data)
    renderer.header(data)
    renderer.summary(data["summary"])
    renderer.competencies(data["competencies"])
    renderer.experience(data["experience"])
    renderer.certifications(data["certifications"])
    renderer.education(data["education"])
    remaining = renderer.save()
    print(f"Wrote {out} ({remaining:.1f} pt remaining at bottom)")


if __name__ == "__main__":
    main()
