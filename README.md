Full-Stack Intern Portal 🚀
A modern and responsive intern dashboard application built with a separate frontend (HTML, CSS, JavaScript) and a backend (Node.js with Express). This project demonstrates full-stack development skills, including API interaction, data management, and a user-friendly interface.

✨ Features
Frontend
Dummy Login Page: A simple login interface to access the dashboard (no actual authentication implemented).

Dynamic Dashboard: Displays intern's name, a unique referral code, and total donations raised.

Rewards/Unlockables Section: A static display of rewards.

Live Leaderboard: A dedicated page showing all interns ranked by their donations, updating in real-time when donations are simulated.

Responsive Design: Optimized for both desktop and mobile viewing.

Dark Mode Toggle: Allows users to switch between light and dark themes for better accessibility and aesthetics.

Custom Modals: User-friendly pop-up messages instead of browser alerts.

Backend
RESTful API: Built with Node.js and Express to serve data to the frontend.

Mock Data Storage: Uses a local data.json file to simulate a database, storing intern profiles and donation figures.

API Endpoints:

GET /api/intern-data: Retrieves all intern profiles.

GET /api/interns: Retrieves data for the leaderboard.

POST /api/simulate-donation: Updates an intern's donation amount in the data.json file.

🛠️ Technologies Used
Frontend
HTML5: Structure of the web pages.

CSS3: Styling and responsive design.

JavaScript (Vanilla JS): Frontend logic and API interactions.

Font Awesome: For icons.

Backend
Node.js: JavaScript runtime environment.

Express.js: Web application framework for Node.js, used to build the REST API.

cors: Node.js package for enabling Cross-Origin Resource Sharing.

fs (File System): Node.js built-in module for reading from and writing to the data.json file.

⚙️ Setup and Local Development
Follow these steps to get the project running on your local machine.

1. Clone the Repository
First, clone this GitHub repository to your local machine:

git clone https://github.com/sakshimdesai/full-stack-intern-portal.git
cd full-stack-intern-portal

2. Backend Setup
The backend handles the API and data storage.

Navigate to the backend directory:

cd backend

Install dependencies:

npm install

Start the backend server:

node server.js

The server will start on http://localhost:3000. Keep this terminal window open.

3. Frontend Setup
The frontend provides the user interface.

Navigate back to the project root, then into the frontend directory:

cd ../frontend

Open index.html:
Simply open the index.html file in your web browser. You can do this by double-clicking it, or by using a "Live Server" extension in your code editor (recommended for development).

💡 How it Works
The frontend makes HTTP requests to the backend to fetch and update intern data.

The backend reads from and writes to the data.json file to persist changes (e.g., when a donation is simulated).

The leaderboard and individual intern data update dynamically as donations are added.

📸 Screenshots
 <img width="1910" height="929" alt="image" src="https://github.com/user-attachments/assets/e3dfac42-a4e7-4f79-9797-35acc2d1968f" />
 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e5f22574-8087-468f-a322-90ce3e9d42a7" />
 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a818d92f-e5ac-4e56-adc5-ec9a3c718942" />
 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d5105a4c-48c0-4afe-81fe-059c0b9d48a4" />
 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/99f0e899-0fd2-4803-b0dc-e2a690103045" />


Login Page
Dashboard View
Leaderboard View
Dark Mode
🤝 Contribution
Feel free to fork this repository, submit pull requests, or open issues if you have suggestions or find bugs.
