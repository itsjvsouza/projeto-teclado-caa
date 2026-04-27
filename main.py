import pyttsx3
import keyboard
import threading

lock = threading.Lock()

CAA = {
    '1': 'Preciso de ajuda',
    '3': 'Estou com dor',
    '5': 'Estou assustado',
    '7': 'Estou passando mal',
    's': 'Estou com sede',
    'f': 'Estou com fome',
    'h': 'Quero ir ao banheiro',
    'a': 'Quero descansar',
    '9': 'Estou feliz',
    '-': 'Estou triste',
    '=': 'Estou ansioso',
    'v': 'Olá',
    'x': 'Sim',
    '\\': 'Não',
    'm': 'Obrigado',
    'b': 'Você pode repetir por favor?',
    'ç': 'Quero brincar',
    '/': 'Quero assistir',
    '.': 'Quero ir para casa',
    ']': 'Quero meu objeto',
    'k': 'Quero silêncio',
    '0': 'Muito obrigado pela atenção de todos, tenham uma boa noite!'
}

def text_speaker(text):
    def run():
        if lock.locked():
            return
            
        with lock:
            engine = pyttsx3.init()
            engine.setProperty('rate', 200)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
            del engine
    
    threading.Thread(target=run, daemon=True).start()

for key, text in CAA.items():
    keyboard.add_hotkey(key, text_speaker, args=(text,))

keyboard.wait('esc')
