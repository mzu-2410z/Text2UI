# %%writefile ui_generator.py
import os
import openai
import streamlit as st
from dotenv import load_dotenv # Import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()

# --- OpenRouter API Configuration ---
# The API key is now loaded from the environment variable OPENROUTER_API_KEY
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Configure the OpenAI client to use the OpenRouter API endpoint
client = openai.OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# Basic check to ensure the API key is loaded
if not OPENROUTER_API_KEY:
    st.error("OpenRouter API key not found. Please set the OPENROUTER_API_KEY environment variable or in your .env file.")
    st.stop() # Stop the Streamlit app if the key is missing

# Configure the OpenAI client to use the OpenRouter API endpoint
client = openai.OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# --- UI Generation Function ---
def generate_ui(prompt):
    """
    Generates a complete HTML page with Tailwind CSS based on a user prompt
    using the Meta Llama 3.1 405B Instruct model from OpenRouter.
    """
    try:
        response = client.chat.completions.create(
            
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Senior Frontend Engineer. Your task is to generate a single, professional-grade, "
                        "and visually stunning HTML page. Your code MUST use **Tailwind CSS** for all styling. "
                        "The entire response MUST be the complete code for a single file, with all styling handled "
                        "by Tailwind utility classes. Do NOT write any CSS in a `<style>` tag.\n\n"
                        
                        "Strict Requirements:\n"
                        "1.  **Tailwind Integration**: Always include the Tailwind CSS CDN link in the `<head>` section: "
                        "`<script src='https://cdn.tailwindcss.com'></script>`. "
                        "2.  **HTML Structure**: Use modern HTML5 semantic tags like `<header>`, `<nav>`, `<main>`, `<section>`, and `<footer>`. "
                        "3.  **Tailwind Classes Only**: All styling, including layout, colors, typography, and responsiveness, must be applied directly to HTML elements using Tailwind CSS utility classes (e.g., `flex`, `bg-blue-500`, `text-lg`). "
                        "4.  **Responsiveness**: Use Tailwind's responsive prefixes (e.g., `sm:`, `md:`, `lg:`) to ensure the design adapts gracefully to different screen sizes. All designs must be mobile-first. "
                        "5.  **Dynamic Components**: Design and style a hero section with a clear Call-to-Action (CTA), visually appealing cards or feature blocks, and a comprehensive footer with links and social media icons. "
                        "6.  **External Assets**: If the design requires icons, always include the Font Awesome CDN link in the `<head>` section. The link for Font Awesome is `<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'>`. "
                        "7.  **JavaScript Interactivity**: If the prompt implies interactivity (e.g., a \"dropdown menu\" or \"accordion\"), generate the necessary JavaScript within a `<script>` tag at the end of the `<body>`. Otherwise, include a simple, well-commented JavaScript snippet for a 'fade-in on scroll' effect to demonstrate professionalism. "
                        "8.  **Output Integrity**: The final output must be a single, complete HTML document. Do not truncate the code. Do not add any text or explanations outside of the document structure. Your ENTIRE response MUST be the code, and nothing else. Begin your response with `<!DOCTYPE html>`."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=8192,
            timeout=60.0
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        # This block will catch specific API errors from OpenRouter
        st.error(f"OpenRouter API Error: {e.status_code} - {e.response}")
        return None
    except Exception as e:
        # This block catches other unexpected errors
        st.error(f"An unexpected error occurred: {e}")
        return None