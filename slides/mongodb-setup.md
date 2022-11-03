---
layout: presentation
title: MongoDB Setup
permalink: /slides/mongodb-setup/
---

class: center, middle

# MongoDB Setup

Database Design

---

# Agenda

1. [Overview](#overview)
1. [Server Setup](#setup)
1. [Client Setup](#client)
1. [Automation](#automation)
1. [Conclusions](#conclusions)

---

name: overview

# Overview

--

## The Plan

We will outline a few ways to gain access to a MongoDB **server** and use a MongDB **client** to issue commands to the database. Our discussion will include:

--

- running a MongDB server locally

--
, remotely on NYU's **classes-mongodb database server**

--
, and remotely using MongDB Atlas - a cloud-hosted solution.

--

- running a MongoDB client locally

--
, remotely on NYU's **i6 web server**

--
, and using a **driver** with any of today's popular programming languages

---

name: server

# Server Setup

--

## Choices of server

There are several easy ways to try out a MongoDB **server**.

--

- [MongoDB Community Server](https://www.mongodb.com/try/download/community) can be downloaded and tried locally on your own machine for free.

--

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is a cloud-hosted database service with a free tier for new users and small-scale applications.

--

- [Docker image of MongoDB](https://hub.docker.com/_/mongo) can be used to run a MongoDB server in a Docker container.

--

- NYU's Computer Science Department hosts its own MongoDB server at [class-mongodb.cims.nyu.edu:27017](https://cims.nyu.edu/webapps/content/systems/userservices/databases/class-mongodb), which all students can access.

--
**We will use this.**

---

template: server

## Create an account on NYU CS Department's MongoDB server

All students will need to initialize an account on our MongoDB server using the ["Class MongoDB Manager"](https://cims.nyu.edu/class-mongodb/manage)

--

- enter your `i6.cims.nyu.edu` web server username and password. You should have received an email with that password soon after registering for the course.

--

- if your **i6** password does not work, or you can't find it, [reset it](https://cims.nyu.edu/webapps/password/reset) and try a new one.

---

template: server

## Credentials

Once logged in, the Class MongoDB Manager will show you your password for the MongoDB database server - this is different from your **i6** web server password.

--

You will need to save the following credentials somewhere.

- `database server/host` - this is `class-mongodb.cims.nyu.edu`, port `27017`
- `your database name` - this is the same as your NYU Net ID
- `username` - this is the same as your NYU Net ID
- `password` - this will be displayed to you by the Manager tool

---

name: client

# Client setup

--

## Choices of client

Once set up with a server, you must access it using a **client**. There are several common ways to use a MongoDB client:

--

- Download and install [MongoDB's official shell](https://www.mongodb.com/try/download/shell) client, which you can run from the command line of your own machine.

--

- Use a "driver" module to allow code in any popular programming language to connect to a server.

--

- Use `ssh` to remotely log into NYU CS department's `i6.cims.nyu.edu` server, where a `mongo` shell is already installed.

---

template: client

## Logging into NYU CS Department's i6 server

You will need `ssh` to remotely log into most servers, including the CS Department's i6 web server.

--

- Mac users have `ssh` already installed.

--

- Windows users can use [Git for Windows](https://gitforwindows.org/), which includes `ssh` within Git Bash.

--

The command, `ssh fb1258@i6.cims.nyu.edu` will remotely log in to the **i6** server.

--

- You will be asked to enter your **i6** server password.

--

- The password will not show up on the screen as you type it - that is absolutely normal and desireable and not a cause for concern.

---

template: client
name: connect-to-mongo

## Connecting to MongoDB from NYU CS Department's i6 Web Server

Once logged into the **i6** web server, you can use the `mongo` command line client to connect to the MongoDB database server.

--

- Run the command, `module load mongodb-4.0` to load the MongoDB client.

--
This command can be automatically run every time you log into the **i6** web server... [details here](#bashrc).

--

- Next, use the MongoDB client to connect to the database server: `mongo fb1258 --host class-mongodb.cims.nyu.edu -u fb1258 -p`, where `fb1258` is replaced by your own NYU Net ID.

--

- You will be asked to supply your MongoDB server account password... do so.

---

template: client

## Verify that you are truly logged in

Prove to yourself that you are logged into a Javascript command-line interface to MongoDB.

--

- Type `1 + 1` and hit Enter.

--

- Did it respond with `2`?

--
If so, you're ready to start using your MongoDB database.

---

name: automation

# Automation

--

## The problem: typing commands manually with every login

Every time you log into the **i6** web server, you must run the `module load mongodb-4.0` to [load the MongoDB client](#connect-to-mongo) before using it.

--

- It is possible to automatically run this command every time you log in.

--

- You can do this by adding this command to your **i6** account's `.bashrc` settings file.

---

name: bashrc
template: automation

## The solution: .bashrc

Commands placed within the `.bashrc` file on UNIX and Linux machines are automatically executed every time a user begins a new shell session.

--

To automatically run the `module load mongodb-4.0` command from the `.bashrc` script:

--

- trom the **i6** command line, run the command `emacs .bashrc` to open up this file in the [emacs](https://duckduckgo.com/?q=emacs+shortcuts&t=brave&ia=cheatsheet&iax=1) text editor.

--

- add `module load mongodb-4.0` as a line in this file.

--

- save this file by typing `Control-X` and then `Control-S`.

--

- exit emacs by typing `Control-X` and then `Control-C`.

--

Now this command will run automatically every time you log in.

---

template: automation

## The problem: entering passwords with ssh

It is tedious to [remember and] enter passwords every time one logs into a remote server.

--

- We can automate this away with cryptographic `ssh` keys placed locally and on the server.

---

template: automation

## The solution: public and private SSH keys

To automatically authenticate when remotely logging in, we will first generate a pair of linked cryptographic keys locally (a **public key**, which you can share and a matching **private key** which you should keep private) and then place a copy of the public key on the server.

--

- run the command `ssh-keygen -t rsa` locally on your own machine to generate a key pair

--

- you will be asked **where to save the keys** - hit `Enter` to accept the default location.

--

- you will also be asked **whether to use a password** to encrypt the keys... the decision is up to you. If you decide to use a password, please remember it.

---

template: automation

## The solution: public and private SSH keys (continued)

We must now copy the public key to the server. The `ssh-copy-id` command can do this automatically for us.

--

- run the command, `ssh-copy-id fb1258@i6.cims.nyu.edu`, where `fb1258` is replaced with your **i6** web server username.

--

- You will be asked to enter your **i6** password... do so.

--

Assuming the command above worked successfully, you should now be able to log into **i6** by simply entering, `ssh fb1258@i6.cims.nyu.edu`, where `fb1258` is replaced with your own username. You will no longer be asked to enter a password. Try logging out and then logging in again.

---

name: conclusions

# Conclusions

--

Thank you. Good luck.
