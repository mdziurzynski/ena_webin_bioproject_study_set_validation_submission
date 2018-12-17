#!/usr/bin/env python3
# stud_farm.py

import argparse
import subprocess
import re

# Define and parse options
def parse_opts():
    parser = argparse.ArgumentParser(description = "Register studies with ENA")
    parser.add_argument("-u", "--username", type=str,
                        help="Webin Username: Webin-XXXXX")
    parser.add_argument("-p", "--password", type=str,
                        help="Webin password")
    parser.add_argument("-s", "--submit", action="store_true",
                        help="Submit studies to ENA production, default=FALSE")
    parser.add_argument("-i", "--input_csv", type=str,
                        help="Path to input CSV")
    parser.add_argument("-v", "--validate", action="store_true",
                        help="Validate CSV and quit")
    parser.add_argument("-g", "--generate_xml", action="store_true",
                        help="Make XML and quit")

    args = parser.parse_args()
    print(parser.help)
    return args

# Validate credentials
def validate_credentials(username, password, submit):
    # Build curl command:
    c = "curl"
    u = "-u"
    d =  (username + ":" + password)
    F = "-F SUBMISSION=@validate.xml"
    if submit:
        URL = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
    else:
        URL = "https://www.ebi.ac.uk/ena/submit/drop-box/submit/"

    # Run curl validation command, just checks that credentials work
    credential_check = subprocess.check_output([c, u, d, F, URL],
                                               universal_newlines=True)

    if re.search("success=\"true\"", credential_check):
        print("Credentials validated")
        return True
    else:
        print("Invalid username/password")
        quit()

    # see curlthing.py
    # return true or false

# Parse input CSV into list of rows
def get_rows():
    pass
    # see tsv2xml.py

# Validate input spreadsheet content
def validate_csv_row():
    pass
    # write and call subfunctions to validate each element

# Generate Project Set XML
def generate_study_xml():
    pass
    # see tsv2xml.py
    # will call validate_csv_row once written
    validate_csv_row()

# Generate Submission instruction XML
def generate_submission_xml():
    pass

# Generate Validate instruction XML
def generate_validate_xml():
    validate_instruction = """
    <SUBMISSION>
        <ACTIONS>
            <ACTION>
                <VALIDATE/>
            </ACTION>
        </ACTIONS>
    </SUBMISSION>"""

    with open("validate.xml", "w") as validate_xml:
        validate_xml.write(validate_instruction)


# Validate
def curl_validate():
    pass
    # Run submission with validation XML, use to decide whether to proceed

# Submit to ENA
def curl_submit():
    pass
    # Run submission, having previously set test or prod
    # Include warning if TEST
    # Capture output

# Report Accessions
def report_accessions():
    pass
    # parse result of curl_submit, report accessions
    # Repeat TEST warning

# Error reporting along the way


def __main__():

    user_args = parse_opts()

    generate_validate_xml()

    validate_credentials(user_args.username, user_args.password,
                         user_args.submit)

    get_rows()

    generate_study_xml()

    generate_submission_xml()

    curl_validate()

    curl_submit()


if (__name__ == "__main__"):
    __main__()
