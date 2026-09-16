# 14 · Behavioral

**In one sentence.** A behavioral interview asks you to prove a quality about yourself with a
true story that has a number in it, instead of claiming the quality with an adjective.

**Why you care.** Every Amazon round opens with 15 to 25 minutes of this, including the coding
and design rounds, and the Bar Raiser can veto on it alone. Google asks one dedicated round
called Googleyness & Leadership. This chapter is for everyone, at every level. It decides
whether each interviewer can write a paragraph of specific evidence about you. If they cannot,
a perfect coding round does not rescue you.

## The idea, with a story

A friend is planning a trip and asks, "Are you reliable?" Two ways to answer.

The first: "Yes, very." You have given an opinion about yourself. Your friend has no reason to
believe it and nothing to repeat to anyone else.

The second: "Last month the caterer cancelled on my sister's wedding, four days out. I rang
eleven places that afternoon and had a replacement signed by dinner, three hours after the
call." You never said the word reliable. Your friend said it in their own head, and they can
retell that story tonight. That is evidence, and it is the entire chapter.

Look at what the second answer contains. A situation (the caterer cancelled). Your job in it
(find a replacement). What you did (rang eleven places). How it ended (signed in three hours).
That is STAR: Situation, Task, Action, Result. It is not a formula for sounding polished. It
is the shape a story must take before another person can believe it and write it down.

## The same story with numbers

A whole answer in four sentences, for "Tell me about a time you took on something that was not
your job."

> **S:** In my internship, the team's nightly test run had been failing for two weeks and
> everyone was ignoring the red email.
> **T:** Nobody owned it, and I decided to find out why before the release.
> **A:** I read the log, found one test depended on a server that had been shut down, rewrote
> it to use a local file, and posted the fix with a one-line explanation.
> **R:** The run was green the next morning and stayed green through the release, and the team
> lead asked me to add a "who owns this" line to the failure email.

Count what the interviewer can copy into their notes: two weeks, one test, next morning, and
four things that start with "I." A small story, sized for an intern, and a full pass on
Ownership.

Pause and predict: rewrite the Result sentence with no numbers in it. What did the
interviewer lose?

<details><summary>Answer</summary>
"The tests started passing again and people were happy." Nothing to copy down. "Two weeks red,
green the next morning, stayed green through release" is a fact they can quote at the debrief.
Adjectives evaporate. Numbers survive.
</details>

## STAR, and why "I" is not bragging

Everyone knows the acronym. Almost everyone gets the proportions wrong.

| Part | Time | Rule |
|------|------|------|
| Situation | 15 seconds | Enough to picture it. No history lesson. |
| Task | 10 seconds | Your job, not the team's. "I was responsible for..." |
| Action | 90 to 120 seconds | Three to five decisions, each starting with "I" |
| Result | 20 seconds | A number, then one thing you changed afterward |

Two to three minutes total. Then stop and let them probe. A four-minute monologue is a warning
sign. A ninety-second answer with a number in it is a gift.

The interviewer is hiring you, not your team. Every "we decided" forces them to ask "what did
*you* do?" and costs you a follow-up. "I" is not bragging when what follows it is a fact. "I
brought p99 from 800 to 400 milliseconds" is a measurement. Credit others by name, then say
your part: "The team's goal was the migration. My piece was the data layer. I did these three
things."

**Strong.** *"Tell me about a time you found the root cause of a difficult problem."*

> Last spring our checkout p99 doubled overnight from 400 to 800 ms, with no deploy on our
> side. I was on call and owned finding the cause. I checked the dashboards and saw the jump
> was only on requests that hit pricing, which ruled out the load balancer and database. I
> pulled traces for fifty slow requests and found the time was inside one call to the
> promotions service. Their team said nothing had changed. I diffed their deploy history anyway
> and found a config change that cut their cache TTL from ten minutes to ten seconds. I sent
> their on-call a two-paragraph summary with trace IDs and the diff. They reverted within an
> hour and p99 returned to 400 ms. I then added a latency alert per downstream dependency. It
> fired twice the next quarter and both times we found the cause in under thirty minutes.

**Weak, same events.**

> We had a latency problem in checkout that was really bad. We looked at the dashboards and
> did a lot of investigation. Eventually we figured out it was the promotions team's fault
> because they changed their cache config. They fixed it and things went back to normal. I
> learned you should always check dependencies.

No number. No "I." Blame. No follow-up change. A generic lesson anyone could say. Same events.
One gets a hire, the other gets "candidate was vague."

## The 16 Leadership Principles

Amazon takes these literally. Promotions are argued under these headings, and so is your
interview. Each interviewer is assigned two or three. Learn the names so you know which one you
are answering.

| Principle | Plain meaning | A question they ask |
|-----------|---------------|---------------------|
| Customer Obsession | Start from what the customer needs, not what is convenient to build | "Tell me about a time you went above and beyond for a customer." |
| Ownership | Act for the whole company, not just your ticket | "Describe a time you saw a problem nobody owned." |
| Invent and Simplify | Find a simpler way; reject "this is how it has always been done" | "Tell me about a time you simplified a process or system." |
| Are Right, A Lot | Good judgment, and seeking views that might prove you wrong | "Tell me about a time you were wrong." |
| Learn and Be Curious | You keep learning on your own and it shows up in your work | "Describe a time you had to learn a new technology quickly." |
| Hire and Develop the Best | You raise the bar for the people around you | "Tell me about a time you helped someone grow." |
| Insist on the Highest Standards | You do not ship what you know is not good enough | "Tell me about a time you refused to compromise on quality." |
| Think Big | You propose direction beyond this quarter and make people see it | "Tell me about a time you proposed something bold." |
| Bias for Action | Most decisions are reversible; do not wait for perfect information | "Describe a time you took a calculated risk." |
| Frugality | Do more with less | "Tell me about a time you delivered with limited resources." |
| Earn Trust | Listen, speak candidly, own mistakes publicly | "Describe a time you received hard feedback." |
| Dive Deep | Go to the data and the code; do not accept a summary | "Tell me about a time you found the root cause of a hard problem." |
| Have Backbone; Disagree and Commit | Push back with data, then commit fully once decided | "Tell me about a time you disagreed with your manager." |
| Deliver Results | Ship on time, at quality, despite setbacks | "Tell me about a time you delivered under a tight deadline." |
| Strive to be Earth's Best Employer | Make the workplace better for the people in it | "Describe a time you supported a struggling colleague." |
| Success and Scale Bring Broad Responsibility | Your decisions affect people outside the room | "Describe a decision where the right thing and the easy thing differed." |

If time is short, start with Ownership, Dive Deep, Deliver Results, Customer Obsession, Have
Backbone, Earn Trust, Bias for Action, and Invent and Simplify. Those eight cover most Amazon
questions.

Google's round has no list. The interviewer looks for four things: collaboration across teams,
handling ambiguity, ownership without authority, and judgment. For ambiguity, describe the
process you used to reduce it, not the fact that you tolerated it. For disagreement, tell both
halves: how you pushed back, and how you committed after losing.

## Your story bank

You need about eight true stories, one page each in STAR form. Each should be strong for two
or three principles, so every principle has at least two stories behind it and you never tell
the same story twice to one interviewer. The eight situations interviewers ask about over and
over: a conflict with a peer, a mistake you owned, a tight deadline, ambiguous requirements,
disagreeing with a manager, going beyond scope, mentoring someone, and a hard technical problem
you dug to the bottom of. Rules: last two years, sized to your level, something went wrong, and
a number in every result. Memorize the beats, not the words.

| Story | Ownership | Dive Deep | Backbone | Deliver | Earn Trust |
|-------|-----------|-----------|----------|---------|------------|
| Latency root cause | X | **X** | X | | |
| Migration under deadline | X | | | **X** | |
| Bad deploy I owned | **X** | | | | **X** |
| Disagreed on the rewrite | | | **X** | | X |

Bold is the story's main principle. If a column has fewer than two marks, find a story for it.

## Red flags

Interviewers write these down. Each one alone can produce a no-hire.

- **Blaming others.** Even if true, the story is about what you did next.
- **"We" with no "I."** Three in a row and they stop listening and start planning the probe.
- **No result.** "And then we shipped it" with no number and no learning.
- **No conflict.** Everything went fine, everyone agreed. Zero signal.
- **Rehearsed perfection.** One or two stories where you were wrong make the rest believable.
- **Wrong size for the level.** A one-week bug fix as a senior Deliver Results story.
- **Vagueness under probing.** Details getting fuzzier as they dig reads as invention.

The probes decide the vote. "What would you do differently?" wants one specific thing, not
"communicate more." "What was the metric?" wants a number, with "roughly" if you do not
recall it exactly. "Who else was involved?" wants precise credit, then your part restated. If
you did not do something, say so. That scores higher than a smooth fiction.

## Questions to ask them

You get about five minutes at the end. Pick two.

Good:

1. "What does a strong engineer at this level do in their first six months that a merely fine one doesn't?"
2. "What is the hardest technical problem your team is working on right now, and what makes it hard?"
3. "How does your team decide what to build next, and how are disagreements settled?"
4. "What has the team changed about how it works in the last year, and why?"
5. "What made you stay as long as you have?"

Bad:

1. "What does the company do?" Anything the careers page answers.
2. "How did I do?" They cannot tell you, and it signals insecurity.
3. "What's the work-life balance like?" Wrong room. Ask the recruiter, or ask "what does a typical on-call week look like?"

## Words you will hear

- **STAR.** Situation, Task, Action, Result. The shape of every answer.
- **Leadership Principle (LP).** One of Amazon's sixteen named values.
- **Bar Raiser.** An Amazon interviewer from another team who protects the hiring standard. Can veto.
- **Debrief.** The meeting where interviewers read each other's notes and argue.
- **Probe.** The follow-up question. "What was the metric?" Probes decide the vote.
- **Story bank.** Your eight prepared stories, written in STAR form.
- **Googleyness & Leadership.** Google's one behavioral round.
- **Hiring committee.** At Google, people who never met you read all the notes and decide.
- **Disagree and commit.** Push back with data, lose, then support the decision fully.
- **p99.** The time the slowest 1 in 100 requests take. A common number in engineering stories.

## Mistakes everyone makes once

- **Treating it as the warm-up.** It is the interview, with a rubric and a vote per principle.
- **Waiting for an impressive story.** Specific is the bar, not impressive. A two-week bug with three "I" decisions beats a vague "I led a migration."
- **Ending every story being right.** Real careers include losing arguments.
- **Rounding up a number you do not remember.** Say "roughly" and give what you recall. Invented details get vaguer under probing, not sharper.

## What to do next

Set a 20-minute timer. Pick one true thing from the last two years where something went wrong
and you did something about it. Write it in four sentences labeled S, T, A, R, with a number in
R and at least three "I" verbs in A. Read it aloud with a timer. If it is under two minutes and
has the number, you have story one of eight. Tomorrow, write story two.
