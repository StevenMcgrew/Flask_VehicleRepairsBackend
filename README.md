# Flask Backend for a Vehicle Repairs Blog

[![Linkedin Badge](https://img.shields.io/badge/-Steven_McGrew-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/steven-mcgrew/)

<br/>

### **Languages and Tools:**

<div>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original.svg" alt="Python" width="60"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/flask/flask-original.svg" alt="Flask" width="60"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/sqlalchemy/sqlalchemy-original.svg" alt="SQLAlchemy" width="60"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" width="60"/>
  <img src="" alt="" width="60"/>&nbsp;
</div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Flask &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SQLAlchemy &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PostgreSQL
<br/>
<br/>

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

<br/>
<br/>


### **PostgreSQL Database:**
<br/>
<img src="https://github.com/StevenMcgrew/Flask_VehicleRepairsBackend/blob/master/ERD_vehicle_repairs.png?raw=true" />

