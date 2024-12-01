import torch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.shortcuts import render
from transformers import AutoModelForCausalLM, AutoTokenizer
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from transformers import pipeline


# Define the path to the model and tokenizer
MODEL_PATH = r'C:\Users\astha\Downloads\mental_health_bot_trained'
TOKENIZER_PATH = r'C:\Users\astha\Downloads\mental_health_bot_trained'

Quotes=["'Our wounds are often the openings into the best and most beautiful part of us.' — David Richo",
"'Talk to yourself like you would to someone you love.' — Brené Brown",
"'And still, I rise.'  —  Maya Angelou",
"'Happiness can be found even in the darkest of times, if one only remembers to turn on the light.' — Albus Dumbledore",
"It’s okay to fall apart sometimes. Tacos do, and we still love them.",
"If you’re going through hell, keep going—just don’t forget to hydrate.",
"'You, yourself, as much as anybody in the entire universe, deserve your love and affection.' — Buddha",
"'Even if we don’t have the power to choose where we come from, we can still choose where we go from there.' — Stephen Chbosky",
"'There is no standard normal. Normal is subjective. There are seven billion versions of normal on this planet.' — Matt Haig, Reasons to Stay Alive",
"'I am not afraid of storms for I am learning how to sail my ship.' – Louisa May Alcott",
"'You don’t have to control your thoughts. You just have to stop letting them control you.' — Dan Millman",
"' There is a crack in everything, that's how the light gets in' - Leonard Cohen",
"Go on easy yourself . Whatever you do today, let it be enough." ,
"Be kind to yourself. Remember, you’re doing the best you can.",
"'You may have to fight a battle more than once to win it.' - Ratan Tata",
"'The only journey is the journey within.' – Rainer Maria Rilke",
"Remember, self-care isn’t selfish. Unless it’s eating the last slice of pizza—then you’re just bold, and I respect that.",
"You’re allowed to scream, cry, or take a nap. Just don’t forget to keep going after that—champions recharge.",
"You are the plot twist that makes life interesting. Don’t forget how essential you are to the story.",
"You have survived every bad day, tough moment, and challenge so far. That makes you undefeated, my friend.",
"You bring light to the room without even trying. Seriously, it’s like you’re solar-powered.",
"'You are not your illness. You have a story to tell. You have a name, a history, a personality. Staying yourself is part of the battle.' – Julian Seifter",
"'Healing doesn’t mean the damage never existed. It means the damage no longer controls your life.' – Akshay Dubey",
"You are allowed to take up space. You are allowed to rest. You are allowed to just be.",
"The strongest people are not those who show strength in front of us but those who win battles we know nothing about.",
"You’re doing the best you can with what you’ve got, and that’s always enough.",
"Taking care of yourself doesn’t mean me first; it means me too.",
"'If you get tired, learn to rest, not to quit.' – Banksy",
"Sometimes, asking for help is the bravest move you can make. You don’t have to go it alone.",
]

chat_history=[]

def home(request):
    random_quote = random.choice(Quotes)
    return render(request, 'home.html',{'quote':random_quote})  # Root URL template


# Load the model and tokenizer once when the server starts
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True,
        torch_dtype=torch.float16
    )
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    if model.config.pad_token_id is None:
        model.config.pad_token_id = tokenizer.eos_token_id
    print("Model and tokenizer loaded successfully!")
    return model, tokenizer

# Load the model and tokenizer globally
model, tokenizer = load_model()


@csrf_exempt
def chat(request):
    """
    Endpoint to render the chat page and handle chat requests.
    """
    print("Chat endpoint hit!")  # Debugging log

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging log
            
            user_message = data.get("message", "").strip()
            chat_history.append(user_message)
            if not user_message:
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            print("User message:", user_message)  # Debugging log
            
            # Generate AI response
            ai_response = generate_ai_response(user_message, model, tokenizer)
            print("AI response:", ai_response)  # Debugging log
            
            return JsonResponse({"response": ai_response}, status=200)

        except Exception as e:
            print("Error occurred:", str(e))  # Debugging log
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    # Render the chatbot page if it's a GET request
    print("Rendering chatbot page.")  # Debugging log
    return render(request, 'index.html')


def generate_ai_response(user_message, model, tokenizer):
    """
    Generates AI response using the fine-tuned model.
    """
    try:
        print("Encoding input...")  # Debugging log
        inputs = tokenizer(user_message, return_tensors="pt", padding=True, truncation=True).to(model.device)
        print("Encoded input:", inputs)  # Debugging log

        # Generate response
        print("Generating response...")  # Debugging log
        output = model.generate(
            inputs["input_ids"],
            max_length=50,
            attention_mask=inputs["attention_mask"],  # Explicitly pass the attention mask
            num_return_sequences=1,
            do_sample=True,
            top_p=0.95,
            top_k=60,
            pad_token_id=tokenizer.eos_token_id
        )
        print("Generated output:", output)  # Debugging log

        # Decode the output and return
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print("Decoded response:", response)  # Debugging log
        return response

    except Exception as e:
        print("Error in generate_ai_response:", str(e))  # Debugging log
        return f"Error generating response: {str(e)}"


model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def analyze_sentiment(text):
    return sentiment_task(text)

def generate_mood_graph(chat_history):
    
    value = [analyze_sentiment(chat) for chat in chat_history]
    
    sns.set_theme(style="darkgrid", palette="muted")
    plt.figure(figsize=(10, 6))
    
    colors = []
    scores = []
    
    for sentiment_data in value:
        if sentiment_data[0]['label'] == 'negative':
            score = -1 * sentiment_data[0]['score']
        elif sentiment_data[0]['label'] == 'neutral':
            score = 0
        else:
            score = sentiment_data[0]['score']
        scores.append(score)
        if score > 0:
            colors.append('forestgreen')
        elif score == 0:
            colors.append('white')
        else:
            colors.append('firebrick')

    # Scatter plot for sentiment points
    for i, score in enumerate(scores):
        plt.scatter(i, score, color=colors[i], s=100, zorder=5)
    
    # Line plot to connect the points
    sns.lineplot(x=range(len(chat_history)), y=scores, marker='o', color='darkgray', linewidth=2.5, markersize=8)
    
    # Customize labels and title
    plt.title("Mood Graph Based on Sentiment Analysis", fontsize=16, fontweight='bold')
    plt.xlabel("Message Number", fontsize=14)
    plt.ylabel("Sentiment (Compound Score)", fontsize=14)
    
    plt.xticks(range(len(chat_history)), [f"{i+1}" for i in range(len(chat_history))], fontsize=12)
    
    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    
    plt.grid(True, linestyle='--', alpha=0.5)

    # Save the plot to a BytesIO object and encode it for the template
    buf = io.BytesIO()
    FigureCanvas(plt.gcf()).print_png(buf)
    graph_url = base64.b64encode(buf.getvalue()).decode('utf-8')

    plt.close()

    return graph_url

def mood_graph(request):
   
    # Replace this with your actual chat history from the chat
    # chat_history = ["Hello", "How are you?", "I'm feeling great!", "This is not good", "Okay, now it's better!"]

    # Generate the graph URL to display in the template
    graph_url = generate_mood_graph(chat_history)

    # Pass the graph URL to the template
    return render(request, 'mood_graph.html', {'graph_url': graph_url})



# Sample data: Activities and their corresponding steps

activities_data = {
    "Deep Breathing Exercises": [
        "Find a comfortable and quiet place to sit or lie down.",
        "Close your eyes and take a slow, deep breath in through your nose for a count of 4.",
        "Hold your breath for a count of 4.",
        "Slowly exhale through your mouth for a count of 6.",
        "Repeat this cycle for 5-10 minutes, focusing on the rhythm of your breath."
    ],
    "Meditation": [
        "Sit in a comfortable position with your back straight.",
        "Close your eyes and focus on your breathing.",
        "Allow your thoughts to come and go without judgment.",
        "If your mind wanders, gently bring your focus back to your breath.",
        "Continue for 5-15 minutes. Use a timer if needed."
    ],
    "Progressive Muscle Relaxation": [
        "Find a quiet space and sit or lie down comfortably.",
        "Start with your feet and tense the muscles for 5 seconds.",
        "Release the tension and notice the difference in sensation.",
        "Gradually move up through your body (calves, thighs, stomach, etc.) until you reach the top of your head.",
        "Repeat the process with each muscle group."
    ],
    "Walking in Nature": [
        "Choose a nearby park, forest, or quiet outdoor area.",
        "Walk at a comfortable pace and pay attention to your surroundings (trees, birds, fresh air).",
        "Breathe deeply and enjoy the movement of your body.",
        "Walk for 15-30 minutes, allowing yourself to disconnect from stressful thoughts."
    ],
    "Listening to Music": [
        "Create a playlist of calming songs that you love.",
        "Put on headphones or play the music through a speaker.",
        "Sit or lie back, close your eyes, and focus on the sounds and lyrics.",
        "Allow the music to uplift or soothe your mood."
    ],
    "Journaling": [
        "Grab a notebook or open a digital journaling app.",
        "Write about your thoughts and feelings without filtering yourself.",
        "Focus on writing for 5-10 minutes to release pent-up emotions.",
        "End by writing down a few things you are grateful for."
    ],
    "Mindful Coloring": [
        "Pick out a coloring book or print a coloring page online.",
        "Choose your favorite colored pencils or markers.",
        "Focus on each color and movement as you fill in the design.",
        "Take your time and enjoy the process, letting your mind relax."
    ],
    "Stretching or Yoga": [
        "Find a quiet spot and put on comfortable clothing.",
        "Start with simple stretches like reaching for your toes or doing gentle side bends.",
        "Practice yoga poses such as child's pose or cat-cow for a calming effect.",
        "Hold each pose for 5-10 seconds, breathing deeply and focusing on how your body feels."
    ],
    "Drinking Herbal Tea": [
        "Choose a calming herbal tea, such as chamomile or peppermint.",
        "Boil water and steep the tea for 5-7 minutes.",
        "Sit down in a cozy spot, sip the tea slowly, and focus on its warmth and flavors.",
        "Take deep sips and let the tea help you unwind."
    ],
    "Guided Visualization": [
        "Find a quiet place and sit or lie down.",
        "Close your eyes and take a few deep breaths.",
        "Picture a peaceful scene, like a beach or forest, in as much detail as possible.",
        "Imagine yourself there, feeling the environment around you.",
        "Stay with the visualization for 5-10 minutes."
    ]
}



def activities(request):
    return render(request, 'activities.html', {'activities': activities_data})
