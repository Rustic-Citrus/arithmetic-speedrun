# Arithmetic Speedrun!

**Author**: Harry Stuart Curtis

**Published**: 2023-07-02

**Last Updated**: 2026-01-12

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    1. [Setup](#setup)
    2. [Running the Application](#running-the-application)
3. [Background](#background)
4. [Recent Changes](#recent-changes)
5. [Thanks](#thanks)

## Introduction

This is a simple maths game that I made using Python. The goal is to solve as many arithmetic equations as quickly as possible, and in doing so, help the user improve their core mathematical skills. At the end of every round, you receive a score that is calculated based on the difficulty, the total number of problems, how many of those problems you got correct, and how long you took. 

There are several difficulty levels and all four types of arithmetic operation, ranging from single-digit addition to three-digit division. When you finish the round, you can save your score to the leaderboard with a unique username, which you can then use to track your progress over time or to compete with others.

### Difficulty Settings

1 = EASY (2 one-digit numbers)

2 = BASIC (1 one-digit & 1 two-digit number)

3 = MEDIUM (1 one-digit & 1 three-digit number)

4 = MODERATE (2 two-digit numbers)

5 = CHALLENGING (1 two-digit & 1 three-digit number)

6 = HARD (2 three-digit numbers)

## Getting Started

### Setup

You can run Arithmetic Speedrun locally on your machine. You need access to a command-line interface and the internet. You must have Python 3.11 or greater installed in your system, as I haven't tested the application on earlier versions. You'll also need Git, which is installed by default on most Linux and Mac systems, to follow along with the instructions below.

For more information on how to download Python for your system, follow [this link](https://www.python.org/downloads/) to the official Python website.

If you are using Windows and do not have Git installed on your system, follow [this link](https://git-scm.com/download/win) to access the official Git website.

Once you have met those prerequisites, continue to the instructions below.

### Running the application

Open the default command line interface for your computer. This will probably be PowerShell for Windows, or Bash for Linux and Mac.

1. Clone the directory to your system by typing the command below.

```bash
git clone https://github.com/Rustic-Citrus/arithmetic-speedrun
```

2. Navigate into the cloned directory using the appropriate change directory command, for example:

```bash
cd arithmetic-speedrun
```

3. Build a virtual environment.

```bash
python -m venv .venv
```

4. Activate the virtual environment.

```bash
.\.venv\Scripts\activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Execute the application entrypoint script.

```bash
python main.py
```

A startup sound should play and the game should open.

## Background

In 2021, I taught a bilingual maths course at a school in Brazil. Initially, I imagined it would be challenging, but doable. At that time, I had completed two years of a Chemistry bachelor's degree, which I assumed would qualify me to teach secondary-school maths. Turns out, I was wrong. It was a humbling experience. 

Around that time, I also thought that I might suffer from maths anxiety. This realisation happened because, whenever I had to solve a problem with the students, I would freeze up. Later, I would go home and solve the problem without much difficulty. However, I soon realised that it was not only a question of anxiety. There were some significant gaps in my learning. For example, I'd forgotten how to multiply or divide fractions. 

With a bit of persistence, I got through the course. Granted, with some help from a Brazilian maths teacher colleague.

I had managed to stay positive, but I haven't always had a growth mindset,an ability to see failure as an opportunity. For a long time, I looked at my lack of mathematical skill as something fixed, something that would be that way for the rest of my life. One of the positive aspects of my experience as a teacher was that I learned how to learn. I learned to have a growth mindset. 

For those unfamiliar with a growth mindset, the idea is that scientific research has shown that our abilities are not usually set in stone at birth. Sure, some people do have a genetic advantage in some areas, but for the most part, it's our environment and our behaviour that shape how well we do. Learning about the concept of a growth mindset helped me to face my maths anxiety.

The realisation that most ten year-olds are better mathematicians than you is quite intellectually humbling. I imagined myself sitting down to do homework with my son or daughter in the future, then realising that they knew more than I did. I wanted to be able to support them. As my understanding of the concepts improved, I realised that my confidence was still far behind. That's why I built Arithmetic Speedrun.

## Recent Changes

The application is more or less finished in the way that I intended it. In the future, I may make some changes, but I'm content with the project as it stands.

For more changes, check CHANGELOG.md.

## Thanks

Thank you for showing an interest in my humble project. This was the first complete application I ever developed. If you tried it, I hope you enjoyed it and that it worked without bugs. If it didn't, please let me know and I'll try and fix it.
