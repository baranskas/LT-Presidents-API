from fastapi import FastAPI
import json
import random

with open('presidents.json', 'r', encoding='utf-8') as file:
    duomenys = json.load(file)

app = FastAPI()


@app.get("/")
async def root():
    random_president = random.choice(duomenys["presidents"])
    return random_president