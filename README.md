# Testudo
This program allows students who currently attend the University of Maryland, College Park to search for course sections on testudo via the command line, and to be notified when a section that was previously closed opens. Rather than paying [$50](http://umd.thecoursehunter.com/faq.php#accordion) per course on services such as [CourseHunter](http://umd.thecoursehunter.com), testudo provides an open-source alternative.

To use testudo, run the file `testudo.py` using Python version 3, and provide the name of the course that you want to see the sections available for. Use the following syntax, and provide that name of the course where it says `<course-name>`.

```Shell
python3 testudo.py <course-name>
```
Below, example output it shown for when the course name provided is `math140`. Every possible section for the class in the upcoming semester is listed, with an index number in the leftmost section of the window.

<p align="center">
<img src="https://media.giphy.com/media/3o6fIW5pCWYCSQIHE4/giphy.gif">
</p>

Once the list of sections offered is returned, the only thing left to do is pick a section. Type in the number of the row containing the section that you want to be notified of as soon as it opens. Hit the enter/return key and wait. The program will stop running and let you know as soon as the section requested becomes available.

It is important to understand that because this program continuously operates, whichever machine it's running on needs to be powered on until you are notified. Otherwise, the program will not be able to notify you if the section becomes available. Also, due to the nature of registering for classes, this is NOT meant to be a substitute for the waitlist. You will always want to get on the course's waitlist if possible. This program is meant to assist you in registering.

---
## How's it work?
Most people would think that whoever is on the waitlist would be the first to get into a section that finally opens up more seats. This assumption is outright incorrect. Whenever a seat is added to a class that is full, there is a 15 minute lag-time before students on the waitlist are added into the class. During this time, anyone who sees the opening is able to add the section to their schedule.

Instead of constantly refreshing the page and hoping the section that you want opens up, this program will run in the background and notify you once the section opens (if at all). The way it does this is by checking the class registrar every so many seconds, and examining if the desired section has seats.

<p align="center">
<img src="https://media.giphy.com/media/l3mZ8V9ScGTyx72aQ/giphy.gif">
</p>

Every time that the program checks the registrar, it will output a message that details whether the section is currently open or closed, and the date and time of when the check occurred. The GIF above is sped-up, in reality the program checks the registrar about every 35-45 seconds.

## How will I be notified?
Because third-party notifications such as SMS, Twitter-bots, emails and etc. require API keys, the only included notification system is the command-line output. If you wish to modify `testudo.py` to send you custom alerts when a section has opened up, locate the following snippet of code in the file.

```Python
'''
Place custom notification code in this area!
'''
```
Replace the comment with whatever API or custom notification system you have in mind! The code should only be executed inside of the final `if` statement in the `testudo` method.
