# EpyToDo

## <img width="26px" src="https://newsroom.ionis-group.com/wp-content/uploads/2018/12/epitech-logo-signature-quadri.png"/> Epitech project :

Basic website interface in python with flask, using MySQL and an MVC architecture

---

### :globe_with_meridians: Web server :

• run.py : your entry program <br>
• __init__.py : your app package file <br>
• models.py : all objects / functions which will interact with your database <br>
• views.py : all routes which are described into the API file <br>
• controller.py : all interactions between your views and your models <br>
• config.py : all settings for your program (debug mode, database configuration, etc.) <br>

---

### :flower_playing_cards: HTML page :

• All data will transit into JSON format

---

### :pencil: MySQL database :

1. user table <br>
    • user_id (mandatory not null) <br>
    • username (mandatory not null) <br>
    • password (mandatory not null) <br>
    • etc.
  
<br>

2. task table <br>
    • task_id (mandatory not null) <br>
    • title (mandatory not null) <br>
    • begin (optional value when creating a task, current date by default) <br>
    • end (optional value when creating a task, empty by default) <br>
    • status (not started by default / in progress / done) <br>
    • etc.

<br>

3. user_has_task table <br>
    • fk_user_id <br>
    • fk_task_id

---

### :exclamation: Rule :
> Your server will implement a MVC architecture.

---

Made in Python with Flask
