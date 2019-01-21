#!/usr/bin/env python3
# stud_farm.py
#
# Accepts a table of study attributes in TSV format, parses them to a
# PROJECT_SET XML, validates the XML and then submits it to ENA.
# Options exist to just generate the XML and validate it, without submitting.
# TODO:
#   - Validate content of TSV file
#   - Merge various functions for readability, maintainability, etc.

import argparse
import csv
import re
import subprocess
import xml.etree.ElementTree as ET

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

    # Concatenation will fail if one value cannot be coerced to string
    try:
        d =  (username + ":" + password)
    except:
        print("ERROR: Username or password is null, cannot validate submission")
        return False

    F = "-F SUBMISSION=@validate.xml"

    if submit:
        URL = "https://www.ebi.ac.uk/ena/submit/drop-box/submit/"
    else:
        URL = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"

    # Submission command with validation XML to check credential validity
    print("Validating Webin credentials:")
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
    # write and call subfunctions to validate each element
    return True


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
    next(csv_rows) # Skips header row

    xml = open("project_set.xml", "w")
    xml.write("<PROJECT_SET>")

    for row in csv_rows:
        validate_csv_row(row) # Revisit line once function does something
        try:
            project_xml = csv_to_xml(row)
        except:
            # Would be good to specify which row the error occurs on
            print("Failed to convert row to XML, check validity of TSV file")
            xml.close()
            quit()

        xml.write(project_xml)

    xml.write("\n</PROJECT_SET>")
    xml.close()


# Generate Submission instruction XML
def generate_submission_xml():
    submission_instruction = """
    <SUBMISSION>
        <ACTIONS>
            <ACTION>
                <ADD/>
            </ACTION>
        </ACTIONS>
    </SUBMISSION>"""

    with open("submit.xml", "w") as submission_xml:
        submission_xml.write(submission_instruction)
        return True

    return False


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


# Run submission with validation XML, use to decide whether to proceed
def curl_validate(username, password, submit, validate):
    # Build curl command:
    c = "curl"
    u = "-u"

    # Concatenation will fail if one value cannot be coerced to string
    try:
        d =  (username + ":" + password)
    except:
        print("ERROR: Username or password is null, cannot validate submission")
        return False

    F = "-F SUBMISSION=@validate.xml"
    P = "-F PROJECT=@project_set.xml"

    if submit:
        URL = "https://www.ebi.ac.uk/ena/submit/drop-box/submit/"
    else:
        URL = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"

    # Submission command with validation XML to check credential validity
    print("Validating project set submission:")
    validate_study_XML = subprocess.check_output([c, u, d, F, P, URL],
                                               universal_newlines=True)
    print(validate_study_XML)

    # Handle result of check
    if re.search("Access Denied", validate_study_XML):
        print("Access to ENA submission server denied")
        return False
    elif re.search("success=\"false\"", validate_study_XML):
        print("Invalid submission, please check input TSV")
        return False
    elif re.search("success=\"true\"", validate_study_XML) and validate:
        print("Study set validated, exiting")
        return False
    elif re.search("success=\"true\"", validate_study_XML):
        print("Study set validated, proceeding")
        return True
    else:
        print("Study set could not be processed, exiting")
        return False

    return False


# Submit to ENA, return output of submission
def curl_submit(username, password, submit):
    # Build curl command:
    c = "curl"
    u = "-u"

    # Concatenation will fail if one value cannot be coerced to string:
    try:
        d =  (username + ":" + password)
    except:
        print("ERROR: Username or password is null, cannot validate submission")
        return False

    F = "-F SUBMISSION=@submit.xml"
    P = "-F PROJECT=@project_set.xml"

    if submit:
        URL = "https://www.ebi.ac.uk/ena/submit/drop-box/submit/"
    else:
        URL = "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"

    # Submission command with validation XML to check credential validity
    print("Submitting project set:")
    submit_study_xml = subprocess.check_output([c, u, d, F, P, URL],
                                               universal_newlines=True)

    # Handle result of check
    if re.search("Access Denied", submit_study_xml):
        print("Access to ENA submission server denied")
        return False, submit_study_xml
    elif re.search("success=\"false\"", submit_study_xml):
        print("Invalid submission, please check input TSV")
        return False, submit_study_xml
    elif re.search("success=\"true\"", submit_study_xml) and submit:
        print("Study set submission completed")
        return True, submit_study_xml
    elif re.search("success=\"true\"", submit_study_xml):
        print("Study set TEST submission completed")
        return True, submit_study_xml
    else:
        print("Study set could not be processed, exiting")
        return False, submit_study_xml

    return False, submit_study_xml


# Report Accessions
def report_accessions(submission_result):
    tree = ET.fromstring(submission_result)
    #root = tree.getroot()

    print("Assigned accessions follow:\n")
    print("Alias\tPrimary_ID\tSecondary_ID")

    for project in tree.findall("PROJECT"):
        alias = project.get("alias")
        prj = project.get("accession")
        erp = project.find("EXT_ID").attrib.get("accession")
        print("%s\t%s\t%s" % (alias, prj, erp))

    for messages in tree.findall('MESSAGES'):
        infos = messages.findall('INFO')
        for info in infos:
            if re.match("This submission is a TEST", info.text):
                print("\nNOTICE: this was a TEST submission, you have not "
                      "truly submitted any ENA studies. If you are happy "
                      "with this submission, rerun with the `-s` flag")


def __main__():

    user_args = parse_opts()

    # Check an input CSV has been given:
    try:
        infile_exists = open(user_args.input_csv, "r")
    except:
        print("Input file path invalid or no path given, exiting")
        quit()

    # Generate validation XML
    try:
        generate_validate_xml()
    except:
        print("Could not generate validation XML, exiting")
        quit()

    # Validate credentials if we will be running curl commands:
    if user_args.generate_xml:
        pass # Credential validation is irrelevant in this case
    else:
        if validate_credentials(user_args.username, user_args.password,
                             user_args.submit):
            pass
        else:
            print("Credential validation failed, exiting")
            quit()

    # Produce project set XML
    generate_study_xml(user_args.input_csv, user_args.validate,
                       user_args.generate_xml)

    # Generate submission XML
    try:
        generate_submission_xml()
    except:
        print("Could not generate submission XML, exiting")
        quit()

    curl_validate(user_args.username, user_args.password, user_args.submit,
                  user_args.validate)

    submission_result = curl_submit(user_args.username, user_args.password,
                                    user_args.submit)

    if submission_result[0]:
        report_accessions(submission_result[1])
    else:
        quit()




if (__name__ == "__main__"):
    __main__()
