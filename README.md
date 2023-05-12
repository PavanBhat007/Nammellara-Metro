# **Nammellara-Metro** : A surface level implmentation of a basic path-finding algorithm with UI

A team of 3 students, **Nuthan**, **Amith Kumar** and myself, worked on this project as a submission for an event called **Protothon** in which the theme we chose was *mobility*.
We chose to implement a software that finds least costly path using a path-finding algorithm based on a Namma Metro map, designed as a graph with each metro station being a node in that graph. The algotrithm uses *Djikstra's* path-finding algorithm.

Our project consists of,
- A login / signup page to login or register
- A profile page to view logged in user's profile.
  - Here the user's details like name, age, credits and any passes they have are shown.
- A history page to view part travels and their prices
  - This page shows a detailed view of their travels including departure station, destination station and cost of that travel ticket.
- A wallet page to view past transactions and current credits in user's account
  - This page is similar to the history page, but is mainly focused on credits where only the credits spent is shown and the credits available in the account is shown.
- A map page to view the Namma Metro map on which our algorithm is based
- A buy tickets page to purchase tickets where the user enters their desired station to travel to and the station they are currently at.
  - The user enters the departure and destinantion station and click the "Buy ticket" button upon which the lowest cost for that travel is shown and that entry is added to the database.

We have used,
- **Djikstra's algorithm** for path-finding to find the shortest path and calculate the lowest cost. Here we could'nt find any databases with all the metro stations and their costs, so we have created our own database where cost to travel from one station to the next station is taken as 8 credits.
- **HTML, CSS** for front-end web design
- **Flask** Python framework for back-end. Along with Flask, we have used **SQLite3** as our database software.
- Some images on the site were taken directly from Google search and the Namma Metro website also, but most of them were pictures taken by one of the three team members.

Also, we have coded on the official **CS50 IDE** because of it has Flask and SQLite3 pre-installed on it, which made it more simple for us to code and manage the database.

**NOTE: Source code files are avilable inside the Ubuntu folder**
