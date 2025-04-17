import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Set page config
st.set_page_config(
    page_title="Wedding Planner AI",
    page_icon="💒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for chat history and wedding details
if "messages" not in st.session_state:
    st.session_state.messages = []
if "wedding_date" not in st.session_state:
    st.session_state.wedding_date = None
if "guest_count" not in st.session_state:
    st.session_state.guest_count = None
if "budget" not in st.session_state:
    st.session_state.budget = None
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Add custom CSS
st.markdown("""
    <style>
    /* Main container */
    .main {
        background-color: #FFF0F5;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #FFF0F5;
    }
    
    /* Input fields */
    .stTextInput>div>div>input {
        background-color: white;
        border-radius: 10px;
        border: 1px solid #FF69B4;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        width: 100%;
        margin: 5px 0;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #FF1493;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Chat messages */
    .stChatMessage {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #FF1493;
        font-family: 'Playfair Display', serif;
    }
    
    /* Number input */
    .stNumberInput>div>div>input {
        background-color: white;
        border-radius: 10px;
        border: 1px solid #FF69B4;
    }
    
    /* Date input */
    .stDateInput>div>div>input {
        background-color: white;
        border-radius: 10px;
        border: 1px solid #FF69B4;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for wedding details
with st.sidebar:
    st.markdown("""
        <h1 style='text-align: center;'>💒 Wedding Planner</h1>
        <p style='text-align: center; color: #666;'>Your AI Wedding Planning Assistant</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h3 style='color: #FF1493;'>Your Wedding Information</h3>
    """, unsafe_allow_html=True)
    
    # Wedding date picker
    wedding_date = st.date_input(
        "📅 Wedding Date",
        value=st.session_state.wedding_date,
        min_value=datetime.now().date()
    )
    st.session_state.wedding_date = wedding_date
    
    # Guest count
    guest_count = st.number_input(
        "👥 Number of Guests",
        min_value=1,
        value=st.session_state.guest_count or 50,
        step=1
    )
    st.session_state.guest_count = guest_count
    
    # Budget
    budget = st.number_input(
        "💰 Budget (₹)",
        min_value=0,
        value=st.session_state.budget or 500000,  # Default value in INR
        step=50000  # Step size in INR
    )
    st.session_state.budget = budget
    
    st.markdown("""
        <h3 style='color: #FF1493;'>Quick Actions</h3>
    """, unsafe_allow_html=True)
    
    # Quick action buttons
    if st.button("📋 Create Timeline"):
        prompt = f"Create a detailed wedding planning timeline for a wedding on {wedding_date} with {guest_count} guests and a budget of ₹{budget}."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating timeline..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("💰 Budget Breakdown"):
        prompt = f"Provide a detailed budget breakdown for a wedding with {guest_count} guests and a total budget of ₹{budget}."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating budget breakdown..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🎨 Theme Suggestions"):
        prompt = "Suggest some wedding themes and color schemes that would work well for our wedding."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Generating theme ideas..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🎵 Music & Entertainment"):
        prompt = "Suggest some wedding music and entertainment options that would work well for our wedding."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Suggesting entertainment options..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🍽️ Catering Ideas"):
        prompt = f"Suggest catering options and menu ideas for {guest_count} guests with a budget of ₹{budget}."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating menu suggestions..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

# Main content
st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 20px;'>
        <h2 style='color: #FF1493; text-align: center;'>Developer Information</h2>
        <div style='text-align: center;'>
            <p style='font-size: 1.2em; margin: 10px 0;'><strong>Abhinandan Pandey</strong></p>
            <p style='margin: 5px 0;'>Lovely Professional University</p>
            <p style='margin: 5px 0;'>Contact: +91 9709925057</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center;'>💒 AI Wedding Planner</h1>
    <p style='text-align: center; color: #666;'>Your Personal Wedding Planning Assistant</p>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
        <h3 style='color: #FF1493;'>Wedding Planning Services</h3>
        <p>Click on any service below to get started:</p>
    </div>
""", unsafe_allow_html=True)

# Create columns for the buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📅 Timeline & Checklist", use_container_width=True):
        prompt = f"Create a detailed wedding planning timeline and checklist for a wedding on {st.session_state.wedding_date} with {st.session_state.guest_count} guests. Include all major milestones and tasks."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating timeline and checklist..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("💰 Budget Planning", use_container_width=True):
        prompt = f"Provide a detailed budget breakdown and planning guide for a wedding with {st.session_state.guest_count} guests and a budget of ₹{st.session_state.budget}. Include cost-saving tips and budget allocation recommendations."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating budget plan..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🏰 Venue Suggestions", use_container_width=True):
        prompt = f"Suggest suitable wedding venues for {st.session_state.guest_count} guests with a budget of ₹{st.session_state.budget}. Include indoor and outdoor options, and consider the wedding date {st.session_state.wedding_date}."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Finding venue suggestions..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🎨 Theme & Decor", use_container_width=True):
        prompt = "Suggest wedding themes and decoration ideas that would create a beautiful and memorable atmosphere. Include color schemes, floral arrangements, and lighting ideas."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating theme suggestions..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

with col2:
    if st.button("👥 Vendor Recommendations", use_container_width=True):
        prompt = f"Recommend essential vendors for a wedding with {st.session_state.guest_count} guests and a budget of ₹{st.session_state.budget}. Include photographers, videographers, makeup artists, and other key vendors."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Finding vendor recommendations..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🎵 Music & Entertainment", use_container_width=True):
        prompt = "Suggest wedding music and entertainment options. Include recommendations for ceremony music, reception entertainment, and DJ/band options."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Planning entertainment..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("🍽️ Catering & Menu", use_container_width=True):
        prompt = f"Suggest catering options and menu ideas for {st.session_state.guest_count} guests with a budget of ₹{st.session_state.budget}. Include appetizers, main course, desserts, and beverage options."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Creating menu suggestions..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    if st.button("💝 Additional Services", use_container_width=True):
        prompt = "Suggest additional wedding services and ideas that could enhance the wedding experience. Include transportation, accommodation, wedding favors, and other special touches."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Finding additional services..."):
            response = st.session_state.chat.send_message(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("💭 Ask me anything about your wedding planning..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("💫 Planning your perfect wedding..."):
            try:
                # Create context for the AI
                context = f"""You are a friendly and experienced AI wedding planner. 
                Current wedding details:
                - Wedding Date: {st.session_state.wedding_date}
                - Guest Count: {st.session_state.guest_count}
                - Budget: ₹{st.session_state.budget}
                
                Please provide detailed, practical, and personalized wedding planning advice.
                Focus on creating a memorable and well-organized wedding experience.
                """
                
                # Send context and user message to Gemini
                response = st.session_state.chat.send_message(f"{context}\n\nUser question: {prompt}")
                response_content = response.text
                
                st.markdown(response_content)
                st.session_state.messages.append({"role": "assistant", "content": response_content})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please make sure you have set up your API key in the .env file.")

# Add a sidebar with information
with st.sidebar:
    st.title("About")
    st.markdown("""
    This is an AI chatbot powered by Gemini AI.
    
    **Developer Information:**
    - Name: Abhinandan Pandey
    - Institution: Lovely Professional University
    - Contact: +91 9709925057
    
    To use this chatbot:
    1. Create a `.env` file in the project directory
    2. Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`
    3. Install the required packages using `pip install -r requirements.txt`
    4. Run the app using `streamlit run app.py`
    """) 