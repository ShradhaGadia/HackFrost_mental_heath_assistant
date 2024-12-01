import torch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from transformers import AutoModelForCausalLM, AutoTokenizer

# Define the path to the model and tokenizer
MODEL_PATH = r'C:\Users\astha\Downloads\mental_health_bot_trained'
TOKENIZER_PATH = r'C:\Users\astha\Downloads\mental_health_bot_trained'



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

def home(request):
    return render(request, 'home.html')  # Root URL template

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
