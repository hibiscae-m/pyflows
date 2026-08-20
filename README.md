### Upload d'un fichier
> curl -X POST "http://127.0.0.1:8000/putfile" -F "file=@test.txt"

### Téléchargement d'un fichier
> curl -X GET --output test.txt "http://127.0.0.1:8000/getfile/10"

où 10 représente la taille voulue en MB
