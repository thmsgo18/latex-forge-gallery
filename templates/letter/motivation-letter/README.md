# MotivationLetterLatexTemplate
Latex Template for motivations Letter used with Pandoc

# Usage

create a file config.yaml or use the sequences to end and start a yaml file in a markdown file :

\---  
...

the fields to put in the config file are :  
 
 - yourName:
 - yourAddress:
 - yourPostalCode:
 - yourCity:
 - yourCountry:
 - yourPhone: (optional)
 - yourEmail: (optional)
 - receiver:
 - department:
 - company:
 - receiverAddress:
 - receiverPostalCode: 
 - receiverCity: 
 - receiverCountry: 
 - subject:
 - opening:
 - closing:
 - lang:
 
 
Opening and closing are already ended respectively by a comma and a dot.
Long sentences or sequences with space in it should be enclosed in squared brackets and quotation marks :
 
 - yourAddress: ["somewhere in the wolrd 54"]

# Installation

Install last version of pandoc and xelatex

# Compilation

run :    

pandoc --template=template_motivation_letter.latex **my_file.md** -o **output_file.pdf** --pdf-engine=xelatex --filter pandoc-latex-fontsize --highlight-style kate
