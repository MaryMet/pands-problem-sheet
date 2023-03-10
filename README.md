# **Pands Problem Sheet**

## **Introduction**

This readme file is a decriptor of weekly tasks assigned to us in order to practice learning in the Module - Programming and Scripting. The Programming and scripting module form part of the higher diploma in Data Analytics from the Atlantic Technological University - ATU.

In this readme file I will explain the aim of the weekly tasks that were assigned. I will explain how I came to write the programs I uploaded. I will also explain my thought processes behind the programmes and I will identify what websites or resources gave me inspiration.

## **Table of Contents** 
* [Weekly Tasks](#weekly-tasks)
    * [Week 1 helloworld](helloworld.py)
    Setting up the environment.
    * [Week 2 bank](bank.py)
    Statements. 
    * [Week 3 accounts](accounts.py)
      [Week 3 extra](accountsextra2.py)
    Variables - Bank Security Number Task accounts.py 
    * [Week 4 collatz](collatz.py)
      [Week 4.2](collatz2.py)
    Controlling the Flow   
    * [Week 5 weekday](Weekday.py)
    Data. 
    * [Week 6 Squareroot](sroot.py)(Sqrt.py)
    

### **Week 1** - Hello World Task

There was a number of tasks in Week1. I introduced myself in the discussion forum. I created my environment by following the instuctions in the lectures. I have always had an interest in computing but more from a gaming and communication aspect. I found setting up the environment a challange due to my lack of knowlege about computing vocabulary. I installed the software as instructed - visual basic, commander, python and set up an account on Github.
I than wrote by first programme. This was a very basic programme and was solution were easily found on [w3schools.com](https://w3schools.com).
What challanged me mostly this week was learning the add, commit, and push commands to Github. It took some brainpower to figure out how to push to the pands problem sheet.
This week I also completed practice on tutorials in [w3schools.com](https://w3schools.com) to become more familiar with basics. I pushed these to mywork on Git hub.

### Week 2 - Bank.py

Week 2 task asked to write a programme titled bank.py. The objective of the programme was to prompt the user to enter two amounts of money -in cents. It must the complete the addition and display the answer in euros and cents.
I again consulted with [w3schools.com](https://w3schools.com) and with the lectures this week. I also looked at some examples of programs in [stackoverflow.com](http://stackoverflow.com) 
It took be some effort because I lacked any real understanding of syntax at this point. I wote a very basic prgramme and needed to correct many spaces, commas, colons and brackets before I got it to work.
I have no been able to figure out yet how to put in the intial amounts in cents only. The programme only works if the amount is enter a decimal number.
I used the float function to create this programme.

### Week 3 - Accounts.py

Week 3 task concentrated on Bank Account numbers and security. The objective of the task was to prompt the user to enter a ten digit number. The programme would than format the number to only show the last four digits. The first six digits were to be replaced by XXXXXX.
I again consulted with the lectures of this week. I referred back to the labs of the week taking some inspiration from the. I researched on [w3schools.com](https://w3schools.com). I also gor some inspiration from [stackoverflow.com](http://stackoverflow.com) and [digitalocean.com](https://digitalocean.com). I found the last two websites inspirational in that it lead me to the function len - to count the numbers of numbers. I found the code on these websites too advanced to use in my program. it was difficult for a beginner to read/comprehend. Once I though about len and its application I went back to w3schools - here I managed to put together a basic programme which completes the task above. 
Counting the number of numbers and "slicing" to achieve my results.
I also made 2 attempts at the extra part of this programme. I struggled to find a way to change all number except for the last four in this programme. Other attempts saved under [accountextra](accountextra.py) and [accountextra2](accountsextra2.py)

### Week 04 - Collatz.py
This week we needed to write a programme that complete teh COLLATZ maths phenomena.
At the beginning of this I was absolutley flummoxed - I went to all google pages as above  [stackoverflow.com](http://stackoverflow.com) and [digitalocean.com](https://digitalocean.com) I could not interpret what they were doing 
 As this week we covered while and for loops - if and elses and eilifs. I spent hours trying to use them to reflect my thoughts ie if even divide by 2. If odd multiply by 3 and add one. 
I got a number of the dreaded infinty loops.
Eventually I saw a mention of the collatz function on stackoverflow.
I did my research on this function in [w3schools.com](https://w3schools.com) and this knowledge utterly simplified my code. Please see my two versions of collatz.py. Both versions work though my favourite is collatz.py as it is more explanatory

### Week 05 
I really struggled this week. Initally I was imagining a very complex mathematical solution and indeed when I looked at my trusted sites above the code appeared very complex. The programmer were assigning digits to weekdays 0 - 7 and writing complex codes.
I learned my lesson from last week and quickly visited the trusted site [w3schools.com](https://w3schools.com) and there I foud the datetime function. I imported same.
Initally my programme only printed out the days for me - I used some of the lab exercises we completed this week to assist me. I could get it to print all the days and their associated weekday or weekend but I cant get it it to just print todays day and whether its a week day or weekend
After I made a number of attempts with different methods I achieved success by using - for and in. The in part reflected that it is only today that we needed printed.
I have left in my other attempts and turned it into comments for you to see

### Week 06
Newtonian method of getting a square root is an algorithim which produces successively better approximations of the square root of a number (or an equation)
The main resource I turned to this week was youtube
I looked at, understood and followed a video called The last minute professor. It did not work for me. It descibed the programme in very little details - no mention of what type of loop or iteration was used.
I consulted with  [stackoverflow.com](http://stackoverflow.com) and [digitalocean.com](https://digitalocean.com) but I , again, could not interpret what they were doing. [tutorialsinhand](http:tutorialinhand.com) - I understood and copied this. It work but I didn't like its simplistic printing. And there was no code to enter any number - it only worked on 10
I completed what I could and it does work to some degree - though I would like to know how to repeat the steps a number of times to get a more accurate answer.
I re read the assignment and released that I was going down the wrong path to def a function
Rewite sqrt.py - I used a tutorial from [andreamarino](https://andreamarino.it) to assist me. And I personalised same.
I than made a new file called sroot which reflects my thoughts on the task - use it for any numebr and complete the function on ten occasions to get a very accurate approximation of the square root of the number entered.

