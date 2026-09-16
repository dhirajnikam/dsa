# 14 · Behavioral, explained from zero

Read this first if "STAR" and "Leadership Principles" sound like corporate wallpaper. When
the wedding story below makes sense, open `LESSON.md`, which lists all sixteen principles, the
story bank, and the two-week drill. This file is the conversation before it.

## In one sentence

A behavioral interview asks you to prove a quality about yourself with a true story that has
a number in it, instead of claiming the quality with an adjective.

## Start with something you already do

A friend is planning a trip and asks, "Are you reliable?" Two ways to answer.

The first: "Yes, very." You have just given an opinion about yourself. Your friend has no
reason to believe it, and they have nothing to repeat to anyone else.

The second: "Last month the caterer cancelled on my sister's wedding, four days out. I rang
eleven places that afternoon and had a replacement signed by dinner, three hours after the
call." You never said the word reliable. Your friend said it in their own head, and they can
retell that story to someone else tonight. That is evidence, and it is the entire chapter.

Look at what the second answer contains. A situation (the caterer cancelled). Your job in it
(find a replacement). What you did (rang eleven places). How it ended (signed in three hours).
That is STAR: Situation, Task, Action, Result. It is not a formula for sounding polished. It
is the shape a story has to take before another person can believe it and write it down.

Now the other phrase. A **Leadership Principle** is a named value a company uses to judge
behavior. Amazon has sixteen and takes them literally: promotions are argued under those
headings, and so is your interview. Three of them, in plain words:

- **Ownership.** You fix things even when they are not your job. The build has been red for
  two weeks and everyone ignores the email; you go find out why.
- **Dive Deep.** You go look at the actual data instead of accepting a summary. Someone says
  "nothing changed on our side"; you read their deploy history anyway.
- **Customer Obsession.** You start from what the user needs, not what is easy to build. You
  cut a feature you liked because support tickets said users wanted something else.

Each interviewer is assigned two or three of these. Their job is to write a paragraph of
specific evidence about you under each one. If they cannot, you fail, no matter how the
coding went.

## Now the same thing with numbers

Here is a whole STAR answer in four sentences, for "Tell me about a time you took on
something that was not your job" (Ownership):

> **S:** In my internship, the team's nightly test run had been failing for two weeks and
> everyone was ignoring the red email. **T:** Nobody owned it, and I decided to find out why
> before the release. **A:** I read the log, found one test depended on a server that had been
> shut down, rewrote it to use a local file, and posted the fix with a one-line explanation.
> **R:** The run was green the next morning and stayed green through the release, and the
> team lead asked me to add a "who owns this" line to the failure email.

Count what the interviewer can copy into their notes: two weeks, one test, next morning, and
four things that start with "I." That is a small story, sized for an intern, and it is a full
pass on Ownership.

The proportions matter as much as the content:

| Part | Time | What it is for |
|------|------|----------------|
| Situation | 15 seconds | So they can picture it |
| Task | 10 seconds | Your job, not the team's |
| Action | 90 seconds | Three to five decisions, each starting with "I" |
| Result | 20 seconds | A number, then one thing you changed afterward |

Pause and predict: rewrite the Result sentence with no numbers in it. What did the
interviewer lose?

<details><summary>Answer</summary>
"The tests started passing again and people were happy." Nothing to copy down. "Two weeks
red, green the next morning, stayed green through release" is a fact they can quote at the
debrief. Adjectives evaporate; numbers survive.
</details>

Now the "I" question, because it worries everyone. The interviewer is hiring you, not your
team. Every "we decided" forces them to ask "what did *you* do?" and costs you a follow-up.
"I" is not bragging when what follows it is a fact. "I brought the page load from 800 to 400
milliseconds" is a measurement. Credit others by name, then say your part: "The team's goal
was the migration; my piece was the data layer; I did these three things."

## The words people use

- **Behavioral interview.** Questions that start "Tell me about a time..." Graded, not chit-chat.
- **STAR.** Situation, Task, Action, Result. The shape every answer takes.
- **Leadership Principle (LP).** One of Amazon's sixteen named values. Each interviewer probes two or three.
- **Evidence vs adjective.** "Found the config diff" is evidence. "Very thorough" is an adjective.
- **Loop / onsite.** The day of four or five back-to-back interviews.
- **Bar Raiser.** An Amazon interviewer from another team whose only job is to protect the
  hiring standard. They can veto.
- **Debrief.** The meeting after your loop where interviewers read each other's notes and argue.
- **Probe / follow-up.** "What would you do differently?" "What was the metric?" The probes
  decide the vote.
- **Story bank.** Your eight prepared true stories, written one page each in STAR form.
- **Story matrix.** A grid of stories against LPs so you know which story covers which principle.
- **Googleyness & Leadership (G&L).** Google's one behavioral round. No LP list; they look for
  collaboration, handling ambiguity, ownership, and judgment.
- **Hiring committee.** At Google, people who never met you read all the notes and decide.
- **Disagree and commit.** Push back with data, lose, then support the decision fully. Both halves are graded.
- **Level / leveling.** SDE1, SDE2, L4, L5. Your stories must be the size of the level.
- **Red flag.** Blame, "we" with no "I," no number, no conflict, vagueness under probing.
- **p99.** The time the slowest 1 in 100 requests take. A common number in engineering stories.

## Why this matters more than it looks

At Amazon, every round opens with 15 to 25 minutes of this. Four or five rounds means 60 to
125 minutes of behavioral in one loop, more than any single coding problem gets. The Bar
Raiser typically spends their whole hour on it and can veto. If two interviewers write "no
evidence of Ownership," a perfect coding round does not rescue you.

The lesson calls this the highest failure rate per minute of preparation skipped in the
course, and the arithmetic backs it up. The preparation is eight true stories, one page each,
and 30 minutes a day for two weeks. Roughly seven hours to remove the most common reason
strong coders get rejected.

## Try it in your head

1. Spot everything wrong with: "We had a really bad outage and worked hard to fix it."

<details><summary>Answer</summary>
No number ("really bad"). No "I" (who did what?). No action you can picture ("worked hard").
No result. No follow-up change. Same events, told well: "The API was down 40 minutes; I found
the expired certificate in the load balancer logs, rotated it, and added an expiry alert."
</details>

2. "Tell me about a time you disagreed with your manager." Which principle, and which half
   do people forget?

<details><summary>Answer</summary>
Have Backbone; Disagree and Commit. People tell the disagreement and forget the commit: what
you did after the decision went against you, and how it turned out.
</details>

3. You fixed a small bug in one day. Can that be a story? For which level is it too small?

<details><summary>Answer</summary>
Yes for Dive Deep if you show three layers of investigation and a number. Too small as a
Deliver Results story for SDE2 and above, where they expect a service or a cross-team project.
</details>

## Common confusions, cleared

- **"Isn't this the warm-up before the real interview?"** It is the interview. There is a
  rubric, notes, and a vote per principle.
- **"I don't have impressive stories."** Impressive is not the bar. Specific is. A two-week bug
  with three "I" decisions and a number beats a vague "I led a migration." Size the story to
  your level and pick ones where something went wrong.
- **"Should every story end with me being right?"** No. One or two where you were wrong and
  changed how you work make the others believable.
- **"If I don't remember the exact number, can I round up a bit?"** Say "roughly" and give
  what you remember. Interviewers spot invention because details get vaguer under probing, not
  sharper.

## What to do next

Open `LESSON.md` and read §3, "STAR done right," including the strong and weak versions of
the same story. Then a 20-minute first task: pick one true thing from the last two years
where something went wrong and you did something about it. Write it in four sentences labeled
S, T, A, R, with a number in R and at least three "I" verbs in A. Read it aloud with a timer.
If it is under two minutes and has the number, you have story one of eight. Then read §4 to
build the matrix.
