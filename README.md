# CWC Website Backend
**Deployed Host :** `cwciitk.herokuapp.com`
## API Endpoints
- `POST /api/createuser` : Endpoint to create user. <br>
 	Request Json :
	```js
	{
		"id" : userId,
		"pass" : password
	}
	```

- `POST /api/login` : Endpoint to login. <br>
 	Request Json :
	```js
	{
		"id" : userId,
		"pass" : password
	}
	```
- `POST /api/createpost` : Endpoint to create post. <br>
 	Request Json :
	```js
	{
		"club" : club,
		"title" : title,
		"content" : content
	}
	```
	Also, the user must be logged in.

- `POST /api/posts` : Endpoint to see posts. <br>


- `POST /api/session` : Endpoint to check session user. <br>

- `POST /api/deletepost?id=...` : Endpoint to delete post. <br>
- `POST /api/apply` : Endpoint to aply for volunteer. <br>
    Request Json :
	```js
	{
		"name" : name,
		"address" : address,
        "mobile" : mobile
	}
	```

- `GET /api/applicants` : Endpoint to see volunteer applications
