# Distributor queries

## ua_licensing_backlog

_High-quality movies (rating >=7.5, votes >=10k) NOT yet localized in UA. Licensing shortlist._

| tconst | primaryTitle | startYear | averageRating | numVotes |
|---|---|---|---|---|
| tt0252487 | The Chaos Class | 1975 | 9.2 | 45879 |
| tt33175825 | Attack on Titan the Movie: The Last Attack | 2024 | 9.2 | 24981 |
| tt0259534 | Ramayana: The Legend of Prince Rama | 1993 | 9.1 | 17549 |
| tt5354160 | Mirror Game | 2016 | 8.9 | 30915 |
| tt0253828 | Tosun Pasha | 1976 | 8.9 | 26232 |
| tt5275892 | O.J.: Made in America | 2016 | 8.9 | 23771 |
| tt16747572 | The Silence of Swastika | 2021 | 8.9 | 10685 |
| tt0253779 | The Foster Brothers | 1976 | 8.8 | 22437 |
| tt0084302 | The Marathon Family | 1982 | 8.8 | 18103 |
| tt2077886 | The Phantom of the Opera at the Royal Albert Hall | 2011 | 8.8 | 10785 |
| tt7391996 | C/o Kancharapalem | 2018 | 8.8 | 10723 |
| tt38063392 | Mission Muh Dikhayi | 2025 | 8.8 | 10430 |
| tt0088178 | Stop Making Sense | 1984 | 8.7 | 23905 |
| tt0252490 | The Chaos Class Is Waking Up | 1976 | 8.7 | 22268 |
| tt0253614 | Saban, Son of Saban | 1977 | 8.7 | 19923 |

## dubbing_roi_by_language

_Per language: avg rating x avg log(votes). ROI for dubbing budget._

| language | title_count | avg_rating | avg_log_votes | dubbing_roi |
|---|---|---|---|---|
| kk | 82 | 7.63 | 5.23 | 39.9 |
| uz | 50 | 7.75 | 4.74 | 36.74 |
| az | 55 | 8.01 | 4.56 | 36.53 |
| gu | 55 | 7.34 | 4.78 | 35.09 |
| mr | 91 | 7.52 | 4.35 | 32.71 |
| lt | 111 | 7.43 | 4.19 | 31.13 |
| et | 75 | 7.35 | 4.04 | 29.69 |
| ur | 83 | 6.89 | 4.1 | 28.25 |
| sk | 466 | 6.99 | 4.04 | 28.24 |
| th | 300 | 6.66 | 4.21 | 28.04 |
| kn | 147 | 6.8 | 4.1 | 27.88 |
| he | 4989 | 6.5 | 4.26 | 27.69 |
| mi | 50 | 6.81 | 4.06 | 27.65 |
| es | 13095 | 6.31 | 4.24 | 26.75 |
| uk | 216 | 7.26 | 3.68 | 26.72 |

## genre_share_per_region

_Top 3 genres per region by share of localized titles. Regional acquisition mix._

| region | rank_in_region | genre | title_count | share_pct | region_total |
|---|---|---|---|---|---|
| AE | 1 | Drama | 5007 | 24.68 | 20287 |
| AE | 2 | Comedy | 2338 | 11.52 | 20287 |
| AE | 3 | Action | 1902 | 9.38 | 20287 |
| AL | 1 | Documentary | 528 | 21.15 | 2496 |
| AL | 2 | Drama | 523 | 20.95 | 2496 |
| AL | 3 | Comedy | 245 | 9.82 | 2496 |
| AM | 1 | Drama | 186 | 25.07 | 742 |
| AM | 2 | Comedy | 133 | 17.92 | 742 |
| AM | 3 | Documentary | 88 | 11.86 | 742 |
| AR | 1 | Drama | 19268 | 26.13 | 73727 |
| AR | 2 | Comedy | 10139 | 13.75 | 73727 |
| AR | 3 | Romance | 5245 | 7.11 | 73727 |
| AT | 1 | Drama | 9803 | 27.09 | 36193 |
| AT | 2 | Comedy | 4801 | 13.26 | 36193 |
| AT | 3 | Romance | 2972 | 8.21 | 36193 |
| AU | 1 | Drama | 37715 | 23.33 | 161641 |
| AU | 2 | Comedy | 20104 | 12.44 | 161641 |
| AU | 3 | Thriller | 11377 | 7.04 | 161641 |
| AZ | 1 | Drama | 873 | 18.52 | 4714 |
| AZ | 2 | Comedy | 682 | 14.47 | 4714 |
| AZ | 3 | Adventure | 576 | 12.22 | 4714 |
| BA | 1 | Drama | 606 | 21.06 | 2877 |
| BA | 2 | Comedy | 343 | 11.92 | 2877 |
| BA | 3 | Horror | 251 | 8.72 | 2877 |
| BD | 1 | Drama | 1766 | 36.22 | 4876 |
| BD | 2 | Romance | 693 | 14.21 | 4876 |
| BD | 3 | Action | 612 | 12.55 | 4876 |
| BE | 1 | Drama | 11377 | 26.78 | 42485 |
| BE | 2 | Comedy | 5814 | 13.68 | 42485 |
| BE | 3 | Romance | 3378 | 7.95 | 42485 |

## genre_gaps

_Regions where local genre share trails global by >=5 pct. Unmet demand to address._

| region | genre | local_share_pct | global_share_pct | share_gap | local_count | region_total |
|---|---|---|---|---|---|---|
| XAS | Drama | 14.3 | 25.47 | 11.17 | 308 | 2154 |
| KP | Comedy | 3.5 | 12.85 | 9.35 | 17 | 486 |
| UG | Comedy | 4.39 | 12.85 | 8.46 | 29 | 660 |
| KZ | Drama | 17.15 | 25.47 | 8.32 | 1564 | 9122 |
| IS | Drama | 17.51 | 25.47 | 7.96 | 510 | 2913 |
| BD | Comedy | 5.05 | 12.85 | 7.8 | 246 | 4876 |
| XSA | Drama | 17.76 | 25.47 | 7.71 | 57 | 321 |
| UZ | Drama | 17.92 | 25.47 | 7.55 | 1145 | 6388 |
| IQ | Comedy | 5.81 | 12.85 | 7.04 | 19 | 327 |
| AZ | Drama | 18.52 | 25.47 | 6.95 | 873 | 4714 |
| LV | Drama | 19.13 | 25.47 | 6.34 | 2461 | 12864 |
| BY | Drama | 19.16 | 25.47 | 6.31 | 273 | 1425 |
| MY | Drama | 19.26 | 25.47 | 6.21 | 1470 | 7631 |
| CM | Comedy | 6.83 | 12.85 | 6.02 | 59 | 864 |
| EE | Drama | 19.5 | 25.47 | 5.97 | 9929 | 50918 |

## globally_portable_writers

_Writers whose work is localized in many regions. Universal storytellers for cross-border IP._

| rank | primaryName | region_count | title_count | avg_rating |
|---|---|---|---|---|
| 1 | Mark Burton | 113 | 17 | 6.91 |
| 2 | Nick Park | 111 | 17 | 7.51 |
| 3 | Robert Zemeckis | 108 | 18 | 6.74 |
| 4 | Charles Dickens | 107 | 79 | 7.01 |
| 5 | Peri Segel | 107 | 3 | 5.57 |
| 6 | Burny Mattinson | 106 | 15 | 7.29 |
| 7 | Richard Starzak | 104 | 5 | 7.38 |
| 8 | Ron Clements | 102 | 18 | 6.83 |
| 9 | John Musker | 102 | 17 | 6.8 |
| 10 | Rosemary Contreras | 102 | 4 | 5.15 |
| 11 | H.G. Wells | 99 | 42 | 5.77 |
| 12 | Vance Gerry | 98 | 14 | 7.23 |
| 13 | David Koepp | 98 | 37 | 6.55 |
| 14 | Mark Zaslove | 97 | 22 | 6.88 |
| 15 | Ted Berman | 95 | 8 | 7.26 |

## emerging_regional_markets

_Regions with biggest volume growth in recent 5y vs prior 5y. Where audience is expanding._

| rank | region | recent_count | prior_count | count_growth_pct | recent_rating |
|---|---|---|---|---|---|
| 1 | KZ | 666 | 241 | 176.3 | 6.08 |
| 2 | VE | 304 | 115 | 164.3 | 6.39 |
| 3 | BY | 140 | 53 | 164.2 | 6.4 |
| 4 | TH | 4043 | 1857 | 117.7 | 5.85 |
| 5 | EG | 4641 | 2177 | 113.2 | 5.72 |
| 6 | EC | 2563 | 1262 | 103.1 | 5.82 |
| 7 | MY | 468 | 236 | 98.3 | 6.07 |
| 8 | IL | 4922 | 2483 | 98.2 | 5.85 |
| 9 | HK | 5491 | 2802 | 96.0 | 5.9 |
| 10 | ZA | 7021 | 3675 | 91.0 | 5.65 |
| 11 | CR | 79 | 42 | 88.1 | 6.14 |
| 12 | IN | 14578 | 8154 | 78.8 | 5.88 |
| 13 | AZ | 246 | 138 | 78.3 | 6.38 |
| 14 | MD | 58 | 34 | 70.6 | 6.28 |
| 15 | AE | 3166 | 1863 | 69.9 | 5.61 |
