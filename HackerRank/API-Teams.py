#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests


def getTotalGoals(team, year):
    r1 = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(
        team) + '&page=1').json()

    r2 = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(
        team) + '&page=1').json()

    n1 = r1['total']
    n2 = r2['total']

    sum = 0







    # Get goals as team is home
    for i in range(n1):
        sum += int(r1['data'][i]['team1goals'])

    # Get goals as team is home
    for i in range(n2):
        sum += int(r2['data'][i]['team2goals'])

    return sum


if __name__ == '__main__':
    pass

print(getTotalGoals('Barcelona', 2011))