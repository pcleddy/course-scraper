#!/usr/bin/env python3
"""
UNM Course Scraper
==================
Wrapper around the shared Banner scraper configuration for UNM.
"""

from cnm_course_scraper import run_cli


UNM_BASE_URL = "https://lobowebapp.unm.edu/StudentRegistrationSsb/ssb"


def main():
    run_cli(
        default_base_url=UNM_BASE_URL,
        default_school_label="UNM",
        default_output_stem="unm_courses",
        default_bundle_name="unm_courses_data.js",
    )


if __name__ == "__main__":
    main()
