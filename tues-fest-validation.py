#!/usr/bin/env python3

RESULTS_CSV     = 'tues-fest.tsv'
VALID_KEYS_FILE = 'valid-keys.txt'
KEY_INDEX       = 1

def main():
    with open(RESULTS_CSV, 'r') as file:
        results = file.readlines()

    with open(VALID_KEYS_FILE) as key_file:
        valid_keys = key_file.readlines()

    valid_keys = [key.strip() for key in valid_keys]

    teams = {}
    for line in results[1:]:
        line = line.split('\t')
        if check_key_if_valid(valid_keys, line[KEY_INDEX]):
            for team in line[2:]:
                team = team.strip()
                if team in teams:
                    teams[team] += 1
                else:
                    teams[team] = 1

    for key, value in teams.items():
        print("{}: {}".format(value, key))

def check_key_if_valid(valid_keys, key):
    if key in valid_keys:
        del valid_keys[valid_keys.index(key)]
        return True
    else:
        return False

main()