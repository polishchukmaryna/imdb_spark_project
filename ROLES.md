# Ролі та внески учасників команди

## Учасники команди

| Учасник | Git-автор | Стейкхолдер / модуль |
|---|---|---|
| Поліщук Марина | `polishchukmaryna` | Студія — `src/queries/studio.py` |
| Гошовська Діана | `DianaHosh` | Регіональний дистриб'ютор — `src/queries/distributor.py` |
| Павлюх Вікторія | `ViktoriiaPavlushka` | Стрімінг-платформа — `src/queries/streaming.py` |
| Нападайло Микита | `mykytanpdl` | Талант-агенція — `src/queries/agency.py` |

---

## Етап 1: Підготовчий етап

| Завдання | Відповідальний |
|---|---|
| Створення репозиторію GitHub, налаштування гілок | Поліщук |
| Налаштування `.gitignore`, базова структура проекту | Гошовська |
| Завантаження та попередній перегляд набору даних IMDB | Павлюх |
| Аналіз структури даних, визначення корисних ознак | Нападайло |

## Етап 2: Налаштування

| Завдання | Відповідальний |
|---|---|
| Створення `Dockerfile` та `requirements.txt` | Поліщук |
| Створення `docker-compose.yml`, налаштування томів | Павлюх |
| Створення `main.py` — точки входу зі `SparkSession`, фікси збірки | Нападайло |

## Етап 3: Видобування даних

| Завдання | Відповідальний |
|---|---|
| Визначення схем для всіх 7 датасетів | Поліщук |
| Реалізація `_read_tsv()`, `extract_all()`, інтеграція в `main.py` | Гошовська |

## Етап 4: Попередня обробка даних

| Завдання | Відповідальний |
|---|---|
| Загальна статистика, аналіз числових ознак, null-каунти, виявлення/видалення дублікатів (Part 1) | Нападайло |
| Cleaner-функції по таблицях, видалення неінформативних ознак (`isAdult`, `attributes`), кешування (Part 2) | Павлюх |

## Етап 5: Трансформація — бізнес-питання за стейкхолдерами

| Стейкхолдер / модуль | Запити | Відповідальний |
|---|---|---|
| Студія (`src/queries/studio.py`) | `bankable_directors`, `genre_momentum`, `optimal_runtime_band`, `franchise_anchor_actors`, `director_consistency_vs_variance`, `oversaturated_release_years` | Поліщук |
| Регіональний дистриб'ютор (`src/queries/distributor.py`) | `ua_licensing_backlog`, `dubbing_roi_by_language`, `genre_share_per_region`, `genre_gaps`, `globally_portable_writers`, `emerging_regional_markets` | Гошовська |
| Стрімінг (`src/queries/streaming.py`) | `hidden_gems`, `renewal_risk`, `binge_classics`, `dead_weight`, `episode_consistency`, `globally_portable_titles` | Павлюх |
| Талант-агенція (`src/queries/agency.py`) + загальна інфраструктура запитів (скелет `src/queries/`, `save_result`, спільна константа `LATEST_FULL_YEAR`) | `rising_stars`, `genre_profile`, `co_star_chemistry`, `signature_collaborations`, `comeback_actors`, `typecast_decline` | Нападайло |

## Етап 6: Запис результатів і презентація

| Завдання | Відповідальний |
|---|---|
| Запуск повного пайплайну, валідація CSV-файлів | Поліщук |
| Перевірка коректності та форматування результатів | Гошовська |
| Налаштування `.gitignore` для папки `output/` | Павлюх |
| Генерація MD-зведень результатів (`scripts/make_summaries.py`, `summaries/*.md`) | Нападайло |

---

## Командна робота

Робота велася через feature-гілки + pull-request-и:
- `main` — стабільна
- `develop` — інтеграційна
- `feature/*` — окремі завдання

Список feature-гілок (з активних/нещодавніх): `feature/add_main_py`, `feature/fix_dockerfile`, `feature/preprocessing_part1`, `feature/add-preprocessing-part-2`, `feature/add_schemas`, `feature/add_functions`, `feature/transformations-skeleton`, `feature/agency-queries`.
