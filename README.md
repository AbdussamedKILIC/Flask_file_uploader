# Flask-File-upload-server

Simple Flask and MongoDB file upload server with authentication

## Step 1. install packages from packages.txt

`pip install <package name>`

## Step 2. change db connection in db.py

change connection string and database name and collection name

### Application have 6 end points

- /
  for serve static files
- /home
  for test server connection
- /signin
  for authinticate user
- /signup
  for register new user
- /upload
  for upload picture
- /files/:filename
  for serve uploaded pictures

## Best Luck.
