### flasky-recipe

#### ingredients tried
1. flaks-rest-api with json request and response
2. flask support/integration with sqlalchemy (package: flask_sqlalchemy)
3. flask support with httpauth for username-password or token based authentication (package: flask_httpauth)
4. flask supprt for file-upload (package: flask_uploads)

###### P.S. I am using sqlite db for poc here which is used for user-management

#### how to taste this recipe
start flask api using following command
$ python api.py

your dish is ready - its time to attack

* Create user api

$ curl -i -X POST -H "Content-Type: application/json" -d '{"username":"python"}' http://127.0.0.1:5000/api/users

* Once user is created you can start passing username:password as basic httpauth params

$ curl -u kppatel:python -i -X GET http://127.0.0.1:5000/api/resource
note: without -u param in request - you will be getting 403

* Don't like username-password to send in request, you can get auth-token

$ curl -u eyJleHAiOjE0NTg4MDc4NzMsImlhdCI6MTQ1ODgwNzI3MywiYWxnIjoiSFMyNTYifQ.eyJpZCI6MX0.UIBgFXcM3nRqIFxYzxjRWkXOHQtsB9Iq_2hbXrSL530:pass -i http://127.0.0.1:5000/api/resource

* Its time to upload files

$ curl -i -u 'kunal:python' -X POST -F name=kppatel -F filedata=@1030.csv "http://localhost:5000/api/upload"
