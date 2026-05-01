# Studio queries

## bankable_directors

_Directors with >=10 titles, avg rating >=7.0, avg numVotes >=50k. Shortlist for first-look deals._

| primaryName | title_count | avg_rating | avg_votes |
|---|---|---|---|
| Christopher Nolan | 12 | 8.17 | 1503831.0 |
| Hayao Miyazaki | 18 | 7.97 | 196392.0 |
| Alik Sakharov | 23 | 7.96 | 277383.0 |
| Michelle MacLaren | 25 | 7.89 | 382320.0 |
| Frank Darabont | 10 | 7.88 | 812271.0 |
| Joss Whedon | 13 | 7.85 | 367204.0 |
| Laura Innes | 17 | 7.84 | 94696.0 |
| Yûji Tokuno | 10 | 7.82 | 65750.0 |
| Julie Hébert | 10 | 7.82 | 53499.0 |
| Timothy Van Patten | 28 | 7.78 | 190179.0 |
| Alan Taylor | 39 | 7.78 | 187836.0 |
| David Fincher | 15 | 7.77 | 741708.0 |
| Michael Slovis | 27 | 7.77 | 308756.0 |
| Peter Jackson | 17 | 7.75 | 568914.0 |
| Jeremy Podeswa | 47 | 7.75 | 181446.0 |

## genre_momentum

_Genres expanding in volume AND quality (recent 10y vs prior 10y). Where to direct slate development._

| genre | recent_count | prior_count | count_growth_pct | recent_rating | prior_rating | rating_delta | momentum_score |
|---|---|---|---|---|---|---|---|
| Western | 378 | 194 | 94.8 | 5.56 | 5.58 | -0.02 | 9.38 |
| Thriller | 12057 | 7455 | 61.7 | 5.57 | 5.53 | 0.04 | 6.37 |
| Horror | 11285 | 7258 | 55.5 | 4.86 | 4.88 | -0.02 | 5.45 |
| Animation | 2708 | 1778 | 52.3 | 6.29 | 6.27 | 0.02 | 5.33 |
| Sci-Fi | 2972 | 1974 | 50.6 | 5.36 | 5.38 | -0.02 | 4.96 |
| Adult | 94 | 84 | 11.9 | 6.59 | 5.85 | 0.74 | 4.89 |
| Mystery | 4735 | 3137 | 50.9 | 5.67 | 5.76 | -0.09 | 4.64 |
| Fantasy | 3263 | 2330 | 40.0 | 5.76 | 5.75 | 0.01 | 4.05 |
| Sport | 1709 | 1251 | 36.6 | 6.85 | 6.78 | 0.07 | 4.01 |
| Action | 9598 | 7135 | 34.5 | 5.8 | 5.71 | 0.09 | 3.9 |
| Crime | 6925 | 5250 | 31.9 | 6.01 | 6.0 | 0.01 | 3.24 |
| Documentary | 25291 | 19148 | 32.1 | 7.21 | 7.24 | -0.03 | 3.06 |
| Drama | 40945 | 32800 | 24.8 | 6.27 | 6.25 | 0.02 | 2.58 |
| Adventure | 4981 | 3892 | 28.0 | 5.95 | 6.05 | -0.1 | 2.3 |
| Comedy | 21453 | 18133 | 18.3 | 5.9 | 5.88 | 0.02 | 1.93 |

## optimal_runtime_band

_Runtime band that maximises ratings within each genre. Helps producers set target length._

| genre | rank_in_genre | runtime_band | avg_rating | movie_count |
|---|---|---|---|---|
| Action | 1 | 150+ | 6.43 | 922 |
| Action | 2 | 120-150 | 6.4 | 1780 |
| Action | 3 | <60 | 6.27 | 55 |
| Adventure | 1 | 150+ | 6.78 | 221 |
| Adventure | 2 | 120-150 | 6.65 | 767 |
| Adventure | 3 | 90-120 | 6.06 | 2959 |
| Animation | 1 | 120-150 | 7.41 | 69 |
| Animation | 2 | <60 | 6.87 | 54 |
| Animation | 3 | 90-120 | 6.74 | 770 |
| Biography | 1 | 150+ | 7.35 | 154 |
| Biography | 2 | 120-150 | 6.98 | 696 |
| Biography | 3 | 60-90 | 6.95 | 220 |
| Comedy | 1 | 150+ | 6.58 | 592 |
| Comedy | 2 | 120-150 | 6.53 | 1803 |
| Comedy | 3 | 90-120 | 6.15 | 10185 |
| Crime | 1 | 150+ | 6.96 | 386 |
| Crime | 2 | 120-150 | 6.71 | 1320 |
| Crime | 3 | 90-120 | 6.23 | 4762 |
| Documentary | 1 | 150+ | 7.73 | 64 |
| Documentary | 2 | 120-150 | 7.52 | 150 |
| Documentary | 3 | 90-120 | 7.21 | 1398 |
| Drama | 1 | 150+ | 6.93 | 1752 |
| Drama | 2 | 120-150 | 6.81 | 5152 |
| Drama | 3 | 90-120 | 6.43 | 15945 |
| Family | 1 | 150+ | 7.09 | 87 |
| Family | 2 | 120-150 | 6.87 | 242 |
| Family | 3 | 90-120 | 6.15 | 1153 |
| Fantasy | 1 | 150+ | 6.7 | 101 |
| Fantasy | 2 | 120-150 | 6.46 | 328 |
| Fantasy | 3 | 90-120 | 5.91 | 1585 |
| Film-Noir | 1 | 90-120 | 7.06 | 210 |
| Film-Noir | 2 | 60-90 | 6.69 | 238 |
| History | 1 | 150+ | 7.24 | 226 |
| History | 2 | 120-150 | 6.87 | 549 |
| History | 3 | 60-90 | 6.82 | 169 |
| Horror | 1 | 150+ | 6.34 | 62 |
| Horror | 2 | 120-150 | 6.12 | 325 |
| Horror | 3 | 90-120 | 5.37 | 3494 |
| Music | 1 | 120-150 | 6.97 | 234 |
| Music | 2 | 90-120 | 6.64 | 951 |
| Music | 3 | 60-90 | 6.46 | 213 |
| Musical | 1 | 150+ | 6.97 | 169 |
| Musical | 2 | 120-150 | 6.75 | 169 |
| Musical | 3 | 90-120 | 6.41 | 379 |
| Mystery | 1 | 150+ | 7.03 | 90 |
| Mystery | 2 | 120-150 | 6.75 | 546 |
| Mystery | 3 | 90-120 | 5.93 | 2562 |
| Romance | 1 | 150+ | 6.75 | 503 |
| Romance | 2 | 120-150 | 6.67 | 1402 |
| Romance | 3 | 90-120 | 6.33 | 4992 |
| Sci-Fi | 1 | 120-150 | 6.55 | 245 |
| Sci-Fi | 2 | 90-120 | 5.46 | 1315 |
| Sci-Fi | 3 | 60-90 | 4.92 | 735 |
| Sport | 1 | 120-150 | 6.96 | 140 |
| Sport | 2 | 90-120 | 6.44 | 608 |
| Sport | 3 | 60-90 | 6.28 | 98 |
| Thriller | 1 | 150+ | 6.69 | 262 |
| Thriller | 2 | 120-150 | 6.59 | 1158 |
| Thriller | 3 | 90-120 | 5.79 | 4397 |
| War | 1 | 150+ | 7.28 | 100 |
| War | 2 | 120-150 | 6.93 | 271 |
| War | 3 | 90-120 | 6.68 | 698 |
| Western | 1 | 120-150 | 6.82 | 83 |
| Western | 2 | 90-120 | 6.38 | 371 |
| Western | 3 | 60-90 | 6.27 | 168 |

## franchise_anchor_actors

_Actors with >=20 credits, votes-weighted avg rating >=7.0, total_votes >=100k. Casting tentpoles._

| rank | primaryName | title_count | weighted_rating | total_votes |
|---|---|---|---|---|
| 1 | Betsy Brandt | 25 | 9.44 | 2637042 |
| 2 | Anna Gunn | 23 | 9.19 | 2991498 |
| 3 | James Whitmore | 73 | 9.07 | 3607660 |
| 4 | John Marley | 54 | 9.06 | 2339713 |
| 5 | Michael Socha | 28 | 9.06 | 1129132 |
| 6 | Richard Conte | 68 | 9.04 | 2360050 |
| 7 | Monique Gabriela Curnen | 21 | 9.01 | 3339946 |
| 8 | Kishô Taniyama | 40 | 8.99 | 757537 |
| 9 | Una Stubbs | 24 | 8.98 | 1093304 |
| 10 | Michael V. Gazzo | 22 | 8.91 | 1531475 |
| 11 | Trina Nishimura | 32 | 8.91 | 865227 |
| 12 | Jack Klugman | 36 | 8.9 | 1143136 |
| 13 | John Bach | 49 | 8.89 | 4117816 |
| 14 | Kate Flannery | 30 | 8.88 | 864375 |
| 15 | Justin Roiland | 22 | 8.88 | 741672 |

## director_consistency_vs_variance

_Per director (>=5 titles): max - median rating. Investor risk profiling._

| rank | primaryName | title_count | max_rating | median_rating | avg_rating | variance_range |
|---|---|---|---|---|---|---|
| 1 | Gregory Hatanaka | 12 | 7.8 | 2.9 | 3.39 | 4.9 |
| 2 | Michael J. Gallagher | 5 | 8.8 | 4.2 | 5.02 | 4.6 |
| 3 | Todor Chapkanov | 7 | 8.0 | 3.6 | 4.19 | 4.4 |
| 4 | Marcel Walz | 5 | 7.9 | 3.8 | 4.32 | 4.1 |
| 5 | Ian Curtis | 5 | 8.7 | 4.9 | 5.72 | 3.8 |
| 6 | Matt Holt | 5 | 8.7 | 4.9 | 5.72 | 3.8 |
| 7 | Elisa Amoruso | 5 | 8.1 | 4.3 | 5.5 | 3.8 |
| 8 | Andy Sidaris | 14 | 8.2 | 4.5 | 5.16 | 3.7 |
| 9 | Richard John Taylor | 5 | 6.4 | 2.7 | 3.56 | 3.7 |
| 10 | Mark McQueen | 6 | 8.7 | 5.1 | 6.08 | 3.6 |
| 11 | Dharani | 6 | 8.2 | 4.6 | 5.87 | 3.6 |
| 12 | Jeff Fisher | 6 | 8.1 | 4.5 | 5.38 | 3.6 |
| 13 | Robert Lee | 6 | 7.9 | 4.3 | 5.2 | 3.6 |
| 14 | Martin Guigui | 7 | 8.0 | 4.5 | 5.19 | 3.5 |
| 15 | Harley Wallen | 8 | 6.8 | 3.3 | 3.86 | 3.5 |

## oversaturated_release_years

_Genre x year cells: count growth + median rating delta YoY. Scheduling release windows._

| genre | startYear | title_count | count_yoy_pct | median_rating | median_yoy | flag |
|---|---|---|---|---|---|---|
| Action | 1957 | 95 | 41.8 | 6.2 | -0.1 | oversaturated |
| Action | 1958 | 82 | -13.7 | 6.3 | 0.1 | opportunity |
| Adult | 1972 | 116 | -35.2 | 5.0 | 0.2 | opportunity |
| Adult | 1986 | 220 | -21.7 | 6.0 | 0.1 | opportunity |
| Adventure | 1963 | 158 | -16.8 | 5.9 | 0.2 | opportunity |
| Adventure | 1980 | 142 | -24.5 | 6.1 | 0.1 | opportunity |
| Animation | 1952 | 3 | -57.1 | 6.9 | 0.2 | opportunity |
| Animation | 1954 | 6 | -45.5 | 7.2 | 0.2 | opportunity |
| Biography | 1958 | 24 | -33.3 | 6.5 | 0.2 | opportunity |
| Biography | 1965 | 33 | 106.3 | 6.6 | -0.3 | oversaturated |
| Comedy | 1977 | 527 | -14.6 | 5.8 | 0.2 | opportunity |
| Comedy | 2025 | 1832 | -16.4 | 6.3 | 0.3 | opportunity |
| Crime | 1966 | 238 | 38.4 | 5.9 | -0.2 | oversaturated |
| Crime | 1978 | 222 | -13.3 | 6.0 | 0.2 | opportunity |
| Documentary | 1955 | 24 | -11.1 | 6.9 | 0.2 | opportunity |
| Documentary | 1959 | 27 | 42.1 | 6.6 | -0.2 | oversaturated |
| Drama | 2025 | 3325 | -19.7 | 6.6 | 0.1 | opportunity |
| Family | 1963 | 65 | -24.4 | 6.5 | 0.2 | opportunity |
| Family | 1968 | 67 | -11.8 | 6.5 | 0.1 | opportunity |
| Fantasy | 1952 | 34 | 30.8 | 6.4 | -0.3 | oversaturated |
| Fantasy | 1955 | 39 | -15.2 | 6.4 | 0.1 | opportunity |
| Film-Noir | 1958 | 23 | -51.1 | 6.3 | 0.1 | opportunity |
| Game-Show | 2014 | 2 | 100.0 | 3.3 | -3.1 | oversaturated |
| Game-Show | 2020 | 1 | -50.0 | 8.8 | 5.5 | opportunity |
| History | 1954 | 37 | -14.0 | 6.4 | 0.1 | opportunity |
| History | 1957 | 37 | -14.0 | 6.7 | 0.2 | opportunity |
| Horror | 1951 | 15 | 114.3 | 6.3 | -0.4 | oversaturated |
| Horror | 1953 | 24 | 118.2 | 5.9 | -0.1 | oversaturated |
| Music | 1959 | 29 | -17.1 | 6.2 | 0.2 | opportunity |
| Music | 1973 | 35 | -14.6 | 6.9 | 0.2 | opportunity |
| Musical | 1954 | 81 | -19.0 | 6.2 | 0.1 | opportunity |
| Musical | 1968 | 81 | -22.1 | 5.8 | 0.1 | opportunity |
| Mystery | 1956 | 29 | -23.7 | 6.1 | 0.1 | opportunity |
| Mystery | 1970 | 59 | -15.7 | 6.2 | 0.2 | opportunity |
| News | 2007 | 4 | 300.0 | 7.4 | -0.8 | oversaturated |
| News | 2009 | 31 | 520.0 | 7.3 | -0.5 | oversaturated |
| Reality-TV | 2013 | 2 | 100.0 | 2.9 | -2.2 | oversaturated |
| Reality-TV | 2015 | 5 | 150.0 | 7.2 | -1.7 | oversaturated |
| Romance | 1973 | 208 | -14.0 | 6.0 | 0.1 | opportunity |
| Romance | 2025 | 681 | -12.7 | 6.4 | 0.2 | opportunity |
| Sci-Fi | 1957 | 38 | 35.7 | 5.3 | -0.5 | oversaturated |
| Sci-Fi | 1959 | 35 | -22.2 | 5.3 | 0.4 | opportunity |
| Sport | 1952 | 14 | -17.6 | 6.4 | 0.2 | opportunity |
| Sport | 1954 | 9 | -35.7 | 6.1 | 0.1 | opportunity |
| Talk-Show | 2020 | 2 | 100.0 | 3.3 | -3.9 | oversaturated |
| Talk-Show | 2022 | 1 | -83.3 | 7.5 | 1.0 | opportunity |
| Thriller | 1953 | 30 | -16.7 | 6.3 | 0.1 | opportunity |
| Thriller | 1955 | 30 | -26.8 | 6.5 | 0.1 | opportunity |
| War | 1953 | 52 | 44.4 | 6.0 | -0.2 | oversaturated |
| War | 1954 | 43 | -17.3 | 6.2 | 0.2 | opportunity |
| Western | 1951 | 103 | -18.9 | 6.2 | 0.1 | opportunity |
| Western | 1953 | 79 | -22.5 | 6.2 | 0.1 | opportunity |
