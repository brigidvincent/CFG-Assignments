## CFG-Assignments

### Introduction

Hi! I'm **Brigid**, and I'll be using this repository for all CFG assignments, my first assignment being to create this README :)

### What I've worked on before

I've always been interested in tech, and have dabbled in many different areas of interest within this...
 - <ins>*Python*</ins>: After completing a Data Analytics course (*Google*), I used Python to collect, clean and analyse thousands of chess games by my favourite/ the most renowned chess players (Fischer, Kasparov, Carlsen, Nakamura, etc) in PGN format to reveal insights I was interested in - their 'favourite' piece to open with, their win and lose rate, if playing as white would make a measurable difference to their performance, which opening would most likely lead to their victory/loss, etc...
 - <ins>*HTML, CSS, Javascript*</ins>: learnt through freecodecamp, and have been recently learning *React* to create interactive and visually appealing websites (please see my [plan_my_week](https://github.com/brigidvincent/plan-your-week.git) project documenting my *React* learning journey). Web development has been super fun for me :)
 - <ins>*C# with Unity*</ins>: the most enjoyable foray I've had into tech - I created a small rocket blaster game. I'd love to return to this and create a more complicated narrative game...

---
### What I've learnt in week 1

<ins>**Git commands**</ins>
 > - `cd /path` change directory
 > - `git init` creates a new, empty git repo in the current folder
> - `git status` gives you useful info on the directory/project you’re on (like any untracked files).
> - `git add “name_of_file”` adds file to tracking by git (tracks it and any changes to the file, tells Git which files you want to include in your next ‘commit’/save)
> - `git add .` adds everything to tracking.
> - `git commit` saves a snapshot of changes in the local repo.
> - `git commit -m “explaining the feature we are committing”`
> - `touch “file_name”` creates a file within the folder you’re in. *not specifically a Git command*
> - `git remote add origin url`
> - `git push -u origin main` pushes your local repo to the global repo/GitHub
> - `git branch feature` creates a branch called feature
> - `git switch feature` switches you to feature branch
> - `git branch -d feature` deletes *feature* branch
> - `git branch` lists all branches

## Assignment 1 - Git and Github ##

Please see below for my workflow for this assignment - this was mainly testing if we understand how to use a VCS git within github for future group work...

Here, I direct to the correct folder on my laptop and make my *'assignment 1'* folder into a git repo, check the status, create, add to tracking and commit a new file to my main branch to make it live. I then create a branch *my_first_branch*, switch to it, and create a few files within it.

<img width="615" height="328" alt="Screenshot 2026-08-02 at 01 04 42" src="https://github.com/user-attachments/assets/317c688b-56f4-4c28-a4f2-28da40286a8c" />

After committing these two new files, I create a .gitignore and requirements.txt file, add it to staging and commit this to my branch, using `ls -la` to check my gitignore has definitely been created.

<img width="614" height="349" alt="Screenshot 2026-08-02 at 01 20 18" src="https://github.com/user-attachments/assets/7c3392f7-dd56-4f1f-ad6e-19e05e698400" />

<img width="620" height="115" alt="Screenshot 2026-08-02 at 23 40 10" src="https://github.com/user-attachments/assets/05ae8451-4a19-49c4-9fd3-8d75f94a95e7" />

<ins>*Brief explanations*</ins>

*.gitignore file* - a file in the repo to tell Git which files and directories to ignore when you make a commit

*requirements.txt* - a list of all of a project's dependencies + the specific version to help the user/developer know what packages are needed to run the project, avoiding any compatibility issues.

All done (merged)!

<img width="577" height="53" alt="Screenshot 2026-08-03 at 00 16 59" src="https://github.com/user-attachments/assets/55ad3f8c-9ae9-4421-946a-13068a4c1e2b" />

## Assignment 2 - Python and APIs ##

For our API assignment, I think I picked a bit of a complicated project so changed / reduced what I was doing quite a few times...

First I mapped out my initial ideas/workflow in comments with links to APIs I might use:

<img width="1139" height="392" alt="Screenshot 2026-08-16 at 23 22 43" src="https://github.com/user-attachments/assets/922281b7-4226-404f-9591-ee1bc5da3421" />

I decided I wanted to use a few APIs in my project to get the full hang of them, so decided to create a simple "last-minute" holiday planner...
 - <ins>*User preferences*</ins>: It would first ask the user their preferences on weather (Sunny and warm, or cold and snowy)
 - <ins>*Date of holiday*</ins>: Initially I let the user set the start date but this became complicated, so altered the project to make it find a holiday starting tomorrow, and let the user set the length of the holiday (within 14 days to keep weather reliable)
 - <ins>*Result*</ins>: The program then returns a "top 3" cities to visit - initially I was going to base this off the popularity of the location (see above screenshot), but decided instead to give a "weather score" (based off the temp and the 'sunniness'/'snowiness' of the location to make it more personalised towards the user) and randomly choose from these.

I wanted to include multiple cities for each country to look through, but didn't know how to go about this without either spending too much time hand-picking a couple of cities for each country or importing a massive amount of data? (i.e. checking the weather for every city in the world) so I decided on just using [my countries API](https://countries.dev) to grab the capitals of each country and use this to collect the weather forecast with a [weather API](https://www.weatherapi.com) for each. All my steps are detailed more in the comments of the python code) ... I'd like to come back to this to flesh it out more when I know more about python/how to use it efficiently :)

I wrote out how I wanted my program to work in comments, replacing/deleting them (or condensing them to explain what I was doing) as I started to code out the actual program. Please see below my initial bits of code and ideas !

<img width="971" height="503" alt="Screenshot 2026-08-16 at 23 24 13" src="https://github.com/user-attachments/assets/89b03782-e97a-4afc-b478-62d162e1b51d" />

I hope you enjoy using this as it took me a while! :) 

**UPDATE**: Please note, I have now updated this assignment's code to reflect the feedback of my marker:
*feedback as follows*: 
• I would advise using json.dumps when you want to print so as to format your list nicely.
• You did not write the API data after modification into a file.

## Assignment 3 - Data and SQL ##

This Assignment tasked us to design and implement a relational database, demonstrating normalisation and understanding of more complex SQL queries to gain insights into our own data. I chose to create a database that a fictional PI (Private Investigator) company might use to keep track of their clients, potential suspects, cases and detectives. I then carried out various queries to reveal interesting information or queries the PI company might have made - e.g. seeing the best available detective for a specific case. Please see the SQL file for comments in the code.

**UPDATE**: Please note, I have now updated this assignment's code to reflect the feedback of my marker into a separate REVISED edition, under the Assignment 3 folder:
• There is data duplication in your table formation. The  tbl_suspects should have a unique constraint becase of a suspect in case A becomes a suspect in case B, the person's details could be inserted into the table again without any alert. Same with the client table.
• Cases contain detective_id, does this mean that only one detective can work on a case?
• Your foreign key prevents the delete query from running.


## Assignment 4 - Advanced Python ##

This Assignment was tasked to us to bring all our knowledge up to this point (Week 8) together by designing and implementing a simple API - using Flask - to tackle a unique problem or scenario, and show a real-life expected use of a database. I chose to do create a film database, and implemented a *very* simple UI to show potential use of my API (to help users find a film to watch based on their preferences, as well as a Surprise Me! functionality). Please see all code under assignment 4 (with comments and proper separation of components).
