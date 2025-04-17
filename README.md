# AI Wedding Planner

A specialized AI wedding planning assistant built with Streamlit and OpenAI's GPT-3.5 model. This chatbot helps couples plan their perfect wedding by providing personalized advice, timelines, and recommendations.

## Features

- Wedding-specific planning interface
- Interactive wedding details sidebar
- Quick action buttons for common tasks
- Personalized advice based on wedding date, guest count, and budget
- Real-time chat functionality
- Persistent chat history during the session
- Powered by OpenAI's GPT-3.5 model
- Beautiful, wedding-themed UI

## Planning Capabilities

- Wedding timeline creation
- Budget planning and breakdowns
- Venue suggestions
- Theme and decoration ideas
- Vendor recommendations
- Guest list management
- Wedding checklist creation
- And much more!

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Setup

1. Clone this repository or download the files
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Application

1. Open a terminal in the project directory
2. Run the following command:
   ```bash
   streamlit run app.py
   ```
3. The application will open in your default web browser

## Usage

1. Enter your wedding details in the sidebar (date, guest count, budget)
2. Use the quick action buttons for common planning tasks
3. Type any wedding-related questions in the chat input
4. Get personalized advice and recommendations from the AI wedding planner

## Note

Make sure to keep your OpenAI API key secure and never share it publicly. The `.env` file is included in `.gitignore` to prevent accidental commits of sensitive information. 