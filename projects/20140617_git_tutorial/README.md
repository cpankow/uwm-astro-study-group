# Week 2 (2014/06/17)

 * Presenters: Adam Mercer
 * Topics: Introduction to Git and Github

## Overview

 * Why version control?
 * Why Git?
 * Concepts
 * Usage
 * Questions?

## Why Use Version Control

 * Track the development of a project
 * Why a specific change was made
 * Retrieve code that was previously deleted or changed
 * Collaborate with other developers
 * Fix a problem in an earlier version
 * Manage releases

## What is Git?

 * Distributed version control system
  * Every clone is a fully-fledged repository with complete history and full revision tracking capabilities
  * It is not dependent upon network access, not a central server
 * Tracks content, not files
 * Fast and efficient
 * Projects using Git: Git, Linux Kernel, Perl, GNOME, KDE, Android, X.org...

### Git is *NOT* CVS (or SVN!)

 * Whilst Git and CVS/SVN are version control systems they operate very differently and have different development models
 * Do **NOT** think of using Git in the same way as CVS/SVN!
 * They are **VERY** different!
 * Thinking about Git in the same way as CVS/SVN will lead to problems
 * Forget what you know about CVS/SVN!

### Learning Git ###

 * Usually taught by demonstrating a few commands
 * This approach works, but usually leads to problems in that an understanding of the nature of Git in not conveyed
 * An illusion that some magic is happening behind the scenes
 * Explain concepts upon which Git is based

### Git Configuration ###

 * Tell Git who you are
 `git config --global user.name "Adam Mercer"`
 `git config --global user.email adam.mercer@ligo.org`
 * Needs to be done on every machine you use
 * Many other configuration options

## Git Concepts ##

### The Repository ###

 * Contains, amount other things, the following:
  * Commit objects
  * References to commit objects, called heads
 * Stored in the same directory as the project itself, a subdirectory called `.git`
 * Different to centralised systems such as CVS and SVN

### Commit Objects ###

 * Reflect the state of a project at a given point in time
 * The name is composed of a hash of relevant aspects of the commit, so identical commits will always have the same name
 * SHA1, a 40-character hexadecimal string that uniquely identifies the commit object
 * e.g. 3e24626ca9215186891c36d8abd11cf8a3059bf4
 * References to parent commit object(s)
 * Visualise a repository as a directed acyclic graph (DAG) of commit objects
 * Have pointers to parent commits always pointing backwards in time, ultimately to the first commit in the repository
 * Version control with Git is all about manipulating this graph of commits

### Heads ###

 * Simply a reference to a commit object within the repository
 * Usually there is a head in every repository called *master*
 * Repository can contain *any* number of heads
 * At any given time, one head is selected as the "current head", aliased to *HEAD*, always in capitals
 * *HEAD* is the current active working copy

### The Git Index ###

 * The Git index is used a staging area between the working directory and the repository
 * The index is used to build up a set of changes that you want to commit together
 * When the commit is created the changes that end up in the commit is what is currently staged in the index, not what changes are in the working copy

### Creating a Repository ###

 * Create a directory for the project if it doesn't exist
 * Run the command `git init` inside the directory
 * Does not need to be empty
 * This command creates the `.git` directory which contains all the project history and metadata

### Creating a commit ###

 * Specify which files to commit, using `git add`
 * This add the changes to the staging area (or index), marking it for addition to the repository
 * Directories are added recursively
 * Create the commit using `git commit`
 * *HEAD* is the parent of new commit object
 * *HEAD* is updated to point to the new commit object
 * All modified files, that are already under version control, can be added to the index and committed with a single command `git commit -a`
 * It is important to write clear and detailed log messages for commits
 * Clear to other developers why a specific commit was made
 * Clear to yourself when you come back to look at the code in the future
 * Should be able to understand the change from just looking at the log, there should be no need to read the commit itself to understand what it does

### Referring to a commit ###

 * Complete SHA1 hash
 * First few characters of SHA1 has, enough to be unique
 * By a head, such as *master*
 * Relative to another commit
  * A caret (`^`) after a commit retrieves the parent
  * A `~N` after the commit specifies the commit object that is the `N`th generation parent of the named commit object
  * e.g. *HEAD*^ == *HEAD*~1, *HEAD*^^ == *HEAD*~2, etc...

### Moving and renaming files ###

 * Git tracks contents, not files
 * Files can be moved around, copied, and renamed without loss of history
 * Files are marked to be moved or renamed using `git mv`

### Removing files ###

 * Files can be marked for deletion by using `git rm`
 * Only removes files from current working copy, complete history remains in the repository
 * Can be easily retrieved

### Reverting a commit ###

 * Commits can be reverted once they have been made
 `git revert <commit>`
 * The changes introduced by the specified commit is undone as a new commit
 * The original change remains in the repository history
 * The commit can be removed completely but this is an advanced feature that can leave the repository in an unusable state

### Branching ###

 * Software was release several weeks ago
 * Development has continued, not yet ready for release
 * Bug found in release that needs to be fixed
  * Fix the bug on top of current development
  * Jump back to the release version, fix bug, and release
 * This is the idea behind branching
 * *branch* and *head* are nearly synonymous
 * Every *branch* is represented by one *head*, and every *head* represents represents on *branch*
 * *branch* is used to refer to a *head* and the entire history of commits preceding that head
 * *head* is used to refer to the most recent commit in the *branch*

### Creating a branch ###

 * A local branch can be created by running the following command:
 `git branch <new-branch-name> [branch-point]`
 * This will create a new branch, called `new-branch-name`, with `branch-point` as the *head*
 * The newly created branch can be made active in the working copy with:
 `git checkout <new-branch-name>`
 * Creation of branch and checkout can be done in a single step:
 `git checkout -b <new-branch-name> [branch-point]`
 * Creating and switching between branches is very fast
 * All branches are local, unless you specifically share them
 * You can have as many as you like

### Common branching practices ###

 * Maintain one *master* branch and create new branches to implement new features, to fix bugs, etc...
 * *master* is used as the main branch
 * *master* is **always** in a working state
 * Other branches contain half-finished work, new features, etc...
 * Important when there are multiple developers working on the same project
 * *master* should be kept clean, only commit to *master* when you are ready to share your changes
 * If development occurred on *master* new features would need to be implemented in a single commit, otherwise *master* would be in a non-working, or unstable, state
 * With development on a branch commits can be made at any time, and even rearranged later
 * Commits are cheap!

### Merging ###

 * Merging combines the history of two separate heads into a single head
 * Assume the current head is called *current*, the head to be merged is called "merge"
 * Identify the common ancestor of *current* and *merge*, call it *ancestor*
 * If *ancestor* is the same as *merge*, do nothing
 * If *ancestor* is the same as *current*, do a fast-forward merge
 * Otherwise, determine the changes between *ancestor* and *merge* and then attempt to apply those changes to the files in *current*
 * If there were no conflicts, create a new commit object, with two parents, *current* and *merge*
 * Set *HEAD* to point to this new commit, and update the working copy files for the repository accordingly
 * If there was a conflict, insert appropriate conflict markers and inform the user, no commit object is created
 * Two reasons to merge branches
   * Draw the main branch into a feature branch you are developing to keep the feature branch up to date with the latest bug fixes and new features added to the new branch
     * Doing this regularly reduces the risk of creating a conflict when you merge your feature into the main branch
     * One disadvantage of this is that feature branch will end up with a lot of merge commits
     * This can be alleviated with rebasing, although that comes with problems of its own
  * Draw the changes from a new feature branch into the main branch
 * Merging is performed using the command
 `git merge <merge>`

### Resolving conflicts ###

 * Conflicts arise if the two heads being merged have different changes in the same place
 * No automated way to tell which change should take precedence
 * Manually edit the files to fix resolve conflicting changes
 * Use `git add` to add resolved files to the index
 * Use `git commit` to commit the repaired merge
 * Parents of the commit are set appropriately

### Cherry Picking ###

 * Sometimes the entire history of a branch is not ready to be merge, but a few single commits may need to be ported to a different branch
 * Cherry-picking can be used to pick specific commits out of the history of one branch and apply them to another
 `git cherry-pick <commit>`
 * The `-x` option will record the original commit ID into the log message of the cherry-picked commit

### Creating tags ###

 * Single commits refer to the entire state of the repository at a given point in time but the hexadecimal hash is hard to remember
 * A tag can be created which is a symbolic reference to a given commit, created using:
 `git tag -a <tag-name> [commit]`
 * If `[commit]` is not specified, HEAD is used
 * The `-a` option creates an annotated tag, which includes a log message
 * You can checkout a specific tag using:
 `git checkout <tag-name>`
 * You should never commit when a tag is checked out, tags should be considered immutable
 * Tags are detached HEADs
 * A branch can be created from a tag:
 `git checkout -b <new-branch-name> <tag-name>`

### Cleaning the working tree ###

 * Sometimes you need to remove all files that are not part of the repository from your working tree:
 `git clean -dxf`
 * Also may need to remove all non-committed changes to files that are under version control
 `git checkout -f HEAD`
 * These two commands restore the working copy to a state as it it had just been cloned

## Collaboration with github ##

### Cloning an existing repository ###

 * Repository is where Git saves all the data for the history of the project
 * Clone repository
 `git clone git@github.com:cpankow/uwm-astro-study-group.git`
 * Downloads the complete history of the project
 * Store data within the hidden `.git` directory with the repository
 * This directory also houses the local configuration
 * The clone sets up a remote repository reference called "origin" which can be used to refer to the upstream repository
 * Adds remote heads as `origin/<head-name>` that correspond to the heads in the remote repository
 * Set up one head in the cloned repository to track the corresponding remote head, usually *master*

### Tracking remote branches ###

 * Can track a remote branch from the origin repository with:
 `git branch --track <remote-branch> origin/<remote-branch>`
 * Or to create and checkout in a single command:
 `git checkout -b <remote-branch> origin/<remote-branch>`
 * There is nothing stopping you using different names for the local and remote branches but doing so will get very confusing very fast, always use the same name!
 * Never checkout `origin/<remote-branch>` directly!

### Updating remote repository ###

 * As development proceeds collaborators will add new commits to the upstream repository
 * These changes can be obtained, or "pulled", from the remote repository and merged into your local repository by running:
 `git pull`
 * This performs a merge with your current local head and the corresponding remote head
 * The `--rebase` option can be added to overlay your changes on top of the current remote head

### Sharing changes ###

 * Once changes have been committed locally they can be shared with the upstream repository
 * Changes are "pushed" to the remote repository with
 `git push origin <remote-head>`
 * New commit objects are added to the remote repository
 * `remote-head` is updated to point to the same commit that it points to in the local repository
 * If no arguments are given to `git push`, it will push all the branches in the repository that are set up for tracking to their remote counterparts
 * Only push the current branch to its associated upstream branch, not all tracked branches
 `git config --global push.default upstream`
 * Only works for recent git versions

### Remote branches ###

 * A local branch can be pushed to the remote repository using the following
 `git push -u origin <branch-name>`

### Sharing tags ###

 * If you need to share tags then these can be pushed to the remote repository with:
 `git push <tag-name>`
 * Or all tags can be pushed with
 `git push --tags`
 * Once a tag has been pushed to a remote repository it should never to changed, doing do can lead to inconsistent results