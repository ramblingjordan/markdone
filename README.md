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
- [x] Determine and reserve some basic tags.
- [x] Incorporate sub folders as 'Collections'.
- [x] Define some basic automated processing to be implemented in seperate packages.

## Elements

### Collection

- A folder containing multiple project files.
- The Markdone root folder is a top level collection and adheres to the collection standards.

### Project

- A project is any task requiring more than one step.
- Represented by a single file.
- Top level heading is project name.
- Can contain sub-projects which are represented by sub-headers. (`##`, `###`, etc.)

### Task

- A representation of a single unit of work.
- Anallogous to a GTD 'Action Step'.
- Single line of text beginning with `- [ ]`

### Attributes

- Priority:
  - Maintains the same priority designations as Todo.txt
  - Single letter surrounded by parenthesis eg. `(A)`
  - Prioritized by lowest alphabet position.
- Context:
  - Used to denote context for a task as per GTD.
  - Proceeded by `@`
  - Contains no spaces.
  - eg. `@work @school @boss`
  - A task may contain many contexts.
- Project:
  - Used to denote the project the task belongs to.
  - Proceeded by a `#` (or in the case of sub projects multiple `#`'s, eg `##sub-project`)
  - Markdone assumes a project tag based on the file header. Overriding the project in a task line will invalidate the document.
  - Typically only displayed when representing a projects 'Next Action' in a collections TODO.&#8203;md file.
- Collection:
  - Used to denote the collection the task belongs to.
  - Proceeded by a `/` in the case of a sub-collection will be represented as the relative folderpath. eg. `/collection-name/sub-collection-name`
  - Markdone assumes a collection tag based on the file location relative to the root directory. Overriding the collection in a task line will invalidate the document.
  - Typically only displayed when representing a sub collections next action within a parent collections TODO.&#8203;md file.
- Tag:
  - Key-Value Pair (KVP) used to provide processable information about a task.
  - User/extension defined.
  - Keys are case insensitive and contain no spaces
  - Values contain no spaces unless wrapped in quotation marks (`assistant_name:'HAL 9000'`).
  - If a space follows the colon then it is not considered a tag.
  - A value without a key is considered a flag. It's presense indicates the value is `TRUE` its absence `FALSE` eg. `:waiting_on`
  - Standard key words are reserved for dates. `start`, `stop`, and `due` All dates are in the format YYYY-MM-DD
- Due:
  - Due is a special tag and is assumed if a date appears immediately after the prefix and priority (if there is one).
  - eg. `- [ ] (A) 2018-06-30 Pay rent.` is equivalent to `- [ ] (A) Pay rent. due:2018-06-30`

### Info

- Any non-empty line of text that does not start with prefix defined elsewhere in this specification.
- Info lines are ignored by processing, if information is pertinent to a task consider how to include it in it's description.


### INBOX.&#8203;md <!--- Using zero width space character to prevent auto-linking -->

- Resides in the root folder of a collection.
- Used as a collection point for unclassified inputs.
- Each line represents a seperate entry
- Contains top-level header `# INBOX`
- Sub-headers are not supported in this file and are considered an entry like every other line.

### TODO.&#8203;md <!--- Using zero width space character to prevent auto-linking -->

- Resides in the root folder of a collection.
- Contains GTD 'Next Action' list for that collection.

## Processing

### Configuration

- Located in file `/.markdone`
- File denotes the root folder of a Markdone directory.

`- [x] (A) 2016-01-01 Written out description of task. /collection/sub-collection #project ##sub_project @context start:2016-01-01 done:2016-01-01`