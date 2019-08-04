import discord
import random

def wholesome():
    fin = open("wholesome.txt", 'r')
    jokes = []
    for line in fin:
        jokes.append(line)

    return random.choice(jokes)

    fin.close()
