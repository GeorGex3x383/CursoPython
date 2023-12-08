import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Id d la voz que se usa
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'

#Escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #Almacenar recognicer en variable
    r = sr.Recognizer()
    
    #Configurar el microfono
    with sr.Microphone() as origen:
        #Tiempo de espera para que empiece a escuvhar
        r.pause_threshold = 0.8
        
        #Informar que comenzó la grabación
        print('Ya puedes hablar')
        
        #Guardar lo que escuche
        audio = r.listen(origen)
        
        try:
            #Buscar en google lo que escucho
            pedido = r.recognize_google(audio,language="es-mx")
            
            #Prueba de que pudo ingresar voz a texto
            print(f"dijiste: {pedido}")
            
            #Devolver a pedido
            return pedido
        #Si no comprende el audio
        except sr.UnknownValueError:
            #Prueba de que no comprendio el audio
            print("Ups no entendí")
            
            #Devolver error
            return "Sigo esperando"
        
        #En caso de no poder resolver el pedido
        except sr.RequestError:
            #Prueba de que no comprendio el audio
            print("Ups no hay servicio")
            
            #Devolver error
            return "Sigo esperando"
        
        #Error inesperado
        except:
            #Prueba de que no comprendio el audio
            print("Ups algo salio mal")
            
            #Devolver error
            return "Sigo esperando"
        
#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #Encender el motor
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    
    #Pronuncia mensaje
    engine.say(mensaje)
    engine.runAndWait()
    
#Informar el dia de la semana
def pedir_dia():
    #Crear variable con datos de hoy
    dia = datetime.date.today()
    
    #Craer una variable para el día de semana
    dia_semana = dia.weekday()
    
    #Diccionario con nombres de los días
    calendario = {0:'Lunes',1:'Martes',2:'Miércoles',3:'Jueves',4:'Viernes',5:'Sábado',6:'Domingo'}
    
    #Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}.')

# Informar que hora es
def pedir_hora():
    #Variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos con {hora.second} segundos.'
    
    #Decir la hora
    hablar(hora)
    
#Saludo inicial
def saludo_inicial():
    #Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    
    #Decir el saludo
    hablar(f'{momento} soy AI, tu asistente personal. Por favor dime con que te puedo ayudar?')
    
#Central del asisitente
def pedir_cosas():
    #Activar saludo inicial
    saludo_inicial()
    
    #Variable de corte
    comenzar = True
    
    #Loop central
    while comenzar:
        #Activar el microfono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir internet' in pedido:
            hablar('Claro, estoy abriendo internet.')
            webbrowser.open('https://www.google.com')
            continue
        elif 'gracias' in pedido:
            hablar('Con mucho gusto.')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia...')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar(f'Wikipedia dice lo siguiente: {resultado}.')
            continue
        elif 'busca en internet' in pedido:
            hablar('En un momento lo busco...')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar(f'Esto es lo que he encontrado sobre {pedido}: ')
        elif 'reproducir' in pedido:
            hablar('Buena idea! Ahora lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL','amazon':'AMZN','google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}.')
                continue
            except:
                hablar('Perdon pero no la he encontrado.')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas!')
            break
        
pedir_cosas()
