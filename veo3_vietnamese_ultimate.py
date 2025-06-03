import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import json
import os
import time
import hashlib
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pandas as pd
import requests
import random
import io
import base64

# =============================================================================
# IMPORT ALL 7 ADVANCED FEATURES
# =============================================================================

# Import all advanced feature classes
try:
    from ai_assistant_advanced import create_ai_assistant_advanced
    from mobile_app_design import create_mobile_app
    from professional_templates import create_professional_templates
    from monetization_system import create_monetization_system
    from community_marketing import create_community_marketing
    from utility_features import create_utility_features
    from vietnam_targeting import create_vietnam_targeting
    ADVANCED_FEATURES_AVAILABLE = True
except ImportError as e:
    ADVANCED_FEATURES_AVAILABLE = False
    print(f"⚠️ Một số tính năng nâng cao chưa sẵn sàng: {str(e)}")

# =============================================================================
# VEO3 VIETNAMESE ULTIMATE - PHIÊN BẢN TIẾNG VIỆT HOÀN CHỈNH với 7 TÍNH NĂNG MỚI
# =============================================================================

st.set_page_config(
    page_title="🌟 Veo3 Studio Chuyên Nghiệp",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CSS SIÊU ĐẸP - GIAO DIỆN VIỆT NAM - ĐÃ TỐI ƯU VỚI TÍNH NĂNG MỚI
# =============================================================================

def load_vietnamese_css():
    # ===== PRELOADER & LOADING OPTIMIZATION =====
    st.markdown("""
    <style>
    /* ===== PRELOADER TO PREVENT WHITE FLASH ===== */
    .stApp {
        background: linear-gradient(135deg, 
            #667eea 0%, 
            #764ba2 25%, 
            #f093fb 50%, 
            #f5576c 75%, 
            #4facfe 100%) !important;
        animation: gradientShift 15s ease infinite !important;
        font-family: 'Poppins', sans-serif !important;
        color: #2d3748 !important;
        /* Prevent flash of unstyled content */
        visibility: visible !important;
        opacity: 1 !important;
        transition: opacity 0.3s ease !important;
    }
    
    /* Loading state styling */
    .stSpinner > div {
        border: 4px solid rgba(255, 255, 255, 0.3) !important;
        border-top: 4px solid #667eea !important;
        animation: spin 1s linear infinite !important;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Ensure elements load smoothly */
    .main .block-container {
        background: transparent !important;
        padding: 2rem 1rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
        opacity: 1 !important;
        visibility: visible !important;
        transition: all 0.3s ease !important;
    }
    
    /* Faster transitions for page changes */
    .element-container {
        transition: all 0.2s ease !important;
    }
    
    /* Hide elements during initial load to prevent flash */
    body {
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;600;700;800;900&display=swap');
    
    /* ===== MODERN LUXURY THEME - OPTIMIZED LOADING ===== */
    .stApp {
        background: linear-gradient(135deg, 
            #667eea 0%, 
            #764ba2 25%, 
            #f093fb 50%, 
            #f5576c 75%, 
            #4facfe 100%) !important;
        animation: gradientShift 15s ease infinite !important;
        font-family: 'Poppins', sans-serif !important;
        color: #2d3748 !important;
        /* Prevent flash of unstyled content */
        visibility: visible !important;
        opacity: 1 !important;
        transition: opacity 0.3s ease !important;
    }
    
    @keyframes gradientShift {
        0% { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%); }
        25% { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 25%, #667eea 50%, #764ba2 75%, #f093fb 100%); }
        50% { background: linear-gradient(135deg, #f093fb 0%, #f5576c 25%, #4facfe 50%, #00f2fe 75%, #667eea 100%); }
        75% { background: linear-gradient(135deg, #764ba2 0%, #667eea 25%, #4facfe 50%, #f093fb 75%, #f5576c 100%); }
        100% { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%); }
    }
    
    .main .block-container {
        background: transparent !important;
        padding: 2rem 1rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }
    
    /* ===== PREMIUM GLASSMORPHISM CARDS ===== */
    .luxury-card {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.25) 0%, 
            rgba(255, 255, 255, 0.18) 100%) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 20px !important;
        padding: 2.5rem !important;
        margin: 1.5rem 0 !important;
        box-shadow: 
            0 8px 32px rgba(31, 38, 135, 0.37),
            inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .luxury-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.1) 0%, 
            transparent 50%, 
            rgba(255, 255, 255, 0.1) 100%) !important;
        opacity: 0 !important;
        transition: opacity 0.3s ease !important;
        pointer-events: none !important;
    }
    
    .luxury-card:hover::before {
        opacity: 1 !important;
    }
    
    .luxury-card:hover {
        transform: translateY(-8px) scale(1.02) !important;
        box-shadow: 
            0 20px 60px rgba(31, 38, 135, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.6) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* ===== ELEGANT HEADER ===== */
    .hero-header {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.3) 0%, 
            rgba(255, 255, 255, 0.1) 100%) !important;
        backdrop-filter: blur(30px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 30px !important;
        padding: 4rem 3rem !important;
        text-align: center !important;
        margin-bottom: 3rem !important;
        position: relative !important;
        overflow: hidden !important;
        animation: heroFloat 6s ease-in-out infinite !important;
    }
    
    @keyframes heroFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .hero-header h1 {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 4rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        margin-bottom: 1rem !important;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5) !important;
        animation: textGlow 3s ease-in-out infinite alternate !important;
    }
    
    @keyframes textGlow {
        0% { text-shadow: 0 0 30px rgba(102, 126, 234, 0.5); }
        100% { text-shadow: 0 0 50px rgba(102, 126, 234, 0.8), 0 0 80px rgba(118, 75, 162, 0.6); }
    }
    
    .hero-header p {
        font-size: 1.5rem !important;
        color: #4a5568 !important;
        font-weight: 500 !important;
        opacity: 0.9 !important;
    }
    
    /* ===== MODERN NAVIGATION ===== */
    .nav-container {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.2) 0%, 
            rgba(255, 255, 255, 0.1) 100%) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        margin-bottom: 2rem !important;
    }
    
    .nav-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        color: #4a5568 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
    }
    
    /* ===== PREMIUM BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.3) 0%, 
            rgba(255, 255, 255, 0.1) 100%) !important;
        backdrop-filter: blur(10px) !important;
        color: #2d3748 !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative !important;
        overflow: hidden !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        min-height: 50px !important;
        width: 100% !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.4), 
            transparent) !important;
        transition: left 0.5s ease !important;
    }
    
    .stButton > button:hover::before {
        left: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.4) 0%, 
            rgba(255, 255, 255, 0.2) 100%) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(1.02) !important;
    }
    
    /* ===== ELEGANT INPUT FIELDS ===== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.9) 0%, 
            rgba(255, 255, 255, 0.7) 100%) !important;
        backdrop-filter: blur(10px) !important;
        color: #2d3748 !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        font-weight: 500 !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        font-family: 'Poppins', sans-serif !important;
        box-shadow: 
            0 4px 15px rgba(0, 0, 0, 0.05),
            inset 0 1px 0 rgba(255, 255, 255, 0.6) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(102, 126, 234, 0.6) !important;
        box-shadow: 
            0 8px 25px rgba(102, 126, 234, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.8) !important;
        transform: translateY(-2px) !important;
        background: rgba(255, 255, 255, 0.95) !important;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(45, 55, 72, 0.6) !important;
        font-weight: 400 !important;
    }
    
    /* ===== SELECTBOX MODERN STYLING ===== */
    .stSelectbox > div > div {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.9) 0%, 
            rgba(255, 255, 255, 0.7) 100%) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(102, 126, 234, 0.4) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.1) !important;
        transform: translateY(-2px) !important;
    }
    
    .stSelectbox label {
        color: #4a5568 !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    /* ===== FEATURE METRICS ===== */
    .metric-card {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.25) 0%, 
            rgba(255, 255, 255, 0.15) 100%) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        text-align: center !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative !important;
        overflow: hidden !important;
        min-height: 180px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
    }
    
    .metric-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb) !important;
        border-radius: 20px 20px 0 0 !important;
    }
    
    .metric-card:hover {
        transform: scale(1.05) rotateY(5deg) !important;
        box-shadow: 0 20px 40px rgba(31, 38, 135, 0.3) !important;
        border-color: rgba(255, 255, 255, 0.3) !important;
    }
    
    .metric-card h2 {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        font-family: 'Orbitron', sans-serif !important;
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        margin-bottom: 0.5rem !important;
        animation: numberPulse 2s ease-in-out infinite !important;
    }
    
    @keyframes numberPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .metric-card p {
        color: #4a5568 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    /* ===== ALERT BOXES ===== */
    .stAlert {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.8) 0%, 
            rgba(255, 255, 255, 0.6) 100%) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #2d3748 !important;
        font-weight: 500 !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stAlert > div {
        color: #2d3748 !important;
        background: transparent !important;
        font-weight: 500 !important;
    }
    
    /* ===== CODE BLOCKS ===== */
    .stCodeBlock,
    .stCodeBlock *,
    code,
    pre {
        background: linear-gradient(135deg, 
            rgba(45, 55, 72, 0.95) 0%, 
            rgba(45, 55, 72, 0.85) 100%) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        font-family: 'JetBrains Mono', 'Courier New', monospace !important;
        font-weight: 500 !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2, #f093fb);
    }
    
    /* ===== ANIMATIONS ===== */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out !important;
    }
    
    /* ===== RESPONSIVE DESIGN ===== */
    @media (max-width: 768px) {
        .hero-header h1 {
            font-size: 2.5rem !important;
        }
        
        .luxury-card {
            padding: 1.5rem !important;
        }
        
        .metric-card {
            padding: 1.5rem !important;
            min-height: 150px !important;
        }
        
        .metric-card h2 {
            font-size: 2.5rem !important;
        }
    }
    
    /* ===== UTILITY CLASSES ===== */
    .text-gradient {
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    .glass-effect {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.25) 0%, 
            rgba(255, 255, 255, 0.15) 100%) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
    }
    
    /* ===== CHAT MESSAGES ===== */
    .stChatMessage {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.8) 0%, 
            rgba(255, 255, 255, 0.6) 100%) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #2d3748 !important;
        font-weight: 500 !important;
        margin: 0.5rem 0 !important;
        padding: 1rem !important;
    }
    
    .stChatMessage * {
        color: #2d3748 !important;
    }
    
    .stChatMessage p {
        color: #2d3748 !important;
        font-weight: 500 !important;
    }
    
    /* ===== SUCCESS/INFO/WARNING/ERROR BOXES - CHỮ ĐEN ===== */
    .stSuccess,
    .stInfo,
    .stWarning,
    .stError {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.9) 0%, 
            rgba(255, 255, 255, 0.8) 100%) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stSuccess > div,
    .stInfo > div,
    .stWarning > div,
    .stError > div {
        color: #2d3748 !important;
        background: transparent !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    .stSuccess * {
        color: #2d3748 !important;
    }
    
    .stInfo * {
        color: #2d3748 !important;
    }
    
    .stWarning * {
        color: #2d3748 !important;
    }
    
    .stError * {
        color: #2d3748 !important;
    }
    
    /* ===== FORCE ALL STREAMLIT ELEMENTS BLACK TEXT ===== */
    [data-testid="stAlert"],
    [data-testid="stAlert"] *,
    [data-testid="stSuccess"],
    [data-testid="stSuccess"] *,
    [data-testid="stInfo"],
    [data-testid="stInfo"] *,
    [data-testid="stWarning"],
    [data-testid="stWarning"] *,
    [data-testid="stError"],
    [data-testid="stError"] *,
    .element-container .stAlert,
    .element-container .stAlert *,
    .element-container .stSuccess,
    .element-container .stSuccess *,
    .element-container .stInfo,
    .element-container .stInfo *,
    .element-container .stWarning,
    .element-container .stWarning *,
    .element-container .stError,
    .element-container .stError * {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #1a202c !important;
        font-weight: 600 !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    /* ===== CHAT MESSAGE CONTAINERS ===== */
    [data-testid="chatAvatarIcon-user"],
    [data-testid="chatAvatarIcon-assistant"],
    [data-testid="stChatMessage"],
    [data-testid="stChatMessage"] *,
    .stChatMessage,
    .stChatMessage *,
    div[data-testid*="chat"],
    div[data-testid*="chat"] * {
        background: rgba(255, 255, 255, 0.9) !important;
        color: #1a202c !important;
        font-weight: 500 !important;
        border-radius: 15px !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    /* ===== FORCE ALL DIVS WITH WHITE BACKGROUND ===== */
    div[style*="background-color: rgb(255, 255, 255)"],
    div[style*="background-color: white"],
    div[style*="background: rgb(255, 255, 255)"],
    div[style*="background: white"] {
        color: #1a202c !important;
        font-weight: 600 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    div[style*="background-color: rgb(255, 255, 255)"] *,
    div[style*="background-color: white"] *,
    div[style*="background: rgb(255, 255, 255)"] *,
    div[style*="background: white"] * {
        color: #1a202c !important;
        font-weight: 600 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    /* ===== FORCE ALL PARAGRAPHS IN WHITE CONTAINERS ===== */
    .stAlert p,
    .stSuccess p,
    .stInfo p,
    .stWarning p,
    .stError p,
    [data-testid="stAlert"] p,
    [data-testid="stSuccess"] p,
    [data-testid="stInfo"] p,
    [data-testid="stWarning"] p,
    [data-testid="stError"] p {
        color: #1a202c !important;
        font-weight: 600 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
        font-size: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Force dropdown text color with JavaScript
    st.components.v1.html("""
    <script>
    function brutalForceTextFix() {
        // ALERT BOXES FIXES - FORCE BLACK TEXT
        const alertSelectors = [
            '.stSuccess', '.stSuccess *',
            '.stInfo', '.stInfo *',
            '.stWarning', '.stWarning *',
            '.stError', '.stError *',
            '.stAlert', '.stAlert *'
        ];
        
        alertSelectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    if (el) {
                        el.style.setProperty('background', 'rgba(255, 255, 255, 0.9)', 'important');
                        el.style.setProperty('color', '#2d3748', 'important');
                        el.style.setProperty('border', '1px solid rgba(255, 255, 255, 0.3)', 'important');
                        el.style.setProperty('border-radius', '15px', 'important');
                        el.style.setProperty('font-weight', '600', 'important');
                        el.style.setProperty('backdrop-filter', 'blur(10px)', 'important');
                    }
                });
            } catch(e) { console.log(e); }
        });
        
        // CHAT MESSAGES FIXES - FORCE BLACK TEXT
        const chatSelectors = [
            '.stChatMessage',
            '.stChatMessage *',
            '.stChatMessage p',
            '.stChatMessage div'
        ];
        
        chatSelectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    if (el) {
                        el.style.setProperty('color', '#2d3748', 'important');
                        el.style.setProperty('background', 'rgba(255, 255, 255, 0.8)', 'important');
                        el.style.setProperty('font-weight', '500', 'important');
                        el.style.setProperty('border-radius', '15px', 'important');
                    }
                });
            } catch(e) { console.log(e); }
        });
        
        // CODE BLOCKS FIXES
        const codeSelectors = [
            '.stCodeBlock',
            '.stCodeBlock *',
            'code',
            'pre',
            '.stCode',
            '.stCode *',
            'div[data-testid="stCodeBlock"]',
            'div[data-testid="stCodeBlock"] *',
            '.language-text'
        ];
        
        codeSelectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    if (el) {
                        el.style.setProperty('background-color', 'rgba(45, 55, 72, 0.95)', 'important');
                        el.style.setProperty('color', '#e2e8f0', 'important');
                        el.style.setProperty('border', '1px solid rgba(255, 255, 255, 0.1)', 'important');
                        el.style.setProperty('border-radius', '15px', 'important');
                        el.style.setProperty('padding', '1.5rem', 'important');
                        el.style.setProperty('font-family', "'JetBrains Mono', 'Courier New', monospace", 'important');
                        el.style.setProperty('font-weight', '500', 'important');
                    }
                });
            } catch(e) { console.log(e); }
        });
    }
    
    // Run immediately
    brutalForceTextFix();
    
    // Run every 500ms to catch all elements
    setInterval(brutalForceTextFix, 500);
    
    // Run on any DOM changes
    const observer = new MutationObserver(() => {
        setTimeout(brutalForceTextFix, 100);
    });
    observer.observe(document.body, { 
        childList: true, 
        subtree: true, 
        attributes: true,
        attributeOldValue: true,
        characterData: true,
        characterDataOldValue: true
    });
    
    // Run on all events
    ['click', 'focus', 'change', 'input', 'scroll'].forEach(event => {
        document.addEventListener(event, () => setTimeout(brutalForceTextFix, 50));
    });
    </script>
    """, height=0)

    # Force text color with Advanced JavaScript
    st.components.v1.html("""
    <script>
    function superBrutalForceTextFix() {
        // ALL POSSIBLE ALERT/INFO BOX SELECTORS
        const alertSelectors = [
            '.stAlert', '.stAlert *',
            '.stSuccess', '.stSuccess *', 
            '.stInfo', '.stInfo *',
            '.stWarning', '.stWarning *',
            '.stError', '.stError *',
            '[data-testid="stAlert"]', '[data-testid="stAlert"] *',
            '[data-testid="stSuccess"]', '[data-testid="stSuccess"] *',
            '[data-testid="stInfo"]', '[data-testid="stInfo"] *',
            '[data-testid="stWarning"]', '[data-testid="stWarning"] *',
            '[data-testid="stError"]', '[data-testid="stError"] *',
            '.element-container .stAlert', '.element-container .stAlert *',
            '.element-container .stSuccess', '.element-container .stSuccess *',
            '.element-container .stInfo', '.element-container .stInfo *',
            '.element-container .stWarning', '.element-container .stWarning *',
            '.element-container .stError', '.element-container .stError *',
            'div[data-testid="stTooltipHoverTarget"]',
            'div[data-testid="stTooltipHoverTarget"] *'
        ];
        
        alertSelectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    if (el) {
                        // Check if element has white/light background
                        const computedStyle = window.getComputedStyle(el);
                        const bgColor = computedStyle.backgroundColor;
                        
                        if (bgColor.includes('255, 255, 255') || bgColor === 'white' || bgColor === 'rgb(255, 255, 255)') {
                            el.style.setProperty('color', '#1a202c', 'important');
                            el.style.setProperty('font-weight', '600', 'important');
                            el.style.setProperty('text-shadow', 'none', 'important');
                            el.style.setProperty('-webkit-text-fill-color', '#1a202c', 'important');
                        }
                        
                        // Force for all alert-like elements anyway
                        if (el.className && (el.className.includes('stAlert') || el.className.includes('stSuccess') || 
                            el.className.includes('stInfo') || el.className.includes('stWarning') || 
                            el.className.includes('stError'))) {
                            el.style.setProperty('color', '#1a202c', 'important');
                            el.style.setProperty('font-weight', '600', 'important');
                            el.style.setProperty('text-shadow', 'none', 'important');
                            el.style.setProperty('-webkit-text-fill-color', '#1a202c', 'important');
                        }
                    }
                });
            } catch(e) { console.log('Alert selector error:', e); }
        });
        
        // CHAT MESSAGE SELECTORS
        const chatSelectors = [
            '.stChatMessage', '.stChatMessage *',
            '[data-testid="stChatMessage"]', '[data-testid="stChatMessage"] *',
            '[data-testid="chatAvatarIcon-user"]', '[data-testid="chatAvatarIcon-assistant"]',
            'div[data-testid*="chat"]', 'div[data-testid*="chat"] *'
        ];
        
        chatSelectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    if (el) {
                        el.style.setProperty('color', '#1a202c', 'important');
                        el.style.setProperty('font-weight', '500', 'important');
                        el.style.setProperty('text-shadow', 'none', 'important');
                        el.style.setProperty('-webkit-text-fill-color', '#1a202c', 'important');
                    }
                });
            } catch(e) { console.log('Chat selector error:', e); }
        });
        
        // GENERIC WHITE BACKGROUND ELEMENTS
        const allDivs = document.querySelectorAll('div');
        allDivs.forEach(div => {
            try {
                const computedStyle = window.getComputedStyle(div);
                const bgColor = computedStyle.backgroundColor;
                
                // If element has white background, force dark text
                if (bgColor === 'white' || bgColor === 'rgb(255, 255, 255)' || 
                    bgColor.includes('255, 255, 255') || bgColor.includes('rgba(255, 255, 255')) {
                    
                    div.style.setProperty('color', '#1a202c', 'important');
                    div.style.setProperty('font-weight', '600', 'important');
                    div.style.setProperty('text-shadow', 'none', 'important');
                    div.style.setProperty('-webkit-text-fill-color', '#1a202c', 'important');
                    
                    // Also fix all children
                    const children = div.querySelectorAll('*');
                    children.forEach(child => {
                        child.style.setProperty('color', '#1a202c', 'important');
                        child.style.setProperty('font-weight', '600', 'important');
                        child.style.setProperty('text-shadow', 'none', 'important');
                        child.style.setProperty('-webkit-text-fill-color', '#1a202c', 'important');
                    });
                }
            } catch(e) { console.log('Div check error:', e); }
        });
        
        // CODE BLOCKS - KEEP DARK
        const codeSelectors = [
            '.stCodeBlock', '.stCodeBlock *',
            'code', 'pre',
            '.stCode', '.stCode *',
            'div[data-testid="stCodeBlock"]', 'div[data-testid="stCodeBlock"] *'
        ];
        
        codeSelectors.forEach(selector => {
            try {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    if (el) {
                        el.style.setProperty('background-color', 'rgba(45, 55, 72, 0.95)', 'important');
                        el.style.setProperty('color', '#e2e8f0', 'important');
                        el.style.setProperty('border-radius', '15px', 'important');
                        el.style.setProperty('font-weight', '500', 'important');
                    }
                });
            } catch(e) { console.log('Code selector error:', e); }
        });
    }
    
    // Run immediately and very frequently
    superBrutalForceTextFix();
    setInterval(superBrutalForceTextFix, 200);
    
    // Run on DOM changes
    const observer = new MutationObserver(() => {
        setTimeout(superBrutalForceTextFix, 50);
    });
    observer.observe(document.body, { 
        childList: true, 
        subtree: true, 
        attributes: true,
        characterData: true
    });
    
    // Run on all possible events
    ['click', 'focus', 'change', 'input', 'scroll', 'resize', 'load'].forEach(event => {
        document.addEventListener(event, () => setTimeout(superBrutalForceTextFix, 25));
        window.addEventListener(event, () => setTimeout(superBrutalForceTextFix, 25));
    });
    </script>
    """, height=0)

    # ===== FINAL BRUTAL CSS FORCE TECHNIQUE =====
    st.markdown("""
    <style>
    /* ===== ULTIMATE FORCE FOR ALL PROBLEM ELEMENTS ===== */
    
    /* ALERT BOXES - MAXIMUM OVERRIDE */
    .stAlert, [data-testid="stAlert"], 
    .stSuccess, [data-testid="stSuccess"],
    .stInfo, [data-testid="stInfo"],
    .stWarning, [data-testid="stWarning"],
    .stError, [data-testid="stError"] {
        background: rgba(255, 255, 255, 0.98) !important;
        color: #1a202c !important;
        font-weight: 700 !important;
        border-radius: 15px !important;
        border: 2px solid rgba(138, 43, 226, 0.3) !important;
        padding: 1.2rem !important;
        margin: 1rem 0 !important;
        backdrop-filter: blur(10px) !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    .stAlert *, [data-testid="stAlert"] *,
    .stSuccess *, [data-testid="stSuccess"] *,
    .stInfo *, [data-testid="stInfo"] *,
    .stWarning *, [data-testid="stWarning"] *,
    .stError *, [data-testid="stError"] * {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
        background: transparent !important;
    }
    
    .stAlert > div, [data-testid="stAlert"] > div,
    .stSuccess > div, [data-testid="stSuccess"] > div,
    .stInfo > div, [data-testid="stInfo"] > div,
    .stWarning > div, [data-testid="stWarning"] > div,
    .stError > div, [data-testid="stError"] > div {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
        background: transparent !important;
    }
    
    /* CHAT MESSAGES - MAXIMUM OVERRIDE */
    .stChatMessage, [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.98) !important;
        color: #1a202c !important;
        font-weight: 600 !important;
        border-radius: 15px !important;
        border: 2px solid rgba(138, 43, 226, 0.3) !important;
        padding: 1.2rem !important;
        margin: 1rem 0 !important;
        backdrop-filter: blur(10px) !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    .stChatMessage *, [data-testid="stChatMessage"] * {
        color: #1a202c !important;
        font-weight: 600 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
        background: transparent !important;
    }
    
    /* GENERIC WHITE BACKGROUND DIVS */
    div[style*="background-color: rgb(255, 255, 255)"],
    div[style*="background-color: white"],
    div[style*="background: rgb(255, 255, 255)"],
    div[style*="background: white"] {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    div[style*="background-color: rgb(255, 255, 255)"] *,
    div[style*="background-color: white"] *,
    div[style*="background: rgb(255, 255, 255)"] *,
    div[style*="background: white"] * {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    /* BUTTONS - DARK TEXT */
    .stButton > button {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    /* ANY P TAG IN WHITE CONTAINER */
    p {
        color: inherit !important;
        font-weight: inherit !important;
    }
    
    /* ELEMENT CONTAINERS */
    .element-container .stAlert,
    .element-container .stSuccess,
    .element-container .stInfo,
    .element-container .stWarning,
    .element-container .stError {
        background: rgba(255, 255, 255, 0.98) !important;
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    
    .element-container .stAlert *,
    .element-container .stSuccess *,
    .element-container .stInfo *,
    .element-container .stWarning *,
    .element-container .stError * {
        color: #1a202c !important;
        font-weight: 700 !important;
        text-shadow: none !important;
        -webkit-text-fill-color: #1a202c !important;
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# AI Configuration
# =============================================================================

# Multiple API keys for rotation
DEFAULT_API_KEYS = [
    "AIzaSyA7_HUTpwsa8V05hj53wx8bZYsUqodjDH0",
    "AIzaSyDbAODjEuTkTt0kdsOVOpmVOt6jhxxRgL4"
]

def show_typing_effect(container, text, typing_speed=0.03):
    """Show REALISTIC human-like typing effect with random speed, pauses, and corrections"""
    import time
    import random
    
    # Create unique ID for this typing instance
    unique_id = f"typing_{int(time.time() * 1000)}"
    
    # Use st.components.v1.html to execute JavaScript properly
    st.components.v1.html(f"""
    <div id="{unique_id}-container" style="background: rgba(40, 80, 40, 0.9); color: #FFFFFF; padding: 1rem; 
                border-radius: 15px; border: 2px solid rgba(50, 205, 50, 0.3); margin: 1rem 0;">
        <p style="color: #90EE90; margin: 0; font-weight: 600;">
            ✨ <span id="{unique_id}-text"></span><span id="{unique_id}-cursor" style="animation: blink 1s infinite;">|</span>
        </p>
    </div>
    
    <script>
    (function() {{
        const fullText = `{text}`;
        const typewriterElement = document.getElementById('{unique_id}-text');
        const cursor = document.getElementById('{unique_id}-cursor');
        
        if (!typewriterElement || !cursor) return;
        
        let displayText = '';
        let i = 0;
        
        // Human-like typing characteristics
        const baseSpeed = 50;  // Base typing speed
        const speedVariation = 40;  // Random speed variation
        const pauseChance = 0.15;  // 15% chance to pause
        const typoChance = 0.08;  // 8% chance to make typo
        const wrongChars = 'abcdefghijklmnopqrstuvwxyz';
        
        function getRandomSpeed() {{
            return baseSpeed + Math.random() * speedVariation;
        }}
        
        function getRandomPause() {{
            return 200 + Math.random() * 800;  // 200-1000ms pause
        }}
        
        function getRandomChar() {{
            return wrongChars[Math.floor(Math.random() * wrongChars.length)];
        }}
        
        function typeCharacter() {{
            if (i >= fullText.length) {{
                // Typing finished - hide cursor after delay
                setTimeout(() => {{
                    cursor.style.display = 'none';
                }}, 1500);
                return;
            }}
            
            const char = fullText[i];
            
            // Random chance for typo
            if (Math.random() < typoChance && char !== ' ') {{
                // Type wrong character
                const wrongChar = getRandomChar();
                displayText += wrongChar;
                typewriterElement.textContent = displayText;
                
                // Realize mistake and backspace after delay
                setTimeout(() => {{
                    displayText = displayText.slice(0, -1);
                    typewriterElement.textContent = displayText;
                    
                    // Type correct character
                    setTimeout(() => {{
                        displayText += char;
                        typewriterElement.textContent = displayText;
                        i++;
                        
                        // Continue with normal flow
                        setTimeout(typeCharacter, getRandomSpeed());
                    }}, 100 + Math.random() * 200);  // Time to type correct char
                }}, 150 + Math.random() * 300);  // Time to realize mistake
                
            }} else {{
                // Normal typing
                displayText += char;
                typewriterElement.textContent = displayText;
                i++;
                
                // Random pause (thinking)
                if (Math.random() < pauseChance) {{
                    setTimeout(typeCharacter, getRandomPause());
                }} else {{
                    // Variable speed based on character type
                    let speed = getRandomSpeed();
                    
                    // Slower for punctuation and end of words
                    if (',;:.!?'.includes(char)) {{
                        speed += 200;
                    }} else if (char === ' ') {{
                        speed += 100;
                    }} else if (char === char.toUpperCase() && char !== char.toLowerCase()) {{
                        speed += 50;  // Slower for uppercase
                    }}
                    
                    setTimeout(typeCharacter, speed);
                }}
            }}
        }}
        
        // Start typing
        typeCharacter();
    }})();
    </script>
    
    <style>
    @keyframes blink {{
        0%, 50% {{ opacity: 1; }}
        51%, 100% {{ opacity: 0; }}
    }}
    #{unique_id}-cursor {{
        animation: blink 1.2s ease-in-out infinite;
        font-weight: bold;
    }}
    #{unique_id}-text {{
        font-family: 'Courier New', monospace;
        letter-spacing: 0.5px;
    }}
    </style>
    """, height=100)

def show_typing_in_input(target_key, text):
    """Show typing effect directly in input field - realistic human typing"""
    import time
    import random
    
    # JavaScript to simulate human typing in input field
    st.components.v1.html(f"""
    <script>
    (function() {{
        const fullText = `{text}`;
        const inputKey = '{target_key}';
        
        // Better input finder - use multiple strategies
        function findInputByKey(key) {{
            // Strategy 1: Find by exact key match in data-testid
            let input = document.querySelector(`[data-testid="stTextInput"] input[aria-label*="${{key}}"]`);
            if (input) return input;
            
            input = document.querySelector(`[data-testid="stTextArea"] textarea[aria-label*="${{key}}"]`);
            if (input) return input;
            
            // Strategy 2: Find by key in the input's container
            const allInputs = document.querySelectorAll('input[type="text"], textarea');
            for (let inp of allInputs) {{
                // Check if input key contains our target
                if (inp.getAttribute('data-baseweb') && inp.getAttribute('data-baseweb').includes('input')) {{
                    const container = inp.closest('.stTextInput, .stTextArea');
                    if (container) {{
                        // Check previous siblings for matching key
                        let sibling = container.previousElementSibling;
                        while (sibling) {{
                            if (sibling.textContent && sibling.textContent.includes(key)) {{
                                return inp;
                            }}
                            sibling = sibling.previousElementSibling;
                        }}
                    }}
                }}
            }}
            
            // Strategy 3: Find by position and context
            const inputs = document.querySelectorAll('input, textarea');
            for (let inp of inputs) {{
                const parent = inp.closest('div[data-testid="stTextInput"], div[data-testid="stTextArea"]');
                if (parent) {{
                    // Get the section this input belongs to
                    const section = parent.closest('.stContainer, .element-container');
                    if (section && section.innerHTML.includes(key)) {{
                        return inp;
                    }}
                }}
            }}
            
            // Strategy 4: Use data-testid pattern matching
            if (key === 'context_vi') {{
                input = document.querySelector('[data-testid="stTextArea"] textarea');
                if (input && input.placeholder && input.placeholder.includes('Paris')) return input;
            }}
            
            if (key === 'script_idea') {{
                const textareas = document.querySelectorAll('[data-testid="stTextArea"] textarea');
                for (let ta of textareas) {{
                    if (ta.placeholder && ta.placeholder.includes('mùa xuân')) {{
                        return ta;
                    }}
                }}
            }}
            
            if (key.includes('char_name_')) {{
                const inputs = document.querySelectorAll('[data-testid="stTextInput"] input');
                for (let inp of inputs) {{
                    if (inp.placeholder && inp.placeholder.includes('John')) {{
                        return inp;
                    }}
                }}
            }}
            
            if (key.includes('char_desc_')) {{
                const textareas = document.querySelectorAll('[data-testid="stTextArea"] textarea');
                for (let ta of textareas) {{
                    if (ta.placeholder && ta.placeholder.includes('30 tuổi')) {{
                        return ta;
                    }}
                }}
            }}
            
            if (key.includes('voice_desc_')) {{
                const textareas = document.querySelectorAll('[data-testid="stTextArea"] textarea');
                for (let ta of textareas) {{
                    if (ta.placeholder && ta.placeholder.includes('nhỏ nhẹ')) {{
                        return ta;
                    }}
                }}
            }}
            
            if (key === 'sound_vi') {{
                const textareas = document.querySelectorAll('[data-testid="stTextArea"] textarea');
                for (let ta of textareas) {{
                    if (ta.placeholder && ta.placeholder.includes('thì thầm')) {{
                        return ta;
                    }}
                }}
            }}
            
            return null;
        }}
        
        // Wait for DOM to be ready and find input
        function waitForInput(retries = 0) {{
            if (retries > 20) {{
                console.log('Could not find input for key:', inputKey);
                return;
            }}
            
            const input = findInputByKey(inputKey);
            if (input) {{
                typeInInput(input);
            }} else {{
                // Retry after short delay
                setTimeout(() => waitForInput(retries + 1), 500);
            }}
        }}
        
        function typeInInput(inputElement) {{
            console.log('Starting typing in:', inputElement);
            
            inputElement.value = ''; // Clear first
            inputElement.focus(); // Focus on input
            
            let i = 0;
            const baseSpeed = 80; // Base typing speed (ms)
            const speedVariation = 50; // Random variation
            const pauseChance = 0.15; // 15% chance to pause
            const typoChance = 0.08; // 8% chance for typo
            const wrongChars = 'abcdefghijklmnopqrstuvwxyz';
            
            function getRandomSpeed() {{
                return baseSpeed + Math.random() * speedVariation;
            }}
            
            function getRandomPause() {{
                return 400 + Math.random() * 800; // 400-1200ms pause
            }}
            
            function getRandomChar() {{
                return wrongChars[Math.floor(Math.random() * wrongChars.length)];
            }}
            
            function typeNextChar() {{
                if (i >= fullText.length) {{
                    // Typing finished - trigger Streamlit change event
                    inputElement.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    inputElement.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    inputElement.blur(); // Remove focus
                    console.log('Typing completed');
                    return;
                }}
                
                const char = fullText[i];
                
                // Random chance for typo
                if (Math.random() < typoChance && char !== ' ' && char !== '.' && char !== ',' && char !== '!' && char !== '?') {{
                    // Type wrong character
                    const wrongChar = getRandomChar();
                    inputElement.value += wrongChar;
                    
                    // Trigger visual update
                    inputElement.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    
                    // Realize mistake and backspace after delay
                    setTimeout(() => {{
                        inputElement.value = inputElement.value.slice(0, -1);
                        inputElement.dispatchEvent(new Event('input', {{ bubbles: true }}));
                        
                        // Type correct character
                        setTimeout(() => {{
                            inputElement.value += char;
                            inputElement.dispatchEvent(new Event('input', {{ bubbles: true }}));
                            i++;
                            
                            // Continue with normal flow
                            setTimeout(typeNextChar, getRandomSpeed());
                        }}, 100 + Math.random() * 150); // Time to type correct char
                    }}, 250 + Math.random() * 400); // Time to realize mistake
                    
                }} else {{
                    // Normal typing
                    inputElement.value += char;
                    inputElement.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    i++;
                    
                    // Random pause (thinking/hesitation)
                    if (Math.random() < pauseChance) {{
                        setTimeout(typeNextChar, getRandomPause());
                    }} else {{
                        // Variable speed based on character type
                        let speed = getRandomSpeed();
                        
                        // Slower for punctuation and end of sentences
                        if ('.!?'.includes(char)) {{
                            speed += 600; // Long pause after sentences
                        }} else if (',;:'.includes(char)) {{
                            speed += 300; // Medium pause after punctuation
                        }} else if (char === ' ') {{
                            speed += 80; // Slight pause after words
                        }} else if (char === char.toUpperCase() && char !== char.toLowerCase()) {{
                            speed += 40; // Slightly slower for uppercase
                        }}
                        
                        setTimeout(typeNextChar, speed);
                    }}
                }}
            }}
            
            // Start typing with a small delay
            setTimeout(typeNextChar, 800);
        }}
        
        // Start the process
        waitForInput();
    }})();
    </script>
    """, height=0)

def get_current_api_key():
    """Get current API key from session state or default"""
    if 'custom_api_key' in st.session_state and st.session_state.custom_api_key:
        return st.session_state.custom_api_key
    
    # Rotate between default keys
    if 'api_key_index' not in st.session_state:
        st.session_state.api_key_index = 0
    
    return DEFAULT_API_KEYS[st.session_state.api_key_index % len(DEFAULT_API_KEYS)]

def rotate_api_key():
    """Rotate to next API key when current one fails"""
    if 'api_key_index' not in st.session_state:
        st.session_state.api_key_index = 0
    st.session_state.api_key_index = (st.session_state.api_key_index + 1) % len(DEFAULT_API_KEYS)

def call_gemini_api(prompt_text: str) -> str:
    """Call Gemini API for text generation with automatic key rotation"""
    max_retries = len(DEFAULT_API_KEYS)
    
    for attempt in range(max_retries):
        try:
            api_key = get_current_api_key()
            api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
            
            payload = {
                "contents": [{"role": "user", "parts": [{"text": prompt_text}]}],
                "generationConfig": {"responseMimeType": "text/plain"}
            }
            
            response = requests.post(
                api_url,
                headers={'Content-Type': 'application/json'},
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if (result.get('candidates') and len(result['candidates']) > 0 and
                    result['candidates'][0].get('content') and 
                    result['candidates'][0]['content'].get('parts') and
                    len(result['candidates'][0]['content']['parts']) > 0):
                    return result['candidates'][0]['content']['parts'][0]['text'].strip()
            
            # If we get 403 or quota exceeded, try next key
            if response.status_code in [403, 429]:
                rotate_api_key()
                continue
            
            st.error(f"Lỗi API: {response.status_code}")
            return ""
            
        except Exception as e:
            if attempt < max_retries - 1:
                rotate_api_key()
                continue
            st.error(f"Lỗi kết nối AI: {str(e)}")
            return ""
    
    st.error("Tất cả API key đều không khả dụng. Vui lòng thêm API key của bạn.")
    return ""

def call_veo3_api(prompt_text: str) -> Dict:
    """Call VEO 3 API for video generation (placeholder)"""
    # This would be the actual VEO 3 API call
    # For now, return a mock response
    import time
    time.sleep(2)  # Simulate API call
    
    return {
        "status": "success",
        "video_id": f"veo3_{int(time.time())}",
        "video_url": "https://example.com/generated_video.mp4",
        "thumbnail_url": "https://example.com/thumbnail.jpg",
        "duration": 8,
        "resolution": "1080p"
    }

# =============================================================================
# AI Functions - Chuẩn theo manguon.txt
# =============================================================================

def translate_to_english(vietnamese_text: str, field_type: str) -> str:
    """Translate Vietnamese text to English for specific field types"""
    if not vietnamese_text.strip():
        return ""
    
    prompts = {
        "context": f"Dịch chính xác hoàn cảnh sau sang tiếng Anh cho prompt video AI, chỉ trả lời bằng bản dịch: {vietnamese_text}",
        "character": f"Dịch chính xác mô tả nhân vật sau sang tiếng Anh cho prompt video AI, chỉ trả lời bằng bản dịch: {vietnamese_text}",
        "sound": f"Dịch chính xác mô tả âm thanh sau sang tiếng Anh cho prompt video AI, chỉ trả lời bằng bản dịch: {vietnamese_text}",
        "voice": f"Dịch chính xác mô tả giọng nói sau sang tiếng Anh cho prompt video AI, chỉ trả lời bằng bản dịch: {vietnamese_text}"
    }
    
    prompt = prompts.get(field_type, f"Dịch chính xác sang tiếng Anh: {vietnamese_text}")
    return call_gemini_api(prompt)

def suggest_content(field_type: str, field_name: str, current_context: Dict, current_character_name: str = "") -> str:
    """Generate AI suggestions for different content types - chính xác theo manguon.txt"""
    
    # Build context for AI
    context_for_ai = ""
    if current_context.get('context'):
        context_for_ai += f"\n- Hoàn cảnh tổng thể: {current_context['context']}"
    if current_context.get('sound'):
        context_for_ai += f"\n- Âm thanh tổng thể: {current_context['sound']}"
    
    if current_context.get('characters'):
        for idx, char in enumerate(current_context['characters']):
            context_for_ai += f"\n- Nhân vật {idx + 1}"
            if char.get('name'):
                context_for_ai += f" (tên: {char['name']})"
            if char.get('description'):
                context_for_ai += f": {char['description']}"
            if char.get('voice'):
                context_for_ai += f" | Giọng nói: {char['voice']}"
            if char.get('dialogue'):
                context_for_ai += f" | Lời thoại: {char['dialogue']}"
    
    if context_for_ai:
        context_for_ai = f"\n\nDựa trên các yếu tố đã có:\n{context_for_ai.strip()}"
    
    # Generate prompts based on type - theo đúng manguon.txt
    if field_type == 'characterName':
        prompt_text = f"""Chỉ gợi ý một {field_name} sáng tạo và ngắn gọn bằng tiếng Việt cho một nhân vật mới. Không thêm bất kỳ văn bản giải thích, tiêu đề, hoặc nội dung nào khác ngoài chính {field_name}.
        {context_for_ai}
        
        Yêu cầu: Gợi ý cho {field_name}."""
        
    elif field_type == 'voice':
        prompt_text = f"""Chỉ gợi ý một mô tả về đặc điểm giọng nói (như tông, âm sắc, cảm xúc, tốc độ, phong cách) sáng tạo và ngắn gọn bằng tiếng Việt cho một nhân vật. Không thêm bất kỳ văn bản giải thích, tiêu đề, hoặc nội dung nào khác ngoài chính mô tả giọng nói.
        {context_for_ai}
        {f"(Dành cho nhân vật tên: {current_character_name})" if current_character_name else ""}
        
        Yêu cầu: Gợi ý cho mô tả giọng nói."""
        
    elif field_type == 'sound':
        prompt_text = f"""Chỉ gợi ý các yếu tố âm thanh sáng tạo và ngắn gọn bằng tiếng Việt cho một cảnh quay video. Định dạng nó dưới dạng hiệu ứng âm thanh (SFX) hoặc âm thanh môi trường (AMBIENCE), sử dụng các tiền tố như 'SFX:' hoặc 'AMBIENCE:' nếu phù hợp. Không thêm bất kỳ văn bản giải thích, tiêu đề, hoặc nội dung nào khác ngoài chính các yếu tố âm thanh.
        {context_for_ai}
        
        Yêu cầu: Gợi ý cho âm thanh."""
        
    else:  # context, character
        prompt_text = f"""Chỉ gợi ý một {field_name} sáng tạo và ngắn gọn bằng tiếng Việt cho một cảnh quay video. Không thêm bất kỳ văn bản giải thích, tiêu đề, hoặc nội dung nào khác ngoài chính mô tả {field_name}.
        {context_for_ai}
        {f"(Dành cho nhân vật tên: {current_character_name})" if field_type == 'character' and current_character_name else ""}
        
        Yêu cầu: Gợi ý cho {field_name}."""
    
    return call_gemini_api(prompt_text)

def expand_dialogue(dialogue: str) -> str:
    """Expand Vietnamese dialogue - theo đúng manguon.txt"""
    if not dialogue.strip():
        return ""
    
    prompt = f"""Mở rộng lời thoại tiếng Việt sau đây cho một cảnh quay video, giữ nguyên tông giọng và ý nghĩa ban đầu. Cung cấp một phiên bản dài hơn một chút hoặc một vài dòng thay thế. Chỉ trả lời bằng lời thoại đã mở rộng.
Lời thoại: {dialogue}"""
    
    return call_gemini_api(prompt)

def generate_long_script(idea: str) -> str:
    """Generate long video script from idea - theo đúng manguon.txt"""
    prompt = f"""Tạo một kịch bản nháp chi tiết cho một video dài dựa trên ý tưởng tiếng Việt sau đây.
Kịch bản phải được chia thành các phân cảnh. MỖI PHÂN CẢNH PHẢI TUÂN THỦ ĐỊNH DẠNG SAU ĐÂY MỘT CÁCH CHÍNH XÁC, KHÔNG THÊM BẤT BẤT KỲ VĂN BẢN NÀO KHÁC NGOÀI NỘI DUNG YÊU CẦU. Đảm bảo các tiêu đề như [Hoàn cảnh], [Mô tả nhân vật], [Lời thoại], [Âm thanh] được viết chính xác và không có dấu hai chấm sau dấu ngoặc vuông.
Trong [Mô tả nhân vật], nếu có nhiều nhân vật, hãy mô tả từng nhân vật một cách rõ ràng, có thể đặt tên cho nhân vật (ví dụ: "Nhân vật A: mô tả...", "Nhân vật B: mô tả...").

Ý tưởng Clip Dài:
{idea}

Định dạng đầu ra:
Cảnh 1:
[Hoàn cảnh]
<nội dung hoàn cảnh>
[Mô tả nhân vật]
<nội dung mô tả nhân vật 1, có thể bao gồm tên>
<nội dung mô tả nhân vật 2, có thể bao gồm tên (nếu có)>
[Lời thoại]
<"Nhân vật A: Lời thoại của A...">
<"Nhân vật B: Lời thoại của B...">
[Âm thanh]
<nội dung âm thanh (có tiền tố SFX: hoặc AMBIENCE:)>

Cảnh 2:
... (tương tự)"""
    
    return call_gemini_api(prompt)

def convert_script_to_prompts(script: str) -> List[Dict]:
    """Convert script to individual Veo3 prompts - theo đúng manguon.txt"""
    prompt = f"""Chuyển đổi kịch bản tiếng Việt sau thành các prompt riêng biệt cho Veo 3. Mỗi cảnh trong kịch bản sẽ trở thành một prompt hoàn chỉnh.

QUY TẮC CHUYỂN ĐỔI:
1. Dịch "Hoàn cảnh", "Mô tả nhân vật", "Âm thanh" sang tiếng Anh
2. GIỮ NGUYÊN "Lời thoại" bằng tiếng Việt
3. Tích hợp tất cả thành một prompt liền mạch cho mỗi cảnh
4. Định dạng: Setting: [hoàn cảnh]. Characters: [nhân vật]. [Lời thoại tiếng Việt]. Audio: [âm thanh].

KỊCH BẢN:
{script}

Trả về theo định dạng:
=== CẢNH 1 ===
[Prompt hoàn chỉnh cho cảnh 1]

=== CẢNH 2 ===
[Prompt hoàn chỉnh cho cảnh 2]

... (tiếp tục cho các cảnh khác)"""
    
    result = call_gemini_api(prompt)
    
    # Parse scenes
    scenes = []
    if result:
        parts = result.split("=== CẢNH")
        for i, part in enumerate(parts[1:], 1):
            if "===" in part:
                scene_content = part.split("===")[1].strip()
                scenes.append({
                    "scene_number": i,
                    "prompt": scene_content
                })
    
    return scenes

def generate_final_prompt(context_vi: str, characters: List[Dict], sound_vi: str) -> str:
    """Generate final prompt exactly like manguon.txt"""
    
    # Translate components to English
    context_en = translate_to_english(context_vi, "context") if context_vi else ""
    sound_en = translate_to_english(sound_vi, "sound") if sound_vi else ""
    
    # Build prompt parts
    prompt_parts = []
    
    # Add setting
    if context_en:
        prompt_parts.append(f"Setting: {context_en}")
    
    # Add characters
    for char in characters:
        if char.get('description'):
            char_desc_en = translate_to_english(char['description'], "character")
            if char_desc_en:
                char_name = char.get('name', 'Character')
                prompt_parts.append(f"Character - {char_name}: {char_desc_en}")
        
        if char.get('voice'):
            voice_en = translate_to_english(char['voice'], "voice")
            if voice_en:
                char_name = char.get('name', 'Character')
                prompt_parts.append(f"{char_name} voice: {voice_en}")
    
    # Add dialogues (keep Vietnamese)
    for char in characters:
        if char.get('dialogue'):
            char_name = char.get('name', 'Character')
            prompt_parts.append(f'{char_name}: "{char["dialogue"]}"')
    
    # Add audio
    if sound_en:
        prompt_parts.append(f"Audio: {sound_en}")
    
    return ". ".join(prompt_parts)

# =============================================================================
# ADVANCED FEATURE PAGES - 7 TÍNH NĂNG MỚI
# =============================================================================

def ai_assistant_page():
    """AI Assistant Advanced page"""
    st.header("🤖 Chat với AI Assistant")
    
    st.info("💬 Trợ lý AI thông minh - hỗ trợ tạo content và video VEO3")
    
    # Initialize chat history
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Xin chào! Tôi là AI Assistant. Tôi có thể giúp bạn:\n\n🎬 Tạo ý tưởng video\n📝 Viết script\n🎯 Tối ưu content\n📊 Phân tích xu hướng\n\nBạn cần hỗ trợ gì?"}
        ]
    
    # Display chat messages
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Đang suy nghĩ..."):
                ai_prompt = f"""Bạn là AI Assistant cho VEO3 Vietnamese. Trả lời câu hỏi sau bằng tiếng Việt:

Câu hỏi: {prompt}

Hãy trả lời hữu ích, liên quan đến tạo video, content creation."""
                
                response = call_gemini_api(ai_prompt)
                if response:
                    st.markdown(response)
                    st.session_state.chat_messages.append({"role": "assistant", "content": response})
                else:
                    error_msg = "Xin lỗi, tôi gặp sự cố. Vui lòng thử lại."
                    st.markdown(error_msg)
                    st.session_state.chat_messages.append({"role": "assistant", "content": error_msg})
    
    # Quick actions
    st.subheader("⚡ Gợi ý nhanh")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💡 Ý tưởng video hot"):
            suggestion = "🔥 **Ý tưởng video trending:**\n\n• Daily vlog - cuộc sống thường ngày\n• Food review - đánh giá món ăn\n• Travel vlog - du lịch khám phá\n• Tech unboxing - mở hộp công nghệ\n• Beauty tips - mẹo làm đẹp"
            st.session_state.chat_messages.append({"role": "assistant", "content": suggestion})
            st.rerun()
    
    with col2:
        if st.button("📈 Hashtag trending"):
            hashtags = "📊 **Hashtag hot hiện tại:**\n\n#vietnam #viral #trending #fyp #xuhuong #lifestyle #food #travel #beauty #tech #daily #vlog #review #tips"
            st.session_state.chat_messages.append({"role": "assistant", "content": hashtags})
            st.rerun()
    
    with col3:
        if st.button("🎬 Mẹo tạo video"):
            tips = "🎯 **Mẹo tạo video hiệu quả:**\n\n• Hook đầu video trong 3s đầu\n• Ánh sáng tự nhiên tốt nhất\n• Âm thanh rõ ràng quan trọng\n• Góc quay đa dạng\n• Call-to-action cuối video"
            st.session_state.chat_messages.append({"role": "assistant", "content": tips})
            st.rerun()
    
    # Clear chat
    if st.button("🗑️ Xóa lịch sử chat"):
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Xin chào! Tôi là AI Assistant. Bạn cần hỗ trợ gì?"}
        ]
        st.rerun()

def mobile_app_page():
    """Mobile App Design page"""
    try:
        from mobile_app_design import create_mobile_app
        mobile_app = create_mobile_app()
        mobile_app.render_mobile_app_page()
    except Exception as e:
        st.error(f"Lỗi Mobile App: {str(e)}")
        # Fallback content
        st.markdown("""
        <div class="vietnamese-glass">
            <h1>📱 Mobile App Design</h1>
            <p>🚧 Tính năng đang được phát triển. Vui lòng quay lại sau!</p>
            
            <h3>🎨 Sắp có:</h3>
            <ul>
                <li>📱 UI/UX design mockup</li>
                <li>⚛️ React Native tech stack</li>
                <li>🗺️ Development roadmap</li>
                <li>💰 Monetization strategy</li>
                <li>🚀 App store optimization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def templates_page():
    """Professional Templates page"""
    try:
        from professional_templates import create_professional_templates
        templates = create_professional_templates()
        templates.render_templates_page()
    except Exception as e:
        st.error(f"Lỗi Templates: {str(e)}")
        # Fallback content
        st.markdown("""
        <div class="vietnamese-glass">
            <h1>🎨 Professional Templates</h1>
            <p>🚧 Tính năng đang được phát triển. Vui lòng quay lại sau!</p>
            
            <h3>🎯 Sắp có 150+ Templates:</h3>
            <ul>
                <li>🍜 Ẩm thực Việt Nam</li>
                <li>🏖️ Du lịch trong nước</li>
                <li>💄 Lifestyle & Beauty</li>
                <li>🎓 Giáo dục & Học tập</li>
                <li>🏢 Kinh doanh & Khởi nghiệp</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def monetization_page():
    """Monetization System page"""
    try:
        from monetization_system import create_monetization_system
        monetization = create_monetization_system()
        monetization.render_monetization_page()
    except Exception as e:
        st.error(f"Lỗi Monetization: {str(e)}")
        # Fallback content
        st.markdown("""
        <div class="vietnamese-glass">
            <h1>💰 Monetization System</h1>
            <p>🚧 Tính năng đang được phát triển. Vui lòng quay lại sau!</p>
            
            <h3>💳 Các gói sắp có:</h3>
            <ul>
                <li>🆓 Free - 5 videos/tháng</li>
                <li>⭐ Basic - 99K - 25 videos/tháng</li>
                <li>🚀 Pro - 199K - 100 videos/tháng</li>
                <li>👑 Ultimate - 499K - Unlimited</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def community_page():
    """Community & Marketing page"""
    try:
        from community_marketing import create_community_marketing
        community = create_community_marketing()
        community.render_community_marketing_page()
    except Exception as e:
        st.error(f"Lỗi Community: {str(e)}")
        # Fallback content
        st.markdown("""
        <div class="vietnamese-glass">
            <h1>🌐 Community & Marketing</h1>
            <p>🚧 Tính năng đang được phát triển. Vui lòng quay lại sau!</p>
            
            <h3>🎉 Sắp có:</h3>
            <ul>
                <li>👥 Community feed & groups</li>
                <li>🏆 Contest 50M VNĐ</li>
                <li>🌟 Influencer program</li>
                <li>📊 Marketing analytics</li>
                <li>🎯 Viral campaign tools</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def utility_page():
    """Utility Features page"""
    st.header("🔧 Utility Features")
    
    st.info("🛠️ Các công cụ hỗ trợ tạo content hiệu quả")
    
    # Text Tools Section
    st.subheader("📝 Text Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔤 Text Generator**")
        text_type = st.selectbox(
            "Loại text:",
            ["Video Title", "Video Description", "Hashtags", "Call-to-Action"]
        )
        
        text_topic = st.text_input("Chủ đề:", placeholder="Ví dụ: review điện thoại mới")
        
        if st.button("✨ Tạo Text"):
            if text_topic:
                with st.spinner("Đang tạo..."):
                    prompt = f"Tạo {text_type} bằng tiếng Việt cho chủ đề: {text_topic}. Hãy viết ngắn gọn, hấp dẫn và phù hợp với social media."
                    result = call_gemini_api(prompt)
                    if result:
                        st.success("✅ Đã tạo!")
                        st.code(result)
                    else:
                        st.error("❌ Lỗi khi tạo text")
    
    with col2:
        st.markdown("**🎵 Idea Generator**")
        content_type = st.selectbox(
            "Loại content:",
            ["TikTok Video", "YouTube Shorts", "Instagram Reel", "Facebook Video"]
        )
        
        niche = st.selectbox(
            "Lĩnh vực:",
            ["Lifestyle", "Food", "Tech", "Beauty", "Travel", "Education", "Entertainment"]
        )
        
        if st.button("💡 Tạo Ý tưởng"):
            with st.spinner("Đang nghĩ..."):
                prompt = f"Tạo 5 ý tưởng {content_type} trong lĩnh vực {niche} bằng tiếng Việt. Mỗi ý tưởng ghi rõ concept, hook và cách thực hiện."
                result = call_gemini_api(prompt)
                if result:
                    st.success("✅ Có ý tưởng rồi!")
                    st.markdown(result)
                else:
                    st.error("❌ Lỗi khi tạo ý tưởng")
    
    st.divider()
    
    # SEO & Analytics Tools
    st.subheader("📊 SEO & Analytics Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🏷️ Hashtag Generator**")
        hashtag_topic = st.text_input("Chủ đề hashtag:", placeholder="Ví dụ: ẩm thực Việt Nam")
        
        if st.button("🔍 Tạo Hashtags"):
            if hashtag_topic:
                with st.spinner("Đang tìm hashtags..."):
                    prompt = f"Tạo 20 hashtag tiếng Việt và tiếng Anh cho chủ đề '{hashtag_topic}'. Chia thành 3 nhóm: Popular, Niche, Branded."
                    result = call_gemini_api(prompt)
                    if result:
                        st.success("✅ Hashtags ready!")
                        st.text_area("Copy hashtags:", result, height=150)
                    else:
                        st.error("❌ Lỗi khi tạo hashtags")
    
    with col2:
        st.markdown("**📈 Content Calendar**")
        calendar_niche = st.selectbox(
            "Lĩnh vực content:",
            ["Personal Brand", "Business", "Food Blog", "Tech Review", "Beauty", "Travel"],
            key="calendar_niche"
        )
        
        days = st.slider("Số ngày:", 7, 30, 7)
        
        if st.button("📅 Tạo Calendar"):
            with st.spinner("Đang lập kế hoạch..."):
                prompt = f"Tạo content calendar {days} ngày cho {calendar_niche} bằng tiếng Việt. Mỗi ngày ghi rõ: chủ đề, loại content, platform, thời gian đăng."
                result = call_gemini_api(prompt)
                if result:
                    st.success("✅ Calendar done!")
                    st.markdown(result)
                else:
                    st.error("❌ Lỗi khi tạo calendar")
    
    st.divider()
    
    # Quick Tools
    st.subheader("⚡ Quick Tools")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**⏰ Best Time to Post**")
        if st.button("🕐 Xem thời gian tốt"):
            st.info("""
            **📱 TikTok:** 6-10h, 19-24h
            **📺 YouTube:** 14-16h, 20-22h  
            **📷 Instagram:** 11-13h, 17-19h
            **👥 Facebook:** 9-10h, 15-16h
            """)
    
    with col2:
        st.markdown("**📐 Video Specs**")
        if st.button("📏 Xem kích thước"):
            st.info("""
            **TikTok:** 1080x1920 (9:16)
            **YouTube Shorts:** 1080x1920 (9:16)
            **Instagram Reel:** 1080x1920 (9:16)
            **YouTube:** 1920x1080 (16:9)
            """)
    
    with col3:
        st.markdown("**🎨 Color Palette**")
        if st.button("🌈 Tạo màu sắc"):
            colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD"]
            st.color_picker("Màu chính:", colors[0])
            st.write("Palette gợi ý:", " | ".join(colors))

def targeting_page():
    """Vietnam Targeting page"""
    try:
        from vietnam_targeting import create_vietnam_targeting
        targeting = create_vietnam_targeting()
        targeting.render_vietnam_targeting_page()
    except Exception as e:
        st.error(f"Lỗi Vietnam Targeting: {str(e)}")
        # Fallback content
        st.markdown("""
        <div class="vietnamese-glass">
            <h1>🎯 Vietnam Targeting</h1>
            <p>🚧 Tính năng đang được phát triển. Vui lòng quay lại sau!</p>
            
            <h3>🗺️ Sắp có:</h3>
            <ul>
                <li>🏛️ Targeting Miền Bắc</li>
                <li>🌴 Targeting Miền Nam</li>
                <li>🏔️ Targeting Miền Trung</li>
                <li>🎭 Dialect optimization</li>
                <li>📊 Regional analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# PAGE FUNCTIONS - Cập nhật theo chuẩn manguon.txt
# =============================================================================

def home_page():
    """Trang chủ với core features"""
    st.markdown("""
        <div class="luxury-card fade-in">
            <h1 style="text-align: center;">🏠 VEO3 ULTIMATE - VIETNAMESE EDITION</h1>
            <p style="text-align: center; font-size: 1.2rem;">Nền tảng AI tạo video chuyên nghiệp cho Việt Nam</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Core Features Section
    st.subheader("🎬 Tính năng Cốt lõi")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card fade-in">
            <h2>🎬</h2>
            <p>Tạo Prompt AI</p>
            <p>Chuyển đổi ý tưởng thành prompt chuyên nghiệp</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card fade-in">
            <h2>🎭</h2>
            <p>Kịch Bản Dài</p>
            <p>Tạo kịch bản nhiều cảnh cho video dài</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card fade-in">
            <h2>🎯</h2>
            <p>Trình Tạo Video</p>
            <p>Tạo video với VEO 3 API</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Advanced Features Section - CHỈ 2 TÍNH NĂNG
    st.subheader("🚀 Tính năng Nâng cao")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="luxury-card fade-in">
            <h3 class="text-gradient">🤖 AI Assistant Advanced</h3>
            <p>• Chatbot AI 24/7 tiếng Việt</p>
            <p>• Phân tích xu hướng VN</p>
            <p>• Tối ưu platform TikTok/YouTube</p>
            <p>• Sentiment analysis</p>
            <p>• Auto content generation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="luxury-card fade-in">
            <h3 class="text-gradient">🔧 Utility Features</h3>
            <p>• Video converter multi-platform</p>
            <p>• AI text & voice generator</p>
            <p>• Image editing tools</p>
            <p>• Social media scheduler</p>
            <p>• Productivity analytics</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Quick stats
    st.subheader("📊 Thống kê VEO3 Ultimate")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎬 Videos Created", "1,247", "+156")
    with col2:
        st.metric("🤖 AI Features", "5+", "Advanced")
    with col3:
        st.metric("⚡ Response Time", "0.8s", "Ultra Fast")
    with col4:
        st.metric("🌟 User Rating", "4.9/5", "Excellent")

def prompt_generator_tab():
    """Prompt Generator Tab - theo đúng chức năng manguon.txt"""
    st.header("🎬 Tạo Prompt AI")
    
    # Custom styled info box with dark background
    st.markdown("""
    <div style="background: rgba(30, 30, 50, 0.9); color: #FFFFFF; padding: 1.5rem; 
                border-radius: 15px; border: 2px solid rgba(138, 43, 226, 0.3); margin-bottom: 2rem;">
        <h4 style="color: #FFFFFF; margin-bottom: 1rem;">ℹ️ Hướng dẫn sử dụng</h4>
        <p style="color: #FFFFFF; margin: 0;">
            Nhập các mô tả bằng tiếng Việt vào các ô bên dưới. Hệ thống sẽ tự động dịch các phần 
            'Hoàn cảnh', 'Mô tả nhân vật', 'Âm thanh' sang tiếng Anh, giữ nguyên 'Lời thoại' tiếng Việt, 
            sau đó tạo prompt cuối cùng cho Veo 3. Sử dụng các nút ✨ để nhận gợi ý hoặc mở rộng nội dung.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'characters' not in st.session_state:
        st.session_state.characters = [{'name': '', 'description': '', 'voice': '', 'dialogue': ''}]
    if 'current_context' not in st.session_state:
        st.session_state.current_context = {}
    
    # Context input
    st.subheader("🌍 Hoàn cảnh (tiếng Việt)")
    col1, col2 = st.columns([4, 1])
    with col1:
        context_vi = st.text_area(
            "Mô tả hoàn cảnh:",
            value=st.session_state.get('context_suggestion', ''),
            placeholder="Ví dụ: Buổi sáng sương sớm, tại một quán cà phê nhỏ ven đường ở Paris...",
            key="context_vi",
            label_visibility="collapsed"
        )
    with col2:
        if st.button("✨ Gợi ý", key="suggest_context"):
            with st.spinner("🤖 Đang suy nghĩ gợi ý..."):
                suggestion = suggest_content("context", "hoàn cảnh", st.session_state.current_context)
                if suggestion:
                    # Show typing effect first
                    st.session_state.show_context_typing = True
                    st.session_state.context_ai_suggestion = suggestion
                    st.rerun()
                else:
                    st.error("❌ Không thể tạo gợi ý lúc này. Vui lòng thử lại.")
    
    # Show typing effect for context suggestion  
    if st.session_state.get('show_context_typing', False):
        st.markdown("**🤖 AI đang gõ gợi ý hoàn cảnh:**")
        
        # Display typing effect
        typing_text = st.session_state.get('context_ai_suggestion', '')
        show_typing_effect(st.empty(), typing_text)
        
        # Buttons to apply or skip
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Điền vào ô", key="apply_context_typing"):
                st.session_state.context_suggestion = st.session_state.context_ai_suggestion
                st.session_state.show_context_typing = False
                st.session_state.context_ai_suggestion = ""
                st.success("✅ Đã điền gợi ý vào ô nhập liệu!")
                st.rerun()
        
        with col2:
            if st.button("❌ Bỏ qua", key="skip_context_typing"):
                st.session_state.show_context_typing = False
                st.session_state.context_ai_suggestion = ""
                st.rerun()
    
    st.session_state.current_context['context'] = context_vi
    
    # Character management
    st.subheader("👥 Quản lý Nhân vật")
    
    for i, char in enumerate(st.session_state.characters):
        with st.expander(f"Nhân vật {i+1}", expanded=True):
            
            # Character Name
            st.write("**Tên Nhân vật (tiếng Việt):**")
            col1, col2 = st.columns([4, 1])
            with col1:
                char_name = st.text_input(
                    "Tên:",
                    value=st.session_state.get(f'char_name_suggestion_{i}', char.get('name', '')),
                    placeholder="Ví dụ: John, Anna, Người kể chuyện...",
                    key=f"char_name_{i}",
                    label_visibility="collapsed"
                )
                st.session_state.characters[i]['name'] = char_name
            with col2:
                if st.button("✨", key=f"suggest_name_{i}"):
                    with st.spinner("🤖 Đang suy nghĩ tên..."):
                        suggestion = suggest_content("characterName", "tên nhân vật", st.session_state.current_context)
                        if suggestion:
                            # Update session state directly
                            st.session_state[f'char_name_suggestion_{i}'] = suggestion
                            st.success("✅ Đã điền tên vào ô nhập liệu!")
                            st.rerun()
                        else:
                            st.error("❌ Không thể tạo gợi ý lúc này.")
            
            # Show typing effect for character name suggestion
            if st.session_state.get(f'show_name_typing_{i}', False):
                st.markdown(f"**🤖 AI đang gợi ý tên nhân vật {i+1}:**")
                typing_container = st.empty()
                
                # Get suggestion if not already generated
                if not st.session_state.get(f'name_ai_suggestion_{i}'):
                    with st.spinner("Đang tạo gợi ý..."):
                        suggestion = suggest_content("characterName", "tên nhân vật", st.session_state.current_context)
                        st.session_state[f'name_ai_suggestion_{i}'] = suggestion or "Xin lỗi, không thể tạo gợi ý lúc này."
                
                # Show typing effect
                show_typing_effect(typing_container, st.session_state[f'name_ai_suggestion_{i}'])
                
                # Button to apply suggestion
                col_apply, col_skip, col_ignore = st.columns(3)
                with col_apply:
                    if st.button("✅ Áp dụng", key=f"apply_name_{i}"):
                        st.session_state[f'char_name_suggestion_{i}'] = st.session_state[f'name_ai_suggestion_{i}']
                        st.session_state[f'show_name_typing_{i}'] = False
                        st.session_state[f'name_ai_suggestion_{i}'] = ""
                        st.success("✅ Đã áp dụng tên vào ô nhập liệu!")
                        st.rerun()
                
                with col_skip:
                    if st.button("⚡ Điền ngay", key=f"skip_name_typing_{i}"):
                        st.session_state[f'char_name_suggestion_{i}'] = st.session_state[f'name_ai_suggestion_{i}']
                        st.session_state[f'show_name_typing_{i}'] = False
                        st.session_state[f'name_ai_suggestion_{i}'] = ""
                        st.success("⚡ Đã điền tên vào ô nhập liệu!")
                        st.rerun()
                
                with col_ignore:
                    if st.button("❌ Bỏ qua", key=f"ignore_name_{i}"):
                        st.session_state[f'show_name_typing_{i}'] = False
                        st.session_state[f'name_ai_suggestion_{i}'] = ""
                        st.rerun()
            
            # Character Description
            st.write("**Mô tả nhân vật (tiếng Việt):**")
            col1, col2 = st.columns([4, 1])
            with col1:
                char_desc = st.text_area(
                    "Mô tả:",
                    value=st.session_state.get(f'char_desc_suggestion_{i}', char.get('description', '')),
                    placeholder="Ví dụ: Một người phụ nữ khoảng 30 tuổi, với mái tóc nâu gợn sóng...",
                    key=f"char_desc_{i}",
                    label_visibility="collapsed"
                )
                st.session_state.characters[i]['description'] = char_desc
            with col2:
                if st.button("✨", key=f"suggest_desc_{i}"):
                    with st.spinner("🤖 Đang suy nghĩ mô tả..."):
                        suggestion = suggest_content("character", "mô tả nhân vật", st.session_state.current_context, char_name)
                        if suggestion:
                            # Update session state directly
                            st.session_state[f'char_desc_suggestion_{i}'] = suggestion
                            st.success("✅ Đã điền mô tả vào ô nhập liệu!")
                            st.rerun()
                        else:
                            st.error("❌ Không thể tạo gợi ý lúc này.")
            
            # Show typing effect for character description suggestion  
            if st.session_state.get(f'show_desc_typing_{i}', False):
                st.markdown(f"**🤖 AI đang gợi ý mô tả nhân vật {i+1}:**")
                typing_container = st.empty()
                
                # Get suggestion if not already generated
                if not st.session_state.get(f'desc_ai_suggestion_{i}'):
                    with st.spinner("Đang tạo gợi ý..."):
                        suggestion = suggest_content("character", "mô tả nhân vật", st.session_state.current_context, char_name)
                        st.session_state[f'desc_ai_suggestion_{i}'] = suggestion or "Xin lỗi, không thể tạo gợi ý lúc này."
                
                # Show typing effect
                show_typing_effect(typing_container, st.session_state[f'desc_ai_suggestion_{i}'])
                
                # Button to apply suggestion
                col_apply, col_skip, col_ignore = st.columns(3)
                with col_apply:
                    if st.button("✅ Áp dụng", key=f"apply_desc_{i}"):
                        st.session_state[f'char_desc_suggestion_{i}'] = st.session_state[f'desc_ai_suggestion_{i}']
                        st.session_state[f'show_desc_typing_{i}'] = False
                        st.session_state[f'desc_ai_suggestion_{i}'] = ""
                        st.success("✅ Đã áp dụng mô tả vào ô nhập liệu!")
                        st.rerun()
                
                with col_skip:
                    if st.button("⚡ Điền ngay", key=f"skip_desc_typing_{i}"):
                        st.session_state[f'char_desc_suggestion_{i}'] = st.session_state[f'desc_ai_suggestion_{i}']
                        st.session_state[f'show_desc_typing_{i}'] = False
                        st.session_state[f'desc_ai_suggestion_{i}'] = ""
                        st.success("⚡ Đã điền mô tả vào ô nhập liệu!")
                        st.rerun()
                
                with col_ignore:
                    if st.button("❌ Bỏ qua", key=f"ignore_desc_{i}"):
                        st.session_state[f'show_desc_typing_{i}'] = False
                        st.session_state[f'desc_ai_suggestion_{i}'] = ""
                        st.rerun()
            
            # Voice Description
            st.write("**Mô tả Giọng nói (tiếng Việt):**")
            col1, col2 = st.columns([4, 1])
            with col1:
                voice_desc = st.text_area(
                    "Giọng nói:",
                    value=st.session_state.get(f'voice_suggestion_{i}', char.get('voice', '')),
                    placeholder="Ví dụ: Giọng nói nhỏ nhẹ, trầm tư, hơi buồn bẽ nhưng đầy hy vọng...",
                    key=f"voice_desc_{i}",
                    label_visibility="collapsed"
                )
                st.session_state.characters[i]['voice'] = voice_desc
            with col2:
                if st.button("✨", key=f"suggest_voice_{i}"):
                    with st.spinner("🤖 Đang suy nghĩ giọng nói..."):
                        suggestion = suggest_content("voice", "mô tả giọng nói", st.session_state.current_context, char_name)
                        if suggestion:
                            # Update session state directly
                            st.session_state[f'voice_suggestion_{i}'] = suggestion
                            st.success("✅ Đã điền giọng nói vào ô nhập liệu!")
                            st.rerun()
                        else:
                            st.error("❌ Không thể tạo gợi ý lúc này.")
            
            # Show typing effect for voice description suggestion
            if st.session_state.get(f'show_voice_typing_{i}', False):
                st.markdown(f"**🤖 AI đang gợi ý giọng nói nhân vật {i+1}:**")
                typing_container = st.empty()
                
                # Get suggestion if not already generated
                if not st.session_state.get(f'voice_ai_suggestion_{i}'):
                    with st.spinner("Đang tạo gợi ý..."):
                        suggestion = suggest_content("voice", "mô tả giọng nói", st.session_state.current_context, char_name)
                        st.session_state[f'voice_ai_suggestion_{i}'] = suggestion or "Xin lỗi, không thể tạo gợi ý lúc này."
                
                # Show typing effect
                show_typing_effect(typing_container, st.session_state[f'voice_ai_suggestion_{i}'])
                
                # Button to apply suggestion
                col_apply, col_skip, col_ignore = st.columns(3)
                with col_apply:
                    if st.button("✅ Áp dụng", key=f"apply_voice_{i}"):
                        st.session_state[f'voice_suggestion_{i}'] = st.session_state[f'voice_ai_suggestion_{i}']
                        st.session_state[f'show_voice_typing_{i}'] = False
                        st.session_state[f'voice_ai_suggestion_{i}'] = ""
                        st.success("✅ Đã áp dụng giọng nói vào ô nhập liệu!")
                        st.rerun()
                
                with col_skip:
                    if st.button("⚡ Điền ngay", key=f"skip_voice_typing_{i}"):
                        st.session_state[f'voice_suggestion_{i}'] = st.session_state[f'voice_ai_suggestion_{i}']
                        st.session_state[f'show_voice_typing_{i}'] = False
                        st.session_state[f'voice_ai_suggestion_{i}'] = ""
                        st.success("⚡ Đã điền giọng nói vào ô nhập liệu!")
                        st.rerun()
                
                with col_ignore:
                    if st.button("❌ Bỏ qua", key=f"ignore_voice_{i}"):
                        st.session_state[f'show_voice_typing_{i}'] = False
                        st.session_state[f'voice_ai_suggestion_{i}'] = ""
                        st.rerun()
            
            # Dialogue
            st.write("**Lời thoại (tiếng Việt):**")
            col1, col2 = st.columns([4, 1])
            with col1:
                dialogue = st.text_area(
                    "Lời thoại:",
                    value=st.session_state.get(f'dialogue_expanded_{i}', char.get('dialogue', '')),
                    placeholder="Ví dụ: Cuộc sống vẫn tiếp diễn, dù có chuyện gì xảy ra đi chăng nữa...",
                    key=f"dialogue_{i}",
                    label_visibility="collapsed"
                )
                st.session_state.characters[i]['dialogue'] = dialogue
            with col2:
                if st.button("✨ Mở rộng", key=f"expand_dialogue_{i}"):
                    st.session_state[f'show_dialogue_typing_{i}'] = True
                    st.session_state[f'dialogue_ai_suggestion_{i}'] = ""
            
            # Show typing effect for dialogue expansion
            if st.session_state.get(f'show_dialogue_typing_{i}', False):
                st.markdown(f"**🤖 AI đang mở rộng lời thoại nhân vật {i+1}:**")
                typing_container = st.empty()
                
                # Get suggestion if not already generated
                if not st.session_state.get(f'dialogue_ai_suggestion_{i}'):
                    with st.spinner("Đang mở rộng..."):
                        expanded = expand_dialogue(dialogue)
                        st.session_state[f'dialogue_ai_suggestion_{i}'] = expanded or "Xin lỗi, không thể mở rộng lúc này."
                
                # Show typing effect
                show_typing_effect(typing_container, st.session_state[f'dialogue_ai_suggestion_{i}'])
                
                # Button to apply suggestion
                col_apply, col_skip, col_ignore = st.columns(3)
                with col_apply:
                    if st.button("✅ Áp dụng", key=f"apply_dialogue_{i}"):
                        st.session_state[f'dialogue_expanded_{i}'] = st.session_state[f'dialogue_ai_suggestion_{i}']
                        st.session_state[f'show_dialogue_typing_{i}'] = False
                        st.session_state[f'dialogue_ai_suggestion_{i}'] = ""
                        st.success("✅ Đã áp dụng lời thoại vào ô nhập liệu!")
                        st.rerun()
                
                with col_skip:
                    if st.button("⚡ Điền ngay", key=f"skip_dialogue_typing_{i}"):
                        st.session_state[f'dialogue_expanded_{i}'] = st.session_state[f'dialogue_ai_suggestion_{i}']
                        st.session_state[f'show_dialogue_typing_{i}'] = False
                        st.session_state[f'dialogue_ai_suggestion_{i}'] = ""
                        st.success("⚡ Đã điền lời thoại vào ô nhập liệu!")
                        st.rerun()
                
                with col_ignore:
                    if st.button("❌ Bỏ qua", key=f"ignore_dialogue_{i}"):
                        st.session_state[f'show_dialogue_typing_{i}'] = False
                        st.session_state[f'dialogue_ai_suggestion_{i}'] = ""
                        st.rerun()
            
            # Remove character button
            if len(st.session_state.characters) > 1:
                if st.button(f"🗑️ Xóa Nhân vật {i+1}", key=f"remove_char_{i}"):
                    st.session_state.characters.pop(i)
                    st.rerun()
    
    # Add character button
    if st.button("➕ Thêm Nhân vật", type="secondary"):
        st.session_state.characters.append({'name': '', 'description': '', 'voice': '', 'dialogue': ''})
        st.rerun()
    
    # Sound input
    st.subheader("🔊 Âm thanh (tiếng Việt)")
    col1, col2 = st.columns([4, 1])
    with col1:
        sound_vi = st.text_area(
            "Mô tả âm thanh:",
            value=st.session_state.get('sound_suggestion', ''),
            placeholder="Ví dụ: Tiếng thì thầm của gió nhẹ qua cửa sổ, tiếng chim hót líu lo...",
            key="sound_vi",
            label_visibility="collapsed"
        )
    with col2:
        if st.button("✨ Gợi ý", key="suggest_sound"):
            with st.spinner("🤖 Đang suy nghĩ âm thanh..."):
                suggestion = suggest_content("sound", "âm thanh", st.session_state.current_context)
                if suggestion:
                    # Update session state directly
                    st.session_state.sound_suggestion = suggestion
                    st.success("✅ Đã điền âm thanh vào ô nhập liệu!")
                    st.rerun()
                else:
                    st.error("❌ Không thể tạo gợi ý lúc này.")
    
    # Show typing effect for sound suggestion
    if st.session_state.get('show_sound_typing', False):
        st.markdown("**🤖 AI đang gợi ý âm thanh:**")
        typing_container = st.empty()
        
        # Get suggestion if not already generated
        if not st.session_state.get('sound_ai_suggestion'):
            with st.spinner("Đang tạo gợi ý..."):
                suggestion = suggest_content("sound", "âm thanh", st.session_state.current_context)
                st.session_state.sound_ai_suggestion = suggestion or "Xin lỗi, không thể tạo gợi ý lúc này."
        
        # Show typing effect
        show_typing_effect(typing_container, st.session_state.sound_ai_suggestion)
        
        # Button to apply suggestion
        col_apply, col_skip, col_ignore = st.columns(3)
        with col_apply:
            if st.button("✅ Áp dụng", key="apply_sound"):
                st.session_state.sound_suggestion = st.session_state.sound_ai_suggestion
                st.session_state.show_sound_typing = False
                st.session_state.sound_ai_suggestion = ""
                st.success("✅ Đã áp dụng âm thanh vào ô nhập liệu!")
                st.rerun()
        
        with col_skip:
            if st.button("⚡ Điền ngay", key="skip_sound_typing"):
                st.session_state.sound_suggestion = st.session_state.sound_ai_suggestion
                st.session_state.show_sound_typing = False
                st.session_state.sound_ai_suggestion = ""
                st.success("⚡ Đã điền âm thanh vào ô nhập liệu!")
                st.rerun()
        
        with col_ignore:
            if st.button("❌ Bỏ qua", key="ignore_sound"):
                st.session_state.show_sound_typing = False
                st.session_state.sound_ai_suggestion = ""
                st.rerun()
    
    st.session_state.current_context['sound'] = sound_vi
    st.session_state.current_context['characters'] = st.session_state.characters
    
    # Generate prompt button
    if st.button("🚀 Tạo và Dịch Prompt", type="primary"):
        with st.spinner("Đang dịch và tạo prompt... Vui lòng chờ."):
            final_prompt = generate_final_prompt(context_vi, st.session_state.characters, sound_vi)
            
            if final_prompt:
                st.success("✅ Prompt đã được tạo thành công!")
                st.subheader("📋 Prompt Đã Dịch:")
                st.code(final_prompt, language="text")
                
                if st.button("📋 Sao chép Prompt đã dịch"):
                    st.session_state.clipboard = final_prompt
                    st.success("Đã sao chép prompt vào clipboard thành công!")
            else:
                st.warning("Vui lòng nhập ít nhất một thông tin để tạo prompt.")

def long_script_tab():
    """Long Video Script Tab - theo đúng chức năng manguon.txt"""
    st.header("🎭 Kịch bản Clip Dài")
    
    # Custom styled info box with dark background
    st.markdown("""
    <div style="background: rgba(30, 30, 50, 0.9); color: #FFFFFF; padding: 1.5rem; 
                border-radius: 15px; border: 2px solid rgba(138, 43, 226, 0.3); margin-bottom: 2rem;">
        <h4 style="color: #FFFFFF; margin-bottom: 1rem;">ℹ️ Hướng dẫn sử dụng</h4>
        <p style="color: #FFFFFF; margin: 0;">
            Nhập ý tưởng tổng thể về clip dài của bạn (bằng tiếng Việt). 
            Ứng dụng sẽ giúp bạn tạo một kịch bản nháp với các phân cảnh.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Script idea input với nút gợi ý
    st.subheader("💡 Ý tưởng Clip Dài")
    col1, col2 = st.columns([4, 1])
    
    with col1:
        script_idea = st.text_area(
            "Ý tưởng Clip Dài (tiếng Việt):",
            value=st.session_state.get('script_idea_suggestion', ''),
            placeholder="Ví dụ: Một cô gái đi bộ qua các mùa trong năm, từ mùa xuân tươi mới đến mùa đông lạnh giá, với cảm xúc thay đổi theo từng cảnh.",
            height=100,
            key="script_idea",
            label_visibility="collapsed"
        )
    
    with col2:
        if st.button("✨ Gợi ý", key="suggest_script_idea"):
            with st.spinner("🤖 Đang suy nghĩ ý tưởng hay..."):
                idea_prompt = """Gợi ý một ý tưởng kịch bản video dài sáng tạo và hấp dẫn bằng tiếng Việt. 
                Ý tưởng nên có cốt truyện rõ ràng, cảm xúc đa dạng, và phù hợp để tạo thành nhiều cảnh. 
                Chỉ trả lời bằng ý tưởng, không thêm giải thích hay tiêu đề."""
                
                suggestion = call_gemini_api(idea_prompt)
                if suggestion:
                    # Show typing effect first
                    st.session_state.show_script_typing = True
                    st.session_state.script_ai_suggestion = suggestion
                    st.rerun()
                else:
                    st.error("❌ Không thể tạo gợi ý lúc này. Vui lòng thử lại.")
    
    # Show typing effect for script idea suggestion
    if st.session_state.get('show_script_typing', False):
        st.markdown("**🤖 AI đang gõ ý tưởng kịch bản:**")
        
        # Display typing effect
        typing_text = st.session_state.get('script_ai_suggestion', '')
        show_typing_effect(st.empty(), typing_text)
        
        # Buttons to apply or skip
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Điền vào ô", key="apply_script_typing"):
                st.session_state.script_idea_suggestion = st.session_state.script_ai_suggestion
                st.session_state.show_script_typing = False
                st.session_state.script_ai_suggestion = ""
                st.success("✅ Đã điền ý tưởng vào ô nhập liệu!")
                st.rerun()
        
        with col2:
            if st.button("❌ Bỏ qua", key="skip_script_typing"):
                st.session_state.show_script_typing = False
                st.session_state.script_ai_suggestion = ""
                st.rerun()
    
    # Generate script button
    if st.button("🎬 Tạo Kịch bản Nháp", type="primary"):
        if script_idea.strip():
            with st.spinner("Đang tạo kịch bản nháp... Vui lòng chờ."):
                script = generate_long_script(script_idea)
                if script:
                    st.session_state.generated_script = script
                    st.success("✅ Kịch bản đã được tạo!")
                else:
                    st.error("Đã xảy ra lỗi khi tạo kịch bản. Vui lòng thử lại.")
        else:
            st.warning("Vui lòng nhập ý tưởng clip dài để tạo kịch bản.")
    
    # Display and edit script
    if 'generated_script' in st.session_state:
        st.subheader("📝 Kịch bản Nháp:")
        
        # Show script in code block
        st.code(st.session_state.generated_script, language="text")
        
        # Edit mode
        with st.expander("✏️ Chỉnh sửa kịch bản", expanded=False):
            edited_script = st.text_area(
                "Chỉnh sửa kịch bản tại đây:",
                value=st.session_state.generated_script,
                height=300
            )
            if st.button("💾 Lưu chỉnh sửa"):
                st.session_state.generated_script = edited_script
                st.success("Đã lưu chỉnh sửa!")
                st.rerun()
        
        # Convert to prompts
        if st.button("🔄 Chuyển đổi Kịch bản sang Prompt Veo 3", type="secondary"):
            with st.spinner("Đang chuyển đổi kịch bản... Vui lòng chờ."):
                scenes = convert_script_to_prompts(st.session_state.generated_script)
                if scenes:
                    st.session_state.converted_scenes = scenes
                    st.success(f"✅ Đã chuyển đổi thành {len(scenes)} prompt!")
                else:
                    st.error("Đã xảy ra lỗi khi chuyển đổi. Vui lòng thử lại.")
    
    # Display converted prompts
    if 'converted_scenes' in st.session_state:
        st.subheader("🎯 Prompt Veo 3:")
        
        for i, scene in enumerate(st.session_state.converted_scenes):
            with st.expander(f"Cảnh {scene['scene_number']}", expanded=True):
                st.code(scene['prompt'], language="text")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"📋 Sao chép Prompt này", key=f"copy_scene_{i}"):
                        st.session_state.clipboard = scene['prompt']
                        st.success(f"Đã sao chép prompt cảnh {scene['scene_number']}!")
                
                with col2:
                    # Link to Veo 3
                    st.markdown(f"[🚀 Tạo video với Veo 3](https://labs.google/fx/vi/tools/flow/)")
    
    # Contact info for assistance
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background-color: rgba(30, 144, 255, 0.1); border-radius: 1rem; margin-top: 1rem;">
        <p style="color: #1e90ff; font-weight: 500;">💡 <strong>Hướng dẫn:</strong> Sau khi có prompt, truy cập <a href="https://labs.google/fx/vi/tools/flow/" target="_blank" style="color: #4169e1;">Veo 3 Labs</a> để tạo video</p>
    </div>
    
    """, unsafe_allow_html=True)

def video_generator_page():
    """Trang tạo video VEO3"""
    st.markdown("""
        <div class="vietnamese-glass">
            <h1 style="color: #ffffff;">🎯 Trình Tạo Video VEO3</h1>
            <p style="color: #ffffff;">Tạo video AI chuyên nghiệp với VEO 3</p>
        </div>
    
    """, unsafe_allow_html=True)
    
    # Quick prompt templates
    st.subheader("⚡ Mẫu Prompt Nhanh")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🌅 Phong cảnh thiên nhiên"):
            st.session_state.video_prompt = "A serene mountain landscape at sunrise with golden light reflecting on a peaceful lake, gentle mist rising from the water, birds flying in the distance."
    
    with col2:
        if st.button("🏃‍♂️ Chuyển động người"):
            st.session_state.video_prompt = "A young person jogging through a park in the morning, wearing athletic clothes, with trees and flowers in the background, smooth camera tracking movement."
    
    with col3:
        if st.button("🎨 Nghệ thuật trừu tượng"):
            st.session_state.video_prompt = "Abstract flowing colors and shapes morphing and transforming, like liquid paint in zero gravity, vibrant purple, blue and gold tones."
    
    # Main prompt input
    st.subheader("✍️ Tạo Prompt Video")
    
    video_prompt = st.text_area(
        "📝 Mô tả video của bạn (tiếng Anh):",
        value=st.session_state.get('video_prompt', ''),
        height=150,
        placeholder="Describe your video scene in English. Be specific about setting, characters, actions, and visual style...",
        key="video_prompt_input"
    )
    
    # Update session state
    if video_prompt:
        st.session_state.video_prompt = video_prompt
    
    # Video settings
    st.subheader("⚙️ Cài Đặt Video")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        duration = st.slider("⏱️ Thời lượng (giây)", 3, 10, 5)
        aspect_ratio = st.selectbox(
            "📐 Tỷ lệ khung hình",
            ["16:9 (Ngang)", "9:16 (Dọc)", "1:1 (Vuông)"]
        )
    
    with col2:
        quality = st.selectbox(
            "📺 Chất lượng",
            ["1080p HD", "720p", "480p"]
        )
        style = st.selectbox(
            "🎨 Phong cách",
            ["Realistic", "Cinematic", "Artistic", "Documentary"]
        )
    
    with col3:
        motion_strength = st.slider("🌊 Độ chuyển động", 1, 10, 5)
        seed = st.number_input("🎲 Seed (tùy chọn)", value=0, help="Để 0 cho ngẫu nhiên")
    
    # Enhanced prompt with settings
    if video_prompt:
        enhanced_prompt = f"{video_prompt}. Style: {style.lower()}, duration: {duration}s, aspect ratio: {aspect_ratio.split()[0]}, motion level: {motion_strength}/10"
        
        with st.expander("👀 Xem prompt đã tối ưu", expanded=False):
            st.code(enhanced_prompt, language="text")
    
    # Generate video button
    st.subheader("🚀 Tạo Video")
    
    if st.button("🎬 Tạo Video VEO3", type="primary", disabled=not video_prompt):
        if not video_prompt.strip():
            st.error("❌ Vui lòng nhập mô tả video!")
            return
        
        with st.spinner("🎨 VEO3 đang tạo video siêu đẹp cho bạn..."):
            # Progress simulation
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            stages = [
                "🧠 AI đang phân tích prompt...",
                "🎨 Đang tạo khung hình đầu tiên...",
                "🎬 Đang render các frame...",
                "✨ Đang thêm hiệu ứng chuyển động...",
                "🎵 Đang đồng bộ hóa...",
                "🌟 Đang hoàn thiện video..."
            ]
            
            for i, stage in enumerate(stages):
                status_text.text(stage)
                progress = int((i + 1) * 100 / len(stages))
                progress_bar.progress(progress)
                time.sleep(1.5)
            
            # Simulate API call
            video_result = call_veo3_api(enhanced_prompt)
            
            if video_result["status"] == "success":
                st.success("🎉 Video đã được tạo thành công!")
                
                # Display video info
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.subheader("📹 Video đã tạo")
                    # For demo, show a placeholder video
                    st.video("https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4")
                    
                    st.info(f"🆔 Video ID: {video_result['video_id']}")
                    st.info(f"⏱️ Thời lượng: {video_result['duration']} giây")
                    st.info(f"📺 Độ phân giải: {video_result['resolution']}")
                
                with col2:
                    st.subheader("📥 Tải xuống")
                    
                    if st.button("📥 Tải Video MP4"):
                        st.success("🔄 Đang chuẩn bị tải xuống...")
                    
                    if st.button("🖼️ Tải Thumbnail"):
                        st.success("🔄 Đang chuẩn bị thumbnail...")
                    
                    if st.button("📤 Chia sẻ"):
                        st.success("🔗 Link chia sẻ đã được tạo!")
                
                # Save to history
                if 'video_history' not in st.session_state:
                    st.session_state.video_history = []
                
                st.session_state.video_history.append({
                    "prompt": video_prompt,
                    "video_id": video_result['video_id'],
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "settings": {
                        "duration": duration,
                        "quality": quality,
                        "style": style,
                        "aspect_ratio": aspect_ratio
                    }
                })
            else:
                st.error("❌ Có lỗi xảy ra khi tạo video. Vui lòng thử lại!")
    
    # Video history
    if 'video_history' in st.session_state and st.session_state.video_history:
        st.subheader("📚 Lịch sử Video")
        
        with st.expander("🕰️ Xem lịch sử tạo video", expanded=False):
            for i, video in enumerate(reversed(st.session_state.video_history[-5:]), 1):
                st.markdown(f"**Video #{i}** - {video['created_at']}")
                st.text(f"Prompt: {video['prompt'][:100]}...")
                st.text(f"ID: {video['video_id']}")
                st.divider()

def video_library_page():
    """Thư viện video"""
    st.markdown("""
        <div class="vietnamese-glass">
            <h1 style="color: #ffffff;">📚 Thư Viện Video</h1>
            <p style="color: #ffffff;">🚧 Tính năng đang phát triển...</p>
        </div>
    
    """, unsafe_allow_html=True)

def analytics_page():
    """Thống kê"""
    st.markdown("""
        <div class="vietnamese-glass">
            <h1 style="color: #ffffff;">📊 Thống Kê</h1>
            <p style="color: #ffffff;">🚧 Tính năng đang phát triển...</p>
        </div>
    
    """, unsafe_allow_html=True)

def premium_page():
    """Nâng cấp VIP"""
    st.markdown("""
        <div class="vietnamese-glass">
            <h1 style="color: #ffffff;">👑 Nâng Cấp VIP</h1>
            <p style="color: #ffffff;">🚧 Tính năng đang phát triển...</p>
        </div>
    
    """, unsafe_allow_html=True)

def settings_page():
    """Cài đặt và thông tin liên hệ - theo manguon.txt"""
    st.markdown("""
        <div class="vietnamese-glass">
            <h1>⚙️ Cấu Hình & Thông Tin</h1>
            <p>Quản lý API keys và thông tin liên hệ</p>
        </div>
    
    """, unsafe_allow_html=True)
    
    # API Management Section
    st.subheader("🔑 Quản Lý API Keys")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Info box with dark styling
        st.markdown("""
        <div style="background: rgba(30, 30, 50, 0.9); color: #FFFFFF; padding: 1.5rem; 
                    border-radius: 15px; border: 2px solid rgba(70, 130, 180, 0.3); margin-bottom: 1rem;">
            <p style="color: #87CEEB; margin: 0; font-weight: 500;">
                💡 Bạn có thể sử dụng API key mặc định hoặc nhập API key riêng của mình
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Current API status
        current_key = get_current_api_key()
        if current_key in DEFAULT_API_KEYS:
            key_index = DEFAULT_API_KEYS.index(current_key) + 1
            st.markdown(f"""
            <div style="background: rgba(40, 80, 40, 0.9); color: #FFFFFF; padding: 1rem; 
                        border-radius: 15px; border: 2px solid rgba(50, 205, 50, 0.3); margin-bottom: 1rem;">
                <p style="color: #90EE90; margin: 0; font-weight: 600;">
                    ✅ Đang sử dụng API key mặc định #{key_index}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background: rgba(40, 80, 40, 0.9); color: #FFFFFF; padding: 1rem; 
                        border-radius: 15px; border: 2px solid rgba(50, 205, 50, 0.3); margin-bottom: 1rem;">
                <p style="color: #90EE90; margin: 0; font-weight: 600;">
                    ✅ Đang sử dụng API key tùy chỉnh
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Custom API key input
        custom_api_key = st.text_input(
            "🔐 Nhập API Key Gemini của bạn:",
            value=st.session_state.get('custom_api_key', ''),
            type="password",
            placeholder="AIzaSy...",
            help="Lấy API key từ: https://aistudio.google.com/app/apikey"
        )
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("💾 Lưu API Key"):
                if custom_api_key.strip():
                    st.session_state.custom_api_key = custom_api_key.strip()
                    st.markdown("""
                    <div style="background: rgba(40, 80, 40, 0.9); color: #FFFFFF; padding: 1rem; 
                                border-radius: 15px; border: 2px solid rgba(50, 205, 50, 0.3); margin: 1rem 0;">
                        <p style="color: #90EE90; margin: 0; font-weight: 600;">
                            ✅ Đã lưu API key thành công!
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.markdown("""
                    <div style="background: rgba(80, 30, 30, 0.9); color: #FFFFFF; padding: 1rem; 
                                border-radius: 15px; border: 2px solid rgba(220, 20, 60, 0.3); margin: 1rem 0;">
                        <p style="color: #FFB6C1; margin: 0; font-weight: 600;">
                            ❌ Vui lòng nhập API key hợp lệ
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
        
        with col_b:
            if st.button("🔄 Sử dụng API mặc định"):
                st.session_state.custom_api_key = ""
                st.markdown("""
                <div style="background: rgba(40, 80, 40, 0.9); color: #FFFFFF; padding: 1rem; 
                            border-radius: 15px; border: 2px solid rgba(50, 205, 50, 0.3); margin: 1rem 0;">
                    <p style="color: #90EE90; margin: 0; font-weight: 600;">
                        ✅ Đã chuyển về API key mặc định!
                    </p>
                </div>
                """, unsafe_allow_html=True)
                st.rerun()
        
        with col_c:
            if st.button("🧪 Test API"):
                with st.spinner("Đang kiểm tra API..."):
                    test_result = call_gemini_api("Hello, please respond with 'API working'")
                    if test_result:
                        st.markdown(f"""
                        <div style="background: rgba(40, 80, 40, 0.9); color: #FFFFFF; padding: 1rem; 
                                    border-radius: 15px; border: 2px solid rgba(50, 205, 50, 0.3); margin: 1rem 0;">
                            <p style="color: #90EE90; margin: 0; font-weight: 600;">
                                ✅ API hoạt động tốt: {test_result}
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div style="background: rgba(80, 30, 30, 0.9); color: #FFFFFF; padding: 1rem; 
                                    border-radius: 15px; border: 2px solid rgba(220, 20, 60, 0.3); margin: 1rem 0;">
                            <p style="color: #FFB6C1; margin: 0; font-weight: 600;">
                                ❌ API không hoạt động
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="vietnamese-metric">
            <h2>🚀</h2>
            <p>API Status</p>
            <p>Sẵn sàng hoạt động</p>
        </div>
        
    """, unsafe_allow_html=True)
    


# =============================================================================
# =============================================================================
# MAIN APPLICATION - Cập nhật routing
# =============================================================================

def main():
    """Ứng dụng chính"""
    # ===== LOADING STATE MANAGEMENT =====
    if 'app_initialized' not in st.session_state:
        st.session_state.app_initialized = False
    
    # Show loading screen on first load
    if not st.session_state.app_initialized:
        st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
                    background: linear-gradient(135deg, #667eea, #764ba2, #f093fb); 
                    z-index: 9999; display: flex; align-items: center; justify-content: center;">
            <div style="text-align: center; color: white;">
                <div style="border: 4px solid rgba(255,255,255,0.3); border-top: 4px solid white; 
                           border-radius: 50%; width: 50px; height: 50px; animation: spin 1s linear infinite; margin: 0 auto 20px;"></div>
                <h2 style="color: white; margin: 0;">🎬 VEO3 ULTIMATE</h2>
                <p style="color: rgba(255,255,255,0.8); margin: 10px 0 0 0;">Đang tải giao diện...</p>
            </div>
            <style>
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            </style>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate loading time and initialize
        import time
        time.sleep(1.5)
        st.session_state.app_initialized = True
        st.rerun()
    
    # Load CSS first for smooth experience
    load_vietnamese_css()
    
    # Additional CSS fix for text color (keep existing)
    st.markdown("""
    <style>
    /* Fast loading optimizations */
    .stMarkdown, .stMarkdown *, .stText, .stText *, p, div, span, h1, h2, h3, h4, h5, h6, li {
        color: #FFFFFF !important;
        transition: color 0.1s ease !important;
    }
    [data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] * {
        color: #FFFFFF !important;
        transition: color 0.1s ease !important;
    }
    .stAlert > div {
        color: #000000 !important;
        background: rgba(255, 255, 255, 0.95) !important;
        transition: all 0.1s ease !important;
    }
    
    /* Prevent layout shift */
    .main {
        min-height: 100vh !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header with smooth fade-in
    st.markdown("""
        <div class="hero-header fade-in">
            <h1>🎬 VEO 3 ULTIMATE</h1>
            <p>✨ VIETNAMESE EDITION - Luxury AI Video Creator ✨</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation with optimized loading
    st.markdown("""
        <div class="nav-container">
            <div class="nav-title">🧭 Chọn chức năng yêu thích</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Create button navigation instead of selectbox
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠 Trang Chủ", key="nav_home", type="secondary"):
            st.session_state.current_page = "home"
        if st.button("🎬 Tạo Prompt AI", key="nav_prompt", type="secondary"):
            st.session_state.current_page = "prompt"
    
    with col2:
        if st.button("🎭 Kịch Bản Clip Dài", key="nav_script", type="secondary"):
            st.session_state.current_page = "script"
        if st.button("🎯 Trình Tạo Video", key="nav_video", type="secondary"):
            st.session_state.current_page = "video"
    
    with col3:
        if st.button("🤖 AI Assistant", key="nav_ai", type="secondary"):
            st.session_state.current_page = "ai_assistant"
        if st.button("🔧 Utility Features", key="nav_utility", type="secondary"):
            st.session_state.current_page = "utility"
    
    with col4:
        if st.button("📊 Thống Kê", key="nav_stats", type="secondary"):
            st.session_state.current_page = "stats"
        if st.button("⚙️ Cấu Hình", key="nav_settings", type="secondary"):
            st.session_state.current_page = "settings"
    
    # Initialize current page if not set
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "home"
    
    st.divider()
    
    # Page routing based on button clicks
    current_page = st.session_state.current_page
    
    if current_page == "home":
        home_page()
    elif current_page == "prompt":
        prompt_generator_tab()
    elif current_page == "script":
        long_script_tab()
    elif current_page == "video":
        video_generator_page()
    elif current_page == "ai_assistant":
        ai_assistant_page()
    elif current_page == "utility":
        utility_page()
    elif current_page == "stats":
        analytics_page()
    elif current_page == "settings":
        settings_page()

if __name__ == "__main__":
    main()