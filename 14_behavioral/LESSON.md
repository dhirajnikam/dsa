# 14 · Behavioral

> Amazon does not hire the best coder in the loop. It hires the person every interviewer can
> write a paragraph of evidence about. Your job in this chapter is to make that paragraph
> easy to write.

**Interview frequency:** every single Amazon round, 15 to 25 minutes each, including the
coding and design rounds. Google asks one dedicated round called Googleyness & Leadership.
Nothing else in this course has a higher failure rate per minute of preparation skipped.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

A behavioral interview asks you to prove a quality about yourself with a true story that has
a number in it, instead of claiming the quality with an adjective.

### Start with something you already do

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

### Now the same thing with numbers

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

### The words people use

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

### Why this matters more than it looks

At Amazon, every round opens with 15 to 25 minutes of this. Four or five rounds means 60 to
125 minutes of behavioral in one loop, more than any single coding problem gets. The Bar
Raiser typically spends their whole hour on it and can veto. If two interviewers write "no
evidence of Ownership," a perfect coding round does not rescue you.

The lesson calls this the highest failure rate per minute of preparation skipped in the
course, and the arithmetic backs it up. The preparation is eight true stories, one page each,
and 30 minutes a day for two weeks. Roughly seven hours to remove the most common reason
strong coders get rejected.

### Try it in your head

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

### Common confusions, cleared

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

### What to do next

Open Part 2 below and read Part 2 §3, "STAR done right," including the strong and weak versions of
the same story. Then a 20-minute first task: pick one true thing from the last two years
where something went wrong and you did something about it. Write it in four sentences labeled
S, T, A, R, with a number in R and at least three "I" verbs in A. Read it aloud with a timer.
If it is under two minutes and has the number, you have story one of eight. Then read Part 2 §4 to
build the matrix.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Amazon's Leadership Principles are not interview
decoration. They are how promotions and performance reviews are actually run inside the
company. A promotion packet is evidence written under headings like Ownership and Dive Deep,
argued over by a committee the way the debrief will argue over you. The
behavioral interview is a preview of your review. Google's Googleyness round exists for a
blunter reason: a brilliant engineer who cannot collaborate costs a team more than they add.
Companies bother because the coding rounds measure what you can do alone, and nobody there
works alone.

**The analogy.** A job reference that you deliver yourself. A weak reference says "she is very
proactive." A strong one says "when the payment service was paging every night, she found the
config change nobody had noticed and the pages dropped from seven a week to one." The second
is a lawyer presenting evidence, not offering an opinion. Your job in this chapter is to be
that lawyer for your own case: specific systems, specific numbers, and the interviewer
supplies the adjective.

**How it works, in plain words.** The interviewer has been assigned two or three principles and
needs to write a paragraph of specific evidence about you under each one. If that paragraph is
easy to write, you pass. If they are left with "seemed capable but was vague," you fail,
whatever the coding round showed. STAR exists to make the paragraph easy to write: Situation and
Task so they can picture it, Action as three to five "I" decisions they can quote, Result as
a number they can copy down. The story bank in section 4 makes sure that
material exists for every principle before you walk in.

**What learning this will feel like.** Engineers resist this chapter more than any other.
Telling stories about yourself feels like bragging, or worse, like lying, and the round gets
discounted as "soft." That reaction is why the failure rate is so high: the people who
feel it skip the preparation. Two things dissolve it. The story bank turns this into
preparation rather than performance: you are recalling eight things that actually happened,
written down in advance, not improvising a sales pitch. And specific numbers make
modesty unnecessary. "I brought p99 from 800 back to 400 milliseconds" is not a boast. It is a
fact, and facts do not need a humble voice. The aha is hearing yourself on a recording and
realizing you sound like a colleague describing work, not a candidate selling.

**You will know you have it when** an interviewer names any principle and a specific story,
with its number, is in your mouth within five seconds.

### 1. Why this decides Amazon loops

An Amazon onsite is four to five interviewers plus a **Bar Raiser**: a trained interviewer
from an unrelated team whose only job is to protect the hiring bar. The Bar Raiser has veto
power. They typically spend their entire hour on behavioral questions and are the best
question-asker in the room.

Before the loop, each interviewer is assigned **two or three Leadership Principles** (LPs) to
probe. They write their questions to hit those LPs, take notes during your answer, and then
write a verdict per LP: evidence, level, and a hire / no-hire vote. At the debrief they read
each other's feedback and argue it out. If two interviewers say "no evidence of Ownership,"
your excellent coding round does not save you.

This means:

- You will be asked about the same LP by more than one person. You need two different stories
  for the important ones.
- "Tell me about a time" questions are not small talk before the real interview. They *are*
  the interview, graded to a rubric.
- The grader is looking for specifics they can quote. Adjectives ("I was very proactive") are
  worth nothing. Numbers, names of systems, decisions, and dates are evidence.

**Google's equivalent** is the Googleyness & Leadership round (sometimes written G&L). No
principles list to memorize. The interviewer looks for four things: **collaboration** (how you
work with people who are not on your team), **navigating ambiguity** (what you do when nobody
tells you the requirements), **ownership and leadership without authority** (did you step up
when nobody asked), and **ethics and judgment** (do you push back on the wrong thing). A
hiring committee reads the written feedback from every round, so the same "quotable
specifics" rule applies. Section 6 covers the Google-specific angles.

### 2. The 16 Amazon Leadership Principles

For each: what it means in plain English, two questions you will actually hear, and what a
strong answer must contain. Learn the names. Interviewers rarely say "this is a Dive Deep
question," but you should know which one you are answering so you can hit its marks.

#### Customer Obsession
**Meaning.** Start from what the customer needs, not from what is convenient to build.
**Questions.** "Tell me about a time you went above and beyond for a customer." "Describe a
time you had to balance customer needs against business or technical constraints."
**Strong answer contains.** A named customer (internal counts), a specific thing they needed
that was not on your plan, what you gave up to serve it, and how you knew it worked (usage,
feedback, a metric).

#### Ownership
**Meaning.** You act on behalf of the whole company, not just your ticket. "That's not my
job" is the anti-pattern.
**Questions.** "Tell me about a time you took on something outside your responsibilities."
"Describe a time you saw a problem nobody owned. What did you do?"
**Strong answer contains.** The gap you noticed, why it was nobody's job, the moment you
decided to own it, and the long-term fix (not a one-time patch).

#### Invent and Simplify
**Meaning.** Find a simpler way; do not accept "this is how it has always been done."
**Questions.** "Tell me about a time you simplified a process or system." "Describe the most
innovative thing you have done."
**Strong answer contains.** The before-state with a measure of its complexity (steps, lines,
hours, services), the idea, why it was not obvious, and the after-state with the same measure.

#### Are Right, A Lot
**Meaning.** Good judgment, and the habit of seeking out views that might prove you wrong.
**Questions.** "Tell me about a time you made a decision with incomplete information." "Tell
me about a time you were wrong."
**Strong answer contains.** What data you had, what you did not have, how you decided, the
outcome, and (for the "wrong" version) what changed in how you decide now.

#### Learn and Be Curious
**Meaning.** You keep learning on your own and it shows up in your work.
**Questions.** "Tell me about something you learned recently that made you better at your
job." "Describe a time you had to learn a new technology quickly."
**Strong answer contains.** What triggered the learning, how you did it (specific: a book, a
codebase, an expert you cornered), and the concrete thing it let you do that you could not do
before.

#### Hire and Develop the Best
**Meaning.** You raise the bar for the people around you: mentoring, feedback, interviewing.
**Questions.** "Tell me about a time you helped someone grow." "Describe how you have given
difficult feedback."
**Strong answer contains.** The person's starting point, what you did (not "I mentored them"
but what you actually said and set up), and where they ended up. For senior roles: how you
changed a team's hiring or review process.

#### Insist on the Highest Standards
**Meaning.** You do not ship things you know are not good enough, even under pressure.
**Questions.** "Tell me about a time you refused to compromise on quality." "Describe a time
you were not satisfied with the status quo."
**Strong answer contains.** The standard that was at risk, who was pushing to lower it and
why (they had a reason), what you did instead, and the cost you paid for holding the line.

#### Think Big
**Meaning.** You propose direction beyond the current quarter, and you make people see it.
**Questions.** "Tell me about a time you proposed something bold." "Describe a time you
influenced a strategy or roadmap."
**Strong answer contains.** The small thing you were asked for, the bigger thing you saw, how
you sold it, and what actually got built. If it did not get built, what you learned.

#### Bias for Action
**Meaning.** Speed matters; most decisions are reversible; do not wait for perfect information.
**Questions.** "Tell me about a time you had to make a quick decision." "Describe a time you
took a calculated risk."
**Strong answer contains.** Why waiting was expensive, what you did *and how you limited the
downside* (feature flag, rollback plan, small blast radius), and the result. Recklessness is
the failure mode; "calculated" is the word.

#### Frugality
**Meaning.** Do more with less; constraints breed invention.
**Questions.** "Tell me about a time you delivered with limited resources." "Describe a time
you saved money or effort."
**Strong answer contains.** The resource you did not have (people, budget, time, compute),
the cheaper path you found, and the cost you saved in a unit (dollars, hours, instances).

#### Earn Trust
**Meaning.** Listen, speak candidly, own your mistakes publicly, treat others with respect.
**Questions.** "Tell me about a time you had to earn the trust of a team." "Describe a time
you received hard feedback."
**Strong answer contains.** The trust deficit and why it existed, the concrete things you did
over time (not one gesture), and how you knew trust had been restored. For feedback: what
you were told, exactly, and what you changed.

#### Dive Deep
**Meaning.** You go to the data and the code; you do not accept a summary when the detail
matters.
**Questions.** "Tell me about a time you found the root cause of a hard problem." "Describe a
time the data told you something different from what people believed."
**Strong answer contains.** The symptom, at least three layers of investigation with the tool
or query at each layer, the root cause, and the fix. This is where you may talk technically.

#### Have Backbone; Disagree and Commit
**Meaning.** Push back respectfully when you disagree, even with seniors; once decided,
commit fully.
**Questions.** "Tell me about a time you disagreed with your manager." "Describe a time you
pushed back on a decision and lost."
**Strong answer contains.** What you disagreed with and why, how you argued (data, in the
right forum), the decision, and *how you committed* afterward, including the outcome. Both
halves are graded. A story where you won is fine; a story where you lost and committed
gracefully is better.

#### Deliver Results
**Meaning.** You ship, on time, at quality, despite setbacks.
**Questions.** "Tell me about a time you delivered under a tight deadline." "Describe a
project that hit obstacles. How did you get it over the line?"
**Strong answer contains.** The commitment, the obstacle (specific), the trade-off you made
(scope, not quality), and the shipped result with a date and a number.

#### Strive to be Earth's Best Employer
**Meaning.** You make the workplace safer, more inclusive, and better for the people in it.
**Questions.** "Tell me about a time you improved your team's working environment." "Describe
a time you supported a colleague who was struggling."
**Strong answer contains.** Something you did for others that was not required, why it
mattered to them, and what changed. Empathy shown through actions, not stated as a trait.

#### Success and Scale Bring Broad Responsibility
**Meaning.** Your decisions affect people outside the room; consider them.
**Questions.** "Tell me about a time you considered the wider impact of a technical decision."
"Describe a decision where the right thing and the easy thing differed."
**Strong answer contains.** Who was affected beyond the immediate stakeholder (users, other
teams, the public), what you did about it, and what it cost you.

Priorities if your time is short: **Ownership, Dive Deep, Deliver Results, Customer Obsession,
Have Backbone, Earn Trust, Bias for Action, Invent and Simplify.** Those eight cover the
overwhelming majority of Amazon questions. The other eight show up more at senior levels.

### 3. STAR done right

STAR is Situation, Task, Action, Result. Everyone knows the acronym. Almost everyone gets the
proportions wrong. The fix:

| Part | Budget | Rule |
|------|--------|------|
| **Situation** | 2 sentences, 15 seconds | Enough context for the interviewer to picture it. No history lesson. |
| **Task** | 1–2 sentences | *Your* responsibility, not the team's. "I was responsible for..." |
| **Action** | 60% of the answer, 90–120 seconds | Three to five steps, each starting with "I". Decisions, not activities. |
| **Result** | 20 seconds | A number. Then one sentence on what you learned or changed afterward. |

Total: two to three minutes. Then stop and let them probe. A four-minute monologue is a
warning sign to the interviewer; a ninety-second answer with a number in it is a gift.

**"I", not "we."** The interviewer is hiring you, not your team. Every "we decided" forces
them to ask "what did *you* do?" and costs you a probe. Say "the team's goal was X; my part was
Y; I did Z."

#### A strong answer (about 200 words)

*Question: "Tell me about a time you found the root cause of a difficult problem."* (Dive Deep)

> **S:** Last spring our checkout service's p99 latency doubled overnight, from 400 ms to 800 ms,
> with no deploy on our side. **T:** I was the on-call engineer and owned finding the cause;
> the team lead wanted to roll back a dependency and move on.
>
> **A:** I first checked our dashboards and confirmed the jump was only on requests that hit
> the pricing endpoint, which ruled out the load balancer and the database. I pulled traces
> for fifty slow requests and saw the extra time was inside a single downstream call to the
> promotions service. Their team said nothing had changed. I did not accept that; I diffed
> their deploy history and found a config change that had dropped their cache TTL from ten
> minutes to ten seconds, which pushed every request through to their database. I wrote a
> two-paragraph summary with the trace IDs and the exact config diff and sent it to their
> on-call.
>
> **R:** They reverted within an hour and p99 returned to 400 ms. I then added a latency
> alert per downstream dependency so we would catch this in minutes, not overnight. It fired
> twice in the next quarter and both times we found the cause in under thirty minutes.

Why it works: a metric at the start and end, four "I" actions each of which is a decision, a
disagreement handled with evidence, and a follow-up that changed the system.

#### The same story, weak version, annotated

> We had a latency problem in checkout that was really bad and affecting a lot of customers.
> *[No number. "Really bad" is an adjective. Who were the customers?]*
> We looked at the dashboards and did a lot of investigation.
> *["We." "A lot of investigation" says nothing about what you did.]*
> Eventually we figured out it was the promotions team's fault because they changed their
> cache config.
> *["Their fault." Blame. Also: how did you figure it out? The whole Dive Deep signal is in
> the "how," and it is missing.]*
> They fixed it and things went back to normal.
> *[No number. No "I". Nothing you did to prevent it recurring.]*
> I learned that you should always check dependencies.
> *[Generic. A lesson anyone could say without having lived the story.]*

Same events. One gets a hire; the other gets "no evidence, candidate was vague."

### 4. The story bank

You need about eight stories. Each story should be strong for two or three LPs, so that
every LP you are likely to be asked has at least two stories behind it and you never tell the
same story twice to the same interviewer (they compare notes at the debrief).

#### Template

Fill this in before you do anything else in this chapter. The X marks are an example of what a
finished matrix looks like; yours will differ.

| Story (short name) | Cust. Obs. | Owner. | Invent | Right | Learn | Hire/Dev | Standards | Think Big | Bias Action | Frugal | Trust | Dive Deep | Backbone | Deliver | Best Empl. | Broad Resp. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1. Latency root cause | | X | | | | | | | | | | **X** | X | | | |
| 2. Migration under deadline | | X | | X | | | | | X | | | | | **X** | | |
| 3. Disagreed with manager on rewrite | | | X | X | | | | | | X | | | **X** | | | |
| 4. Mistake I owned (bad deploy) | X | **X** | | X | | | X | | | | **X** | | | | | |
| 5. Mentored a junior to ship alone | | | | | | **X** | | | | | X | | | | X | |
| 6. Ambiguous requirements, customer interviews | **X** | | X | | X | | | X | | | | | | X | | |
| 7. Simplified a process nobody liked | | X | **X** | | | | | | X | **X** | | | | | | |
| 8. Went beyond scope: reliability fix | X | **X** | | | | | **X** | X | | | | X | | | | X |

Bold X is the story's primary LP; plain X is a secondary LP the same story supports.

Check the columns. Every LP in your priority eight should have at least two marks. If a column
is empty, you need a story for it or you need to find that angle in an existing story.

#### Picking the eight

Interviewers ask about the same eight situations over and over. Have one story for each:

1. **A conflict** with a peer or another team, resolved without escalation.
2. **A failure or mistake you owned**, with the fix and the systemic change.
3. **A tight deadline** where you cut scope, not quality, and shipped.
4. **Ambiguous requirements** where you went and found out what was actually needed.
5. **Disagreeing with a manager** or senior, with data, and committing afterward.
6. **Going beyond scope**: fixing something nobody assigned you.
7. **Mentoring or growing someone**, or improving how the team works.
8. **A hard technical problem** you dug to the bottom of.

Rules for choosing:

- **Recent beats old.** Last two years. A college project for a senior role is a red flag.
- **Sized to the role.** SDE1: a feature or a bug. SDE2: a service or a cross-team project.
  SDE3 / senior: a system, a roadmap, or an organizational change. A one-week task cannot
  carry a senior answer.
- **Conflict required.** A story where everything went smoothly has no signal. The
  interviewer wants to see you under some pressure: a disagreement, a deadline, a failure.
- **You must have a number.** Latency, dollars, hours saved, users, percentage, incident
  count. If you did not measure it, estimate it honestly and say "roughly."
- **Write them down.** One page per story in STAR form. Rehearse them out loud until you can
  tell each one in two minutes and answer probes on any detail. Do not memorize the words;
  memorize the beats.

### 5. Follow-up probes and how to answer them

The first answer gets you on the board. The probes decide the vote. A good interviewer asks
three to five follow-ups per story. Common ones:

| Probe | What they are checking | How to answer |
|-------|------------------------|---------------|
| "What would you do differently?" | Self-awareness; whether you learned | Name one specific thing, not "communicate more." "I would have added the dependency alert before the incident, not after." |
| "What did your manager say?" | Whether you actually did it, and how it landed | Quote them roughly. "She said the write-up was the clearest incident summary she had seen and asked me to present it at the team meeting." |
| "What was the metric?" | Whether the result is real | Give the number. If you do not know precisely: "Roughly a 40% reduction; I remember it went from about 25 to about 15 a week." |
| "Why did you decide that?" | Judgment | The two options you weighed and why you picked one. |
| "Who else was involved? What did *they* do?" | Whether "I" was really "we" | Credit them precisely, then restate your part. |
| "What was the hardest part?" | Depth | Pick the moment of genuine difficulty, usually a person, not a technology. |
| "How did the other person feel about it?" | Earn Trust | Their perspective in their terms; whether the relationship survived. |
| "What happened afterward? Is it still in place?" | Whether the fix stuck | Honest status. "It ran for a year; it was replaced when we moved to the new platform." |

**Do not invent.** Interviewers are good at spotting the moment a candidate starts making
things up: the details get vaguer, not sharper. If you do not remember, say so and give what
you do remember: "I don't recall the exact number, but it was the difference between a page
a night and a page a week." If you did not do something, say so: "I did not follow up with
the other team afterward; in hindsight I should have." That answer scores higher than a
smooth fiction.

### 6. Google-specific: Googleyness & Leadership

Google's behavioral round is less structured than Amazon's and the interviewer has more
freedom. They still write to a rubric, and the hiring committee reads it looking for the
same four things named in section 1. Use STAR; keep the "I" rule.

**Ambiguity.** Google wants to hear what you do when nobody has written the requirements.
The wrong answer is "I asked my manager." The right shape: "I wrote down what I thought the
goal was, listed the three things I did not know, found the person who knew each one, wrote a
one-page proposal, and got the two stakeholders to agree before I built anything." Describe
the process you used to reduce the ambiguity, not just the fact that you tolerated it.

**Cross-team collaboration.** Google is a matrix of teams that do not report to each other.
Stories about influencing someone who did not have to listen to you score highest: another
team's engineer, a PM, an infra owner. Show how you understood their priorities, what you
offered, and how you kept them informed. "I set up a weekly fifteen-minute sync and sent a
short written status every Friday" is a concrete detail; "I collaborated closely" is not.

**Disagreements.** The question will come in some form: *"Tell me about a time you disagreed
with a decision. What did you do?"* Google is checking for two things at once: that you
pushed back (not a pushover) and that you did it well (not a bulldozer). The shape:

1. What the decision was and why you disagreed, in terms of user or system impact, not taste.
2. How you raised it: in the right forum, with data or a prototype, early.
3. What happened. If you were overruled: how you committed and whether you were later proven
   right or wrong. Say which, honestly. "I was wrong, and here is what I learned about why
   they were right" is a strong ending.
4. What the relationship looked like afterward.

**Ethics and judgment.** Occasionally: "Tell me about a time you were asked to do something
you thought was wrong." Have one story ready, even a small one: a metric you refused to game,
a shortcut on user data you pushed back on, a test you would not skip. Keep it factual, not
sanctimonious.

**Leveling.** For L4 the committee wants to see you own a component and work well with the
team. For L5 they want evidence you led something: a design others implemented, a project
across teams, a decision you were accountable for. Pick stories sized to the level you are
interviewing for.

### 7. Red flags that fail candidates

Interviewers write these down. Each one alone can produce a no-hire.

- **Blaming others.** "The other team broke it," "my manager didn't give me enough time." Even
  if true, the story is about what *you* did next.
- **"We" with no "I".** Three "we"s in a row and the interviewer stops listening and starts
  planning the probe.
- **No result.** A story that ends "and then we shipped it" with no number and no learning.
- **No conflict.** Everything went fine, everyone agreed, nothing was hard. Zero signal.
- **Rehearsed perfection.** Every story ends with you being right and praised. Real careers
  include losing arguments and making mistakes. One or two stories where you were wrong make
  the rest believable.
- **Wrong size for the level.** A one-week bug fix as your Deliver Results story for a senior
  role. Or a story where your "ownership" was doing your assigned ticket.
- **Vagueness under probing.** Details getting fuzzier as the interviewer digs. This reads as
  either exaggeration or a story you were not really central to.
- **Speaking badly of a former employer or colleague.** Frustration is fine; contempt is not.
- **No question for the interviewer**, or a question that shows you did not research the
  company. Small, but noted.
- **Talking for five minutes without pausing.** The interviewer has probes to ask and a
  rubric to fill. Give them room.

### 8. Questions to ask the interviewer

You usually get five minutes at the end. Interviewers do note what you ask. Pick two.

**Good**

1. "What does a strong engineer at this level do in their first six months on your team that a
   merely fine one doesn't?" (Shows you are thinking about the bar.)
2. "What is the hardest technical problem your team is working on right now, and what makes it
   hard?" (Lets them talk; you learn about the real work.)
3. "How does your team decide what to build next? Who has input and how are disagreements
   settled?" (Ambiguity, ownership, and culture in one question.)
4. "What's something the team has changed about how it works in the last year, and why?"
   (Tests whether the team learns.)
5. "What made you stay at [Amazon / Google] as long as you have?" (Human, and their answer
   tells you a lot.)

**Bad**

1. "What does the company do?" or anything answerable by the careers page.
2. "How did I do?" Puts the interviewer in an awkward position and signals insecurity. They
   are not allowed to tell you anyway.
3. "What's the work-life balance like?" Not because the question is illegitimate, but because
   this is the wrong room for it. Ask the recruiter, or ask a specific version: "What does a
   typical on-call week look like?"

### 9. The 30-minute daily drill, two weeks

Do this alongside the coding practice. Out loud, standing up if you can, with a timer.

**Week 1: build the bank**

| Day | 30 minutes |
|-----|-----------|
| 1 | Fill in the story matrix from section 4. Pick 8 stories. Write one-line titles. Find the empty LP columns. |
| 2 | Write stories 1 and 2 in STAR form, one page each. Put a number in every Result. |
| 3 | Write stories 3 and 4. For story 4 (the mistake), write what changed in the system afterward. |
| 4 | Write stories 5 and 6. Check: does each story have at least three "I" actions? |
| 5 | Write stories 7 and 8. Re-check the matrix. Every priority LP has two stories? |
| 6 | Tell stories 1–4 out loud, timed. Target under 2:30 each. Record yourself. |
| 7 | Tell stories 5–8 out loud, timed. Listen to day 6's recording and count "we"s. |

**Week 2: pressure-test**

| Day | 30 minutes |
|-----|-----------|
| 8 | Have a friend (or a text file of the section 5 probes) ask three follow-ups per story for stories 1–4. Note where you got vague. |
| 9 | Same for stories 5–8. Fix the vague spots by going back to the facts, not by inventing. |
| 10 | Pick 6 random LP questions from section 2. For each, decide in 5 seconds which story fits, then tell it. This is the real skill. |
| 11 | Do the Google set: ambiguity, cross-team, disagreement. Two stories each, out loud. |
| 12 | Full mock: 4 questions, 25 minutes, someone probing. Then 5 minutes of your questions to them. |
| 13 | Listen to the mock recording. Score it: number in every result? "I" ratio? Any blame? Any 4-minute answers? |
| 14 | Light day. Re-read the red flags. Tell your two weakest stories once more. Stop. |

After two weeks you are done building. From then on, once a week, tell all eight stories in
one sitting to keep them warm, and add a new story whenever something worth telling happens
at work. That habit is what makes the next loop, and the one after that, easy.
