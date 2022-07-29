# Flask Backend for a Vehicle Repairs Blog
### **Built with:**
* Python 3.9.9
* psycopg2
* Flask-SQLAlchemy
* Flask-Migrate

This backend is built for an application where people can document their vehicle repairs and share their step-by-step procedures with the ability to add images for each step. They can also search for repairs that have been posted by other users. (*Work in progress. Not all routes finished.)
<br/>
<br/>
### **API routes completed thus far:**
<br/>

| auth              | users                                        |
|-------------------|----------------------------------------------|
| POST /auth/signup | DELETE /users                                |
| POST /auth/login  | PUT /users/email                             |
| POST /auth/logout | PUT /users/username                          |
|                   | GET /users/emails/{email}/is-available       |
|                   | GET /users/usernames/{username}/is-available |
