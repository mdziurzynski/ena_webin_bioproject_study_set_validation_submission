#!/usr/bin/env python3
# tsv_creation_wizard.py

from pprint import pprint
import csv

STUDY_HEADERS = ['alias','name', 'title', 'description']
SAMPLE_HEADERS = ['alias', 'title', 'description']
EXPERIMENT_HEADERS = ['alias', 'study_ref', 'sample_descriptor', 'title', 'library_strategy', 'library_source', 'library_selection', 'library_layout', 'library_construction_protocol', 'instrument_model']
RUN_HEADERS = ['alias', 'experiment_ref', 'file_1_name', 'file_2_name', 'file_1_filetype', 'file_2_filetype', 'file_1_checksum_method', 'file_2_checksum_method', 'file_1_checksum', 'file_2_checksum']


def _build_tsv(object_list, object_type, header):
    with open("{0}_data.tsv".format(object_type), 'w') as output_csv:
        writer = csv.writer(output_csv, dialect='excel')
        writer.writerow(header)
        for object_name in object_list:
            writer.writerow([object_name])


def create_tsvs(structure_dict):
    
    study_aliases = []
    sample_aliases = []
    experiment_aliases = []
    run_aliases = []
    for study_name in structure_dict:
        study_aliases.append(study_name)

        for sample_name in structure_dict[study_name]:
            sample_aliases.append(sample_name)

            for experiment_name in structure_dict[study_name][sample_name]:
                experiment_aliases.append(experiment_name)

                for run_name in structure_dict[study_name][sample_name][experiment_name]:
                    run_aliases.append(run_name)

    _build_tsv(study_aliases, 'study', STUDY_HEADERS)
    _build_tsv(sample_aliases, 'sample', SAMPLE_HEADERS)
    _build_tsv(experiment_aliases, 'experiment', EXPERIMENT_HEADERS)
    _build_tsv(run_aliases, 'run', RUN_HEADERS)

    print("\nFinished building input TSVs. Have fun.")

def define_deep_structure(parent_name, child_type):
    type_number = 0
    print("\nDEFINE {0}s for {1}".format(child_type.upper(), parent_name))
    while type_number == 0:
        type_number_tmp = input("How many {0}S do you have in {1}? ".format(child_type.upper(), parent_name))

        try:
            type_number_tmp = float(type_number_tmp)
        except ValueError:
            print("Wrong value type. Please input an integer bigger than 0\n")
            continue

        if type_number_tmp < 1:
            print("Wrong value type. Please input an integer bigger than 0\n")
            continue
        
        type_number = type_number_tmp


    return type_number_tmp


def create_aliases(base_name, count):
    res = []
    for num in range(1, int(count+1)):
        res.append("{0}_{1}".format(base_name, num))
    return res


def tsv_wizard():
    print("pyENA input data wizard\n")
    print("Here you can define your study data structure. The wizard will create all the necessary TSV files for your metadata.")
    start = input("Do you want to proceed?\n WARINING: all the TSV in this directory will be REMOVED\n(Y/n) ")
    if start != "Y":
        print("Exiting TSV creation wizard.")


    structure_dict = {}

    study_number = 0
    while study_number == 0:
        study_number_tmp = input("How many STUDIES do you have? ")

        try:
            study_number_tmp = float(study_number_tmp)
        except ValueError:
            print("Wrong value type. Please input an integer bigger than 0\n")
            continue

        if study_number_tmp < 1:
            print("Wrong value type. Please input an integer bigger than 0\n")
            continue
        
        study_number = study_number_tmp

    study_structure = {base_name:{} for base_name in create_aliases("study", study_number)}
    structure_dict.update(study_structure)
    
    print("Your study structure looks like that:")
    pprint(structure_dict)

    for study_name in structure_dict:
        sample_count = define_deep_structure(study_name, 'sample')

        base_name = study_name + "/sample"

        sample_structure = {base_name:{} for base_name in create_aliases(base_name, sample_count)}

        structure_dict[study_name] = sample_structure

    print("Your STUDY and SAMPLE structure looks like that:")
    pprint(structure_dict)

    for study_name in structure_dict:
        for sample_name in structure_dict[study_name]:
            experiment_count = define_deep_structure(sample_name, 'experiment')

            base_name = sample_name + "/experiment"

            experiment_structure = {base_name:{} for base_name in create_aliases(base_name, experiment_count)}

            structure_dict[study_name][sample_name] = experiment_structure

    print("Your STUDY, SAMPLE and EXPERIMENT structure looks like that:")
    pprint(structure_dict)

    for study_name in structure_dict:
        for sample_name in structure_dict[study_name]:
            for experiment_name in structure_dict[study_name][sample_name]:

                run_count = define_deep_structure(experiment_name, 'run')

                base_name = experiment_name + "/run"

                run_structure = {base_name:{} for base_name in create_aliases(base_name, run_count)}

                structure_dict[study_name][sample_name][experiment_name] = run_structure

    print("\n\nYour final structure looks like that:")
    pprint(structure_dict)
    create_tables = input("\nCreate TSVs? (Y/n) ")
    if create_tables == 'Y':
        create_tsvs(structure_dict)
    else:
        print("Aborting.")

    return True