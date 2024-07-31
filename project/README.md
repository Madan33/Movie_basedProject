AK Movies - Movie Listing Website

**Overview**
AK Movies is a web application designed for listing, creating, editing, and deleting movies. It provides a user-friendly interface for managing movie information.

**Features**
List Movies: View a list of movies with title, summary, year, and optional image.
Search Movies: Search functionality to filter movies by title.
Create Movie: Add new movies to the database, including uploading an image.
Edit Movie: Modify existing movie details.
Delete Movie: Remove movies from the database with confirmation.

**Technologies Used**

Frontend: HTML, CSS, Bootstrap
Backend: Django (Python)
Database: SQLite (for development)
Deployment: Local development environment

**Setup Instructions**
Clone the repository:

**bash**
git clone https://github.com/your-username/ak-movies.git
cd ak-movies

**Install dependencies:**

pip install -r requirements.txt

**Run migrations:**
python manage.py migrate

**Create a superuser (admin):**

python manage.py createsuperuser

**Start the development server:**
python manage.py runserver

**Access the application:**
Open your web browser and go to http://localhost:8000/

**Usage**
Login: If not authenticated, access the signup or login page.
Navigation: Use the navigation bar to access different sections (List Movies, Create Movie, Logout).
Create, Edit, Delete: Manage movies through intuitive forms and actions.
Responsive Design: Ensure the website works well on different devices and screen sizes.

**Folder Structure**
/ak_movies: Main Django application folder.
/templates: HTML templates for pages like list.html, create.html, etc.
/static: Static files including CSS stylesheets and images.

**Credits**
Icons: FontAwesome (https://fontawesome.com/)
Color Palette: Inspired by Aqua themes for a clean and modern look.

**Contributing**
Feel free to fork this repository, suggest enhancements, and submit pull requests. Contributions are welcome!

**License**
This project is licensed under the MIT License - see the LICENSE file for details.
