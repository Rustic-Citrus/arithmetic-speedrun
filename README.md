# Arithmetic Speedrun!

**Author**: Harry Stuart Curtis

**Published**: 2023-07-02

**Last Updated**: 2024-01-02

## Getting Started

### Windows

1. Download [arithmetic_speedrun.exe](arithmetic_speedrun.exe).
2. Execute the file.

### Linux

1. Clone the directory to your system.

```bash
git clone https://github.com/Rustic-Citrus/arithmetic-speedrun
```

Make sure you navigate into the cloned directory.

2. Install the required packages and modules into your virtual environment.

```
pip install requirements.txt
```

3. Execute the application.

```
python main.py
```

## Introduction

This is a simple maths game that I made using Python. The goal is to solve as many arithmetic equations as quickly as possible, and in doing so, help the user improve their core mathematical skills. At the end of every round, you receive a score that is calculated based on the difficulty, the total number of problems, how many of those problems you got correct, and how long you took. 

There are several difficulty levels and all four types of arithmetic operation, ranging from single-digit addition to three-digit division. When you finish the round, you can save your score to the leaderboard with a unique username, which you can then use to track your progress over time or to compete with others.

## Background

In 2021, I was asked to teach a bilingual maths course for a programme at a school in Brazil. Initially, I figured that the experience would be challenging, but doable. I had studied two years of a Chemistry bachelor's degree, which I had assumed would make me sufficiently qualified to teach secondary-school maths. Turns out, I was wrong. It was a... humbling experience. Around this time, I realised that I might suffer from a kind of maths anxiety. This realisation happened because, whenever I had to solve a problem with the students, I would freeze up. But then later, I would go home and be able to solve the problem without much difficulty. I realised that it was not just maths anxiety. There were some significant gaps in my learning. I couldn't remember how to multiply or divide fractions. Luckily, I managed to get through the course, and I asked for help from one of the Brazilian maths teachers.

In this situation, I managed to stay positive, but I haven't always had what's called a growth mindset. For a long time, I looked at my not being good at maths as something fixed, something that I would have for the rest of my life. One of the positive aspects of my experience as a teacher has been that it has brought me in touch with educational theory, specifically this idea of a growth mindset. Basically, for those who haven't heard it before, the idea is that scientific research has shown that our abilities are not usually set in stone at birth. Sure, some people do have a genetic advantage in some areas, but for the most part, it's our environment and our behaviour that shape how well we do. Learning about the growth mindset helped me to face my maths anxiety.

I decided to seize the problem by the horns. Like the philosopher Rene Descartes, I was going to start from the foundations, assuming that I knew nothing, and make my way up. I went to the Khan Academy website and started the 2nd Grade maths course. Why not the first grade? Well, starting at the foundation is great, but I was fairly confident that I could count the number of butterflies. As I made my way through the content, I gradually began to find more and more concepts difficult, and earlier than I expected. Then I began to wonder. At some points, there seemed to be more challenges. The first clue was around the fifth grade. Why was I finding this basic course more difficult? That's when I remembered what had happened when I was nine and a half. My family and I had moved house, and I had lost contact with most of my friends. I'd also moved to a school that was first-language Welsh when I knew almost none. So I wondered, had I fallen behind at that point and not realised it? I think maybe I had.

The sensation of realising that most ten year-olds might be better at maths than me is quite intellectually humbling. I imagined myself sitting down to do homework with my son or daughter in the future, then realising that they knew more than I did. I wanted to be able to support them. So, as I got better at understanding the concepts, I realised that what I needed to improve now was how confidently I could do them. And that's why I built this app, to help me solve basic arithmetics quickly. Of course, there are dozens of maths games on the internet, many of them better than mine. But as far as I'm concerned, this app helps me a lot, and if it helps even one other person, or inspires someone to adopt a growth mindset, then that's a bonus.

## Difficulty Settings

1 = EASY (2 one-digit numbers)
2 = BASIC (1 one-digit & 1 two-digit number)
3 = MEDIUM (1 one-digit & 1 three-digit number)
4 = MODERATE (2 two-digit numbers)
5 = CHALLENGING (1 two-digit & 1 three-digit number)
6 = HARD (2 three-digit numbers)

## Recent Changes

The app is fairly new and so a lot has changed recently. The most significant change has been the creation of a graphical user interface (GUI). Before that, it was exclusively accessible via the terminal.

For more changes, check CHANGELOG.md.

## Upcoming Changes

- Accessibility: Make the app accessible to more people by releasing a single executable file.
- Aesthetics: Find out if there is a way to make the app look more modern within the tkinter module.
- Warning Messages: Add warning message windows when an exception is raised in the game.
- Housecleaning: Removing unnecessary functions and variables.
- Readability: Adding comments and docstrings to make the code more readable.

## Thanks

Thank you for showing an interest in my little game! If you tried it, I hope you enjoyed it and that it worked for you without errors. If it didn't, please let me know and I'll try and fix it.
