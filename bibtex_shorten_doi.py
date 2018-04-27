#!/usr/bin/env python3
#
# This script takes a BibTeX file and converts all the DOI fields to shortened DOI names (see http://shortdoi.org)
import sys
import urllib
import urllib.request
import pybtex.database
import json


def get_short_doi(doi):
    print(f'Shortening DOI: {doi}')
    url = 'http://shortdoi.org/' + urllib.parse.quote(doi) + '?format=json'
    print(f'Requesting URL: {url}')
    response = urllib.request.urlopen(url)
    data = response.read()
    json_response = json.loads(data)
    print(json_response)
    return json_response['ShortDOI']


def shorten_doi_fields(input_filename):
    bib = pybtex.database.parse_file(input_filename)
    for (k,v) in bib.entries.items():
        print('='*64)
        print(f'Citation Key: {k}')
        print(v)
        try:
            doi = v.fields['doi']
        except KeyError:
            print('No DOI field, continuing')
            continue

        short_doi = get_short_doi(doi)
        v.fields['doi'] = short_doi

    output_filename = input_filename+'.shortdoi.bib'
    print(f'Writing output to {output_filename}')
    bib.to_file(output_filename)


def main():
    if len(sys.argv) == 2:
        shorten_doi_fields(sys.argv[1])
    else:
        print(f'Usage: {sys.argv[0]} <bibfile>')


if __name__ == '__main__':
    main()
