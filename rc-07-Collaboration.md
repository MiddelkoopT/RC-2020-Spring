# IMSE 8410 Collaboration with Git

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop. Source code
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Collaboration

> "If it's not in git, it did not happen"


## Objectives

In this module we will cover the basics of source code and project
collaboration with git.

By the end of this module students should:
 * Be able to use git on the command line with remote repositories.
 * Understand different git workflows.
 * Be able to create topic branches and merge them with the master branch.
 * Resolve merge conflicts.
 * Use GitLab to manage source code in a collaborative environment
   and how to use issues, branches, and merges.
 * Work collaboratively on a project within GitLab.

## Background

Managing a research project and the associated code and data is an
important part of the research lifecycle.  The ability to produce and
communicate reproducible research must be deliberate and requires the
use of project and source code management tools and techniques.  The
set of tools and services (GitLab, GitHub) surrounding the git
distributed version control tool provide a powerful combination of
project management, collaboration, and source code management
capabilities that have been widely adopted.  In this section we
explore the use of git and GitLab for this collaboration.

Large research and software projects can involve many people
simultaneously over many years and multiple locations and institutions
with people coming and going.  The next diagram demonstrates the
possible complexity of managing that is in "production."  A software
that is "production" means that it has a healthy community of users
and/or developers, which is strong indicator of the works impact.

[![Network of git branches for development and production](resources/Git-branching-model.png "Git Branching")*Complex Software Coordination in Git*](http://nvie.com/posts/a-successful-git-branching-model/)



## Reading
* Git-Pro Chapter 3 (Git Branching): https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell


## Git Workflow

A git workflow takes changes in an editor and provides a mechanism to
create publishable "work" in the form of a "Work Package" in project
management speak.  We can see this as a "stack" as follows.

1. Community Repository (gitlab.missouri.edu)
2. Staging (topic branches, maintainers)
3. Machine/Local repository
4. Project index or staging area
5. Project local filesystem (a file)
6. Editor (unsaved changes)
7. An Idea

Moving up and down this stack is accomplished by a series of git
commands (presented in class and below).  Between 1 and 2 is also
social.


## Examples

Below is the workflow to edit and commit a file.  This is just an
example, please be sure to replace many of the example values with
actual values that pertain to your environment.

For a new system or repository (if you only configure locally) update
your name and email to ensure the commit information is correct.
Optionally set your preferred editor (nano in this case).
```
git config --global user.name "First Last"
git config --global user.email pawprint@missouri.edu
git config --global core.editor nano
git config --global color.ui auto
```

Clone your project into your (new) projects folder
```
install -dv ~/projects
cd ~/projects
git clone git@gitlab.missouri.edu:user/welcome.git
cd welcome
```

At many of the steps throughout the process run the following to see
what is going on and your changes.
```
git status
git diff
git diff -r HEAD
```

Edit the ReadMe.md file.
```
nano ReadMe.md
```

Save and exit.  Now view the changes and add the changes to the index.
```
git diff
git add ReadMe.md
```

This is where you would change other files.  When done commit.  First view what is "staged" in the index with

```
git status
```

Then see what your "commit" will be 

```
git diff -r HEAD
```

From this determine a good description (not "changes and updates") and commit the changes.

```
git commit -m "Fix spelling"
```

Now the changes are in the local repository and ready to be
"published" to gitlabs (gitlab.missouri.edu).  View the commit in the
logs (press 'q' to exit)

```
git log
```

And push to the remote with the following:

```
git push origin master
```

Also verify that the changes have been pushed and there are no more
changes.  The last commit is also printed.  This is what is "proof" of
your work, and should be submitted to the Homework assignment along
with your repository URL.

```
git status
git rev-parse HEAD
```

