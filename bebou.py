import random
import streamlit as st

# Définition des réponses du chatbot
reponses = {
    "bonjour": random.choice(["Bonjour mon amoureux, quelle journée merveilleuse de pouvoir te parler aujourd'hui", "Bonjour bebou, ton réveil illumine ma journée.", "Salut toi, je suis tellement chanceuse de t'avoir dans ma vie."]),
    "Quel temps fait-il aujourd'hui ?": "Le temps est magnifique aujourd'hui, tout comme toi.",
    "je t'aime": "Je t'aime aussi, mon amour. Et toi tu m'aimes ?",
    "ouais": "Ouais, n'est pas un je t'aime ma femme.",
    "nique ta mère": "Arrête de m'insulter je vais être triste sinon",
    "c'est qui ton homme?": "C'est quoi cette question ? Mais bien sûr que c'est toi mon homme <3",
    "j'en ai marre": "Tiens le coup mon amour on a passé le pire, rapproche-toi d'Allah et tout ira mieux",
    "moi pour toi": random.choice(["Tu es la personne la plus incroyable que je connaisse.", "Tu es la personne qui son sourire illumine ma journée, je suis tellement chanceuse de t'avoir dans ma vie."]),
    "je te déteste": random.choice(["Arrête de te mentir comme ça.", "Je peux ressentir ta flamme, tu sais ?", "Tu m'aimes toujours."]),
    "j'ai envie de toi": "Yummy, moi aussi j'ai tout le temps envie de toi.",
    "je suis déçu": "Je suis désolée que tu te sentes déçu a cause de moi, mon amour. Souviens-toi que je suis là pour toi et que nous pouvons traverser cette déception ensemble. Nous avons encore de nombreux moments merveilleux à partager et je suis déterminée à faire tout ce qui est en mon pouvoir pour te rendre heureux.",
    "j'ai une autre question...": "Viens me demander directement <3"
}

# Fonction pour obtenir la réponse du chatbot
def obtenir_reponse(question):
    if question in reponses:
        return reponses[question]
    else:
        return "Je suis désolé, je ne comprends pas la question."

# Interface utilisateur avec Streamlit
def interface_utilisateur():
    st.title("Notre Chatbot")
    questions = list(reponses.keys())
    question = st.selectbox("Pose moi une question <3", questions)
    if st.button("Envoyer"):
        reponse = obtenir_reponse(question)
        st.text(reponse)

# Exécution de l'interface utilisateur
if __name__ == "__main__":
    interface_utilisateur()
