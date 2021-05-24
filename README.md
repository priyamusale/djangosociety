# Django Mini Project 1
## Django Society 2021
### Homepage
Homepage of the website can be accessed on:
[Django Society 2021](http://localhost:8000/society/)
This page displays and describes my project.
This society is a group of entry-level and experienced developers who are interested in learning Django.
The three buttons on the bottom display a list of all the events, all the groups, and all the people respectively once clicked.

---
### Events page
If the events button is clicked on the homepage, this page is shown. This page can also be accessed by the link: [Events](http://localhost:8000/society/events/)
It shows the number of events and displays a list of all the events in the society with their titles.
To learn more about a particular event, click on it.
The "Go Back" button on the bottom of the page will redirect back to the homepage.

### Event detail page
Once a specific event is clicked, this page appears. It will show a detailed page with the title on top, the start and end time, the location, description, and details of the event.
A specific event can also be accessed with the event ID with the link: [Event](http://localhost:8000/society/events/<event_id>/)
The "Go Back" button on this page redirects to the events page with a list of all events.

---
### Groups page
Similar to the events page, this page displays the number of groups and lists them with their titles. This page can be accessed by clicking on the Groups button on the homepage or by the link: [Groups](http://localhost:8000/society/groups/)
The "Go Back" button on this page will take you back to the homepage of the project.

### Group detail page
By clicking on a group on the groups page, a detailed page with the title of the group, the category, URL of the group, group description, and a list of group members is displayed. Details of the group can also be accessed with the group ID with the link: [Group](http://localhost:8000/society/groups/<group_id>/)
To "Go Back" to the Groups page to look at the list of all groups click the "Go Back" button.

---
### People page
The people page can be accessed by the link [People](http://localhost:8000/society/people/) or by clicking on the People button on the homepage.
Like the events and group page, this page diplays the number of people and lists them with their first and last name. The "Go Back" button will take you back to the homepage. To know more about someone, click on their name.

### Person page
This page shows the first name and last name of the person, their birth date, username, about them, their favorite movies, and a their URL.
This information can be accessed either by clicking on the person from the list of people or by using people ID with the link: [Person](http://localhost:8000/society/people/<people_id>/)
To go back to the groups page, click on the "Go Back" button.