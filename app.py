import random
import os
from dotenv import load_dotenv
import google.generativeai as genai
from ui import create_stylish_interface, UI_CONFIG
from PIL import Image
import io

load_dotenv()

# --- Set your Gemini API Key here ---
api_key = os.getenv("GEMINI_API_KEY")
print("✅ Loaded API Key:", api_key[:6] + "..." if api_key else "❌ Not found")

# Error handling for missing API key
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

genai.configure(api_key=api_key)

# --- Gemini Model (use the Flash version for faster and cheaper results) ---
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_text_from_prompt(prompt, platform):
    """
    Generate social media content using Gemini AI from text prompt
    
    Args:
        prompt (str): The theme or keyword for content generation
        platform (str): Target social media platform
        
    Returns:
        tuple: (caption, emojis, hashtags)
    """
    # Input validation
    if not prompt or not prompt.strip():
        return "Please enter a valid keyword or theme.", "", ""
    
    if not platform:
        return "Please select a platform.", "", ""
    
    full_prompt = (
        f"You are an expert social media writer. Create a high-quality post for **{platform}** based on the theme: '{prompt}'.\n\n"
        f"Your output should be formatted as:\n"
        f"Caption: (Write 2 to 4 complete sentences. Use a tone suitable for {platform}. For example: "
        f"Instagram is casual and expressive, LinkedIn is professional and inspiring, Twitter is witty and concise. Do NOT include emojis or hashtags here.)\n"
        f"Emojis: (List 3 to 5 relevant emojis that match the tone. Use sparingly for LinkedIn.)\n"
        f"Hashtags: (Provide 5 to 8 popular and relevant hashtags for {platform}. Keep them professional for LinkedIn, trendy for Instagram, and brief for Twitter.)\n\n"
        f"Example:\n"
        f"Caption: Just touched down in paradise! The waves are crashing, the sun is shining, and I can't wait to soak it all in. This place is pure magic. Grateful for every moment.\n"
        f"Emojis: 🌴 🌞 🏖️ ✨ 💫\n"
        f"Hashtags: #BeachVibes #Wanderlust #TravelGoals #GoaDays #VacationMode #SunAndSand #GratefulHeart\n\n"
        f"Now generate your response:"
    )

    try:
        response = model.generate_content(full_prompt)
        return parse_response(response.text.strip())
    
    except Exception as e:
        error_msg = f"Error generating content: {str(e)}"
        print(f"❌ {error_msg}")
        return error_msg, "", ""

def generate_text_from_image(image, platform, additional_context=""):
    """
    Generate social media content using Gemini AI from uploaded image
    
    Args:
        image: PIL Image object or image path
        platform (str): Target social media platform
        additional_context (str): Optional additional context or theme
        
    Returns:
        tuple: (caption, emojis, hashtags)
    """
    if image is None:
        return "Please upload an image.", "", ""
    
    if not platform:
        return "Please select a platform.", "", ""
    
    # Context addition
    context_part = f" and consider this additional context: '{additional_context}'" if additional_context.strip() else ""
    
    full_prompt = (
        f"You are an expert social media writer. Analyze this image and create a high-quality post for **{platform}**{context_part}.\n\n"
        f"Look at the image carefully and describe what you see. Then create engaging content based on the visual elements, mood, colors, objects, people, setting, and overall vibe of the image.\n\n"
        f"Your output should be formatted as:\n"
        f"Caption: (Write 2 to 4 complete sentences that capture the essence of the image. Use a tone suitable for {platform}. For example: "
        f"Instagram is casual and expressive, LinkedIn is professional and inspiring, Twitter is witty and concise. Do NOT include emojis or hashtags here.)\n"
        f"Emojis: (List 3 to 5 relevant emojis that match the image content and tone. Use sparingly for LinkedIn.)\n"
        f"Hashtags: (Provide 5 to 8 popular and relevant hashtags for {platform} based on what you see in the image. Keep them professional for LinkedIn, trendy for Instagram, and brief for Twitter.)\n\n"
        f"Example for a sunset beach image:\n"
        f"Caption: Golden hour magic at its finest! The way the sun kisses the horizon creates the most breathtaking canvas nature could paint. Sometimes the best moments are the quiet ones where you just stop and appreciate the beauty around you.\n"
        f"Emojis: 🌅 🏖️ ✨ 🧡 🌊\n"
        f"Hashtags: #GoldenHour #BeachSunset #NaturalBeauty #SunsetVibes #PeacefulMoments #GratefulHeart #SunsetLovers\n\n"
        f"Now analyze the uploaded image and generate your response:"
    )

    try:
        # Convert image if needed
        if hasattr(image, 'save'):
            # It's already a PIL Image
            processed_image = image
        else:
            # Convert to PIL Image
            processed_image = Image.open(image)
        
        # Generate content with image
        response = model.generate_content([full_prompt, processed_image])
        return parse_response(response.text.strip())
    
    except Exception as e:
        error_msg = f"Error analyzing image: {str(e)}"
        print(f"❌ {error_msg}")
        return error_msg, "", ""

def parse_response(text):
    """
    Parse the AI response into caption, emojis, and hashtags
    
    Args:
        text (str): The AI response text
        
    Returns:
        tuple: (caption, emojis, hashtags)
    """
    caption, emojis, hashtags = "", "", ""

    for line in text.splitlines():
        line = line.strip()
        if line.lower().startswith("caption:"):
            caption = line.split(":", 1)[1].strip()
        elif line.lower().startswith("emojis:"):
            emojis = line.split(":", 1)[1].strip()
        elif line.lower().startswith("hashtags:"):
            hashtags = line.split(":", 1)[1].strip()

    # Fallback if parsing fails
    if not caption and not emojis and not hashtags:
        return text, "", ""

    return caption, emojis, hashtags

def generate_content_unified(prompt, image, platform, additional_context=""):
    """
    Unified function to generate content from either text prompt or image
    
    Args:
        prompt (str): Text prompt/theme
        image: Uploaded image
        platform (str): Target social media platform
        additional_context (str): Additional context for image analysis
        
    Returns:
        tuple: (caption, emojis, hashtags)
    """
    # Priority: Image > Text Prompt
    if image is not None:
        print("🖼️ Generating content from uploaded image...")
        return generate_text_from_image(image, platform, additional_context)
    elif prompt and prompt.strip():
        print("✍️ Generating content from text prompt...")
        return generate_text_from_prompt(prompt, platform)
    else:
        return "Please either upload an image or enter a text prompt.", "", ""

def main():
    """Main function to run the application"""
    print("🚀 Starting Enhanced AI Social Media Caption Generator...")
    print("✨ Now with Image Upload Support!")
    print("🖼️ Loading beautiful UI...")
    
    # Create the interface using the enhanced UI module
    interface = create_stylish_interface(generate_content_unified)
    
    # Launch configuration - use a more compatible approach
    launch_config = {
        "server_name": "0.0.0.0",
        "server_port": 7860,
        "share": True,
        "inbrowser": True,
        "show_error": True,
        "debug": False,
        "quiet": False
    }
    
    # Try to use UI_CONFIG, but fall back to launch_config if there's an issue
    try:
        interface.launch(**UI_CONFIG)
    except Exception as e:
        print(f"⚠️ Warning: Could not use UI_CONFIG, falling back to basic config: {e}")
        interface.launch(share=True)

if __name__ == "__main__":
    main()