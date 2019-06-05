#!/usr/bin/env python3
# study_subs.py
import os
import sys

STUDY_HEADER = ["ALIAS", "NAME", "TITLE", "DESCRIPTION", "LOCUS_TAG_PREFIX"]

def check_if_file_exists(file_path):
    if os.path.isfile(file_path):
        sys.exit(f'Submission file {file_path} exists! Will not overwrite. Exiting')

def create_study_submission_tsv():
    study_submission_tsv_path = "study_submission.tsv"
    check_if_file_exists(study_submission_tsv_path)
    with open(study_submission_tsv_path, w) as tsv_file:
        csv_writer = csv.writer(tsv_file, delimiter='\t')
        csv_writer.writerow(STUDY_HEADER)
    study_tsv_full_path = os.path.abspath(study_submission_tsv_path)
    print(f'Study tsv file created at: {study_tsv_full_path}')
    return True

def create_experiment_submission_tsv():
    pass

def create_sample_submission_tsv():
    pass

def create_run_submission_tsv():
    pass