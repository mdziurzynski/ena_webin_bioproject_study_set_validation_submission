#!/usr/bin/env python3
# stud_farm.py

import argparse
import subprocess

# Define and parse options
def parse_opts(TODO:args):
    parser = argparse.ArgumentParser(descriptions = "Register studies with ENA")
    parser.add_argument("-u", "--username", help="Webin Username: Webin-XXXXX",
                        type=str, dest=username)
    parser.add_argument("-p", "--password", help="Webin password",
                        type=str, dest=password)
    parser.add_argument("-s", "--submit", help="Submit studies, default=FALSE",
                        action="store_true", dest=submit)
    parser.add_argument("-i", "--input_csv", help="Path to input CSV",
                        type=str, dest=input_csv)
    parser.add_argument("-v", "--validate", help="Validate CSV and quit",
                        action="store_true", dest=validate)
    parser.add_argument("-g", "--generate_xml", help="Make XML and quit",
                        action="store_true", dest=generate_xml)


# Validate credentials
def validate_credentials(TODO:args):
    # see curlthing.py
    # return true or false

# Parse input CSV into list of rows
def get_rows(TODO:args):
    # see tsv2xml.py

# Validate input spreadsheet content
def validate_csv_row(TODO:args):
    # write and call subfunctions to validate each element

# Generate Project Set XML
def generate_study_xml(TODO:args):
    # see tsv2xml.py
    # will call validate_csv_row once written
        validate_csv_row()

# Generate Validate and Submission XMLs
def generate_submission_xml(TODO:args):
def generate_validate_xml(TODO:args):

# Validate
def curl_validate(TODO:args):
    # Run submission with validation XML, use to decide whether to proceed

# Submit to ENA
def curl_submit(TODO:args):
    # Run submission, having previously set test or prod
    # Include warning if TEST
    # Capture output

# Report Accessions
def report_accessions(TODO:args):
    # parse result of curl_submit, report accessions
    # Repeat TEST warning

# Error reporting along the way


def __main__():

    parse_opts()

    generate_validate_xml()

    validate_credentials()

    get_rows()

    generate_study_xml()

    generate_submission_xml()

    curl_validate()

    curl_submit()
