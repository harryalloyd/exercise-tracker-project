This Python project tracks your exercises based on natural language input and logs the data in a spreadsheet using the Nutritionix and Sheety APIs. 
It processes exercise descriptions and records details such as the exercise name, duration, and calories burned.
e.g., "I ran 3 miles" or "I did 20 push-ups"

Tech Used:
Python
Nutritionix API (for exercise data)
Sheety API (for logging data)
Requests
dotenv (for securely storing sensitive information)

Clone this repository to your local machine
git clone https://github.com/harryalloyd/exercise-tracker-project.git
pip install -r requirements.txt

Create a .env file in the root of your project and add your API keys and credentials:
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
AUTHENTICATION=your_sheety_basic_auth_token



