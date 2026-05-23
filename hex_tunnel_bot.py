from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

# Configuración
TOKEN = "TU_TOKEN_DEL_BOTFATHER"
CANAL_ID = -1001234567890  # Tu ID de canal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MENSAJE = """🌎 Bienvenido a Hex Tunnel - Tunnel AIO

🚀 La VPN todo en uno que te mantiene conectado cuando más lo necesitas.

🔒 Navega con privacidad, seguridad y velocidad desde cualquier parte del mundo, sin bloqueos y sin restricciones.

🔥 Miles de usuarios ya disfrutan de una conexión rápida y estable en países como:
🇲🇽 México | 🇨🇴 Colombia | 🇦🇷 Argentina | 🇨🇱 Chile | 🇵🇪 Perú | 🇧🇷 Brasil | 🇬🇧 Reino Unido | 🇲🇦 Marruecos | 🇿🇦 Sudáfrica | 🇰🇪 Kenia | 🇳🇬 Nigeria | 🇮🇳 India | 🇵🇰 Pakistán | 🇨🇺 Cuba … ¡y muchos más!

⚡ ¿Sin megas? ¿Internet lento? ¿Páginas bloqueadas?
Con Hex Tunnel - Tunnel AIO podrás seguir conectado de forma estable y segura.

✨ Disfruta de:
✔️ Servidores rápidos y optimizados
✔️ Conexión estable 24/7
✔️ Navegación privada y protegida
✔️ Acceso sin restricciones
✔️ Compatible con múltiples redes y países
✔️ Interfaz simple y fácil de usar
✔️ Mejor rendimiento para juegos, redes sociales y streaming

📖 Cómo usar Hex Tunnel - Tunnel AIO:

1️⃣ Actualizar Servidores
Presiona "Actualizar" y obtén los servidores más recientes y rápidos disponibles.

2️⃣ Generar Tiempo
Toca "Generar Tiempo" y consigue minutos extra para seguir navegando sin límites.

3️⃣ Elegir Servidor
Selecciona el país que prefieras y conecta al servidor con mejor velocidad para ti.

4️⃣ Conectar
Pulsa "Conectar" y comienza a disfrutar de Internet rápido, privado y sin restricciones.

💥 Con Hex Tunnel - Tunnel AIO podrás mantenerte conectado donde otros fallan.

🌐 Más velocidad.
🔒 Más privacidad.
⚡ Más libertad.

🚀 ¡Descarga Hex Tunnel - Tunnel AIO ahora y lleva tu conexión al siguiente nivel!
👉🏻 https://play.google.com/store/apps/details?id=com.hex.tunnel.jotchuast 👈🏻"""

async def enviar_mensaje(app: Application):
    """Envía el mensaje cada 3 horas"""
    keyboard = [
        [InlineKeyboardButton("👤 Usuario Admin", url="https://t.me/tu_usuario_admin")],
        [InlineKeyboardButton("📢 Canal", url="https://t.me/tu_canal")],
        [InlineKeyboardButton("📱 App", url="https://play.google.com/store/apps/details?id=com.hex.tunnel.jotchuast")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    try:
        await app.bot.send_message(chat_id=CANAL_ID, text=MENSAJE, reply_markup=reply_markup)
        logger.info("Mensaje enviado ✓")
    except Exception as e:
        logger.error(f"Error: {e}")

async def post_init(app: Application):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(enviar_mensaje, "interval", seconds=10800, args=[app])
    scheduler.start()
    logger.info("Bot iniciado - Enviará cada 3 horas")

def main():
    app = Application.builder().token(TOKEN).build()
    app.post_init = post_init.__get__(app, Application)
    logger.info("🚀 Arrancando...")
    app.run_polling()

if __name__ == '__main__':
    main()
