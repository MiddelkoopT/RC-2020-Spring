# IMSE 8410 Workflows

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Research and Engineering Computational and Data Workflows

> "One, Two, Three, and Go"

> "If it's not Reproducible, it's Magic" 

## Objectives

In this module we will present a methodology for reproducible
scientific and engineering workflows. 

By the end of this module students should be:
 * Familiar with the "1, 2, 3, and Go" method,
 * Familiar with what is required to start a reproducable,
   sustainable, and scaleable scientific workflow including metadata
   and data management plans.
 * Familiar with scientific workflows and the general steps in the
   workflow.
 * Familiar with the different components to manage a scientific
   workflow.


## Methodology

We will use the common term "Scientific Workflows" and "Computational
and Data Workflows" throughout the class but this also includes
engineering, digital humanities, and other computational and data
intensive scholarly work.

Computational and Data workflows are about building new systems and
scaling existing ones.  The best approach is to do things deliberately
and incrementally, which means starting small, testing often, and
scaling slowly both in terms of code and data.

One method for this is to use the 1,2,3 Go method, which can be expanded to 1:
  1. Hello - get the technology working.
  2. Textbook Example - do something easy.
  3. Benchmark and Reference problems - resolve community problems.

Only after this go and solve your original problem.

This will provide a framework to test code and data alike in a
sustainable way, making the use of techniques such as Test Driven
Development (TDD) and Continuous Integration (CI) a natural and
logical next step.

## Reading
Required Reading:
 * Scientific Workflows:
   http://www.pnl.gov/computing/technologies/sci_workflow.stm
 * A modern ‘Hello, World’ program needs more than just code:
   https://stackoverflow.blog/2020/03/05/a-modern-hello-world-program-needs-more-than-just-code/


## Workflows

Even before a workflow is created there are important prerequisites.

1. A problem statement.  What research, engineering, or business
   question are you trying to answer.
2. A description of the system.  Detailed information about the system
   that the question derives its information.
3. Actual data.  Access to the full raw data.  A subset in an
   spreadsheet does not count.  The way in which the data is to be
   extracted in used must also be in place (access to the database for
   instance).
4. Metadata.  A proper description of the actual data fields and the
   data relations is required.
5. A Data Management Plan.  Who owns the data and can you publish the
   results?  What are the security requirements?  Who will have access
   to this data? Where will the data live? How will it be stored and
   tracked? How will the integrity of the data be assured (checksums,
   backups, etc).

Once the these requirements have been met, then a workflow can be
developed. A workflow in general consists of the following steps:

1. Data Acquisition (Input)
   * Test Data (simple and known-good-solutions)
   * Generated Data
   * Benchmark Problems
   * Real Data
2. Data Pre-Processing
   * Data format conversion
   * Data filtering (subset)
   * Data cleaning (matching events, outliers etc.)
   * Data transformation (arc based to node based)
   * Data pre-processing and storage (preparation for analysis)
3. Experimental and Analysis Control
   * Plan and generate jobs (experiments, analysis parameters etc).
   * Prepare data and jobs (marshal data)
   * Monitor job progress
4. Computation
   * SLRUM runs the jobs on the cluster
   * Job get's input for computation
   * Job runs computation (Python)
   * Job collects and writes data
5. Results Collection
   * Collect and verify data (feasibility and structure/format).
   * Transform and filter for analysis
   * Comparison with *known good solutions* for verification
6. Analysis and Analytics (Output)
   * Statistics (R)
   * Visualization 
   * Report generation

These steps utilize the following components:
1. A source code management system (git) to manage code.
2. A project management system (gitlabs) to manage people and work.
3. A data management system (may include a database) to manage data and metadata.
4. A job management system (experiment generation and a cluster with SLURM) to manage compute.
5. An information management system to coordinate everything (workflows).
6. Documentation to help others understand, including yourself.
7. Data visualization to see the data, the code, and the analysis in action.

## Example Workflow

The example workflow that will be used throughout this module and
subsequent modules is based around reproducing Chapter 4, Benchmarking
in the HPC textbook.  The complete example is located in
the [benchmark/](benchmark/) folder.

### Prerequisites

1. Problem statement: To use the HPC top 500 benchmarking tools to
   determine the performance of the cluster and compare it to the
   current top 500 and to previous years.
2. Description of the system: See Chapter 4 "Benchmarking" in the HPC textbook
3. Data:
   * https://www.top500.org/lists/2019/11/
   * https://www.top500.org/lists/2019/11/download/TOP500_201911_all.xml
4. Metadata: https://www.top500.org/project/top500_description/ [Metadata.md](benchmark/docs/Metadata.md)
5. Data Management Plan: All data is public and will be retrieved from
   external sources.  Workflow will be stored in git and replicated to GitLab.com.

### Data Acquisition (Input)

Data should be retrieved via automated scripts and stored in the
appropriate locations.  No data except "1" and "2" should be stored in
the repository.  Larger data-sets should have integrity (checksum)
information stored.

* Download data [download.sh](benchmark/download.sh)
* Metadata [data.md5](benchmark/data.md5)

A local copy of the metadata should be stored in case it is located in
a separate location of the data and in case it changes (in our case).

* [Metadata.md](benchmark/docs/Metadata.md)

Note the data is stored in the `data` folder that is ignored by git to
prevent accidental committing and to be able to "reset" the project quickly.

* [.gitignore](benchmark/.gitignore) file.

Often it will be necessary to test technologies and techniques in the
process.  By using small data-sets we can test if it is appropriate
for use.  Most of these small tests do not need to be automated to a
large degree as they are a proof of concept.  All source files should
be stored in the repository, even examples that failed.  Examples that
are derived from online examples should reference them for "proper
referencing" and future reference.  Tests *should* not use actual
data, or data referenced in online examples, but simple synthetic data
as small as possible to exercise a the libraries and demonstrate
minimal capacities in a way that is consistent with the workflow.
This process will give a feel of the quality, fit, and appropriateness
of the tools.  

* [input.xml](benchmark/examples/input.xml)
* [convert.py](benchmark/examples/convert.py)
* [process.R](benchmark/examples/process.R)

Intermediary files should not be stored in git as well.
* [.gitignore](benchmark/examples/.gitignore)

#### Exercise

After reading the above materal re-implement them in your own class
repository under `benchmark/` without looking back at the
solutions. You should follow the following process.

1. Utilize a proper git workflow with commits, branches, and
   merges. This can be on a single "feature branch" with a single
   "Merge" at the end.
2. Create a `ReadMe.md` file describing the project (prerequisites
   section) in Markdown in the `benchmark/` folder. Include a
   references and resources section to help the reader.
3. Download the top 500 XML file.
4. Produce and verify the integrity of the data (use `sha256sum` instead of `md5sum`).
5. Create an example Python script to read in XML and produce CSV data
   with headers.
6. Create an example R Processing script to read in the resulting data
   and compute the average of one of the columns.

Attempt to do the following:
1. Read in the Top500 XML data and produce a CSV file with relevant
   data.
2. Compute some summary statistics of interest on the Top500 list.

