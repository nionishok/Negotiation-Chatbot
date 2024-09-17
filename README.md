# Negotiation Chatbot API

## Description
This project implements a negotiation chatbot API using **FastAPI** and **OpenAI's GPT (e.g., ChatGPT)** to simulate a negotiation process between a customer and a supplier. The chatbot allows the customer to propose a price, and the bot, using negotiation logic and AI responses, either accepts, rejects, or counters the offer.

The project is designed to work as a backend service, exposing RESTful API endpoints for initiating negotiations and offering prices. Optional features like sentiment analysis can enhance the negotiation process based on user behavior.

---

## Features
- **AI-Powered Negotiation**: Utilizes OpenAI’s GPT model to simulate natural conversations during negotiation.
- **Dynamic Pricing Logic**: The chatbot adjusts its offers based on user inputs.
- **Counteroffers and Discounts**: Based on the offer and sentiment, the bot can propose counteroffers or discounts.
- **Optional Sentiment Analysis**: The chatbot can adjust its responses based on the politeness or tone of the user’s input.

---

## Technology Stack
- **FastAPI**: Python web framework for building APIs.
- **OpenAI API**: To integrate GPT-based conversational AI.
- **Python**: Programming language used for backend development.
- **Uvicorn**: ASGI server to run FastAPI applications.
- **Docker**: (Optional) For containerization and easy deployment.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **Git** (for version control)
- **Pip** (for Python package management)
- **Postman** or any API testing tool (optional but useful)
- **OpenAI API key** (you’ll need to set this up for the AI integration)

---

## Installation Instructions

### Step 1: Clone the Repository
Start by cloning the project to your local machine:

```bash
git clone https://github.com/nionishok/Negotiation-Chatbot
cd negotiation-chatbot
