import os
from flask import Flask, render_template_string, request

app = Flask(name)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Центр Управления Доступом</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .container { max-width: 600px; width: 100%; background: #1e293b; padding: 25px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { text-align: center; color: #38bdf8; font-size: 22px; margin-bottom: 20px; }
        .status-card { background: #334155; padding: 20px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }
        .badge { padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 13px; }
        .active { background: #22c55e; color: white; }
        .inactive { background: #ef4444; color: white; }
        button { background: #3b82f6; color: white; border: none; padding: 12px 20px; border-radius: 8px; cursor: pointer; font-size: 15px; font-weight: bold; transition: background 0.2s; width: 100%; margin-top: 10px; }
        button:hover { background: #2563eb; }
        button.stop { background: #ef4444; }
        button.stop:hover { background: #dc2626; }
        .section { margin-bottom: 20px; background: #334155; padding: 15px; border-radius: 12px; }
        .section h3 { margin-top: 0; color: #38bdf8; font-size: 16px; }
        .link-box { word-break: break-all; background: #0f172a; padding: 12px; border-radius: 8px; font-family: monospace; font-size: 13px; color: #38bdf8; border: 1px solid #475569; }
        p { font-size: 14px; line-height: 1.5; color: #cbd5e1; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Панель управления доступом</h1>
        
        <div class="status-card">
            <div>
                <div style="font-size: 13px; color: #94a3b8;">Текущий статус:</div>
                <div id="statusText" style="font-size: 18px; font-weight: bold; margin-top: 4px;">СЕРВЕР АКТИВЕН</div>
            </div>
            <div id="statusBadge" class="badge active">РАБОТАЕТ</div>
        </div>

        <button id="toggleBtn" class="stop" onclick="toggleServer()">Выключить систему</button>

        <div class="section" style="margin-top: 20px;">
            <h3>Поделиться ссылкой</h3>
            <p>Отправьте эту ссылку друзьям или откройте на другом устройстве (работает на ПК, телефоне, при Wi-Fi и мобильном интернете):</p>
            <div class="link-box" id="shareLink"></div>
        </div>

        <div class="section">
            <h3>Инструкция для ПК и Телефона</h3>
            <p>1. Откройте эту ссылку в браузере любого устройства.<br>
            2. Сервер работает в режиме 24/7 на базе Railway.<br>
            3. Вы можете в любой момент зайти на эту страницу и нажать кнопку включения/выключения.</p>
        </div>
    </div>

    <script>
        const linkBox = document.getElementById('shareLink');
        linkBox.innerText = window.location.origin;

        let isRunning = true;
        function toggleServer() {
            isRunning = !isRunning;
            const btn = document.getElementById('toggleBtn');
            const badge = document.getElementById('statusBadge');
            const text = document.getElementById('statusText');

            if (isRunning) {
                btn.innerText = "Выключить систему";
                btn.className = "stop";
                badge.className = "badge active";
                badge.innerText = "РАБОТАЕТ";
                text.innerText = "СЕРВЕР АКТИВЕН";
                } else {
                btn.innerText = "Включить систему";
                btn.className = "";
                badge.className = "badge inactive";
                badge.innerText = "ОТКЛЮЧЕН";
                text.innerText = "СЕРВЕР ОСТАНОВЛЕН";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if name == 'main':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
