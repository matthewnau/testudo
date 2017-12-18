# Testudo
This program allows students who currently attend the University of Maryalnd, College Park to search for course sections on testudo via the command line, and to be notified when a section that was previously closed opens.

Rather than paying [$50](http://umd.thecoursehunter.com/faq.php#accordion) per course on services such as [CourseHunter](http://umd.thecoursehunter.com), testudo offers the same functionality for free!

---
## How's it work?
Most people would think that whoever is on the waitlist would be the first to get into a section that finally opens up more seats. This assumption is outright incorrect. Whenever a seat is added to a class that is full, there is a 15 minute lagtime before students on the waitlist are added into the class. During this time, anyone who sees the opening is able to add the section to their schedule.

Instead of constantly refreshing the page and hoping the section that you want opens up, this program will run in the background and notify you once the section opens (if at all). The way it does this is by checking the class registrar every so many seconds, and examining if the desired section has seats.

<p align="center">
<img src="https://media.giphy.com/media/l3mZ8V9ScGTyx72aQ/giphy.gif">
</p>

Every time that the program checks the registrar, it will ouput a message that details whether the section is currently open or closed, and the date and time of when the check occurred. The GIF above is sped-up, in reality the program checks the registrar about every 35-45 seconds.
