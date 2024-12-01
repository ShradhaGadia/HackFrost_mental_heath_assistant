
# **Therapy AI App**

**Therapy AI** is a web application designed to assist users with their mental health through daily reflections, mood tracking, task management, and personalized interactions with an AI-powered therapist. It creates a supportive and calming environment for users to improve their well-being.

## **Features**

- **Daily Thought**: A new, motivational thought appears every time a user visits the app, encouraging reflection.
- **Chat with AI**: Users can interact with an AI therapist, which offers empathetic and supportive responses.
- **Task Management**: Organize and manage daily tasks to reduce stress and improve productivity.
- **Mood Tracking**: Visualize mood patterns over time with a mood graph.
- **Soft Vibes Interface**: A calming, intuitive user interface designed for relaxation.

## **Tech Stack**

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Node.js (MERN Stack)
- **AI**: Python, Hugging Face (Transformers models)
- **Database**: MongoDB
- **Deployment**: Cloud-based (Heroku, AWS, or local deployment)

## **Getting Started**

### 1. Clone the repository

```bash
git clone https://github.com/your-username/therapy-ai-app.git
cd therapy-ai-app
```

### 2. Install dependencies

Make sure you have **Node.js** and **MongoDB** installed. Then install the necessary dependencies:

```bash
npm install
```

### 3. Run the app locally

Start the app locally:

```bash
npm start
```

The app will be available at `http://localhost:3000`.

### 4. Python environment setup (for AI therapist)

Make sure you have Python 3.x installed and then install the required libraries:

```bash
pip install transformers torch
```

### 5. Configure MongoDB

Ensure your MongoDB instance is running. Update the connection string in the app's config file.

### 6. Deployment

To deploy to production, follow the deployment guide for platforms like Heroku or AWS. Configure environment variables and install dependencies as per the respective documentation.

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
- **Node.js & Express**: For backend development.

