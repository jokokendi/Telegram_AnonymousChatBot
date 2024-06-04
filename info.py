def welcome(name):
    return f"""Hai {name}🖐\n
 Kirimi saya teks, tautan, gif, stiker, foto, video, atau pesan suara dan saya akan meneruskannya secara anonim ke patner Anda

 Perintah
 /start - memulai bot
 /help - tampilkan panduan bantuan
 /next — cari pasangan baru
 /stop — menghentikan dialog
 /settings - menu pengaturan
"""


def user_help():
    return """Dengan bot ini Anda dapat mengobrol dengan Cowok dan Cewek secara anonim berdasarkan jenis kelamin.
    
Perintah 
/start - memulai bot
/help - tampilkan panduan bantuan
/next — cari pasangan baru
/stop — menghentikan dialog
/sharelink - berbagi profil ke patner
/settings - menu pengaturan
"""


def partner_match(gender):
    if gender == "Boy":
        partner = "🤴🏻 Boy"
    else:
        partner = "👸🏻 Girl"

    return f"""Partner: {partner}
/next — mencari pasangan baru
/stop — hentikan obrolan ini"""


def partner_not_found():
    return """🔎 Mencari pasangan"""


def destroy(who=None):
    if who == "You":
        return """Anda menghentikan obrolan ini 🙄
 Ketik /next untuk mencari patner baru
"""
    elif who == "Your":
        return """Lawan Anda menghentikan obrolan ini 🙄
 Ketik /next untuk mencari patner baru
"""


def invalid_destroy():
    return """Anda tidak memiliki lawan bicara 🤔
 Ketik /next untuk mencari patner baru"""
