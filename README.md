# Introduction

This repo contains various scripts for computing sequences related to the Enots Wolley sequence. I created these scripts for an on-going research into the properties of these sequences ([ArXiv link](https://arxiv.org/pdf/2207.01448.pdf).)

# File descriptions

The directory `./text_output` contains examples of the output of all of the programs. You can view these without having to download/run this project.

The following files are for computing sequences. These are meant to be executed directly:

- `primefact_enots.py` - The original Enots Wolley sequence ([OEIS link](https://oeis.org/A336957))
- `binary_enots.py` - The binary Enots Wolley sequence  ([OEIS link](https://oeis.org/A338833))
- `natural_enots.py` - The Enots Wolley sequence. Effectively, this is a version of the Enots Wolley sequence where the value of `i`th digit is `i`. Currently, there is no OEIS page for this sequence. 
- `primefact_EKG.py` - The original EKG sequence ([OEIS link](https://oeis.org/A064413))
- `binary_EKG.py` - The binary analog of the EKG sequence ([OEIS link](https://oeis.org/A115510))
- `partitions_lex.py` - Generates a table of integer partitions in lexicographical order, formatted in a style simillar to the outputs of the other programs in this repo.



- `generate_figure_binary_enots.py` - A one-off script that I wrote to generate a figure for a paper ([ArXiv link](https://arxiv.org/pdf/2207.01448.pdf).) 
- `generate_figure_enots.py` - Another one-off script that I wrote to generate a figure for a paper ([ArXiv link](https://arxiv.org/pdf/2207.01448.pdf).) 

Libraries/utilities. These are not meant to be executed directly.

- `bitlib.py` - Functions for working with the binary representation of a number.
- `factlib.py` - Functions for working with the prime factorization of a number.
- `print_table.py` - Contains functions for formatting the output into a nice table.

# Installation

First, install the required packages:

`pip3 install tabulate`
`pip3 install primefac`
`pip3 install sympy`

Then, execute the file you want to run. 
