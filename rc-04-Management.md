# IMSE 8410 Projects

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop. Source code
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Managing Research

> "If it is not in git, it did not happen."

Managing a research effort and scientific or engineering workflows is
a lot like managing a project.  Many times a research effort will be
directly linked to a sponsored (or sponsored) research project, or
even a dissertation, with specific deliverables, milestones, and
products that must be coordinated, managed, and with input (research,
code, or simply feedback) from multiple individuals.  Managing the
code and the project are so often intertwined it makes a lot sense to
use a tool such as GitLab or GitHub.  In this course we use GitLab due
to it's Open Source background and it's use at the University. Many of
the tools are directly mapable to other project management and source
code management systems (such as GitLab).  By using these tools (and
specifically GitLab) in a structured and systematic matter it is
possible to manage the project, code, and people all in one location.
It takes a bit of discipline to maintain this effort but is well worth
it.

For all research and projects the first steps should be the following:
 1. Create a Git Project.
 2. Clone the repo on the cluster.
 3. Do some work
 4. Gather some collaborators (publish project)
 5. Create a Git Group (optional)
 6. Work as a Team
 7. Profit.

## Reading
 * Pro Git (https://git-scm.com/book/en/v2) Chapters 1 (except 1.5), 2, 3, 5, (6 Optional)
 * GitLab Markdown https://docs.gitlab.com/ee/user/markdown.html
 * GitLab Issues https://docs.gitlab.com/ee/user/project/issues/
 * GitLab Issue Boards https://docs.gitlab.com/ee/user/project/issue_board.html

## Lessons

### GitLab

GitLab (https://gitlab.com) and local GitLab websites
(https://gitlab.missouri.edu) contain a number of tools and
capabilities, which are as follows:

1. Projects: A Project is the basic unit for which most of the real
   functionality is contained, divided by project.  A project contains
   the following elements:
   1. Git Repository (source and documentation)
   1. Issues
   1. Milestones
   1. Continuous Integration and Continuous Deployment.
   1. Documentation (Wiki) and Wiki's.
   1. Metrics
1. Groups: A number of projects can be combined together as a group.
   Good for larger projects that may contain multiple repositories or
   larger groups such as research labs.  Groups contain some of the
   capabilities as projects but applies to the group as a whole.
   Groups also allow projects to be abstracted from specific
   individuals (ownership of repositories).
1. Access and Permission: Git allows for sharing of projects with
   different permissions to facilitate a large number of workflows.


### Git

Git is a distributed source control management system.  It is used to
manage source files, through changes, in a decentralized and
distributed manner in a secure way (verifiable and integrity).  At
it's heart is just a series of "changes" with a tools to manage
workflows.  A git repository is a standalone database that contains
the following concepts (covered in the text):
1. Blobs (files)
1. Commits (changes)
1. Branches (trees)
1. Files (checkout)
1. Staging area (index)
1. Tags (releases)
1. Remotes (repositories)


### Markdown
Markdown is a human readable markup language that is easy to use and
similar in style to programming.  The Markdown format is visually
similar to the rendered results and has eclipsed many of it's
competitors in adoption due to it's simplicity, visual style, and ease
of use.  All documentation should be written in Markdown even if it is
not going to be rendered. There are many extensions and flavors of
Markdown, and in this class we will be using GitLab Markdown due to
it's strong integration into the GitLab website.  These extensions
allow for easy cross referencing to issues, milestones, commits,
etc. to allow for easier navigation through a project.  The
authoritative reference for GitLab flavored markdown can be found at
the following website: https://docs.gitlab.com/ee/user/markdown.html

#### Exercise E04-Markdown
The purpose of this exercise is to familiarize yourself with basics of
Git and GitLab and to provide a basic student profile.  This exercise
will also familiarize the student with how to submit exercises,
assessments, and projects and how feedback will be provided. 

The goal of this exercise is to write your profile in the `ReadMe.md`
if your course repository.  Please consider the following points.
 1. Place the profile in the `ReadMe.md` file noting the upper/lower
    case of the file (not `readme.md` or `README.md`). The profile should
    contain the following information:
    1. Name:
    2. How you wish to be referred by:
    2. Department:
    3. Degree/Standing (B.S.+ M.S.; M.S.; Ph.D Student; Ph.D. Candidate; Faculty; Staff; Other)
    4. Degree focus area:
    5. About you (optional): something trivial/interesting about yourself.
 2. Include an image that is
    1. stored in the repository (uploaded), and
	2. preferably your profile picture.
 3. You may use the GitLab editor and edit on the 'master' branch.
 4. Post the repository URL (the `clone with ssh` URL under clone) and
    the long commit ID.  Use the `Copy Commit SHA` on the proper
    commit in the "`commits` section of the `Repository` section of
    your project.  Please note that the example commit
    `542720c4aa671f6267ff211d110cd81deb06d177` is a long commit id,
    and `542720c4` is the short commit ID.

## References
 * GitLab https://gitlab.com
 * GitHub https://github.com
 * Git https://git-scm.com/book/en/v2
 * GitLab Markdown https://docs.gitlab.com/ee/user/markdown.html
 * Formal project management (PMBOK) https://www.pmi.org/pmbok-guide-standards
