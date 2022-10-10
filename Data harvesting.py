# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:40:57 2022

@author: paulb
"""


from bs4 import BeautifulSoup
import requests

r = requests.get("https://ratings.fide.com/a_top.php?list=open")
soup = BeautifulSoup(r.content, 'html.parser')



s = soup.find_all(href=True)
tournaments = []
try: 
    for k in s[:50]:
        print('New player')
        number = k['href'].split('/')[-1]
        for year in range(2013, 2018):
            print('New year')
            for mois in range(1, 13):
                if mois >=10:
                    r = requests.get(f"https://ratings.fide.com/a_indv_calculations.php?id_number={number}&rating_period={year}-{mois}-01&rating=0")
                else:
                    r = requests.get(f"https://ratings.fide.com/a_indv_calculations.php?id_number={number}&rating_period={year}-0{mois}-01&rating=0")
                soupT = BeautifulSoup(r.content, 'html.parser')
                sTournoi = soupT.find_all(href=True)
                print(len(sTournoi))
                for link in sTournoi:
                    tournaments.append(link['href'])
#Quand on se fait choper par l'anti-DoS du site, on récupère les tournois qu'on a listés
except ConnectionAbortedError:
    for tournoi in tournaments:
        code = tournoi[20:-3]
        r = requests.get(f"https://ratings.fide.com/view_pgn.phtml?code={code}&download=1")
        with open(f"{code}.txt", "wb") as f:
            f.write(r.content)
        print(code)

#Si on atteint le bout, on peut copier le bloc précédent dans la console pour récupérer les tournois
