"""
Jyväskylän tapahtumien haku ja kalenterin luonti GitHub Actionsille
"""

import requests
import json
import os
from datetime import datetime, timedelta
from icalendar import Calendar, Event
import feedparser
from urllib.parse import urljoin

class GitHubCalendarGenerator:
    def __init__(self):
        self.events = []
        self.docs_dir = "docs"
        
    def ensure_docs_dir(self):
        """Varmistaa että docs-kansio on olemassa"""
        os.makedirs(self.docs_dir, exist_ok=True)
        
    def fetch_events_from_sources(self):
        """Hakee tapahtumat eri lähteistä"""
        print("🔄 Haetaan tapahtumia...")
        
        # 1. RSS-syötteet (jos saatavilla)
        self.fetch_rss_events()
        
        # 2. Jyväskylän kaupungin sivut (scraping)
        self.fetch_jyvaskyla_events()
        
        # 3. Lisää esimerkkitapahtumat
        self.add_sample_events()
        
        print(f"✅ Löydettiin {len(self.events)} tapahtumaa")
        
    def fetch_rss_events(self):
        """Hakee tapahtumat RSS-syötteistä"""
        rss_feeds = [
            # Lisää oikeat RSS-URLit tähän kun löytyy
            # "https://www.jyvaskyla.fi/rss/tapahtumat",
        ]
        
        for feed_url in rss_feeds:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries:
                    self.events.append({
                        'title': entry.get('title', 'Nimetön tapahtuma'),
                        'description': entry.get('summary', ''),
                        'start_date': self.parse_date(entry.get('published')),
                        'location': 'Jyväskylä',
                        'url': entry.get('link', ''),
                        'source': 'RSS Feed'
                    })
            except Exception as e:
                print(f"❌ RSS-syöte {feed_url} epäonnistui: {e}")
    
    def fetch_jyvaskyla_events(self):
        """Hakee tapahtumat Jyväskylän sivuilta (yksinkertainen scraping)"""
        try:
            # Tämä on esimerkki - muokkaa oikeisiin API-endpointteihin
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; JyvaskylaEventsBot/1.0)'}
            
            # Kokeile eri API-endpointtejä
            api_urls = [
                "https://kalenteri.jyvaskyla.fi",  # Hypoteettinen API
                # Lisää muita kun löydät
            ]
            
            for api_url in api_urls:
                try:
                    response = requests.get(api_url, headers=headers, timeout=10)
                    if response.status_code == 200:
                        # Tämä riippuu API:n rakenteesta
                        data = response.json()
                        # Käsittele data...
                        print(f"✅ API {api_url} toimii")
                except:
                    print(f"⚠️  API {api_url} ei saatavilla")
                    
        except Exception as e:
            print(f"❌ Jyväskylän API-haku epäonnistui: {e}")
    
    def add_sample_events(self):
        """Lisää esimerkkitapahtumia"""
        now = datetime.now()
        
        sample_events = [
            {
                'title': '🎭 Jyväskylän Kesäteatteri',
                'description': 'Kesäteatterin upea esitys Jyväsjärven rannalla. Kansainvälisesti arvostettu teatteri tarjoaa elämyksiä koko perheelle.',
                'start_date': now + timedelta(days=3, hours=19),
                'end_date': now + timedelta(days=3, hours=21, minutes=30),
                'location': 'Jyväskylän Kesäteatteri, Jyväsjärvi',
                'url': 'https://www.jyvaskyla.fi/kesateatteri',
                'source': 'Jyväskylän Kesäteatteri'
            },
            {
                'title': '🏛️ Alvar Aalto -museo: Arkkitehtuurinäyttely',
                'description': 'Alvar Aallon suunnittelun salat -näyttely. Tutustu maailmankuulun arkkitehdin töihin.',
                'start_date': now + timedelta(days=7, hours=10),
                'end_date': now + timedelta(days=7, hours=18),
                'location': 'Alvar Aalto -museo, Keskusta',
                'url': 'https://www.alvaraalto.fi',
                'source': 'Alvar Aalto -museo'
            },
            {
                'title': '🎵 Jyväskylän Sinfonia: Kevätkonsertti',
                'description': 'Klassinen konsertti Jyväskylän kulttuuritalossa. Ohjelmassa Sibelius ja Grieg.',
                'start_date': now + timedelta(days=12, hours=19),
                'end_date': now + timedelta(days=12, hours=21),
                'location': 'Jyväskylän kulttuuritalo',
                'url': 'https://www.jso.fi',
                'source': 'Jyväskylän Sinfonia'
            },
            {
                'title': '🏊‍♀️ Lutakko: Uintikoulu alkaa',
                'description': 'Aikuisten uintikoulu alkaa Lutakon liikuntakeskuksessa. Ilmoittautuminen käynnissä.',
                'start_date': now + timedelta(days=5, hours=18),
                'end_date': now + timedelta(days=5, hours=19),
                'location': 'Lutakon Liikuntakeskus',
                'url': 'https://www.jyvaskyla.fi/liikunta',
                'source': 'Jyväskylän liikunta'
            },
            {
                'title': '📚 Jyväskylän pääkirjasto: Kirjailijan tapaaminen',
                'description': 'Paikallinen kirjailija kertoo uusimmasta teoksestaan. Keskustelua ja kahvia.',
                'start_date': now + timedelta(days=9, hours=18),
                'end_date': now + timedelta(days=9, hours=19, minutes=30),
                'location': 'Jyväskylän pääkirjasto',
                'url': 'https://www.jyvaskyla.fi/kirjasto',
                'source': 'Jyväskylän kirjasto'
            },
            {
                'title': '🌿 Jyväskylän Yliopisto: Luontoretki',
                'description': 'Opastettu luontoretki Jyväskylän ympäristössä. Tutustutaan paikalliseen luontoon.',
                'start_date': now + timedelta(days=14, hours=14),
                'end_date': now + timedelta(days=14, hours=17),
                'location': 'Tapaaminen yliopistolla',
                'url': 'https://www.jyu.fi',
                'source': 'Jyväskylän yliopisto'
            }
        ]
        
        self.events.extend(sample_events)
    
    def parse_date(self, date_str):
        """Parsii päivämäärän"""
        if not date_str:
            return datetime.now() + timedelta(days=1)
            
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%SZ',
            '%a, %d %b %Y %H:%M:%S %z',
            '%Y-%m-%d'
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(str(date_str).replace('GMT', '+0000'), fmt)
            except (ValueError, AttributeError):
                continue
        
        return datetime.now() + timedelta(days=1)
    
    def generate_ical(self):
        """Luo iCalendar-tiedosto"""
        cal = Calendar()
        cal.add('prodid', '-//Jyväskylän Tapahtumakalenteri//GitHub//')
        cal.add('version', '2.0')
        cal.add('calscale', 'GREGORIAN')
        cal.add('method', 'PUBLISH')
        cal.add('x-wr-calname', 'Jyväskylän Tapahtumat')
        cal.add('x-wr-caldesc', 'Ajankohtaiset tapahtumat Jyväskylän alueelta - Päivittyy automaattisesti')
        cal.add('x-wr-timezone', 'Europe/Helsinki')
        
        for event_data in self.events:
            event = Event()
            event.add('summary', event_data['title'])
            
            description = f"{event_data.get('description', '')}\n\n"
            description += f"📍 {event_data.get('location', 'Jyväskylä')}\n"
            description += f"🔗 Lähde: {event_data.get('source', 'Tuntematon')}"
            if event_data.get('url'):
                description += f"\n🌐 Lisätietoja: {event_data['url']}"
            description += f"\n\n📅 Kalenteri päivitetty: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
            
            event.add('description', description)
            
            start_date = event_data.get('start_date')
            if start_date:
                event.add('dtstart', start_date)
                
                end_date = event_data.get('end_date')
                if end_date:
                    event.add('dtend', end_date)
                else:
                    event.add('dtend', start_date + timedelta(hours=2))
            
            event.add('location', event_data.get('location', 'Jyväskylä'))
            
            if event_data.get('url'):
                event.add('url', event_data['url'])
            
            # Uniikki ID
            uid = f"{abs(hash(event_data['title'] + str(start_date)))}@jyvaskyla-events.github.io"
            event.add('uid', uid)
            
            event.add('dtstamp', datetime.now())
            
            cal.add_component(event)
        
        return cal.to_ical()
    
    def generate_html_page(self):
        """Luo HTML-sivu kalenterin tilaamiseen"""
        
        repo_name = os.environ.get('GITHUB_REPOSITORY', 'käyttäjä/jyvaskyla-tapahtumat')
        username = repo_name.split('/')[0]
        
        calendar_url = f"https://{username}.github.io/jyvaskyla-tapahtumat/calendar.ics"
        
        # Järjestä tapahtumat päivämäärän mukaan
        sorted_events = sorted(
            [e for e in self.events if e.get('start_date')], 
            key=lambda x: x['start_date']
        )
        
        html_content = f"""<!DOCTYPE html>
<html lang="fi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📅 Jyväskylän Tapahtumakalenteri</title>
    <meta name="description" content="Tilaa Jyväskylän tapahtumat suoraan omaan kalenteriisi. Päivittyy automaattisesti!">
    
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        .header {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 20px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .subscribe-section {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .url-box {{
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Monaco', 'Menlo', monospace;
            margin: 15px 0;
            word-break: break-all;
            font-size: 0.9em;
        }}
        
        .copy-btn {{
            background: #667eea;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9em;
            margin-left: 10px;
        }}
        
        .copy-btn:hover {{
            background: #5a6fd8;
        }}
        
        .platforms {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 25px 0;
        }}
        
        .platform {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }}
        
        .platform h4 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
        
        .events-section {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }}
        
        .event {{
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 15px 0;
            background: #f8f9fa;
            border-radius: 0 10px 10px 0;
            transition: transform 0.2s;
        }}
        
        .event:hover {{
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .event-title {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
        }}
        
        .event-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 10px;
            font-size: 0.9em;
            color: #666;
        }}
        
        .event-description {{
            color: #555;
            margin-top: 10px;
        }}
        
        .badge {{
            background: #667eea;
            color: white;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8em;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 50px;
            color: rgba(255,255,255,0.8);
        }}
        
        .download-btn {{
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            margin: 20px 0;
            transition: background 0.3s;
        }}
        
        .download-btn:hover {{
            background: #218838;
        }}
        
        @media (max-width: 768px) {{
            .container {{ padding: 15px; }}
            .header {{ padding: 25px 20px; }}
            .header h1 {{ font-size: 2em; }}
            .event-meta {{ flex-direction: column; gap: 5px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📅 Jyväskylän Tapahtumakalenteri</h1>
            <p>Tilaa kalenteri ja pysy ajan tasalla Jyväskylän tapahtumista!</p>
            <p>🔄 Päivittyy automaattisesti GitHub Actionseilla</p>
        </div>

        <div class="subscribe-section">
            <h2>🔗 Tilaa kalenteri</h2>
            <p>Kopioi alla oleva URL ja lisää se kalenteriisi:</p>
            
            <div class="url-box">
                <span id="calendar-url">{calendar_url}</span>
                <button class="copy-btn" onclick="copyToClipboard()">📋 Kopioi</button>
            </div>
            
            <a href="{calendar_url}" class="download-btn" download="jyvaskyla_tapahtumat.ics">
                ⬇️ Lataa kalenteri (.ics)
            </a>

            <div class="platforms">
                <div class="platform">
                    <h4>📱 Google Kalenteri</h4>
                    <ol>
                        <li>Avaa Google Kalenteri</li>
                        <li>Klikkaa "+" → "Tilaa URL:stä"</li>
                        <li>Liitä yllä oleva URL</li>
                    </ol>
                </div>
                
                <div class="platform">
                    <h4>💼 Outlook</h4>
                    <ol>
                        <li>Avaa Outlook</li>
                        <li>"Lisää kalenteri" → "Tilaa internetistä"</li>
                        <li>Syötä URL ja nimi</li>
                    </ol>
                </div>
                
                <div class="platform">
                    <h4>🍎 Apple Kalenteri</h4>
                    <ol>
                        <li>Asetukset → Kalenteri → Tilit</li>
                        <li>"Lisää tili" → "Muu" → "Tilaa kalenteri"</li>
                        <li>Syötä URL</li>
                    </ol>
                </div>
            </div>
        </div>

        <div class="events-section">
            <h2>🎭 Tulevat tapahtumat ({len(sorted_events)} kpl)</h2>
            <p><small>📅 Viimeksi päivitetty: {datetime.now().strftime('%d.%m.%Y %H:%M')}</small></p>
            
            {"".join([f'''
            <div class="event">
                <div class="event-title">{event['title']}</div>
                <div class="event-meta">
                    <span>📅 {event['start_date'].strftime('%d.%m.%Y %H:%M') if event.get('start_date') else 'Aika ei tiedossa'}</span>
                    <span>📍 {event.get('location', 'Paikka ei tiedossa')}</span>
                    <span class="badge">{event.get('source', 'Tuntematon lähde')}</span>
                </div>
                {f'<div class="event-description">{event["description"][:300]}{"..." if len(event.get("description", "")) > 300 else ""}</div>' if event.get('description') else ''}
            </div>
            ''' for event in sorted_events[:15]])}
            
            {f'<p><em>... ja {len(sorted_events) - 15} muuta tapahtumaa kalenterissa</em></p>' if len(sorted_events) > 15 else ''}
        </div>

        <div class="footer">
            <p>🤖 Automaattisesti päivittyvä kalenteri</p>
            <p>Powered by GitHub Actions | 
               <a href="https://github.com/{repo_name}" style="color: rgba(255,255,255,0.8);">
                   📦 Lähdekoodi GitHubissa
               </a>
            </p>
        </div>
    </div>

    <script>
        function copyToClipboard() {{
            const url = document.getElementById('calendar-url').textContent;
            navigator.clipboard.writeText(url).then(function() {{
                const btn = document.querySelector('.copy-btn');
                btn.textContent = '✅ Kopioitu!';
                setTimeout(() => {{
                    btn.textContent = '📋 Kopioi';
                }}, 2000);
            }});
        }}
    </script>
</body>
</html>"""
        
        return html_content
    
    def save_files(self):
        """Tallentaa tiedostot docs-kansioon"""
        self.ensure_docs_dir()
        
        # Tallenna iCalendar
        ical_content = self.generate_ical()
        with open(os.path.join(self.docs_dir, 'calendar.ics'), 'wb') as f:
            f.write(ical_content)
        
        # Tallenna HTML-sivu
        html_content = self.generate_html_page()
        with open(os.path.join(self.docs_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Luo JSON-data (valinnainen, API-käyttöä varten)
        events_json = [{
            'title': event['title'],
            'description': event.get('description', ''),
            'start_date': event['start_date'].isoformat() if event.get('start_date') else None,
            'end_date': event['end_date'].isoformat() if event.get('end_date') else None,
            'location': event.get('location', ''),
            'url': event.get('url', ''),
            'source': event.get('source', '')
        } for event in self.events]
        
        with open(os.path.join(self.docs_dir, 'events.json'), 'w', encoding='utf-8') as f:
            json.dump({
                'updated': datetime.now().isoformat(),
                'count': len(events_json),
                'events': events_json
            }, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Tiedostot tallennettu {self.docs_dir}/ kansioon")
        print(f"   📄 index.html")
        print(f"   📅 calendar.ics")
        print(f"   📊 events.json")

if __name__ == "__main__":
    generator = GitHubCalendarGenerator()
    generator.fetch_events_from_sources()
    generator.save_files()
    
    print("\n🎉 Kalenteri generoitu onnistuneesti!")
    print("GitHub Pages aktivoituna kalenteri on saatavilla osoitteessa:")
    print("https://[käyttäjänimi].github.io/[repo-nimi]/calendar.ics")
