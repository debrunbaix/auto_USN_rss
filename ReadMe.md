# Ubuntu Security Notice RSS Reader

This project provides a simple script for monitoring and sending email notifications about the latest security notices from Ubuntu. The script periodically checks the Ubuntu Security Notices RSS feed and sends an email containing new articles.

## Usage

### Configuring Email Settings

To enable email notifications in the script, you need to create a `config.ini` file with the necessary email configuration. Below are the steps to set up and use the `config.ini` file.

1. Create `config.ini`

Create a file named `config.ini` in the same directory as your script (`main.py`). Use the following structure for the configuration:

```ini
[Mail_Info]
my_mail = email1@example.com, email2@example.com, email3@example.com

[Mail_Config]
SMTP_SERVER = SMTP_SERVER
SMTP_PORT = PORT
GMAIL_USERNAME = MAIL
GMAIL_PASSWORD = PASS
```

Replace the placeholder values with your actual email addresses and Gmail credentials.

### With Docker

1. Make sure you have Docker installed on your system.

2. Clone the repository:

   ```bash
   git clone git@github.com:Igaemas/auto_USN_rss.git
   ```

3. Navigate to the project directory:

   ```bash
   cd auto_USN_rss
   ```

4. Build the Docker image:

   ```bash
   docker-compose up --build -d
   ```

   This will build the Docker image using the provided Dockerfile.

5. Check the logs to monitor the script's activity:

   ```bash
   docker-compose logs -f
   ```

   You should see output indicating whether new articles are being detected and emails are being sent.

### Without Docker

1. Make sure you have Python 3 installed on your system.

2. Clone the repository:

   ```bash
   git clone git@github.com:Igaemas/auto_USN_rss.git 
   ```

3. Navigate to the project directory:

   ```bash
   cd auto_USN_rss
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirement.txt
   ```

5. Run the script:

   ```bash
   python main.py
   ```

   The script will start checking for new articles and, if found, send email notifications.

## Configuration

You can customize the script's behavior by modifying the `*.py` file. For example, you may adjust the RSS feed URL.