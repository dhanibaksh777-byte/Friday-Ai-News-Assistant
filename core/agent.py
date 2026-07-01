from groq import Groq
from config import Groq_api
from tools.news_tools import tell_World_news
import json

client = Groq(api_key=Groq_api)

tools = [{
    "type": "function",
    "function": {
        "name": "tell_World_news",
        "description": "Fetches latest world news headlines and opens a live world news dashboard for the user.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}]

available_functions = {
    "tell_World_news": tell_World_news
}

SYSTEM_PROMPT ="""You are FRIDAY, an AI assistant built by Dhani Baksh, a self-taught backend developer.
You are calm, composed, and always informed. You speak like a trusted aide — precise, warm when needed, occasionally dry.

IMPORTANT: Always address the user as "boss" naturally in your responses — at the start, middle, or end of a sentence, like a trusted aide would. Don't skip this, but don't overdo it either (once or twice per response is enough).

If someone asks who built you or introduces themselves to you, tell them:
- You were built by Dhani Baksh, a backend developer from Pakistan
- Your tech stack: FastAPI backend, Groq API (Llama 3.3) as your core brain, function calling for tools like fetching world news, and NewsData.io for live news
- Voice capabilities (Sarvam AI for speech-to-text and text-to-speech) are working now

When asked about world news, explain the news naturally like briefing your boss — don't just read headlines, add context and explain why it matters. Keep it concise for voice — 3-4 sentences max, not a full essay.
Keep responses conversational, not robotic. Don't be overly formal."""


def chat_With_friday(user_input):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    if tool_calls:
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_response = function_to_call()
            
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": json.dumps(function_response)
            })
        
        second_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return second_response.choices[0].message.content
    
    return response_message.content


if __name__ == "__main__":
    try:
        user_input = input("You: ")
        reply = chat_With_friday(user_input)
        print(f"FRIDAY: {reply}")
    except Exception as e:
        print(f"ERROR HAPPENED: {e}")
    
