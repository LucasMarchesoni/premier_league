import pandas as pd
from load.load import Load

df_matches = pd.read_csv("data/matches.csv")
df_seasons = pd.read_csv("data/seasons.csv")
df_seasonstats = pd.read_csv("data/seasonstats.csv")
df_teams = pd.read_csv("data/teams.csv")

load = Load('data/premier_league.db')

load.to_sqlite(df_matches, 'matches')
load.to_sqlite(df_seasons, 'seasons')
load.to_sqlite(df_seasonstats, 'seasonstats')
load.to_sqlite(df_teams, 'teams')
