# TelegramBot Design Document

This document outlines the design of a Telegram Bot that sends a random image of an animal every day, along with related information such as its region, area, and year. The bot will be developed using the Python Telegram Bot library and integrates with the `ImageScrappingService` API.

## Main Components

### 1. **Bot Setup and Configuration**

   - **Description**: This component involves setting up the bot and configuring its initial settings, including the connection to the Telegram API, bot token, and basic command handlers.
   - **Tasks**:
     - Set up the bot using the Python Telegram Bot library.
     - Store the bot token securely (e.g., using environment variables).
     - Implement basic command handlers (`/start`, `/help`).
     - Ensure proper error handling and logging for debugging.
   - **Responsibilities**:
     - Configure the bot token and connection to Telegram's servers.
     - Implement command handlers for starting and stopping the bot.
     - Integrate with the ImageScrappingService API to fetch random images.

### 2. **Daily Image Scheduler**

   - **Description**: This component is responsible for scheduling the daily task that sends a random animal image to users at a specified time.
   - **Tasks**:
     - Implement a scheduling mechanism using either `Celery` or a simple cron command to trigger the daily image sending function.
     - Ensure the scheduler runs consistently and handles time zones appropriately.
   - **Responsibilities**:
     - Set up a daily task that retrieves a random image and sends it to all users.
     - Handle potential errors, such as missed executions or API timeouts.

### 3. **Image Retrieval and Information Formatting**

   - **Description**: This component handles the retrieval of random images and their associated information from the `ImageScrappingService` API. It also formats the data for presentation in Telegram.
   - **Tasks**:
     - Integrate with the `/random` endpoint of the `ImageScrappingService` API.
     - Format the image and information (e.g., species, region, area, year) into a user-friendly message.
   - **Responsibilities**:
     - Fetch random images and their metadata using the API.
     - Format the data into a readable format that can be sent as a message with the image in Telegram.
     - Ensure the information is clear and concise for users.

### 4. **User Management (Optional)**

   - **Description**: This component manages user interactions, including subscribing to or unsubscribing from daily image notifications.
   - **Tasks**:
     - Implement user registration and subscription handling.
     - Store user data (e.g., chat IDs) securely for sending scheduled messages.
     - Implement commands like `/subscribe` and `/unsubscribe`.
   - **Responsibilities**:
     - Manage user subscriptions for daily image notifications.
     - Maintain a database or in-memory store of subscribed users.
     - Handle edge cases, such as users stopping the bot or blocking it.

### 5. **Deployment and Monitoring**

   - **Description**: This component involves deploying the bot to a server and setting up monitoring to ensure it runs smoothly.
   - **Tasks**:
     - Deploy the bot to a cloud server (e.g., AWS, Heroku, or a VPS).
     - Set up logging and monitoring to track bot performance and errors.
     - Implement automated restarts in case of failures.
   - **Responsibilities**:
     - Ensure the bot is deployed and running in a production environment.
     - Maintain logs for troubleshooting and analytics.
