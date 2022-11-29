# Závěrečná práce: MusicDB

### Cíle projektu
 - stránka s hudebními alby (ČSFD-like)
 - možnost přidat hodnocení a komentáře
 - [x] použít jinou databázi
 - [x] vytvořit scraper na data o albech
 - [x] použít Docker
 - [ ] přidat uživatelské funkce (přidávání komentářů, hodnocení atd.)

### Použité technologie
 - Django
 - Docker
 - PostgreSQL ([datový model](https://drive.google.com/file/d/1iVIWZ0uJ85QCOSOrcJgmU03e6yA9e2oN/view?usp=sharing))
 - Bootstrap 5

### Časový harmonogram
- [x] květen 2022 - současná verze
- [x] říjen 2022 - použití jiné databáze, scraper, Docker
- [ ] listopad 2022 - uživatelské funkce

### Zdroje informací
- https://docs.djangoproject.com/
- https://getbootstrap.com/
- https://stackoverflow.com/


## v1.3.4

- search, signup form

### Jak spustit server
```
python manage.py runserver
```

### Jak spustit scrapery
```
python manage.py runscript album_scraper
python manage.py runscript review_scraper
```

> Pro spuštění v Dockeru je potřeba se dostat do kontejneru:
> ```
> docker exec -it zaverecny_projekt_web_1 bash
> ```

### Jak spustit Docker
```
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py loaddata data.json
```

### Jak zobrazit datový model
1. Stáhnout z linku uvedeného výše
2. Jít na stránku https://app.diagrams.net/
3. Otevřít (file -> open from -> device)

&nbsp;

Autor projektu: Václav Pfleger<br/>Konzultant: Mgr. Marek Lučný
