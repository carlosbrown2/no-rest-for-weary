# no-rest-for-weary
Keep a free tier heroku app from sleeping

Assumptions
- You have Chrome browser installed on your machine
- You have a recent python 3 release

Steps
1. Clone the repo to your environment
2. Create a virtual environment
    ```python
    python -m venv env
    ```
3. Install req's
    ```python
    pip install -r requirements.txt
    ```
4. Edit the virtual environment activation script location in workflow.sh 
5. Edit the url in browser.get(...) within bot.py. This should be the url of your heroku app
6. If not on a Mac OS, modify the workflow.sh script as needed for your OS
7. Add the workflow.sh script to crontab or systemd depending