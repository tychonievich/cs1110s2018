---
title: Spring 2018 Syllabus
...

# Basic Info

Course website: [http://cs1110.cs.virginia.edu](http://cs1110.cs.virginia.edu)

Lectures and Labs: see [main page](http://cs1110.cs.virginia.edu)

# Contact

Running a course as large as Introduction to Programming requires some coordination.
Please help us by directing your contact in the right direction.

To discuss                                                    You should contact us via
-----------------------------------------------------------   ------------------------------------------------------------
Q about course topics                                         In-class questions, office hours, or Piazza
Q about code not working                                      Office hours
Q about [grading](#grading-concerns-and-appeals)              Regrade request on [the submission site](https://archimedes.cs.virginia.edu/cs1110/)
Conversations about mentoring, research, student life, etc.   Office hours or schedule one-on-one visit
Personal issues impacting coursework                          Your dean, and/or private email to your section's instructor


## Luther Tychonievich

Office: Rice 208

Office hours: will be scheduled during the third week of the semester (one of my courses is not scheduled until then).
Unless otherwise arranged, I will not have office hours on days of exams.
If my door is open, you are welcome to come in even when it is not my scheduled office hours.

Email: tychonievich@virginia.edu

Comments: I read email once each work day if it contains 1110 in the subject line.  I get so much email that email without 1110 in the subject line often goes unread.

## Craig Dill

Office hours: Monday and Wednesday, 1--2pm in Rice 514

Email: cd9au@virginia.edu 

## Upsorn Praphamontripong

Office: Rice 206

Office hours: TBA

Email: up3f@virginia.edu 

Comments: I read email during work hours only, if it contains 1110 in the subject line. I get so much email that email without 1110 in the subject line often goes unread.


## Teaching Assistants
TA office hours are held in the Stacks in Thorton A wing most days; a schedule will be released soon.
See [the office hours tab](oh.html) for more on how to get their help.

We are still in the process of hiring TAs. A list will appear here later.

Our TAs are students too.
Please show them respect and only contact them via piazza, or in person during their scheduled office hours.
    
Pestering our TAs when they are off the clock (including via email) can be penalized under the "professionalism" clause of our grading policy.

## Piazza Message board
Piazza @ [https://piazza.com/class/j6m7hyps7tx66x](https://piazza.com/class/jc22j4dppl6247)

Log in to Piazza and use the threads for quick questions, assignments, and for discussion with other students and staff.

You can also post private messages here that will only be seen by staff members.
Make sure all private messages are visible to *all* instructors, not just one or two.

# Text

## Primary Text

<span class="floater">![Sprock books's cover](files/codercover.png)</span>

*The Coder's Apprentice* by Pieter Spronck; available online for free: [http://www.spronck.net/pythonbook/](http://www.spronck.net/pythonbook/)

So far as we know, no print version of this book is available.

<div style="clear:both;"></div>

## Optional resource

<span class="floater">![Gaddis books's cover](http://wps.pearsoned.com/wps/media/objects/15642/16017913/_skins_/D/default_blue/cover.jpg)</span>

*Starting Out with Python* by Tony Gaddis; available via the UVA bookstore or for purchase online.

We will not refer to this text explicitly, but if you want a printed reference this is a good pick.

<div style="clear:both;"></div>

# Course Requirements

You should meet the following requirements to take this class:

-   Can attend class regularly.
-   For 1110, can attend lab regularly.
-   For 1111, some previous programming experience is required.

# Assessment

In common with many courses in CS, we use a point-based grading system.

Task                        Weight  Comments
-------------------------  -------- ----------------------------------------------
Programming assignments     31.5%   Solo programming assignments will be due almost every week, and will be weighted equally
Project                     7.5%    A larger partner project will be worth more points than the average assignment
Exams                       50%     Per College policy, "Unexcused absence from a final examination results in an automatic grade of F in the course."
Participation               11%     For 1110, most participation points are awarded in lab; for 1111, most will be for in-class exercises.
Professionalism Penalty    0--100%  Excessive missed classes, rude behavior toward instructor or classmates, unauthorized homework assistance, pestering TAs when they are not on the clock, etc., can be held against a student when final grades are calculated.

The exact weights of assignments is subject to change as we further refine the assignments we will give.

Your final letter grade will be calculated as follows:

You get  if you score  GPA value
-------- ------------- ---------
A+       near the top  4.0
A        ≥ 93%         4.0
A−       ≥ 90%         3.7
B+       ≥ 86%         3.3
B        ≥ 83%         3.0
B−       ≥ 80%         2.7
C+       ≥ 76%         2.3
C        ≥ 73%         2.0
C−       ≥ 70%         1.7
D+       ≥ 66%         1.3
D        ≥ 63%         1.0
D−       ≥ 60%         0.7
F        otherwise     0.0

**Rounding:** By default, grades will not be rounded in this course.

**Pass/Fail/Audit:** A course average of 65.0% or higher with at least one passing exam grade is required for successful completion.

# Class Management

## General

- Faculty Office Hours -- We in general have an "open door" policy, in that if our door is open, by all means stop on in and say "hi" or ask a question. If our doors are closed, then we're heads down on some task, on the phone, in a meeting, etc. It's always a good idea to email or call before coming to make sure we're here if it's not office hours.
- When posting on Piazza, please use the search feature first; we prefer not to answer the same question repeatedly.
- If you email, please put 1110 (or 1111) somewhere in the subject. It makes it easier on the staff. And please don’t just reply to an email sent over a month ago. That makes it harder to keep up with your email.
- Please don’t hesitate to contact us if you have any problems, concerns, questions, or issues regarding the course, material, or anything else in the class.

## Academic Honor in Coding

The line between collaborative learning (which is beneficial and encouraged) and cheating (which is counterproductive and discouraged) is often difficult to draw clearly in CS courses.
Additionally, some questionable behavior (like doing a web search for a homework assignment and submitting whatever you find) is correlated with negative learning impact (a lot of misinformation is available online).

### No plagiarism (nor anything like it)

You **must** site any and every source you consult, other than those explicitly provided by the course itself.
Talked to a friend, saw an interesting video, consulted a website, had a tutor?
Tell us!

Citing can be done either as a comment near the code in question, as e.g.

````python
    year = int(input('What year is it? '))
    if (year % 4) == 0:        # I got this line from M.S. Theater (mst3k)
        if (year % 100) == 0:  # ... and used it to figure out this line on my own!
````

or as a docstring at the beginning of the file, as e.g.

````python
"""Source of help:
  I found the distance formula on http://this.web.site/here 
  My friend Thomas Jefferson (tj1a) showed me how to use ** instead of math.sqrt
"""
````

### Write your own code

You must write your own code.
Not just type it (though you need to do that too): compose it yourself.
Beware of looking at other students code or code you find online: it is hard to unsee and can spoil your ability to compose your own solutions!

### Understand what you submit

Working together can help you learn. But make sure you learned!
We may ask you to explain aspects of a solution you turn in,
and may dock points if it appears you simply copied someone else's ideas (or just guessed a lot of things until one worked) without understanding them.

### No help on exams

It would probably go without saying if we didn't say it, but no assistance may be given or received on any supervised evaluation unless specifically announced otherwise by the proctor of the evaluation.


## Programming Assignments

- Homework assignments will not be handed out in class. Everything will be available online.
- You should [cite](#acknowledge-your-sources) any ideas you discuss with other students or outside resources, as well as any code assistance you receive from any source.
- See [the submission system](https://archimedes.cs.virginia.edu/cs1110/) for more information.
- Late policy: Programming assignments can be submitted up to 2 days (48 hours) late, with a 10% penalty for each day late. Assignments are not accepted after 2 days past the deadline.

## Generality of Solutions

Both assignments and exams will frequently describe general problems to be solved, and also give a few concrete examples.
Presenting a solution that works for those specific examples but does not attempt to solve the general problem is a form of the [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) called **[hard coding](faq.html#what-is-hard-coding)** and will usually be graded the same as if you had not even attempted the problem.

## Partners

There will be a partner project in this course. Details of the groups are:

- Normal group size is two. Group sizes of three might arise. Expectations will be adjusted to reflect available person power.
- You will remain in the same group for the entire assignment unless you are asked to change.
- In general, all group members will receive the same grade for graded assignments. However, group members will evaluate their peers and any student who appears to not be contributing may be penalized.

You are expected to work as a member of your group in this course and cooperate with your colleagues.
Cooperation means attending group meetings, completing your assignments properly and on time, letting your group know if you will be out of town, responding to e-mail from your group, and so on.
If there is a lack of cooperation by any group member, it should be brought to the attention of the instructor as soon as it happens.
If the lack of cooperation is serious, the offending group member’s semester grade will be lowered. 

## Attendance

- Attendance in lecture is vital to learning the material and making a good grade in this class.
- We may or may not give graded assessments with or without notice in class; these cannot be made up if missed.
- Even in sections that never check attendance, **attendance is strongly correlated with grade**. Skip at your own risk.

## Exams

- There will be a total of three formal exams during the course of the semester, counting the final exam.
- The midterm exams will be given in class. The final exam will be given during the university-set time.  Note that the university sets a special evening time for classes like 1110/1111 where multiple sections share one exam.
- Any exam that is missed due to any absence that is not a University Excused Absence will result in a zero (0) for that grade.  Note that vacation travel is not excused.
- Any exam that is missed due to a University Excused Absence or due to circumstances that are approved by your instructor beforehand must be made up within a week of the missed exam.

## Grading concerns and appeals

The [submission system](https://archimedes.cs.virginia.edu/cs1110/) is also where you see your grade and any feedback on it, and is also how you can submit a regrade request for an assignment.

Requests are subject to the following policies:

-   All regrade requests must be made within one week of the assignment being returned to the student.
-   We will regrade serious errors in judgement; we will not regrade partial credit judgement calls.
-   When regrading, we reserve the right to regrade the entire exam or assignment, which may result in either an increase or a decrease in your grade. We are not trying to scare off students whose exams or assignments were graded incorrectly, but we are trying to avoid frivolous requests.

What should be regraded?

-   The grader made a comment that is not true of your answer.
-   Your answer is the same as what is on the key, but the grader didn’t realize it.
-   Your answer is different, but is also correct (code that compiles and runs correctly, but is different than the key).

What should not be regraded?

-   “Most of what I wrote is correct, so I think I deserve more partial credit.”
-   “I wrote so much, and the grader didn’t notice that the correct answer is buried somewhere within this long paragraph.”
-   “I’m just 1 point away from an A, so I thought it was worth scrounging around to find an extra point somewhere.”

We reserve the right to dock professionalism points for frivolous regrade requests.


# Professionalism

In this course, there will be a focus on working well together and learning about the development process. A large portion of that process involves interpersonal skills and conflict management. Students and staff are all expected to treat each other with respect. This includes, but certainly is not limited to:

- Excessive web browsing during class
- Disrespectful language
- Promptness for all deadlines and class meetings
- Quality work

Students can and will be penalized for unprofessional behavior.

If a student submits code that was not authored by that student (i.e. copied from another student or from the Internet), or if another student submits code that matches a student's code, then the student's overall course grade will be dropped significantly.

# Research

Your class work might be used for research purposes. For example, we may use anonymized student assignments to design algorithms or build tools to help programmers; use data collected from course support tools to better understand and seek to improve student engagement and learning; etc. Any student who wishes to opt out can contact the instructor or TA to do so after final grades have been issued. This has no impact on your grade in any manner.

# Academic Integrity

The School of Engineering and Applied Science relies upon and cherishes its community of trust. We firmly endorse, uphold, and embrace the University’s Honor principle that students will not lie, cheat, or steal, nor shall they tolerate those who do. We recognize that even one honor infraction can destroy an exemplary reputation that has taken years to build. Acting in a manner consistent with the principles of honor will benefit every member of the community both while enrolled here and in the future.

Students are expected to be familiar with the university honor code, including the section on academic fraud ([http://www.virginia.edu/honor/what-is-academic-fraud-2/](http://www.virginia.edu/honor/what-is-academic-fraud-2/)). Each assignment will describe allowed collaborations, and deviations from these will be considered Honor violations. If you have questions on what is allowable, ask! Unless otherwise noted, exams and individual assignments will be considered pledged that you have neither given nor received help. (Among other things, this means that you are not allowed to describe problems on an exam to a student who has not taken it yet. You are not allowed to show exam papers to another student or view another student’s exam papers while working on an exam.) Sending, receiving or otherwise copying electronic files that are part of course assignments are not allowed collaborations (except for those explicitly allowed in assignment instructions).

Assignments or exams where honor infractions or prohibited collaborations occur will receive a zero grade for that entire assignment or exam. Such infractions will also be submitted to the Honor Committee if that is appropriate. Students who have had prohibited collaborations may not be allowed to work with partners on remaining homeworks.

# SDAC and Other Special Circumstances

If you have been identified as an SDAC student, please let the Center know you are taking this class. If you suspect you should be an SDAC student, please schedule an appointment with them for an evaluation. We happily and discretely provide the recommended accommodations for those students identified by the SDAC. Please contact us at least one week before an exam so we can make accommodations. Website: [http://www.virginia.edu/studenthealth/sdac/sdac.html](http://www.virginia.edu/studenthealth/sdac/sdac.html)

If you have other special circumstances (athletics, other university-related activities, etc.) please contact your instructor and/or Head TA as soon as you know these may affect you in class.

# Weather-Related Issues

Please follow official University channels, including the University website and Twitter feed, for information on official closings. Also check your email regularly. If any given faculty member cannot make it to a lecture, an email will inform students with instructions as to what to do. Assume lectures and labs are happening unless an announcement is made.



# This Syllabus

This syllabus is to be considered a reference document that can and will be adjusted through the course of the semester to address changing needs. This syllabus can be changed at any time without notification. It is up to the student to monitor this page for any changes. Final authority on any decision in this course rests with the professor, not with this document.

