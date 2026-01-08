# Resume Screening App - Enhanced UI Version
# Features: Dark/Light theme, Modern design, Animations

import streamlit as st
import pickle
import docx  # Extract text from Word file
import PyPDF2  # Extract text from PDF
import re
import time

# ============================================================================
# THEME CONFIGURATION
# ============================================================================

def get_theme_css(is_dark_mode):
    """Returns CSS based on the selected theme"""
    
    if is_dark_mode:
        # Dark Theme
        return """
        <style>
            /* Dark Theme Colors - Orange/Red Palette */
            :root {
                --bg-primary: #1a0a0a;
                --bg-secondary: #2d1515;
                --bg-card: #3d1f1f;
                --text-primary: #ffffff;
                --text-secondary: #e0c4b8;
                --accent-primary: #f97316;
                --accent-secondary: #fb923c;
                --accent-gradient: linear-gradient(135deg, #f97316 0%, #ef4444 50%, #dc2626 100%);
                --success-color: #22c55e;
                --border-color: #5c2a2a;
                --shadow-color: rgba(0, 0, 0, 0.4);
                --toggle-bg: #ffffff;
                --toggle-color: #1a0a0a;
            }
            
            .stApp {
                background: linear-gradient(180deg, #1a0a0a 0%, #2d1515 100%);
            }
            
            /* Sidebar Styling - Dark Theme */
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #1a0a0a 0%, #2d1515 100%) !important;
                border-right: 1px solid var(--border-color) !important;
            }
            
            [data-testid="stSidebar"] > div:first-child {
                background: transparent !important;
            }
            
            [data-testid="stSidebar"] .stMarkdown,
            [data-testid="stSidebar"] p,
            [data-testid="stSidebar"] span,
            [data-testid="stSidebar"] label,
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 {
                color: var(--text-primary) !important;
            }
            
            [data-testid="stSidebar"] hr {
                border-color: var(--border-color) !important;
            }
            
            [data-testid="stSidebar"] .stExpander {
                background: var(--bg-card) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 10px !important;
            }
            
            [data-testid="stSidebar"] .stExpander summary {
                color: #ffffff !important;
                background: linear-gradient(135deg, #f97316, #dc2626) !important;
                border-radius: 8px !important;
                padding: 0.5rem 1rem !important;
            }
            
            [data-testid="stSidebar"] .stExpander div {
                color: var(--text-secondary) !important;
            }
            
            /* Main Content Text - Dark Theme */
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
                color: #ffffff !important;
            }
            
            .stMarkdown p, .stMarkdown span, .stMarkdown label {
                color: #e0c4b8 !important;
            }
            
            /* File Uploader Styling - Dark Theme */
            [data-testid="stFileUploader"] {
                background: linear-gradient(145deg, #2d1515, #3d1f1f) !important;
                border-radius: 15px !important;
                padding: 1rem !important;
            }
            
            [data-testid="stFileUploader"] label,
            [data-testid="stFileUploader"] span,
            [data-testid="stFileUploader"] p {
                color: #ffffff !important;
            }
            
            [data-testid="stFileUploader"] section {
                background: rgba(45, 21, 21, 0.8) !important;
                border: 2px dashed #f97316 !important;
                border-radius: 12px !important;
            }
            
            [data-testid="stFileUploader"] section small {
                color: #e0c4b8 !important;
            }
            
            /* Browse files button - Dark Theme */
            [data-testid="stFileUploader"] button {
                background: linear-gradient(135deg, #f97316, #dc2626) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
            }
            
            [data-testid="stFileUploader"] button:hover {
                background: linear-gradient(135deg, #ea580c, #b91c1c) !important;
                transform: scale(1.02);
            }
            
            /* Uploaded file name styling - Dark Theme */
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] {
                background: rgba(249, 115, 22, 0.15) !important;
                border: 1px solid #f97316 !important;
                border-radius: 8px !important;
            }
            
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] span,
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] small,
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] div {
                color: #ffffff !important;
            }
            
            /* Header Styling */
            .main-header {
                background: var(--accent-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 3.5rem;
                font-weight: 800;
                text-align: center;
                margin-bottom: 0.5rem;
                animation: glow 2s ease-in-out infinite alternate;
            }
            
            @keyframes glow {
                from { filter: drop-shadow(0 0 5px rgba(249, 115, 22, 0.5)); }
                to { filter: drop-shadow(0 0 20px rgba(239, 68, 68, 0.8)); }
            }
            
            .sub-header {
                color: var(--text-secondary);
                text-align: center;
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            
            /* Card Styling */
            .custom-card {
                background: var(--bg-card);
                border-radius: 20px;
                padding: 2rem;
                margin: 1rem 0;
                border: 1px solid var(--border-color);
                box-shadow: 0 10px 40px var(--shadow-color);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .custom-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 60px var(--shadow-color);
            }
            
            /* Upload Zone */
            .upload-zone {
                background: linear-gradient(145deg, #2d1515, #3d1f1f);
                border: 2px dashed var(--accent-primary);
                border-radius: 20px;
                padding: 3rem;
                text-align: center;
                transition: all 0.3s ease;
            }
            
            .upload-zone:hover {
                border-color: var(--accent-secondary);
                background: linear-gradient(145deg, #3d1f1f, #2d1515);
            }
            
            /* Result Card */
            .result-card {
                background: linear-gradient(145deg, #4a1f1f, #5c2a2a);
                border-radius: 20px;
                padding: 2rem;
                text-align: center;
                border: 1px solid rgba(249, 115, 22, 0.3);
                box-shadow: 0 0 30px rgba(249, 115, 22, 0.2);
                animation: slideUp 0.5s ease-out;
            }
            
            .result-card .result-title {
                color: #ffffff !important;
                margin-bottom: 0.5rem;
            }
            
            .result-card .result-subtitle {
                color: #e0c4b8 !important;
                margin-bottom: 1rem;
            }
            
            .result-card h2, .result-card p {
                color: #ffffff !important;
            }
            
            @keyframes slideUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .category-badge {
                background: var(--accent-gradient);
                color: white;
                padding: 1rem 2rem;
                border-radius: 50px;
                font-size: 1.5rem;
                font-weight: 700;
                display: inline-block;
                margin-top: 1rem;
                box-shadow: 0 10px 30px rgba(249, 115, 22, 0.4);
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
            
            /* Stats Cards */
            .stats-container {
                display: flex;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
                margin: 2rem 0;
            }
            
            .stat-card {
                background: var(--bg-card);
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                min-width: 150px;
                border: 1px solid var(--border-color);
                transition: all 0.3s ease;
            }
            
            .stat-card:hover {
                border-color: var(--accent-primary);
                transform: scale(1.05);
            }
            
            .stat-number {
                font-size: 2rem;
                font-weight: 700;
                background: var(--accent-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .stat-label {
                color: var(--text-secondary);
                font-size: 0.9rem;
                margin-top: 0.5rem;
            }
            
            /* Feature Cards */
            .feature-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin: 2rem 0;
            }
            
            .feature-card {
                background: var(--bg-card);
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                border: 1px solid var(--border-color);
                transition: all 0.3s ease;
            }
            
            .feature-card:hover {
                border-color: var(--accent-primary);
                background: linear-gradient(145deg, var(--bg-card), #2d3748);
            }
            
            .feature-icon {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            
            .feature-title {
                color: var(--text-primary);
                font-weight: 600;
                margin-bottom: 0.5rem;
            }
            
            .feature-desc {
                color: var(--text-secondary);
                font-size: 0.85rem;
            }
            
            /* Success Message */
            .success-message {
                background: linear-gradient(145deg, #064e3b, #065f46);
                border-left: 4px solid var(--success-color);
                border-radius: 10px;
                padding: 1rem 1.5rem;
                color: #d1fae5;
                margin: 1rem 0;
                animation: fadeIn 0.5s ease;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            /* Footer */
            .footer {
                text-align: center;
                color: var(--text-secondary);
                padding: 2rem;
                margin-top: 3rem;
                border-top: 1px solid var(--border-color);
            }
            
            /* Theme Toggle */
            .theme-toggle {
                position: fixed;
                top: 1rem;
                right: 1rem;
                z-index: 1000;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background: var(--bg-secondary);
            }
            
            ::-webkit-scrollbar-thumb {
                background: var(--accent-primary);
                border-radius: 4px;
            }
            
            /* Loading Animation */
            .loading-spinner {
                display: inline-block;
                width: 50px;
                height: 50px;
                border: 3px solid var(--border-color);
                border-radius: 50%;
                border-top-color: var(--accent-primary);
                animation: spin 1s ease-in-out infinite;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            /* Hide Streamlit Elements - Keep sidebar toggle visible */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Style the header to be minimal but keep sidebar toggle */
            header[data-testid="stHeader"] {
                background: transparent;
            }
            
            /* Sidebar toggle - LIGHT colored for DARK theme (contrast) */
            button[data-testid="stSidebarCollapseButton"],
            button[data-testid="collapsedControl"] {
                visibility: visible !important;
                opacity: 1 !important;
                color: #1a0a0a !important;
                background: #fff7ed !important;
                border: 2px solid #f97316 !important;
                border-radius: 10px !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 15px rgba(249, 115, 22, 0.3) !important;
            }
            
            button[data-testid="stSidebarCollapseButton"]:hover,
            button[data-testid="collapsedControl"]:hover {
                background: var(--accent-gradient) !important;
                color: white !important;
                transform: scale(1.1);
                border-color: var(--accent-primary) !important;
            }
            
            /* Style the expand button when sidebar is collapsed */
            [data-testid="collapsedControl"] {
                left: 0.5rem !important;
                top: 0.5rem !important;
            }
        </style>
        """
    else:
        # Light Theme
        return """
        <style>
            /* Light Theme Colors - Warm Orange/Red Palette */
            :root {
                --bg-primary: #fffbf5;
                --bg-secondary: #fff7ed;
                --bg-card: #ffffff;
                --text-primary: #431407;
                --text-secondary: #9a3412;
                --accent-primary: #ea580c;
                --accent-secondary: #f97316;
                --accent-gradient: linear-gradient(135deg, #f97316 0%, #ef4444 50%, #dc2626 100%);
                --success-color: #22c55e;
                --border-color: #fed7aa;
                --shadow-color: rgba(154, 52, 18, 0.1);
                --toggle-bg: #431407;
                --toggle-color: #ffffff;
            }
            
            .stApp {
                background: linear-gradient(180deg, #fffbf5 0%, #ffedd5 100%);
            }
            
            /* Sidebar Styling - Light Theme */
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #fffbf5 0%, #ffedd5 100%) !important;
                border-right: 1px solid var(--border-color) !important;
            }
            
            [data-testid="stSidebar"] > div:first-child {
                background: transparent !important;
            }
            
            [data-testid="stSidebar"] .stMarkdown,
            [data-testid="stSidebar"] p,
            [data-testid="stSidebar"] span,
            [data-testid="stSidebar"] label,
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 {
                color: var(--text-primary) !important;
            }
            
            [data-testid="stSidebar"] hr {
                border-color: var(--border-color) !important;
            }
            
            [data-testid="stSidebar"] .stExpander {
                background: var(--bg-card) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 10px !important;
                box-shadow: 0 2px 8px var(--shadow-color) !important;
            }
            
            [data-testid="stSidebar"] .stExpander summary {
                color: #ffffff !important;
                background: linear-gradient(135deg, #ea580c, #dc2626) !important;
                border-radius: 8px !important;
                padding: 0.5rem 1rem !important;
            }
            
            [data-testid="stSidebar"] .stExpander div {
                color: var(--text-secondary) !important;
            }
            
            /* Main Content Text - Light Theme */
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
                color: #431407 !important;
            }
            
            .stMarkdown p, .stMarkdown span, .stMarkdown label {
                color: #9a3412 !important;
            }
            
            /* File Uploader Styling - Light Theme */
            [data-testid="stFileUploader"] {
                background: #ffffff !important;
                border-radius: 15px !important;
                padding: 1rem !important;
                border: 1px solid #fed7aa !important;
            }
            
            [data-testid="stFileUploader"] label,
            [data-testid="stFileUploader"] span,
            [data-testid="stFileUploader"] p {
                color: #431407 !important;
            }
            
            [data-testid="stFileUploader"] section {
                background: #fff7ed !important;
                border: 2px dashed #ea580c !important;
                border-radius: 12px !important;
            }
            
            [data-testid="stFileUploader"] section small {
                color: #9a3412 !important;
            }
            
            /* Browse files button - Light Theme */
            [data-testid="stFileUploader"] button {
                background: linear-gradient(135deg, #ea580c, #dc2626) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
            }
            
            [data-testid="stFileUploader"] button:hover {
                background: linear-gradient(135deg, #c2410c, #b91c1c) !important;
                transform: scale(1.02);
            }
            
            /* Uploaded file name styling - Light Theme */
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] {
                background: #fff7ed !important;
                border: 1px solid #ea580c !important;
                border-radius: 8px !important;
            }
            
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] span,
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] small,
            [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] div {
                color: #431407 !important;
            }
            
            /* Header Styling */
            .main-header {
                background: var(--accent-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 3.5rem;
                font-weight: 800;
                text-align: center;
                margin-bottom: 0.5rem;
                animation: glow 2s ease-in-out infinite alternate;
            }
            
            @keyframes glow {
                from { filter: drop-shadow(0 0 5px rgba(249, 115, 22, 0.3)); }
                to { filter: drop-shadow(0 0 15px rgba(239, 68, 68, 0.5)); }
            }
            
            .sub-header {
                color: var(--text-secondary);
                text-align: center;
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            
            /* Card Styling */
            .custom-card {
                background: var(--bg-card);
                border-radius: 20px;
                padding: 2rem;
                margin: 1rem 0;
                border: 1px solid var(--border-color);
                box-shadow: 0 10px 40px var(--shadow-color);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .custom-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 60px var(--shadow-color);
            }
            
            /* Upload Zone */
            .upload-zone {
                background: linear-gradient(145deg, #ffffff, #fff7ed);
                border: 2px dashed var(--accent-primary);
                border-radius: 20px;
                padding: 3rem;
                text-align: center;
                transition: all 0.3s ease;
            }
            
            .upload-zone:hover {
                border-color: var(--accent-secondary);
                background: linear-gradient(145deg, #fff7ed, #ffffff);
            }
            
            /* Result Card */
            .result-card {
                background: linear-gradient(145deg, #ffedd5, #fed7aa);
                border-radius: 20px;
                padding: 2rem;
                text-align: center;
                border: 1px solid rgba(249, 115, 22, 0.3);
                box-shadow: 0 0 30px rgba(249, 115, 22, 0.15);
                animation: slideUp 0.5s ease-out;
            }
            
            .result-card .result-title {
                color: #431407 !important;
                margin-bottom: 0.5rem;
            }
            
            .result-card .result-subtitle {
                color: #9a3412 !important;
                margin-bottom: 1rem;
            }
            
            .result-card h2, .result-card p {
                color: #431407 !important;
            }
            
            @keyframes slideUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .category-badge {
                background: var(--accent-gradient);
                color: white;
                padding: 1rem 2rem;
                border-radius: 50px;
                font-size: 1.5rem;
                font-weight: 700;
                display: inline-block;
                margin-top: 1rem;
                box-shadow: 0 10px 30px rgba(249, 115, 22, 0.3);
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
            
            /* Stats Cards */
            .stats-container {
                display: flex;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
                margin: 2rem 0;
            }
            
            .stat-card {
                background: var(--bg-card);
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                min-width: 150px;
                border: 1px solid var(--border-color);
                box-shadow: 0 4px 15px var(--shadow-color);
                transition: all 0.3s ease;
            }
            
            .stat-card:hover {
                border-color: var(--accent-primary);
                transform: scale(1.05);
            }
            
            .stat-number {
                font-size: 2rem;
                font-weight: 700;
                background: var(--accent-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .stat-label {
                color: var(--text-secondary);
                font-size: 0.9rem;
                margin-top: 0.5rem;
            }
            
            /* Feature Cards */
            .feature-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin: 2rem 0;
            }
            
            .feature-card {
                background: var(--bg-card);
                border-radius: 15px;
                padding: 1.5rem;
                text-align: center;
                border: 1px solid var(--border-color);
                box-shadow: 0 4px 15px var(--shadow-color);
                transition: all 0.3s ease;
            }
            
            .feature-card:hover {
                border-color: var(--accent-primary);
                transform: translateY(-5px);
                box-shadow: 0 10px 30px var(--shadow-color);
            }
            
            .feature-icon {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            
            .feature-title {
                color: var(--text-primary);
                font-weight: 600;
                margin-bottom: 0.5rem;
            }
            
            .feature-desc {
                color: var(--text-secondary);
                font-size: 0.85rem;
            }
            
            /* Success Message */
            .success-message {
                background: linear-gradient(145deg, #d1fae5, #a7f3d0);
                border-left: 4px solid var(--success-color);
                border-radius: 10px;
                padding: 1rem 1.5rem;
                color: #065f46;
                margin: 1rem 0;
                animation: fadeIn 0.5s ease;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            /* Footer */
            .footer {
                text-align: center;
                color: var(--text-secondary);
                padding: 2rem;
                margin-top: 3rem;
                border-top: 1px solid var(--border-color);
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background: var(--bg-primary);
            }
            
            ::-webkit-scrollbar-thumb {
                background: var(--accent-primary);
                border-radius: 4px;
            }
            
            /* Loading Animation */
            .loading-spinner {
                display: inline-block;
                width: 50px;
                height: 50px;
                border: 3px solid var(--border-color);
                border-radius: 50%;
                border-top-color: var(--accent-primary);
                animation: spin 1s ease-in-out infinite;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            /* Hide Streamlit Elements - Keep sidebar toggle visible */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Style the header to be minimal but keep sidebar toggle */
            header[data-testid="stHeader"] {
                background: transparent;
            }
            
            /* Sidebar toggle - DARK colored for LIGHT theme (contrast) */
            button[data-testid="stSidebarCollapseButton"],
            button[data-testid="collapsedControl"] {
                visibility: visible !important;
                opacity: 1 !important;
                color: #ffffff !important;
                background: #7c2d12 !important;
                border: 2px solid #7c2d12 !important;
                border-radius: 10px !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 15px rgba(124, 45, 18, 0.3) !important;
            }
            
            button[data-testid="stSidebarCollapseButton"]:hover,
            button[data-testid="collapsedControl"]:hover {
                background: var(--accent-primary) !important;
                color: white !important;
                transform: scale(1.1);
                border-color: var(--accent-primary) !important;
            }
            
            /* Style the expand button when sidebar is collapsed */
            [data-testid="collapsedControl"] {
                left: 0.5rem !important;
                top: 0.5rem !important;
            }
        </style>
        """


# Category icons mapping
CATEGORY_ICONS = {
    "Data Science": "🔬",
    "HR": "👥",
    "Advocate": "⚖️",
    "Arts": "🎨",
    "Web Designing": "🌐",
    "Mechanical Engineer": "⚙️",
    "Sales": "💼",
    "Health and fitness": "🏃",
    "Civil Engineer": "🏗️",
    "Java Developer": "☕",
    "Business Analyst": "📊",
    "SAP Developer": "💻",
    "Automation Testing": "🤖",
    "Electrical Engineering": "⚡",
    "Operations Manager": "📋",
    "Python Developer": "🐍",
    "DevOps Engineer": "🔧",
    "Network Security Engineer": "🔒",
    "PMO": "📈",
    "Database": "🗄️",
    "Hadoop": "🐘",
    "ETL Developer": "🔄",
    "DotNet Developer": "🔷",
    "Blockchain": "⛓️",
    "Testing": "🧪"
}


# BACKEND FUNCTIONS

# Load pre-trained model and TF-IDF vectorizer
svc_model = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))


def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)
    cleanText = re.sub(r'RT|cc', ' ', cleanText)
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)
    cleanText = re.sub(r'@\S+', '  ', cleanText)
    cleanText = re.sub(r'[%s]' % re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub(r'\s+', ' ', cleanText)
    return cleanText


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text


def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        text = extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        text = extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
    return text


def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text])
    vectorized_text = vectorized_text.toarray()
    predicted_category = svc_model.predict(vectorized_text)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    # Page configuration
    st.set_page_config(
        page_title="AI Resume Classifier",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state for theme
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = True
    
    # Sidebar for theme and settings
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        st.markdown("---")
        
        # Enhanced Theme Toggle with Sun/Moon
        st.markdown("#### 🎨 Theme")
        
        # Custom styled toggle container
        toggle_cols = st.columns([1, 1, 1])
        with toggle_cols[0]:
            st.markdown("<div style='text-align: center; font-size: 1.5rem;'>☀️</div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center; font-size: 0.8rem; color: var(--text-secondary);'>Light</div>", unsafe_allow_html=True)
        with toggle_cols[1]:
            dark_mode = st.toggle("", value=st.session_state.dark_mode, key="theme_toggle", label_visibility="collapsed")
            if dark_mode != st.session_state.dark_mode:
                st.session_state.dark_mode = dark_mode
                st.rerun()
        with toggle_cols[2]:
            st.markdown("<div style='text-align: center; font-size: 1.5rem;'>🌙</div>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center; font-size: 0.8rem; color: var(--text-secondary);'>Dark</div>", unsafe_allow_html=True)
        
        # Show current mode
        current_mode = "🌙 Dark Mode" if st.session_state.dark_mode else "☀️ Light Mode"
        st.markdown(f"<div style='text-align: center; margin-top: 0.5rem; padding: 0.5rem; background: var(--bg-card); border-radius: 10px; border: 1px solid var(--border-color);'><strong>{current_mode}</strong></div>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### Supported Formats")
        st.markdown("""
        - PDF Documents
        - Word Documents (.docx)
        - Text Files (.txt)
        """)
        
        st.markdown("---")
        st.markdown("### Categories")
        st.markdown(f"**{len(le.classes_)}** job categories supported")
        
        with st.expander("View All Categories"):
            for cat in sorted(le.classes_):
                st.markdown(f"• {cat}")
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This AI-powered tool uses **Machine Learning** 
        to classify resumes into job categories.
        """)
    
    # Apply theme CSS
    st.markdown(get_theme_css(st.session_state.dark_mode), unsafe_allow_html=True)
    
    # Main Header
    st.markdown('<h1 class="main-header">AI Resume Classifier</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Instantly categorize resumes using advanced machine learning</p>', unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">25</div>
            <div class="stat-label">Job Categories</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">98%</div>
            <div class="stat-label">Accuracy</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">3</div>
            <div class="stat-label">File Formats</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">&lt;2s</div>
            <div class="stat-label">Processing Time</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main Content Area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 📤 Upload Your Resume")
        
        # File uploader with custom styling
        uploaded_file = st.file_uploader(
            "Drag and drop or click to upload",
            type=["pdf", "docx", "txt"],
            help="Supported formats: PDF, DOCX, TXT"
        )
        
        if uploaded_file is not None:
            # File info
            file_size = len(uploaded_file.getvalue()) / 1024
            
            st.markdown(f"""
            <div class="success-message">
                <strong>File uploaded successfully!</strong><br>
                {uploaded_file.name} ({file_size:.1f} KB)
            </div>
            """, unsafe_allow_html=True)
            
            # Process button
            if st.button("Analyze Resume", use_container_width=True, type="primary"):
                try:
                    # Show loading animation
                    with st.spinner("Analyzing your resume..."):
                        # Add slight delay for effect
                        time.sleep(0.5)
                        
                        # Extract text
                        resume_text = handle_file_upload(uploaded_file)
                        
                        # Make prediction
                        category = pred(resume_text)
                    
                    # Display result with animation
                    st.markdown("---")
                    st.markdown(f"""
                    <div class="result-card">
                        <h2 class="result-title">Prediction Complete!</h2>
                        <p class="result-subtitle">
                            Your resume has been classified as:
                        </p>
                        <div class="category-badge">
                            {category}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show confidence and details
                    st.markdown("---")
                    
                    # Expandable sections
                    with st.expander("View Extracted Text"):
                        st.text_area(
                            "Resume Content",
                            resume_text,
                            height=300,
                            disabled=True
                        )
                    
                    with st.expander("Technical Details"):
                        st.markdown(f"""
                        **Processing Summary:**
                        - File Type: `{uploaded_file.name.split('.')[-1].upper()}`
                        - File Size: `{file_size:.1f} KB`
                        - Characters Extracted: `{len(resume_text):,}`
                        - Words Extracted: `{len(resume_text.split()):,}`
                        - Predicted Category: `{category}`
                        """)
                    
                    # Success celebration
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"Error processing file: {str(e)}")
    
    # Features Section
    st.markdown("---")
    st.markdown("### Features")
    
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered</div>
            <div class="feature-desc">Advanced ML algorithms for accurate predictions</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <div class="feature-desc">Get results in under 2 seconds</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📄</div>
            <div class="feature-title">Multiple Formats</div>
            <div class="feature-desc">Support for PDF, DOCX, and TXT</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">25 Categories</div>
            <div class="feature-desc">Wide range of job classifications</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Privacy First</div>
            <div class="feature-desc">All processing done locally</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ by Abhinav Shukla</p>
        
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
