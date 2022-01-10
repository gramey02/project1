from setuptools import find_packages
from setuptools import setup

setup(
    name= 'seqparser',
    version= '0.0.1',
    author= 'Grace Ramey',
    author_email= 'Grace.Ramey@ucsf.edu',
    packages= find_packages(),
    description= 'Parses out Fasta and Fastq files for transcription and reverse transcription',
	install_requires= ['typing']
)