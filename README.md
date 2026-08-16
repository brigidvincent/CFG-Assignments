## CFG-Assignments

### Introduction

Hi! I'm **Brigid**, and I'll be using this repository for all CFG assignments, my first assignment being to create this README :)

### What I've worked on before

I've always been interested in tech, and have dabbled in many different areas of interest within this...
 - <ins>*Python*</ins>: After completing a Data Analytics course (*Google*), I used Python to collect, clean and analyse thousands of chess games by my favourite/ the most renowned chess players (Fischer, Kasparov, Carlsen, Nakamura, etc) in PGN format to reveal insights I was interested in - their 'favourite' piece to open with, their win and lose rate, if playing as white would make a measurable difference to their performance, which opening would most likely lead to their victory/loss, etc...
 - <ins>*HTML, CSS, Javascript*</ins>: learnt through freecodecamp, and have been recently learning *React* to create interactive and visually appealing websites (please see my [plan_my_week](https://github.com/brigidvincent/plan-your-week.git) project documenting my *React* learning journey). Web development has been super fun for me :)
 - <ins>*C# with Unity*</ins>: the most enjoyable foray I've had into tech - I created a small rocket blaster game. I'd love to return to this and create a more complicated narrative game...

---
### Useful info I've learnt so far

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

## Assignment 1 ##

Please see below for my workflow for this assignment :)

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

## Assignment 2 ##

For our API assignment, I think I picked a bit of a complicated route but stuck to it...

First I mapped out my initial ideas/workflow in comments with links to APIs I might use:

<img width="1139" height="392" alt="Screenshot 2026-08-16 at 23 22 43" src="https://github.com/user-attachments/assets/922281b7-4226-404f-9591-ee1bc5da3421" />

I decided I wanted to use a few APIs in my project to get the full hang of them, so decided to create a simple "last-minute" holiday planner...
 - <ins>*User preferences*</ins>: It would first ask the user their preferences on weather (Sunny and warm, or cold and snowy)
 - <ins>*Date of holiday*</ins>: The start date and the length of the holiday the user wants
 - <ins>*Result*</ins>: Then returns a "top 3" cities to visit - initially I was going to base this off the popularity of the location (see above screenshot), but decided instead to give a "weather score" (based off the temp and the 'sunniness'/'snowiness' of the location to make it more personalised towards the user.

I wanted to include multiple cities for each country to look through, but didn't know how to go about this without either spending too much time hand-picking a couple of cities for each country or importing a massive amount of data? (i.e. checking the weather for every city in the world) so I decided on just using [my countries API](https://countries.dev) to grab the capitals of each country (as well as the coordinates for [my weather API](https://open-meteo.com) to grab the weather forecast and historical weather data for extrapolating for dates past the forecast - max 16 days - but this is detailed more in the comments of the python code) and using those... I'd like to come back to this to flesh it out more when I know more about python/how to use it efficiently :)

I wrote out how I wanted my program to work in comments, replacing/deleting them (or condensing them to explain what I was doing) as i started to code out the actual program. please see below

<img width="971" height="503" alt="Screenshot 2026-08-16 at 23 24 13" src="https://github.com/user-attachments/assets/89b03782-e97a-4afc-b478-62d162e1b51d" />

I hope you enjoy using this as it took me a while! :) 
