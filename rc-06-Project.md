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
in technologies and methods, and ongoing feedback.

## Reading

* "High Performance Computing: Modern Systems and Practices" (Chapter 4, Benchmarking)

Early systems were connected to a typewriter for input and a line
printer for output [HW: verification and citation needed].  Today this
has changed very little and when it comes to most interactions remains
the same.  The only real change is the adoption of monitors and the
adoption of Unicode using UTF-8 over ASCII (which is backwards
compatible).

```
command
```
and
```
response
```

The spirit of the "Unix philosophy" is "Do One Thing and Do It Well,"
and such Unix and Linux is just a collection of small commands that,
when put together, make the whole.  In this module we will be
discussing the general framework, not the specifics of the tools, and
how it is all put together.

### Compute

This framework requires different programs (the `process`) to run and
interact in a multi-user environment in order to accomplish some
useful work.

The *process* is the fundamental unit of "compute."

> "In the beginning there was `init`"

The init process (magically, and now using systemd) is responsible for
running all the programs to setup and run the system.

A program is launched, runs, and then terminates.  Each process has a
number (called a `pid`) and has a parent process and a number of child process.

### Configuration

Processes can get configuration information through *environment
variables*.  Environment variables are `KEY=value` pairs and each
process has it's own (mutable) environment.  Child process get their
own copy of the environment, allowing for the parent to pass
configuration information to the child.


### Storage

The file is the fundamental unit of *storage*.  A file has a name,
ownership, permissions, and a location.  In Linux *files* live in
*directories* and directories are arranged into a single hierarchy of
files starting with the *root* (`/`) folder.  Processes can access
files either by specifying a *absolute path* starting with `/` or a
*relative path*.  The *relative path* is a folder that starts with the
processes *present working directory* or PWD.  Each process has a PWD
(that can change) and children inherent the parents PWD.

There are two special folders named `.` and `..`, which represent the
current and parent directories, relative to the folder that they are
in.

### Networking

In Linux communication between processes is accomplished though
`pipes` - the *network*.  These pipes can be either local or over the
network.  In the CLI this is most often the `stdin`, `stdout`, and
`stderr`.  Process pass information from their `stdout` to a child's
`stdout` (we will convently ignore `stderr`) though the use of
*redirection*.  This information is in the form of a stream of bytes
that is buffered between each process, and each process can run
simultaneously.*.  Redirection also allows directing streams to and
from files (hence the name).  In this way a number of commands can be
chained together transforming the information along the way.


## Reading
 * HPC Carpentry: Linux Shell
   (https://hpc-carpentry.github.io/hpc-shell/) sections 1-4
