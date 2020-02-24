# IMSE 8410 Project

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop. Source code
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Course Project

> Artificial problems yields artificial results.

> Life is messy.


## Objectives

In this module we will cover the overview of the project and the
motivation for real world work.

By the end of this module students should:
 * Be familiar with the course project scope, requirements, and expectations.
 * Start formulating their course project.
 * Have created their class project git repository
   (`rc-project-sso-First-Last`) and assign proper permission.
 * Start executing project code using domain tools and data on the command line.

## Background

This course is designed to elevate students ability to conduct their
research in a *reproducible*, *scalable*, and *sustainable* way.  In
order to effectively teach this materials students should integrate as
much as their real research, data, code, and problems into their
classwork.  An effective way of doing this is to base the course
project on actual ongoing work.  It is important that we are only
interested in the tools and the process not in the research, data, or
results produced.  In this way projects *must* be abstracted in such a
way to remove proprietary research, data, and tools while still
maintaining the spirit of the research work-flow.  This also allows
students to focus on the tools and the process and not on the results
making it easier to solve problems as they arise while maintaining a
realistic environment.  

Projects *will* and *must* evolve over the course of the semester and
constant interaction with the instructor, peers and the students
adviser is required to ensure a successful project, and by extension,
a good grade.  Careful attention to *detail* and *instructions* is
required.

Final project requirements change based on the semesters work, changes
in technologies and methods, and ongoing feedback.  This module will
contain the latest project and project proposal requirements and will
be constantly updated here. Look at the get repository changes for
updates.  The final project requirements will posted a few weeks
before the project is due.

The "Benchmark" chapter in the reading contains many of the elements
that will required in the class project and should be considered in
this context in addition to the actual benchmarking material.

## Reading
* "High Performance Computing: Modern Systems and Practices" (Chapter 4, Benchmarking)


## Project Proposal

As with the entire project this, is a work in progress and a
collaborative process and will evolve over time.

Please ensure that your project repository has been created and made
available and is in the form `rc-project-${SSO}-${FIRST}-${LAST}, all
lower case except your first and last name, which should be
capitalized.  You must share your project with me (@middelkoopt) with
"Reporter" privileges.

Place your proposal in the root of the project as Proposal.md using
proper markdown format.  You may use the gitlabs editor to edit it.
It should contain the following:

 * Title of the project
 * Abstract of the research (what is the research question being asked)
 * Source of the data (Please try to find the original source of the data)
   * Name
   * Short Description
   * URL of the website
   * URL of the data to download
 * Brief overview of the workflow
 * Brief overview of the analysis (tools used) or study (scalability
   study, parameter sweep, sensitivity study etc.) and what you wish
   to accomplish

Please note, you may use proprietary data as part of your research but
it cannot shared or be stored in your project unless it is public
data.  You may do the analysis and share the results as a part of the
project on actual data but the report cannot contain any actual data
that would not be considered public and you must get explicit approval
from the Data Stewart to do this.  If this is the case you must
provide similar (possibly synthetic, preferably benchmark, data) and
the Data Stewart must send me an email indicating their permission to
do this.


## Project

The objective of this project is to gain experience with and
demonstrate competency in developing Scientific and Engineering
Workflows and managing data. The project will utilize the methods and
examples covered in the class. Using the "1,2,3, Go" system discussed
in class the data is expected to be "3" (benchmark) and the
computation is expected to be at least "2" (textbook) class.

The project will use the gitlabs `rc-project-${USER}-${FIRST}-${LAST}` git
repository for the project and shared with "Reporter" permission to
the instructor.


### Specific Instructions
  1. The project must implement a reproducible scientific workflow
     that runs on the Clark cluster.
  2. The project results must be reproducible.  The project will be graded by
     cloning the repository and following the provided instructions.  Absolute 
     hard-coded filenames in configuration files or source code is strictly
     prohibited.
  3. The workflow must consist of at least a data download and/or
     filtering step, an analysis step, and a results step in at least
     two languages.
  4. The workflow must be able to run multiple simultaneous analysis
     or scenarios as SLURM jobs with the same analysis code.  At a
     minimum it must be able to run the textbook example (small, step
     2) and the larger analysis.
  5. All textbook examples (small) must be included in the
     repository with any expected output (use an example folder
     if needed).
  6. There must not be any large data or propriety data in the repo.
     All large data must be public and downloaded as a part of the
     workflow.
  7. Use proper commits.  Commits must be logical and of appropriate
     size with descriptive commit messages.
  8. The workflow must be properly documented, licensed, and use
     proper citation.  The significant use of example code is
     permitted as long as it is sited and the licenses are compatible.
     For the documentation,
	 1. Provide a brief overview of the analysis.
	 2. Document the overall workflow (data, steps, analysis)
     3. Document each step in the process in detail (analysis, transformations).
	 4. Document the source data and the intermediary data (the format
        and metadata of the data between steps).
	 5. Use of the textbook example in the documentation may be helpful.
  9. Multiple workflows must use configuration files (`config.json`),
     not changes in source files.
 10. The primary goal is to build and document a scientific workflow,
     not to do the analysis.


### Grading

The project will be graded on the following areas:
 1. The utilization of git to manage the project including properly
    formed commits and commit comments.
 2. Documentation of the project with a project level
    "project/ReadMe.md" file written in "gitlabs flavored markdown" to
    describe the files, data, and metadata.  This file should contain
    the references to the data used in the project.
 3. Documentation of the project data (metadata) placed in the
    "project/ReadMe.md" file in a "metadata" section.  If this data is
    copied from the website then the URL must be included in the
    document.
 4. The quality of the data processing and analysis.
 5. The quality of the code (formatting, comments, coding style etc.).
 6. The use of SLURM to manage the Workflow.


## Exercise

Develop a preliminary proposal and document the workflow in the
"Benchmarking" chapter in the text.
