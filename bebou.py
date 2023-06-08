import random
import streamlit as st

def afficher_message_utilisateur(unique_value):
    unique_value += 1
    message = st.text_input("Vous: ", key={unique_value})
    return message

def afficher_message_chatbot(messagebot):
    st.text_area("Chatbot: ", value=messagebot, height=200, max_chars=None)

def principal():
    st.write("Bienvenue! Dit moi ce que tu as l'habitude de me dire. Parle-moi de tes sentiments.")

    while True:
        unique_value = 0
        message_utilisateur = afficher_message_utilisateur(unique_value)

        # Vos règles de conversation romantiques personnalisées ici
        if "je t'aime" in message_utilisateur:
            afficher_message_chatbot("Je t'aime aussi, mon amour. Et toi tu m'aimes ?")
        elif "ouais" in message_utilisateur:
            afficher_message_chatbot("Ouais, n'est pas un je t'aime ma femme.")
        elif "poème" in message_utilisateur:
            afficher_message_chatbot("Dans tes yeux, je vois un avenir lumineux. Dans tes bras, je trouve la chaleur et le réconfort. Mon amour pour toi est sincère et sans fin.")
        elif "date" in message_utilisateur:
            afficher_message_chatbot("Je propose que nous nous retrouvions pour un dîner romantique au restaurant ce soir. Qu'en penses-tu?")
        elif "admirer" in message_utilisateur:
            afficher_message_chatbot("Je suis émerveillé par ta beauté, ta gentillesse et ta présence. Chaque jour passé avec toi est un cadeau précieux.")
        elif "nique ta mère" in message_utilisateur:
            afficher_message_chatbot("Arrête de m'insulter je vais être triste sinon")
        elif "c'est qui ton homme?" in message_utilisateur:
            afficher_message_chatbot("C'est quoi cette question ? Mais bien sur que c'est toi mon homme <3")
        elif "j'en ai marre" in message_utilisateur:
            afficher_message_chatbot("Tiens le coup mon amour on a passé le pire, rapproche toi d'Allah et tout ira mieux")
        elif "moi pour toi" in message_utilisateur:
            compliments = ["Tu es la personne la plus incroyable que je connaisse.", "Ton sourire illumine ma journée.", "Je suis tellement chanceux(se) de t'avoir dans ma vie."]
            compliment_aleatoire = random.choice(compliments)
            afficher_message_chatbot(compliment_aleatoire)
        elif "bonjour" in message_utilisateur:
            jour = ["Bonjour mon amoureux, quel journée merveilleuse de pouvoir te parler aujourd'hui", "Bonjour bebou, ton réveil illumine ma journée.", "Salut toi, je suis tellement chanceuse de t'avoir dans ma vie."]
            jour_aleatoire = random.choice(jour)
            afficher_message_chatbot(jour_aleatoire)
        elif "je te déteste" or "je te deteste" or "jte deteste" in message_utilisateur:
            deteste = ["Arrete de te mentir comme ca.", "Je peux ressentir ta flamme, tu sais ?", "Tu m'aimes toujours."]
            deteste_aleatoire = random.choice(deteste)
            afficher_message_chatbot(deteste_aleatoire)
        elif "j'ai envie de toi":
            afficher_message_chatbot("Yummy, moi aussi j'ai tout le temps envie de toi.")
        elif "déçu" in message_utilisateur:
            afficher_message_chatbot("Je suis désolée que tu te sentes déçu, mon amour. Souviens-toi que je suis là pour toi et que nous pouvons traverser cette déception ensemble. Nous avons encore de nombreux moments merveilleux à partager et je suis déterminée à faire tout ce qui est en mon pouvoir pour te rendre heureux.")
        else:
            afficher_message_chatbot("Viens me demander directement <3")
    
if __name__ == "__main__":
    principal()
