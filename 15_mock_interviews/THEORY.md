# 15 · Mock Interviews, explained from zero

Read this first if "mock," "phone screen," and "think out loud" are phrases you have only
heard other people use. When the driving story makes sense, open `LESSON.md`, which has the
minute-by-minute timeline, the script, the rubric, and the 12-week calendar. This file is the
conversation before it.

## In one sentence

A mock interview is a full-length rehearsal of a real interview with the timer, the talking,
and the being-watched all switched on, so that none of those three is new on the day.

## Start with something you already do

You learn to drive. You read the handbook, pass the written test, know every rule. Then you
sit in the car with an examiner in the passenger seat, pull up to the first traffic light, and
stall. Twice.

You did not forget how a clutch works. Three new loads landed at once: someone is watching,
the light is about to change, and the examiner just asked you to say out loud what you are
checking in your mirrors. Each one eats a slice of attention, and attention is the thing you
were using to drive.

The fix is not more handbook. It is the empty parking lot on a Sunday, where you practice
until the clutch and the mirrors cost no thought, then add a passenger, then a stopwatch. Mocks
are the empty parking lot. Every problem in chapters 1 to 12 was learning the rules. This
chapter is driving with a person in the seat.

An interview asks four things at once: solve the problem, talk while you do it, watch the
clock, and be observed. Mocks make the last three automatic so that all your attention goes
back to the first.

## Now the same thing with numbers

A real coding round is 45 minutes. Here is a 5-minute version of the same shape, using Two
Sum from chapter 01, so you can see where each minute goes:

| Time | Phase | What you say or do |
|------|-------|--------------------|
| 0:00 to 0:40 | Clarify | Restate the problem. Ask about size, duplicates, empty input. Write one example. |
| 0:40 to 1:20 | Brute force | "Check every pair, O(n²). The repeated work is re-scanning for each number's partner." |
| 1:20 to 2:00 | Optimize, get buy-in | "A dict of what I have seen makes each check one step: O(n). Does that look right to you?" |
| 2:00 to 3:40 | Code | Write it, narrating decisions, not keystrokes. |
| 3:40 to 4:30 | Test | Trace `[8, 3, 15, 7]`, target 10, with the dict written out. Then the empty list. |
| 4:30 to 5:00 | Wrap | "O(n) time, O(n) space. If this ran a million times on one array, I would precompute." |

Now the phrase "think out loud," which people take to mean "read your code aloud." It does
not. It means narrating decisions. Here are five lines of it, the ones you would say between
0:40 and 2:00:

```
"Brute force is every pair, so n squared. Fine for 100, too slow for a hundred thousand."
"The repeated work is scanning the list again to find each number's partner."
"If I write down the numbers I have already seen, the check for a partner is one step."
"A set would do for yes or no, but I need the index back, so a dict from value to index."
"Before I code it: does that approach look right to you?"
```

Every line is a decision or a question. None is "now I type a for loop."

Why a timer changes everything: at your desk, a medium problem takes however long it takes.
In the room, 40 usable minutes is the whole budget, and the first mock shows most people
spending 20 of them designing and reaching the end with half a function. The timeline exists
so you never have to decide which phase you are in, and the timer is what teaches you the
phases are real.

Pause and predict: at minute 12 you go silent for 90 seconds, staring at the screen and
thinking hard. What does the interviewer write down?

<details><summary>Answer</summary>
"Long silence; unclear whether stuck or thinking." Ninety seconds of good thinking scores the
same as ninety seconds of panic if none of it is spoken. The fix is one sentence: "I am
thinking about how to handle duplicates." Now the silence has a label.
</details>

## The words people use

- **Mock interview.** A timed, out-loud rehearsal, with a friend or a camera, graded afterward.
- **Think out loud.** Narrate your decisions and questions as you make them, not your keystrokes.
- **Phone screen.** The first live interview, 45 to 60 minutes, one engineer, a shared text
  editor. Its job is to decide whether to fly you in.
- **Onsite / loop.** Four or five interviews back to back, in person or on video. The main event.
- **Online Assessment (OA).** Amazon's automated first filter: two coding problems in a browser
  plus a work-style questionnaire, no human present.
- **Shared editor / Google Doc.** Where you type in the interview. No autocomplete, no running
  code. Google literally uses a plain document.
- **Clarifying questions.** What you ask before solving: size, duplicates, empty input, what to return.
- **Brute force.** The obviously correct slow solution. You state it first so something is on the board.
- **Buy-in.** The nod you get after "does this approach look right?" and before you write code.
- **Trace / dry run.** Walking your code on one example by hand, writing each variable's value.
- **Edge case.** Empty input, one element, all duplicates, the largest allowed size.
- **Hint.** A nudge from the interviewer when you are stuck. Budgeted for; not a failure.
- **Rubric.** The scoring sheet. Google uses four axes: algorithms, coding, communication,
  problem solving. Amazon uses a coding bar plus Leadership Principles from chapter 14.
- **Hiring committee / debrief.** The people who read the interviewers' notes and decide.
- **Talk ratio.** How much of the time you are narrating. Silences over 30 seconds count against it.
- **Redo list.** Problems you solved without recognizing the pattern. You do them again a week later.
- **Recognition.** Naming the pattern in the first five minutes instead of finding it by trial.

## Why this matters more than it looks

The lesson names the single biggest reason prepared candidates fail: the gap between solving
at your desk and solving while a stranger watches and a clock runs. Twelve weeks of
preparation can be undone by a three-minute freeze in the first round.

What the interviewer is scribbling makes the cost concrete. At Google, four axes each get a
rating from Strong No Hire to Strong Hire, and two No Hire ratings across the loop usually
end the packet. A silent, correct solution can score Hire on algorithms and No Hire on
communication in the same 45 minutes. At Amazon, a coding round with no evidence for the
assigned Leadership Principles is graded as incomplete even if the code passed.

Hints have arithmetic too. One hint followed by a clean finish reads as "needed a nudge on X,
then finished," which is a Hire in most rooms. The same hint needed twice, or a hint ignored
because you were attached to your approach, is what costs the vote. The cost of a mock is 45
minutes plus 10 minutes of grading. The lesson's minimum before a real loop is five with a
human.

## Try it in your head

1. You solve the problem perfectly in 44 minutes but say nothing for the first 12 while you
   think. What does the rubric give you?

<details><summary>Answer</summary>
A 1 on talk ratio and a 1 on getting buy-in before coding. Correct code with a No Hire on
communication. Twelve silent minutes also means the interviewer could not hint, because they
had nothing to hint at.
</details>

2. The interviewer says, "What if you sorted the input first?" What is the best next sentence?

<details><summary>Answer</summary>
Say what the hint changed: "Right, sorted means duplicates sit next to each other, so I can
skip them with a while loop, and the whole thing becomes O(n log n)." A hint you can restate
as a consequence is evidence you learn fast.
</details>

3. You have no friend available. Can you still run a mock?

<details><summary>Answer</summary>
Yes. A 45-minute timer, a phone camera pointed at your screen, and you talking to the camera,
including "does this look right?" and answering as the interviewer would. Watch it back at
1.5× speed and score the rubric. The recording is what makes it a mock.
</details>

## Common confusions, cleared

- **"Mocks are for after I have finished learning."** The lesson has you using the timeline on
  every problem from week 1 and running the first mock set in week 4. Talking and timing are
  skills; they need reps alongside the material, not after it.
- **"Talking will slow me down."** Narrating decisions costs a few seconds a minute and buys
  you hints, because the interviewer can see where you are. Silence gets no hints.
- **"Needing a hint means I failed."** One hint plus a clean finish and a sentence about what
  it changed is a Hire. Needing the same hint twice is the problem.
- **"The phone screen is the easy one."** Same 45-minute shape with less slack. Amazon's opens
  with behavioral questions. Google's happens in a plain document with no autocomplete, and
  the document is the only thing the interviewer sees, so examples go in writing.

## What to do next

Open `LESSON.md` and read §1, the 45-minute table, and §2, the out-loud script. Then a
20-minute first task: set a 20-minute timer, start your phone recording, and solve `two_sum`
from chapter 01 out loud using the script's sentences, including "does this look right to
you?" answered by yourself. Watch the recording at 1.5× speed and count silences longer than
30 seconds. That count is your starting number. Then read §4 and score yourself with the
rubric before the first real mock set in week 4.
