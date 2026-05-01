# Agency queries

## rising_stars

_Actors whose first significant credit (votes >=50k) is within 5 years, with >=3 titles, avg rating >=7.0. Sign before fees inflate._

| rank | primaryName | first_significant_year | significant_count | avg_rating |
|---|---|---|---|---|
| 1 | Manami Numakura | 2021 | 5 | 9.64 |
| 2 | Masaya Matsukaze | 2020 | 4 | 9.63 |
| 3 | Jirô Saitô | 2020 | 6 | 9.57 |
| 4 | David Sobolov | 2022 | 4 | 9.52 |
| 5 | Bertie Carvel | 2026 | 5 | 9.06 |
| 6 | Eve Best | 2022 | 7 | 8.99 |
| 7 | Henry Ashton | 2026 | 4 | 8.97 |
| 8 | Jack Alcott | 2021 | 3 | 8.9 |
| 9 | Peter Claffey | 2026 | 7 | 8.89 |
| 10 | Finn Bennett | 2025 | 7 | 8.73 |
| 11 | Laura Bailey | 2020 | 3 | 8.7 |
| 12 | Bella Ramsey | 2023 | 11 | 8.69 |
| 13 | Dexter Sol Ansell | 2023 | 8 | 8.6 |
| 14 | Milly Alcock | 2022 | 5 | 8.58 |
| 15 | Emily Carey | 2022 | 5 | 8.58 |

## genre_profile

_Per actor (>=10 titles): dominant-genre share. Specialist (>60%) vs utility (<30%)._

### specialist

| primaryName | total_titles | dominant_genre | dominant_share_pct | classification |
|---|---|---|---|---|
| Tom Byron | 298 | Adult | 70.5 | specialist |
| Joey Silvera | 298 | Adult | 66.2 | specialist |
| Bank Janardhan | 280 | Drama | 76.6 | specialist |
| Anup Kumar | 279 | Drama | 77.9 | specialist |
| Doddanna | 234 | Drama | 65.6 | specialist |
| Uzor Arukwe | 215 | Drama | 62.3 | specialist |
| Richard Allan | 209 | Adult | 81.4 | specialist |
| Billy Dee | 207 | Adult | 77.5 | specialist |
| Kanjûrô Arashi | 204 | Drama | 61.4 | specialist |
| Randy West | 203 | Adult | 63.3 | specialist |

### utility

| primaryName | total_titles | dominant_genre | dominant_share_pct | classification |
|---|---|---|---|---|
| Brahmanandam | 1075 | Drama | 28.1 | utility |
| Eric Roberts | 634 | Drama | 20.6 | utility |
| Shakti Kapoor | 588 | Action | 29.2 | utility |
| Tanikella Bharani | 426 | Drama | 29.0 | utility |
| Mohammad Ali | 402 | Drama | 28.1 | utility |
| Gulshan Grover | 398 | Drama | 28.4 | utility |
| Helen | 367 | Drama | 25.5 | utility |
| Siddique | 305 | Drama | 27.8 | utility |
| Madan Puri | 295 | Drama | 29.6 | utility |
| Pran Sikand | 288 | Drama | 28.3 | utility |

## co_star_chemistry

_Pairs with >=5 shared movies whose joint avg exceeds each actor's solo (without-the-other) avg by enough margin. Power duos._

| name1 | name2 | joint_count | joint_avg | solo_avg1 | solo_avg2 | premium |
|---|---|---|---|---|---|---|
| Carrie Fisher | Mark Hamill | 5 | 8.02 | 5.7 | 5.58 | 2.38 |
| Nandhu | Kottayam Nazeer | 5 | 7.48 | 5.62 | 4.84 | 2.25 |
| James Carew | Alma Taylor | 6 | 7.55 | 5.11 | 5.66 | 2.17 |
| Ilia Livykou | Vangelis Protopappas | 8 | 7.48 | 5.18 | 5.47 | 2.16 |
| Mohan Babu | Vani Viswanath | 5 | 8.54 | 7.47 | 5.59 | 2.01 |
| Ilyas Salman | Ihsan Yüce | 7 | 7.36 | 4.63 | 6.07 | 2.01 |
| Max von Sydow | Gunnar Björnstrand | 5 | 7.9 | 6.38 | 5.48 | 1.97 |
| G. Larry Butler | Anne Lockhart | 5 | 7.6 | 6.15 | 5.15 | 1.95 |
| Fernand Charpin | Robert Vattier | 5 | 7.62 | 5.94 | 5.43 | 1.93 |
| Yograj Singh | Daljeet Kaur Khangura | 6 | 8.32 | 6.54 | 6.27 | 1.92 |
| Giorgos Tzifos | Thanasis Vengos | 5 | 7.36 | 4.79 | 6.12 | 1.91 |
| Vangelis Protopappas | Stefanos Stratigos | 5 | 7.3 | 5.79 | 5.02 | 1.9 |
| Stan Harrington | Robert Pralgo | 5 | 7.52 | 6.22 | 5.04 | 1.89 |
| Walter Koenig | Nichelle Nichols | 6 | 6.8 | 4.86 | 5.0 | 1.87 |
| Sevda Aktolga | Adile Naşit | 5 | 7.96 | 5.77 | 6.42 | 1.87 |

## signature_collaborations

_Director-actor combos with >=5 collaborations whose joint avg exceeds the director's overall avg. Scorsese-DiCaprio pattern._

| director_name | actor_name | collab_count | pair_avg | director_avg | uplift |
|---|---|---|---|---|---|
| Curtis Everitt | Matthew Callahan | 5 | 5.78 | 3.86 | 1.92 |
| Ram Gopal Varma | Paresh Rawal | 6 | 7.25 | 5.44 | 1.81 |
| W.S. Van Dyke | William Powell | 6 | 7.43 | 5.69 | 1.74 |
| Osman F. Seden | Kemal Sunal | 5 | 7.42 | 5.68 | 1.74 |
| Joel Lamangan | Vina Morales | 5 | 7.78 | 6.09 | 1.69 |
| Michael Curtiz | Humphrey Bogart | 8 | 7.34 | 5.7 | 1.64 |
| Godfrey Ho | Min-gyu Choe | 5 | 6.2 | 4.56 | 1.64 |
| Dasari Narayana Rao | Krishnamraju | 5 | 8.32 | 6.69 | 1.63 |
| A. Razak Mohaideen | Vanida Imran | 6 | 6.62 | 5.03 | 1.59 |
| John Ford | John Qualen | 5 | 7.44 | 5.86 | 1.58 |
| Rako Prijanto | Vino G. Bastian | 5 | 7.06 | 5.51 | 1.55 |
| Sibi Malayil | Kaviyoor Ponnamma | 8 | 8.0 | 6.46 | 1.54 |
| René Cardona Jr. | Luis Manuel Pelayo | 5 | 7.22 | 5.68 | 1.54 |
| Gregory Hatanaka | Nino Cimino | 7 | 5.81 | 4.28 | 1.53 |
| Rabi Kinagi | Namrta Das | 6 | 7.88 | 6.35 | 1.53 |

## comeback_actors

_Actors with >=10 titles whose recent-5y avg is >=1.0 above their pre-5y avg. McConaissance pattern._

| primaryName | past_titles | past_avg | recent_titles | recent_avg | improvement |
|---|---|---|---|---|---|
| Ella Becerra | 5 | 4.32 | 5 | 8.22 | 3.9 |
| Kiran Raj | 11 | 4.73 | 4 | 8.27 | 3.54 |
| Firoz Irani | 19 | 5.21 | 3 | 8.73 | 3.52 |
| Steve Hanks | 13 | 3.75 | 8 | 7.24 | 3.49 |
| Dylan Vox | 21 | 3.86 | 19 | 7.34 | 3.48 |
| John Henry Richardson | 61 | 4.34 | 22 | 7.7 | 3.36 |
| Gufi Paintal | 15 | 5.47 | 3 | 8.73 | 3.26 |
| Holt Boggs | 10 | 4.49 | 7 | 7.69 | 3.2 |
| John Migliore | 17 | 2.94 | 5 | 6.08 | 3.14 |
| Mike Nyman | 10 | 5.05 | 5 | 8.18 | 3.13 |
| Nan Xie | 7 | 4.86 | 3 | 7.93 | 3.07 |
| Candice Lidstone | 7 | 2.79 | 6 | 5.78 | 2.99 |
| Nadila Ernesta | 7 | 5.4 | 5 | 8.38 | 2.98 |
| Darrell Philip | 6 | 4.83 | 31 | 7.74 | 2.91 |
| Nick Mancuso | 101 | 5.4 | 3 | 8.3 | 2.9 |

## typecast_decline

_Actors with >=10 titles where >70% in one genre AND avg rating in that genre declining year-over-year (>=3 active years)._

| primaryName | dominant_genre | dominant_share_pct | total_titles | avg_yoy_change |
|---|---|---|---|---|
| Bhupendra Singh | Drama | 84.6 | 13 | -1.32 |
| Tripti Berra | Drama | 75.0 | 18 | -1.32 |
| Roxanne Hall | Adult | 86.7 | 13 | -1.07 |
| Payal Patil | Drama | 81.8 | 11 | -1.05 |
| Raven Richards | Adult | 78.6 | 11 | -1.0 |
| Ali Kazemi | Comedy | 71.4 | 13 | -0.9 |
| Vinod Tripathi | Drama | 71.4 | 21 | -0.88 |
| Sofiya Shaikh | Drama | 78.6 | 12 | -0.86 |
| Drago Krca | Drama | 75.0 | 10 | -0.83 |
| Tiffany Grey | Drama | 90.9 | 10 | -0.82 |
| Steve Douzos | Comedy | 76.5 | 15 | -0.81 |
| Pankaj Kumar | Drama | 80.0 | 10 | -0.8 |
| Siegried Cellier | Adult | 85.7 | 12 | -0.77 |
| Shahab Abbasi | Comedy | 78.6 | 13 | -0.71 |
| Vanessa von Schwarz | Drama | 76.2 | 17 | -0.68 |
