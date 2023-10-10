import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    
    
def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    
    percentage = float(message_certainty) / float (len(recognized_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
        
    if has_required_words or single_response:
        return int(percentage * 100)
    else: 
        return 0
    
def check_all_messages (message):
    highest_prob = {}
        
    def response(bot_response, list_of_words, single_response=False, required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response,required_words)
    
    response('Hola! ¿En que puedo ayudarte?', ["hola", 'que', 'mas' ,'buenas', 'saludos'], single_response = True),
    response('Soy un simple bot, pero estoy fenomenal, gracias por preocuparte', ['como', 'estas', 'sientes'], required_words=['como']),
    response('Esta aplicación tiene como funcionalidad, otorgar una mejor gestion al manejo de la caja menor, tanto en seguridad como en funcionalidad.', ["1", "01"], single_response= True),
    response('La aplicación tiene como beneficios:1. Seguridad en las egresos e ingresos que se generen, tiene como seguridad consultar a un superiro de la empresa para que  permite continuar. 2.El monto limitado lo seleccionara la empresa vinculada. 3.Se le notificará cualquier movimiento de la caja menor.', [2], single_response= True)
    
    best_match = max(highest_prob, key=highest_prob.get)
    return unknown () if highest_prob [best_match] < 1 else best_match

def unknown():
    response = ['Quizas quisiste preguntar otra cosa.', 'No comprendi tu pregunta, hazla de nuevo'][random.randrange(2)]
    return response

while True:
    print("Bot: " + get_response(input("You: ")))
