# Jyväskylän Tapahtumakalenteri 📅

Automaattisesti päivittyvä kalenteri Jyväskylän tapahtumista. Käyttää GitHub Actionsia tapahtumien hakemiseen ja GitHub Pagesia jakamiseen.

## 🚀 Käyttöönotto

1. **Forkkaa** tämä repository
2. **Aktivoi GitHub Pages**:
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main
   - Folder: /docs
3. **Kalenteri on käytettävissä**: `https://[käyttäjänimi].github.io/jyvaskyla-tapahtumat/`

## 📅 Kalenterin tilaaminen

Käy osoitteessa: `https://[käyttäjänimi].github.io/jyvaskyla-tapahtumat/`

**Suora kalenteri-URL**: `https://[käyttäjänimi].github.io/jyvaskyla-tapahtumat/calendar.ics`

## 🔄 Automaattinen päivitys

- Kalenteri päivittyy tunnin välein GitHub Actionsilla
- Voit käynnistää päivityksen manuaalisesti: Actions → "Päivitä Tapahtumakalenteri" → Run workflow

## 🛠 Kehittäminen

Muokkaa tiedostoa `scripts/generate_calendar.py` lisätäksesi uusia tapahtumalähteitä.
