# Dashboard Premier League

O projeto consiste no desenvolvimento de um dashboard da história da premier league (campeonato inglês de futebol).

Para realizar foi utilizado o Power BI para visualização e interação com os dados existentes, python para carregamento dos dados e SQLite como banco.

## Sobre os dados

A análise foi realizada utilizando a base de dados contendo os dados da premier league, os dados foram retirados do site **[Kaggle](https://www.kaggle.com/datasets/evangora/premier-league-data?select=seasonstats.csv)**

## Dashboard:

No dashboard, pode-se conferir quais os indicadores existem para um melhor entendimento e existe a possibilidade de aplicar filtros para diferentes visões.

![Dashboard_Partidas](/assets/partidas.png)

![Dashboard_Estatisticas](/assets/estatisticas.png)

**[Clique para ver o dashboard](https://app.powerbi.com/view?r=eyJrIjoiZjVlZGNkZTYtN2QxZC00NDFlLTg1YzYtM2QyZjcwMzQ1NzIwIiwidCI6ImE5NjgwMmM4LTA0OTAtNDI3NC1iZDVmLTA5NzIxYWQzOWRjNiJ9)**

## Medidas Dax

Para criar o dashboard foi utilizado as seguintes medidas:

- mais gols:

```
MAX(matches[total_goals])
```

- mais penaltis:

```
mais_penaltis = MAX(seasonstats[PK])
```

- partidas com mais gols:

```
partidas_mais_gols =
VAR max_gols = MAX(matches[total_goals])
RETURN
    CALCULATE(
        CONCATENATEX(
            FILTER(matches, matches[total_goals] = Max_Gols),
            matches[Home] & " vs " & matches[Away],
            ", "
        )
    )
```

- times com mais gols de penalti:

```
time_mais_gols_penaltis =
VAR max_penaltis = MAX(seasonstats[PK])
RETURN
    CALCULATE(
        CONCATENATEX(
            FILTER(seasonstats, seasonstats[PK] = max_penaltis),
            seasonstats[Squad],
            ", "
        )
    )
```

- total gols feitos por time:

```
total_gols_feitos_home_away =
VAR team = SELECTEDVALUE('teams'[teams])
VAR home_goals =
    SUMX(
        FILTER(
            'matches',
            'matches'[Home] = team
        ),
        'matches'[Home Goals]
    )
VAR away_goals =
    SUMX(
        FILTER(
            'matches',
            'matches'[Away] = team
        ),
        'matches'[Away Goals]
    )
RETURN
    home_goals + away_goals
```

- total gols feitos por data:

```
total_gols_feitos_home_away_por_data =
VAR data = SELECTEDVALUE('matches'[Date])
VAR home_goals =
    SUMX(
        FILTER(
            'matches',
            'matches'[Date] = data
        ),
        'matches'[Home Goals]
    )
VAR away_goals =
    SUMX(
        FILTER(
            'matches',
            'matches'[Date] = data
        ),
        'matches'[Away Goals]
    )
RETURN
    home_goals + away_goals
```

- total gols levados por time:

```
total_gols_levados_home_away =
VAR team = SELECTEDVALUE('teams'[teams])
VAR home_goals =
    SUMX(
        FILTER(
            'matches',
            'matches'[Home] = team
        ),
        'matches'[Away Goals]
    )
VAR away_goals =
    SUMX(
        FILTER(
            'matches',
            'matches'[Away] = team
        ),
        'matches'[Home Goals]
    )
RETURN
    home_goals + away_goals
```

- xG:

```
xg_home_away =
VAR team = SELECTEDVALUE('teams'[teams])
VAR home_xg =
    SUMX(
        FILTER(
            'matches',
            'matches'[Home] = team
        ),
        'matches'[xG_home]
    )
VAR away_xg =
    SUMX(
        FILTER(
            'matches',
            'matches'[Away] = team
        ),
        'matches'[xG_away]
    )
RETURN
    home_xg + away_xg
```
