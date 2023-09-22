:: This program starts the frontend, hopefully after the backend starts
cd layouts/layout-volu-europe
start "" http://localhost:3000/?backend=ws://localhost:8999
npm start