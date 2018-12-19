#!/usr/bin/env python3
# stud_farm.py

import argparse
import subprocess
import re
import csv

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
    return args


# Validate credentials
def validate_credentials(username, password, submit):
    # Build curl command:
    c = "curl"
    u = "-u"

    try:
        d =  (username + ":" + password)
    except:
        print("ERROR: Username or password is null, cannot validate submission")
        return False

    F = "-F SUBMISSION=@validate.xml"

    if submit:
        URL = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"
    else:
        URL = "https://www.ebi.ac.uk/ena/submit/drop-box/submit/"

    # Submission command with validation XML to check credential validity
    credential_check = subprocess.check_output([c, u, d, F, URL],
                                               universal_newlines=True)

    # Handle result of check
    if re.search("Access Denied", credential_check):
        print("Invalid username/password")
        return False
    else:
        print("Credentials validated")
        return True


# Parse input CSV into list of rows
def get_rows(input_csv):
    tsv_rows = csv.reader(open(input_csv, 'r'), delimiter='\t')
    return tsv_rows
    # see tsv2xml.py


# Validate input spreadsheet content
def validate_csv_row(row):
    #TODO: some actual validation
    return True
    # write and call subfunctions to validate each element


# Convert row from input TSV to study set XML
def csv_to_xml(row):
    return """
    <PROJECT alias="%s">
        <NAME>%s</NAME>
        <TITLE>%s</TITLE>
        <DESCRIPTION>%s</DESCRIPTION>
        <SUBMISSION_PROJECT>
            <SEQUENCING_PROJECT/>
        </SUBMISSION_PROJECT>
        <PROJECT_LINKS>
           <PROJECT_LINK>
              <XREF_LINK>
                 <DB>PUBMED</DB>
                 <ID>%s</ID>
              </XREF_LINK>
           </PROJECT_LINK>
        </PROJECT_LINKS>
    </PROJECT>""" % (
    row[0], row[1], row[2], row[3], row[4])

# Generate Project Set XML
def generate_study_xml(input_csv, validate, generate_xml):
    csv_rows = get_rows(input_csv)

    xml = open("study_set.xml", "w")
    xml.write("<PROJECT_SET>")

    for row in csv_rows:
        validate_csv_row(row)
        csv_to_xml(row)

    xml.write("\n</PROJECT_SET>")
    xml.close()

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
        return True

    return False


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
    print(user_args.validate)

    try:
        generate_validate_xml()
    except:
        print("Could not generate validation XML, exiting")
        quit()

    if (user_args.generate_xml):
        pass
    else:
        if validate_credentials(user_args.username, user_args.password,
                             user_args.submit):
            pass
        else:
            print("Credential validation failed, exiting program")
    
    generate_study_xml(user_args.input_csv, user_args.validate, user_args.generate_xml)

    generate_study_xml()

    generate_submission_xml()

    curl_validate()

    curl_submit()


if (__name__ == "__main__"):
    __main__()
