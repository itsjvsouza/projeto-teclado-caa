import pyttsx3
import keyboard
import threading

lock = threading.Lock()

CAA = {
    '1': 'Socorro ou ajuda',
    '2': 'Estou com dor',
    '3': 'Estou assustado',
    '4': 'Estou passando mal',
    'q': 'Quero água',
    'w': 'Quero comer',
    'e': 'Quero ir ao banheiro',
    'r': 'Quero dormir',
    'a': 'Estou feliz',
    's': 'Estou triste',
    'd': 'Estou ansioso',
    'z': 'Olá',
    'x': 'Sim',
    'c': 'Não',
    'v': 'Obrigado',
    'b': 'Repetir, por favor',
    'f': 'Quero brincar',
    'g': 'Quero assistir',
    'h': 'Quero ir pra casa',
    'j': 'Quero meu objeto',
    'k': 'Quero silêncio'
}

def falar_texto(texto):
    def run():
        if lock.locked():
            return
            
        with lock:
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.say(texto)
            engine.runAndWait()
            engine.stop()
            del engine
    
    threading.Thread(target=run, daemon=True).start()

for tecla, frase in CAA.items():
    keyboard.add_hotkey(tecla, falar_texto, args=(frase,))

keyboard.wait('esc')
