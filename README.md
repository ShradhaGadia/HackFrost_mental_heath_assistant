
# **Therapy AI App**

**Therapy AI** is a web application designed to assist users with their mental health through daily reflections, mood tracking, task management, and personalized interactions with an AI-powered therapist. It creates a supportive and calming environment for users to improve their well-being.

## **Features**

- **Daily Thought**: A new, motivational thought appears every time a user visits the app, encouraging reflection.
- **Chat with AI**: Users can interact with an AI therapist, which offers empathetic and supportive responses.
- **Task Management**: Organize and manage daily tasks to reduce stress and improve productivity.
- **Mood Tracking**: Visualize mood patterns over time with a mood graph.
- **Soft Vibes Interface**: A calming, intuitive user interface designed for relaxation.

## **Tech Stack**
**Frontend**: HTML, CSS, Bootstrap
**Backend**: Django (Python)
**A**I: Hugging Face Transformers models
**Task Management**: Task organization and tracking features
**Mood Tracking**: Graph-based visualization of mood patterns

## **Getting Started**

Here’s a more concise version of the **README** for your Therapy AI app:

---

# **Therapy AI App**

**Therapy AI** is a web application to help users improve their mental health. It offers daily reflections, mood tracking, task management, and personalized chats with an AI therapist. The app is designed to create a calming and supportive environment for users.

## **Features**

- **Daily Thought**: Motivational thoughts appear on each visit to encourage mindfulness.
- **Chat with AI**: Interact with an empathetic AI therapist for personalized support.
- **Task Management**: Organize tasks to reduce stress and stay productive.
- **Mood Tracking**: Visualize your mood over time with a mood graph.
- **Soft Vibes Interface**: A soothing design with a calming layout for relaxation.

## **Tech Stack**

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Python)
- **AI**: Hugging Face Transformers models
- **Task Management**: Task organization and tracking features
- **Mood Tracking**: Graph-based visualization of mood patterns

## **Installation**

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/therapy-ai-app.git
   cd therapy-ai-app
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to view the app.

## **Kestra Integration**

Use **Kestra** for task automation (e.g., sending reminders or processing background tasks). Install the Kestra Python client and interact with the Kestra API to automate workflows.

## **Usage**

- **Home Page**: Displays a daily thought and options to:
  - **Chat with AI**: Interact with the AI therapist.
  - **View Tasks**: Manage and track your tasks.
  - **View Mood Graph**: Track and visualize your mood.

- **Chat with AI**: The AI therapist provides empathetic and supportive responses to help users reflect on their thoughts and emotions.
- **Tasks**: Add, manage, and complete daily tasks to help stay organized and reduce stress.
- **Mood Graph**: Track and visualize emotional patterns over time.

## **Contributing**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the changes to your branch (`git push origin feature-name`).
5. Submit a pull request.

## **Acknowledgments**

- **Hugging Face**: For providing transformer models for AI therapy.
- **Bootstrap**: For the responsive design framework.

