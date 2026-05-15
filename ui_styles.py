"""Shared modern UI styles for Streamlit health apps."""

HEALTH_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(165deg, #f0f9ff 0%, #e0f2fe 35%, #f8fafc 100%);
}

.hero-banner {
    background: linear-gradient(135deg, #0d9488 0%, #0891b2 50%, #0284c7 100%);
    border-radius: 20px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 20px 40px -12px rgba(13, 148, 136, 0.35);
    color: white;
}
.hero-banner h1 {
    color: white !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    margin: 0 0 0.4rem 0 !important;
}
.hero-banner p {
    color: rgba(255,255,255,0.92) !important;
    font-size: 1.05rem !important;
    margin: 0 !important;
}

.disclaimer-box {
    background: #fffbeb;
    border-left: 4px solid #f59e0b;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin: 1rem 0 1.5rem 0;
    font-size: 0.9rem;
    color: #92400e;
    box-shadow: 0 2px 8px rgba(245, 158, 11, 0.1);
}

.example-chip {
    display: inline-block;
    background: white;
    border: 1px solid #99f6e4;
    border-radius: 999px;
    padding: 0.45rem 1rem;
    margin: 0.25rem 0.35rem 0.25rem 0;
    font-size: 0.85rem;
    color: #0f766e;
    cursor: default;
}

div[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f0fdfa 100%);
    border-right: 1px solid #ccfbf1;
}

div[data-testid="stChatMessage"] {
    background: white;
    border-radius: 16px;
    padding: 0.5rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    border: 1px solid #e2e8f0;
}

#MainMenu, footer, header { visibility: hidden; }
</style>
"""

WELLNESS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: linear-gradient(160deg, #faf5ff 0%, #f3e8ff 25%, #ecfdf5 70%, #f0fdf4 100%);
}

.hero-banner {
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 40%, #6366f1 100%);
    border-radius: 24px;
    padding: 2.2rem 2.4rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 24px 48px -12px rgba(124, 58, 237, 0.4);
    color: white;
}
.hero-banner h1 {
    color: white !important;
    font-size: 2.1rem !important;
    font-weight: 700 !important;
    margin: 0 0 0.5rem 0 !important;
}
.hero-banner p {
    color: rgba(255,255,255,0.94) !important;
    font-size: 1.05rem !important;
    margin: 0 !important;
    line-height: 1.5 !important;
}

.disclaimer-box {
    background: linear-gradient(90deg, #fdf4ff, #f0fdf4);
    border: 1px solid #e9d5ff;
    border-radius: 14px;
    padding: 1rem 1.25rem;
    margin: 1rem 0 1.5rem 0;
    font-size: 0.88rem;
    color: #5b21b6;
}

.mood-card {
    background: white;
    border-radius: 16px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #ede9fe;
    box-shadow: 0 4px 14px rgba(124, 58, 237, 0.08);
    transition: transform 0.2s;
}
.mood-card:hover { transform: translateY(-2px); }

motion-card p { margin: 0; font-size: 0.8rem; color: #6b7280; }

motion-card span { font-size: 1.8rem; }

div[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #faf5ff 100%);
}

motion-card { display: block; }

div[data-testid="stChatMessage"] {
    background: white;
    border-radius: 18px;
    border: 1px solid #f3e8ff;
    box-shadow: 0 4px 16px rgba(124, 58, 237, 0.06);
}

#MainMenu, footer, header { visibility: hidden; }
</style>
"""
