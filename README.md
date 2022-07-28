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

auth endpoints| description|
-|-|
POST /auth/signup| Request body example<br/>```JSON{
    "email": "johnson@email.com",
	"username": "johnson",
	"password": "12345678"
}
```
