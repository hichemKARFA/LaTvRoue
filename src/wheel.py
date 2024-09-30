from discord.ext import commands
import discord
import random
import os
# Initialisez votre bot avec le token
TOKEN = os.getenv("TOKEN_LAROUETVS")

intents = discord.Intents.default()
intents.message_content = True  # Activer l'accès au contenu des messages

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} est connecté !')


# Créer une commande 'teams' qui attend un message avec 10 joueurs
@bot.command(name='teams')
async def generate_teams(ctx, *joueurs):
    joueurs = list(joueurs)  # Transformer le tuple en liste
    print(f'Joueurs détectés : {joueurs}')

    if len(joueurs) == 10:
        random.shuffle(joueurs)

        team1 = joueurs[:5]
        team2 = joueurs[5:]

        response = "**Équipes aléatoires :**\n"
        response += "**Équipe 1 :**\n" + "\n".join(team1) + "\n\n"
        response += "**Équipe 2 :**\n" + "\n".join(team2)

        await ctx.send(response)
    else:
        await ctx.send(f"Erreur : vous devez fournir exactement 10 joueurs. Vous en avez fourni {len(joueurs)}.")


bot.run(TOKEN)