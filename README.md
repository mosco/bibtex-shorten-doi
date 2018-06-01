
# BibTeX shorten DOI
Convert the DOI fields of a BibTeX file to shortened DOI names (see http://shortdoi.org)
This is helpful if you want to include DOI links using the Latex DOI package but wish to avoid having huge DOI names in your paper's references section.

## Usage

```bibtex_shorten_doi.py <.bib file name>```


## WARNING

Shortened DOIs are unfortunately *not* DOIs. They can only be used for lookup on doi.org.

This means that if you use the LaTeX doi package, then your paper's DOI links will work, since they point to doi.org, but if your readers try to perform DOI lookup on sites like crossref.org and Sci-Hub, they will be disappointed.

For this reason, I cannot recommend using bibtex-shorten-doi to shorten the DOIs of your entire bibliography.


# Contact
Amit Moscovich

moscovich@gmail.com

http://mosco.github.io
     
