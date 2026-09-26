# Personalized AI Lyrics Generator Flask

This example provides a simple Flask web service that simulates an AI-powered personalized lyrics generator. It takes a song title, artist, and user mood as input and returns a custom lyric snippet, demonstrating the core concept of a personalized content service suitable for deployment on platforms like Google Cloud Run.

## Language

`python`

## How to Run

1. Install Flask: `pip install Flask`
2. Save the code as `main.py` and run it: `python main.py`
3. Send a POST request to test: `curl -X POST -H "Content-Type: application/json" -d '{"title": "My Song", "artist": "Me", "user_mood": "happy"}' http://localhost:8080/generate-lyrics`

## Original Article

This example accompanies the Turkish article: [Şarkı Sözü Lingo'yu Cloud Run'a Dağıtma: Bana Özel Bir Şarkı Sözü Web Sitesi Nasıl Oluşturulur?](https://fatihsoysal.com/blog/sarki-sozu-lingoyu-cloud-runa-dagitma-bana-ozel-bir-sarki-sozu-web-sitesi-nasil-olusturulur/).

## License

MIT — see [LICENSE](LICENSE).
