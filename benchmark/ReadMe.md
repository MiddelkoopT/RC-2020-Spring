# Benchmark Project

## Background

This project is a sample workflow using the "Benchmark" chapter in the
HPC text as an example.  We will be computing the HPC benchmarks on
this system and comparing it with the top 500.  We will also be doing
analysis on the top 500 data.

## Parts.

Setup the environment by running the `setup.sh` command.  This downloads the data as well.

The entire workflow is run using the `run.sh` command.

### Download

The data is downloaded from the top 500 website with the `download.sh` script.

### Preprocess

The preprocess step takes data in XML format and converts it to CSV for R.

### Clean

The `clean.sh` script delete's all temporary and downloaded data (WARNING).

### ToDo

* Need to import into R and do some analysis.
* Create jobfiles.

## Configuration

The configuraiton is stored in `config.json`

 * topdataxml - The data file associated with the analysis input (XML)
 * topdatacsv - The data file associated with the analysis output (CSV)




