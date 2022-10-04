# Závěrečná práce: MusicDB

### Cíle projektu
 - stránka s hudebními alby (ČSFD-like)
 - možnost přidat hodnocení a komentáře
 - [ ] použít jinou databázi
 - [ ] přidat uživatelské funkce (přidávání komentářů, hodnocení atd.)
 - [ ] vytvořit scraper na data o albech
 - [ ] použít React
 - [ ] použít jiný CSS framework

### Použité technologie
 - Django
 - SQLite ([datový model](https://drive.google.com/file/d/1iVIWZ0uJ85QCOSOrcJgmU03e6yA9e2oN/view?usp=sharing))
 - Bootstrap 5

### Časový harmonogram
- [ ] květen 2022 - současná verze
- [ ] říjen 2022 - použití jiné databáze, přidání uživatelských funkcí, scraper
- [ ] listopad 2022 - použití Reactu a jiného CSS frameworku

### Zdroje informací
- https://docs.djangoproject.com/
- https://getbootstrap.com/
- https://stackoverflow.com/


## v1.2.5

- funkční scraper na recenze
- vlastní template tag na změnu třídy v Bootstrapu


### Jak spustit server
```
python manage.py runserver
```

### Jak spustit scraper
```
python manage.py runscript review_scraper
```

### Jak zobrazit datový model
1. Stáhnout z linku uvedeného výše
2. Jít na stránku https://app.diagrams.net/
3. Otevřít (file -> open from -> device)

&nbsp;

Autor projektu: Václav Pfleger<br/>Konzultant: Mgr. Marek Lučný
