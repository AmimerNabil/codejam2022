Hi, Welcome to the repository for our CodeJam 2022 project! 

CodeJam 2022 is the first hackathon experience for most of our team, and we are very excited to present our product *Save The Date*.

We have built and designed a fully functioning web app that allows students to upload their course syllabuses to a website that reads through the entire file while looking for important dates such as exams, presentations or assignments. Our website then creates spreadsheet containing all of the dates with the title of the work associated to it.
The website also implements a Google Calendar API in order to automatically add the exam/assignment dates on a calender.

In order to get the information from the course syllabus, we use the Amazon Textract API that can extract forms, tables, and plain text from .pdf files. Since our goal is to take note of submission and examination dates, we only extract data from tables.

### **INSPIRATION**
Whether you are a student in high school, CEGEP or university, it is very important to stay up to date with all the assigned tasks. During those caffeine-intensive exam sessions, it can be very easy to forget about a seemingly meaningless assignment. To stay ahead of the workload, many students use agendas to write down important dates. While it is very beneficial to do so, many students avoid agendas because of the time it takes to write down all the dates and to keep up with everything. Our goal for this project was to make the use of a planner as efficient as possible by automating the process of writing down evaluation dates.

### **WHAT IT DOES**
*Save The Date* is a website that makes the long and tedious task of organizing an agenda simple and efficient. The website contains a window where a user can drop a .pdf file that will be processed with the Amazon Textract API. The API we are using will read through the tables and extract all of the dates for submissions and exams. A python script will then use the tables extracted by the API and will parse through the table to get the name of the task (ex. Assignment, Midterm, Presentation, etc.) as well as the due dates for all of the tasks. The following step makes use of the calendar API from Google to export all the data onto an online calendar that makes organization simple and clear.

### **HOW WE BUILT IT**
The development process for our web application was done in many simultaneous steps. We split the workload into three major sections: the front-end, the dropbox for the files, and the rest of the backend. For the front-end, we used HTML 5 and CSS to create our webpage. The dropbox was made using Javascript as well as HTML 5 and CSS. The rest of the backend on the website is made up of Python scripts.

### **CHALLENGES WE RAN INTO**
The first design challenge was to write our program so that it can read and understand input from any kind of .pdf file layout. Some syllabi had additional information in their assignments/evaluations section. We adapted our code to only look for certain "trigger" words that allowed us to ignore the rest of the .pdf file.

The first major challenge we ran into during the development of our project was to match the data from the tables with the right assignments. Being able to keep the dates organized during all the intermediate steps was a very tedious task to make sure we extract the data that we want. To keep all the dates organized, we relied on the python script to get every date input and map it to the correct assignment and saving it.

Another big challenge in the information gathering step was that many files don't display the assignment information in the form of a table. This made the search for the information very difficult since we needed to go through each line of the document which made the runtime much longer than it would be if the program was only looking in tables. To solve this issue, we decided that with the limited time we have, we are limiting the use of the program to syllabi with tables.
