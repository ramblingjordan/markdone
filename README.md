# Markdone

![Markdown Logo](assets/logo.svg)

Markdone is a specification for the format and organization of checklist files for the purpose of personal organization and project planning.

## Acknowledgments

- [GitHub Flavored Markdown (GFM)](https://github.github.com/gfm/) - Markdone uses a subset of this specification, Markdone will validate to GFM but not all GFM will validate to Markdone.
- [Todo.txt](http://todotxt.org/) - Markdone borrows a lot from Todo.txt, however we do break or modify formating rules. Even #1!
- [Getting Things Done (GTD)](https://gettingthingsdone.com/) - Markdone is designed to facilitate the implementation of a GTD system.

## Goals

- [x] Combine the human readable styling of Markdown with the machine readable concepts of Todo.txt.
- [x] Allow for organization of projects in separate files.
- [x] Determine some basic tags for task metrics.
- [x] Incorporate sub folders as 'Collections'

## Specification

### Elements

#### Task

- A task represents a single unit of work, think GTD 'action'.
- Is contained in one line.
- Begins with `- [ ]`

#### Projects

- A project is any task requiring more than one step.
- Represented by a single file.
- Top level heading is project name.
- Can contain sub-projects which are represented by sub-headers.

#### Collection

- A folder containing multiple project files.

### Single File Representation

- A Markdone directory can be represented by a single file

### Processing

#### Configuration

- Located in file `/.markdone`
- File denotes the root folder of a Markdone directory.


`- [x] (A) 2016-01-01 Written out description of task. /collection/sub-collection #project ##sub_project @context start:2016-01-01 done:2016-01-01`