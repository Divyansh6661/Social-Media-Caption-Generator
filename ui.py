"""
Enhanced UI Module for Social Media Caption Generator
Beautiful, animated interface with image upload support - RADIO BUTTONS VERSION
"""

import gradio as gr

# --- UI Configuration ---
UI_CONFIG = {
    "server_name": "0.0.0.0",
    "server_port": 7860,
    "share": True,
    "inbrowser": True,
    "show_error": True
}

# --- Custom CSS with Radio Button styling ---
CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --primary-gradient: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    --secondary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --success-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    --text-gradient: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
    --glow-color: rgba(255, 255, 255, 0.3);
    --text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
}

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Main container styling */
.gradio-container {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    background-attachment: fixed;
    min-height: 100vh;
    animation: backgroundShift 15s ease-in-out infinite alternate;
}

@keyframes backgroundShift {
    0% { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); }
    50% { background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%); }
    100% { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); }
}

/* Glass morphism effect */
.block {
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
    animation: slideInUp 0.6s ease-out;
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.block:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4) !important;
}

/* Header styling */
.markdown h1 {
    color: #ffffff !important;
    font-size: 3.5rem !important;
    font-weight: 700 !important;
    text-align: center !important;
    margin-bottom: 1rem !important;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8) !important;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { 
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 255, 255, 0.3); 
    }
    to { 
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8), 0 0 30px rgba(255, 255, 255, 0.5), 0 0 40px rgba(255, 255, 255, 0.3); 
    }
}

.markdown p {
    color: #ffffff !important;
    font-size: 1.2rem !important;
    text-align: center !important;
    margin-bottom: 2rem !important;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8) !important;
    animation: fadeIn 1s ease-out 0.5s both;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Tab styling */
.gr-tabs {
    background: rgba(255, 255, 255, 0.1) !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
}

.gr-tab {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    font-weight: 500 !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.3s ease !important;
}

.gr-tab:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    transform: translateY(-2px) !important;
}

.gr-tab.selected {
    background: var(--secondary-gradient) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* Input fields styling */
.gr-textbox {
    background: rgba(255, 255, 255, 0.2) !important;
    border: 2px solid rgba(255, 255, 255, 0.4) !important;
    border-radius: 15px !important;
    color: #ffffff !important;
    backdrop-filter: blur(10px) !important;
    transition: all 0.3s ease !important;
}

.gr-textbox:focus {
    border-color: rgba(255, 255, 255, 0.7) !important;
    box-shadow: 0 0 25px rgba(255, 255, 255, 0.3) !important;
    transform: scale(1.02) !important;
}

.gr-textbox input, .gr-textbox textarea {
    background: transparent !important;
    color: #ffffff !important;
    border: none !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
}

.gr-textbox input::placeholder, .gr-textbox textarea::placeholder {
    color: rgba(255, 255, 255, 0.8) !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
}

/* RADIO BUTTON STYLING */
.gr-radio {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 2px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 15px !important;
    padding: 20px !important;
    backdrop-filter: blur(10px) !important;
    transition: all 0.3s ease !important;
}

.gr-radio:hover {
    border-color: rgba(255, 255, 255, 0.5) !important;
    background: rgba(255, 255, 255, 0.15) !important;
    transform: scale(1.02) !important;
}

/* Radio button container */
.gr-radio .gr-form {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 15px !important;
    margin: 0 !important;
}

/* Individual radio button styling */
.gr-radio .gr-form > label {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 2px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 12px !important;
    padding: 15px 12px !important;
    color: #ffffff !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
    text-align: center !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    position: relative !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 50px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}

.gr-radio .gr-form > label:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    border-color: rgba(255, 255, 255, 0.6) !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
}

/* Selected radio button styling */
.gr-radio .gr-form > label:has(input:checked) {
    background: var(--secondary-gradient) !important;
    border-color: rgba(255, 255, 255, 0.8) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    transform: translateY(-2px) scale(1.05) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
}

/* Hide the default radio button */
.gr-radio .gr-form > label > input[type="radio"] {
    position: absolute !important;
    opacity: 0 !important;
    width: 0 !important;
    height: 0 !important;
}

/* Add custom radio indicator */
.gr-radio .gr-form > label::before {
    content: '' !important;
    position: absolute !important;
    top: 8px !important;
    right: 8px !important;
    width: 16px !important;
    height: 16px !important;
    border-radius: 50% !important;
    border: 2px solid rgba(255, 255, 255, 0.5) !important;
    background: transparent !important;
    transition: all 0.3s ease !important;
}

.gr-radio .gr-form > label:has(input:checked)::before {
    background: #ffffff !important;
    border-color: #ffffff !important;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.5) !important;
}

/* Platform-specific styling */
.gr-radio .gr-form > label:has(input[value="Instagram"]) {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
    background-size: 0% 100% !important;
    background-repeat: no-repeat !important;
    transition: background-size 0.3s ease !important;
}

.gr-radio .gr-form > label:has(input[value="Instagram"]):hover {
    background-size: 100% 100% !important;
}

.gr-radio .gr-form > label:has(input[value="LinkedIn"]) {
    background: linear-gradient(135deg, #0077b5 0%, #0e76a8 100%) !important;
    background-size: 0% 100% !important;
    background-repeat: no-repeat !important;
    transition: background-size 0.3s ease !important;
}

.gr-radio .gr-form > label:has(input[value="LinkedIn"]):hover {
    background-size: 100% 100% !important;
}

.gr-radio .gr-form > label:has(input[value="Twitter"]) {
    background: linear-gradient(135deg, #1da1f2 0%, #0d8bd9 100%) !important;
    background-size: 0% 100% !important;
    background-repeat: no-repeat !important;
    transition: background-size 0.3s ease !important;
}

.gr-radio .gr-form > label:has(input[value="Twitter"]):hover {
    background-size: 100% 100% !important;
}

/* Responsive design for radio buttons */
@media (max-width: 768px) {
    .gr-radio .gr-form {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px !important;
    }
    
    .gr-radio .gr-form > label {
        padding: 12px 8px !important;
        font-size: 0.9rem !important;
        min-height: 45px !important;
    }
}

@media (max-width: 480px) {
    .gr-radio .gr-form {
        grid-template-columns: 1fr !important;
    }
}

/* Image upload styling */
.gr-image {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 2px dashed rgba(255, 255, 255, 0.4) !important;
    border-radius: 15px !important;
    transition: all 0.3s ease !important;
    min-height: 300px !important;
}

.gr-image:hover {
    border-color: rgba(255, 255, 255, 0.7) !important;
    background: rgba(255, 255, 255, 0.15) !important;
    transform: scale(1.02) !important;
}

.gr-image .gr-upload-text {
    color: #ffffff !important;
    font-size: 1.1rem !important;
    font-weight: 500 !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
}

/* Button styling */
.gr-button:not(.gr-radio .gr-button) {
    background: var(--secondary-gradient) !important;
    border: none !important;
    border-radius: 25px !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    padding: 15px 30px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.4) !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.gr-button:not(.gr-radio .gr-button):hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
    animation: none;
}

.gr-button:not(.gr-radio .gr-button):active {
    transform: translateY(-1px) scale(1.02) !important;
}

/* Output fields styling */
.gr-textbox[data-testid*="output"] {
    background: rgba(255, 255, 255, 0.25) !important;
    border: 2px solid rgba(255, 255, 255, 0.4) !important;
    animation: slideInRight 0.8s ease-out;
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Labels styling */
.gr-label {
    color: #ffffff !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    margin-bottom: 8px !important;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8) !important;
}

/* Copy button styling */
.gr-copy-button {
    background: var(--accent-gradient) !important;
    border: none !important;
    border-radius: 8px !important;
    color: #ffffff !important;
    transition: all 0.3s ease !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
}

.gr-copy-button:hover {
    transform: scale(1.1) !important;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3) !important;
}

/* Examples section styling */
.gr-examples {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 15px !important;
    padding: 20px !important;
    margin-top: 20px !important;
    animation: slideInUp 1s ease-out 0.8s both;
}

.gr-examples .gr-button {
    background: rgba(255, 255, 255, 0.2) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    color: #ffffff !important;
    font-size: 0.9rem !important;
    padding: 8px 16px !important;
    margin: 5px !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5) !important;
    animation: none !important;
}

.gr-examples .gr-button:hover {
    background: rgba(255, 255, 255, 0.3) !important;
    transform: translateY(-2px) !important;
}

/* Responsive design */
@media (max-width: 768px) {
    .markdown h1 {
        font-size: 2.5rem !important;
    }
    
    .gr-button:not(.gr-radio .gr-button) {
        padding: 12px 24px !important;
        font-size: 1rem !important;
    }
    
    .gr-image {
        min-height: 200px !important;
    }
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}
"""

def create_header():
    """Create the animated header section"""
    return gr.HTML("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="font-size: 3.5rem; font-weight: 700; color: #ffffff; 
                   margin-bottom: 1rem; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);">
            ✨ AI Social Media Caption Generator
        </h1>
        <p style="color: #ffffff; font-size: 1.2rem; margin-bottom: 2rem; 
                  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);">
            🚀 Powered by Gemini AI - Create viral content with stunning captions, emojis, and hashtags!
        </p>
        <div style="background: rgba(255, 255, 255, 0.1); padding: 1rem; border-radius: 10px; 
                    border: 1px solid rgba(255, 255, 255, 0.3); margin: 1rem auto; max-width: 600px;">
            <p style="color: #ffffff; font-size: 1rem; margin: 0; 
                      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);">
                🎯 <strong>NEW!</strong> Upload images OR enter text prompts to generate amazing content!
            </p>
        </div>
    </div>
    """)

def create_text_input_tab():
    """Create the text input tab components"""
    return [
        gr.HTML("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: #ffffff; font-size: 1.5rem; font-weight: 600;
                       text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);">
                ✍️ Generate from Text Prompt
            </h3>
            <p style="color: #ffffff; font-size: 1rem;
                      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);">
                Enter a keyword, theme, or describe what you want to post about
            </p>
        </div>
        """),
        gr.Textbox(
            label="💡 Enter Keyword or Theme",
            placeholder="✨ e.g., morning coffee, weekend vibes, product launch, travel adventure, team celebration...",
            lines=4,
            elem_classes=["animated-input"]
        ),
    ]

def create_image_input_tab():
    """Create the image input tab components"""
    return [
        gr.HTML("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: #ffffff; font-size: 1.5rem; font-weight: 600;
                       text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);">
                🖼️ Generate from Image
            </h3>
            <p style="color: #ffffff; font-size: 1rem;
                      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);">
                Upload an image and let AI analyze it to create perfect captions
            </p>
        </div>
        """),
        gr.Image(
            label="📸 Upload Your Image",
            type="pil",
            elem_classes=["animated-input"]
        ),
        gr.Textbox(
            label="💭 Additional Context (Optional)",
            placeholder="✨ e.g., 'This was taken during our team retreat', 'Celebrating our product launch', 'My morning routine'...",
            lines=3,
            elem_classes=["animated-input"]
        ),
    ]

def create_platform_and_generate():
    """Create platform radio buttons and generate button"""
    return [
        gr.HTML("""
        <div style="text-align: center; margin: 2rem 0;">
            <h3 style="color: #ffffff; font-size: 1.3rem; font-weight: 600;
                       text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);">
                📱 Choose Your Platform
            </h3>
            <p style="color: #ffffff; font-size: 1rem; margin-top: 0.5rem;
                      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);">
                Select the social media platform you're targeting
            </p>
        </div>
        """),
        gr.Radio(
            choices=["Instagram", "LinkedIn", "Twitter", "Facebook", "TikTok", "YouTube"], 
            label="🎯 Target Platform",
            value="Instagram",
            elem_classes=["platform-radio"]
        ),
        gr.Button(
            "🚀 Generate Viral Content", 
            variant="primary",
            size="lg",
            elem_classes=["pulse-button"]
        ),
        gr.HTML("""
        <div style="margin-top: 1rem; text-align: center;">
            <small style="color: #ffffff; text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);">
                💫 Click to create magic! AI will analyze your input and create amazing content.
            </small>
        </div>
        """)
    ]

def create_footer():
    """Create the footer section"""
    return gr.HTML("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; 
                background: rgba(255,255,255,0.1); border-radius: 15px; 
                border: 1px solid rgba(255,255,255,0.3);">
        <p style="color: #ffffff; font-size: 1rem; font-weight: 500;
                  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);">
            🌟 Made with ❤️ using Gemini AI & Gradio | 
            <span style="color: #e0e7ff; font-weight: 600;">
                Create. Engage. Go Viral! 🚀
            </span>
        </p>
        <p style="color: #ffffff; font-size: 0.9rem; margin-top: 1rem;
                  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);">
            📸 Now supports both text prompts and image analysis for maximum creativity!
        </p>
    </div>
    """)

def create_stylish_interface(generate_function):
    """
    Create interface with radio buttons for platform selection
    """
    with gr.Blocks(
        title="✨ AI Social Media Caption Generator",
        css=CUSTOM_CSS,
        theme=gr.themes.Base(
            primary_hue="blue",
            secondary_hue="purple",
            neutral_hue="slate",
            spacing_size="md",
            radius_size="lg"
        )
    ) as interface:
        
        # Header
        create_header()
        
        # Main content area
        with gr.Row():
            # Left Column - Input Section
            with gr.Column(scale=1):
                gr.HTML("""
                <div style="text-align: center; margin-bottom: 1rem;">
                    <h3 style="color: #ffffff; font-size: 1.5rem; font-weight: 600;
                               text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8); margin: 0;">
                        🚀 Create Your Content
                    </h3>
                </div>
                """)
                
                # Input tabs
                with gr.Tabs() as input_tabs:
                    with gr.TabItem("✍️ Text Prompt", id="text_tab"):
                        text_components = create_text_input_tab()
                        text_prompt = text_components[1]  # The textbox
                    
                    with gr.TabItem("🖼️ Image Upload", id="image_tab"):
                        image_components = create_image_input_tab()
                        image_input = image_components[1]  # The image component
                        additional_context = image_components[2]  # The context textbox
                
                # Platform and generate section
                platform_components = create_platform_and_generate()
                platform_radio = platform_components[1]  # The radio buttons
                generate_button = platform_components[2]  # The button
            
            # Right Column - Output Section
            with gr.Column(scale=1):
                gr.HTML("""
                <div style="text-align: center; margin-bottom: 1rem;">
                    <h3 style="color: #ffffff; font-size: 1.5rem; font-weight: 600;
                               text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8); margin: 0;">
                        🎨 Generated Content
                    </h3>
                    <p style="color: #ffffff; font-size: 1rem; margin: 0.5rem 0 0 0;
                              text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);">
                        Your AI-powered social media content appears here
                    </p>
                </div>
                """)
                
                caption_output = gr.Textbox(
                    label="📝 Generated Caption",
                    lines=6,
                    show_copy_button=True,
                    elem_classes=["animated-output"]
                )
                emoji_output = gr.Textbox(
                    label="😍 Perfect Emojis",
                    lines=3,
                    show_copy_button=True,
                    elem_classes=["animated-output"]
                )
                hashtag_output = gr.Textbox(
                    label="🔥 Trending Hashtags",
                    lines=4,
                    show_copy_button=True,
                    elem_classes=["animated-output"]
                )
        
        # Examples section
        gr.HTML("""
        <div style="margin: 3rem 0 2rem 0; text-align: center;">
            <h3 style="color: #ffffff; font-size: 1.5rem; font-weight: 600;
                       text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);">
                💡 Get Inspired - Try These Examples
            </h3>
            <p style="color: #ffffff; font-size: 1rem;
                      text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);">
                Click any example to see the magic happen! (Text prompt examples)
            </p>
        </div>
        """)
        
        # Create examples component
        examples = gr.Examples(
            examples=[
                ["☕ morning coffee ritual", None, "Instagram", ""],
                ["🏆 team achievement celebration", None, "LinkedIn", ""],
                ["🎉 weekend adventure plans", None, "Twitter", ""],
                ["🚀 exciting product launch", None, "LinkedIn", ""],
                ["🌍 wanderlust travel story", None, "Instagram", ""],
                ["💪 Monday motivation", None, "LinkedIn", ""],
                ["🍕 foodie paradise", None, "Instagram", ""],
                ["⚡ tech innovation breakthrough", None, "Twitter", ""]
            ],
            inputs=[text_prompt, image_input, platform_radio, additional_context],
            outputs=[caption_output, emoji_output, hashtag_output],
            fn=generate_function,
            cache_examples=False,
            label="💡 Try These Examples"
        )
        
        # Footer
        create_footer()
        
        # Event handlers
        generate_button.click(
            fn=generate_function,
            inputs=[text_prompt, image_input, platform_radio, additional_context],
            outputs=[caption_output, emoji_output, hashtag_output],
            api_name="generate_content"
        )
        
        # Optional: Add enter key support for text input
        text_prompt.submit(
            fn=generate_function,
            inputs=[text_prompt, image_input, platform_radio, additional_context],
            outputs=[caption_output, emoji_output, hashtag_output]
        )
    
    return interface