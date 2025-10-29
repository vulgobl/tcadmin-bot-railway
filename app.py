#!/usr/bin/env python3
"""
Bot TCAdmin para Railway
API Flask + Bot Python otimizado para 256MB RAM
"""

import os
import time
import logging
import requests
import json
from datetime import datetime
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configurar Flask
app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TCAdminBotRailway:
    def __init__(self):
        """Inicializa o bot otimizado para Railway"""
        self.driver = None
        self.wait = None
        self.setup_logging()
        
        # Configurações do Supabase
        self.supabase_url = os.getenv('SUPABASE_URL', 'https://gxvcovuwtbpkvzqdbcbr.supabase.co')
        self.supabase_key = os.getenv('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd4dmNvdnV3dGJwa3Z6cWRiY2JyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0ODIwNTQzOCwiZXhwIjoyMDYzNzgxNDM4fQ.Yw61sbaz1UsSeTgou9yiwjRMOug4mtePzbVTeBr5lQY')
        
    def setup_logging(self):
        """Configura o sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_driver(self):
        """Configura o driver do Chrome otimizado para Railway"""
        try:
            chrome_options = Options()
            
            # Configurações otimizadas para Railway (256MB RAM)
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-plugins')
            chrome_options.add_argument('--disable-images')
            chrome_options.add_argument('--disable-javascript')
            chrome_options.add_argument('--window-size=1280,720')
            chrome_options.add_argument('--memory-pressure-off')
            chrome_options.add_argument('--max_old_space_size=128')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36')
            
            # Configurar ChromeDriver (Railway)
            import glob
            chromedriver_path = glob.glob('/nix/store/*-chromedriver-*/bin/chromedriver')[0]
            service = Service(chromedriver_path)
            
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            
            self.logger.info("✅ Chrome driver configurado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao configurar driver: {e}")
            return False
    
    def login_tcadmin(self):
        """Faz login no TCAdmin"""
        try:
            self.logger.info("🔐 Fazendo login no TCAdmin...")
            
            # Navegar para o TCAdmin
            self.driver.get("https://tcadmin.xyz/")
            time.sleep(2)
            
            # Preencher login
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys(os.getenv('TCADMIN_USERNAME', 'bernardol'))
            
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.send_keys(os.getenv('TCADMIN_PASSWORD', 'Xyr+(191oTPZ7i'))
            
            # Clicar no botão de login
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            
            # Aguardar login
            time.sleep(3)
            
            self.logger.info("✅ Login realizado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro no login: {e}")
            return False
    
    def process_order(self, order_id):
        """Processa um pedido específico"""
        try:
            self.logger.info(f"📦 Processando pedido: {order_id}")
            
            # Buscar dados do pedido no Supabase
            order_data = self.get_order_data(order_id)
            if not order_data:
                self.logger.error("❌ Pedido não encontrado")
                return False
            
            # Aqui você implementa a lógica específica do seu bot
            # Por exemplo: criar usuário, configurar serviço, etc.
            
            self.logger.info(f"✅ Pedido {order_id} processado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao processar pedido: {e}")
            return False
    
    def get_order_data(self, order_id):
        """Busca dados do pedido no Supabase"""
        try:
            # Implementar busca no Supabase
            # Por enquanto, retorna dados mock
            return {"id": order_id, "status": "paid"}
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao buscar dados do pedido: {e}")
            return None
    
    def run_bot(self, order_id):
        """Executa o bot para um pedido específico"""
        try:
            self.logger.info(f"🤖 Iniciando bot para pedido: {order_id}")
            
            # Configurar driver
            if not self.setup_driver():
                return False
            
            # Fazer login
            if not self.login_tcadmin():
                return False
            
            # Processar pedido
            if not self.process_order(order_id):
                return False
            
            self.logger.info("✅ Bot executado com sucesso")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erro na execução do bot: {e}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
    
    def close(self):
        """Fecha o driver"""
        if self.driver:
            self.driver.quit()

# Instanciar o bot
bot = TCAdminBotRailway()

# Rotas da API
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "TCAdmin Bot Railway",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/process-order', methods=['POST'])
def process_order():
    try:
        data = request.get_json()
        order_id = data.get('order_id')
        
        if not order_id:
            return jsonify({"error": "order_id é obrigatório"}), 400
        
        logger.info(f"📦 Recebido pedido para processar: {order_id}")
        
        # Executar bot
        success = bot.run_bot(order_id)
        
        if success:
            return jsonify({
                "status": "success",
                "message": f"Pedido {order_id} processado com sucesso",
                "timestamp": datetime.now().isoformat()
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Erro ao processar pedido {order_id}",
                "timestamp": datetime.now().isoformat()
            }), 500
            
    except Exception as e:
        logger.error(f"❌ Erro na API: {e}")
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
