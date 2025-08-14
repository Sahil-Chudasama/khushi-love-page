from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/khushi", response_class=HTMLResponse)
def love_message():
    html_content = """
    <html>
        <head>
            <title>For Khushi ❤️</title>
            <style>
                body {
                    background-color: #fff0f5;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 60px;
                    color: #ff1493;
                    overflow: hidden;
                }
                h1 {
                    font-size: 5em;
                    font-weight: bold;
                    text-shadow: 0 0 10px #ff69b4, 0 0 20px #ff69b4, 0 0 40px #ff1493;
                    animation: pulse 1.5s infinite;
                }
                h2 {
                    font-size: 2.5em;
                    animation: fadeIn 2s ease-in-out;
                }
                p {
                    font-size: 1.5em;
                }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
                .heart {
                    position: fixed;
                    color: red;
                    animation: floatUp 5s linear infinite;
                    font-size: 24px;
                }
                @keyframes floatUp {
                    0% { transform: translateY(100vh) scale(1); opacity: 1; }
                    100% { transform: translateY(-10vh) scale(1.5); opacity: 0; }
                }
            </style>
        </head>
        <body>
            <h1>💖 I LOVE YOU KHUSHI 💖</h1>
            <h2>💍 Forever & Always Yours 💍</h2>
            <p>You are the most beautiful part of my life 🌸<br>
            Whenever you smile, the whole world feels brighter ✨<br>
            You are my happiness, my heart, and my forever 💕</p>

            <!-- Background Music -->
            <audio autoplay loop>
                <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mpeg">
            </audio>

            <!-- Floating Hearts -->
            <script>
                function createHeart() {
                    const heart = document.createElement("div");
                    heart.className = "heart";
                    heart.innerHTML = "❤️";
                    heart.style.left = Math.random() * 100 + "vw";
                    heart.style.animationDuration = (Math.random() * 3 + 2) + "s";
                    document.body.appendChild(heart);
                    setTimeout(() => heart.remove(), 5000);
                }
                setInterval(createHeart, 300);
            </script>
        </body>
    </html>
    """
    return html_content
