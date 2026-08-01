import os
import json

OUT = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    ("index.html", "בית", "בית"),
    ("massage.html", "עיסוי משולב", "עיסוי משולב"),
    ("breathwork.html", "נשימה + חשיפה לקור", "נשימה וחשיפה לקור"),
    ("about.html", "הדרך שלי", "הדרך שלי"),
    ("contact.html", "יצירת קשר", "יצירת קשר"),
    ("accessibility.html", "הצהרת נגישות", None),
    ("privacy.html", "מדיניות פרטיות", None),
    ("cancellation.html", "מדיניות ביטולים", None),
]

NAV_ITEMS = [
    ("index.html", "בית"),
    ("massage.html", "עיסוי משולב"),
    ("breathwork.html", "נשימה וחשיפה לקור"),
    ("about.html", "הדרך שלי"),
]

BREATH_SVG = ''

def nav_html(current_file):
    lis = []
    for href, label in NAV_ITEMS:
        current = ' aria-current="page"' if href == current_file else ''
        lis.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    return "\n        ".join(lis)

def header(current_file, css_prefix=""):
    return f"""  <header class="site-header">
    <div class="container nav-row">
      <a href="index.html" class="brand">שלומי גולן<span>עיסוי משולב · נשימה וחשיפה לקור</span></a>
      <nav>
        <ul class="nav-links">
        {nav_html(current_file)}
          <li><a href="contact.html" class="nav-cta">יצירת קשר</a></li>
        </ul>
      </nav>
      <button class="nav-toggle" aria-label="פתיחת תפריט" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
"""

def footer():
    return """  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <h4>שלומי גולן</h4>
        <p style="color:#C9C2AC; max-width: 32ch;">קליניקה לעיסוי משולב, נשימה וחשיפה לקור - קיבוץ משמרות, פרדס חנה-כרכור.</p>
        <div class="social-links">
          <a href="https://facebook.com/holisti.co.il" target="_blank" rel="noopener" aria-label="פייסבוק">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.5 9.9v-7H7.9V12h2.6V9.8c0-2.6 1.6-4 3.9-4 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.3 0-1.7.8-1.7 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12Z"/></svg>
          </a>
          <a href="https://instagram.com/Shlomi_holisti.co.il" target="_blank" rel="noopener" aria-label="אינסטגרם">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1"/></svg>
          </a>
          <a href="https://wa.me/c/972546612103" target="_blank" rel="noopener" aria-label="קטלוג בוואטסאפ">
            <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.004 3C9.376 3 4 8.373 4 15c0 2.286.638 4.428 1.744 6.25L4 29l7.938-1.686A11.93 11.93 0 0 0 16.004 27C22.63 27 28 21.627 28 15S22.63 3 16.004 3Zm0 21.75c-1.94 0-3.75-.53-5.303-1.453l-.38-.226-4.71 1 1.03-4.59-.248-.397A9.7 9.7 0 0 1 5.25 15c0-5.93 4.822-10.75 10.754-10.75S26.75 9.07 26.75 15 21.936 24.75 16.004 24.75Zm5.86-8.07c-.32-.16-1.9-.938-2.195-1.046-.294-.108-.508-.16-.723.16-.214.32-.83 1.046-1.018 1.26-.187.214-.374.24-.694.08-.32-.16-1.35-.497-2.572-1.586-.95-.847-1.593-1.893-1.78-2.213-.187-.32-.02-.494.14-.653.144-.143.32-.373.48-.56.16-.187.213-.32.32-.534.107-.214.053-.4-.027-.56-.08-.16-.723-1.744-.99-2.39-.26-.626-.526-.54-.723-.55l-.615-.01c-.213 0-.56.08-.854.4-.294.32-1.12 1.093-1.12 2.666s1.147 3.093 1.307 3.306c.16.214 2.257 3.446 5.47 4.833.764.33 1.36.527 1.825.674.767.244 1.465.21 2.017.128.615-.092 1.9-.777 2.168-1.527.267-.75.267-1.393.187-1.527-.08-.133-.294-.213-.614-.373Z"/></svg>
          </a>
          <a href="https://g.page/r/CW8teVGp989YEAE/review" target="_blank" rel="noopener" aria-label="לפרגן בגוגל" class="stars">
            <span aria-hidden="true">★★★★★</span>
          </a>
        </div>
      </div>
      <div>
        <h4>ניווט</h4>
        <ul class="footer-links">
          <li><a href="massage.html">עיסוי משולב</a></li>
          <li><a href="breathwork.html">נשימה וחשיפה לקור</a></li>
          <li><a href="about.html">הדרך שלי</a></li>
          <li><a href="contact.html">יצירת קשר</a></li>
        </ul>
      </div>
      <div>
        <h4>מידע</h4>
        <ul class="footer-links">
          <li><a href="accessibility.html">הצהרת נגישות</a></li>
          <li><a href="privacy.html">מדיניות פרטיות</a></li>
          <li><a href="cancellation.html">מדיניות ביטולים</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">© 2026 שלומי גולן. כל הזכויות שמורות.</div>
  </footer>
"""

SITE_URL = "https://holisti.co.il"

LOCAL_BUSINESS_SCHEMA = """{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "שלומי גולן - עיסוי משולב, נשימה וחשיפה לקור",
  "image": "%s/assets/treatment-room.png",
  "telephone": "+972546612103",
  "priceRange": "₪₪",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "קיבוץ משמרות, פרדס חנה-כרכור",
    "addressCountry": "IL"
  },
  "url": "%s"
}""" % (SITE_URL, SITE_URL)

def page_shell(title, current_file, body, description=None, extra_schema=None):
    if current_file == "index.html":
        tag_title = "שלומי גולן | עיסוי משולב לטיפול בכאב ואמבטיית קרח"
    else:
        tag_title = f"{title} | שלומי גולן"
    desc = description or "עיסוי משולב, נשימה וחשיפה לקור עם שלומי גולן - קיבוץ משמרות, פרדס חנה-כרכור."
    page_url = f"{SITE_URL}/{current_file}"
    schema_blocks = f'<script type="application/ld+json">\n{LOCAL_BUSINESS_SCHEMA}\n</script>'
    if extra_schema:
        schema_blocks += f'\n<script type="application/ld+json">\n{extra_schema}\n</script>'
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{tag_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{tag_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="{SITE_URL}/assets/treatment-room.png">
<meta property="og:locale" content="he_IL">
<link rel="stylesheet" href="css/style.css">
{schema_blocks}
<!-- Cloudflare Web Analytics -->
<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "cf59eb72f3ce44da95bb66933f09b64c"}}'></script>
<!-- End Cloudflare Web Analytics -->
</head>
<body>
{header(current_file)}
<main>
{body}
</main>
{footer()}
  <a href="https://wa.me/972546612103" class="whatsapp-float" aria-label="שליחת הודעת וואטסאפ" target="_blank" rel="noopener">
    <svg viewBox="0 0 32 32" fill="#fff" xmlns="http://www.w3.org/2000/svg"><path d="M16.004 3C9.376 3 4 8.373 4 15c0 2.286.638 4.428 1.744 6.25L4 29l7.938-1.686A11.93 11.93 0 0 0 16.004 27C22.63 27 28 21.627 28 15S22.63 3 16.004 3Zm0 21.75c-1.94 0-3.75-.53-5.303-1.453l-.38-.226-4.71 1 1.03-4.59-.248-.397A9.7 9.7 0 0 1 5.25 15c0-5.93 4.822-10.75 10.754-10.75S26.75 9.07 26.75 15 21.936 24.75 16.004 24.75Zm5.86-8.07c-.32-.16-1.9-.938-2.195-1.046-.294-.108-.508-.16-.723.16-.214.32-.83 1.046-1.018 1.26-.187.214-.374.24-.694.08-.32-.16-1.35-.497-2.572-1.586-.95-.847-1.593-1.893-1.78-2.213-.187-.32-.02-.494.14-.653.144-.143.32-.373.48-.56.16-.187.213-.32.32-.534.107-.214.053-.4-.027-.56-.08-.16-.723-1.744-.99-2.39-.26-.626-.526-.54-.723-.55l-.615-.01c-.213 0-.56.08-.854.4-.294.32-1.12 1.093-1.12 2.666s1.147 3.093 1.307 3.306c.16.214 2.257 3.446 5.47 4.833.764.33 1.36.527 1.825.674.767.244 1.465.21 2.017.128.615-.092 1.9-.777 2.168-1.527.267-.75.267-1.393.187-1.527-.08-.133-.294-.213-.614-.373Z"/></svg>
  </a>
<script src="js/main.js"></script>
</body>
</html>
"""

def placeholder(label):
    return f'<div class="placeholder-block">[{label} — התוכן ייכנס כאן בשלב הבא]</div>'

# ---------- INDEX ----------
index_body = f"""  <section class="hero">
    <img src="assets/hallway.png" alt="כניסת הקליניקה בקיבוץ משמרות">
    <div class="container hero-content">
      <span class="hero-eyebrow">קיבוץ משמרות, פרדס חנה-כרכור</span>
      <h1>הגוף. לפני הכול.</h1>
      <p style="max-width:50ch;">עיסוי משולב, נשימה וחשיפה לקור.</p>
      <a href="contact.html" class="btn btn-primary hero-cta">יצירת קשר</a>
    </div>
  </section>

  {BREATH_SVG}

  <section class="container">
    <p>העולם משתנה בקצב מסחרר.</p>
    <p>הכול מתייעל. כבר לא צריך לצאת מהבית. בלחיצת כפתור אפשר להזמין אוכל, לבצע פעולות בבנק או לסיים משימות לעבודה.</p>
    <p>הגוף שלנו, לעומת זאת, כמעט שלא השתנה.</p>
    <p>הוא עדיין מופעל על ידי מנגנונים שהתפתחו במשך אלפי שנים, וזקוק לתנועה, למנוחה, למגע, לאתגרים ולהתאוששות, כדי להתמודד טוב יותר עם עומס, מתח וכאב.</p>
  </section>

  <section class="container">
    <h2 style="font-size:1.9rem;">מה הגוף שלך צריך?</h2>
    <div class="track-grid">
      <div class="track-card">
        <span class="tag">טיפול במגע</span>
        <h3>עיסוי משולב</h3>
        <p>לטיפול בכאבים.</p>
        <a href="massage.html" class="btn btn-outline">לעמוד המלא</a>
      </div>
      <div class="track-card">
        <span class="tag">נשימה וחשיפה לקור</span>
        <h3>אמבטיית קרח</h3>
        <p>לחיזוק הגוף ובניית חוסן.</p>
        <a href="breathwork.html" class="btn btn-outline">לעמוד המלא</a>
      </div>
    </div>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">מה מטופלים אומרים</span>
    <h2>חוויות מהטיפולים</h2>
    <div class="testimonial-grid">
      <div class="testimonial-card"><p>"אחד הטיפולים הטובים שקיבלתי בשנים האחרונות, באותו יום הרגשתי בעננים, אבוא שוב בקרוב"</p></div>
      <div class="testimonial-card"><p>"טיפול עמוק ונפלא 🙏 בכל שנותיי לא חוויתי עיסוי כזה - עמוק וקשוב ממש. התחושה הכללית היא של הזנה עמוקה ומלאות 💜"</p></div>
      <div class="testimonial-card"><p>"הרגשתי נהדר, אחרי הטיפול היה שיפור אדיר. תודה על זמן איכות - הרגשתי כאילו התעוררתי משינה 🙏"</p></div>
      <div class="testimonial-card"><p>"שלומי מבחינתי הוא המאסטר! מהאנרגיות הרגועות שהוא מביא איתו ועד לטיפול הסופר מקצועי והמסור שלו. כל טיפול מדוייק ומשלב עוצמות ורכות יחד וכך מרגישה אומנות. למזלי זכיתי גם לחוות ולטבול מספר פעמים באמבטיית הקרח של שלומי. גם כאן.. ההדרכה והנשימות שלפני השרו בי רוגע ושלווה וידעתי שאני בידיים טובות :)"</p><cite>אורלי ברזני</cite></div>
      <div class="testimonial-card"><p>"הייתי אצל שלומי בסדנת אמבטיית קרח, שלומי מדריך נעים ומסביר, מעביר את המשתתפים דרך למידה על נשימה והתגברות על הפחד, קשוב מאוד ונעים לעבור איתו את החוויה הזאת! ממליצה על שלומי מאוד"</p><cite>שי דהן</cite></div>
    </div>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">מי אני</span>
    <div class="bio-row">
      <img src="assets/shlomi.webp" alt="שלומי גולן" class="portrait">
      <p style="max-width:60ch; font-size:1.1rem; margin:0;">שלומי גולן, מטפל במגע ומנחה נשימה וחשיפה לקור. למעלה מעשרים וחמש שנים עוזר לאנשים להרגיש קצת יותר בבית בתוך הגוף שלהם.</p>
    </div>
    <a href="about.html" class="btn btn-outline" style="margin-top:1rem;">הדרך שלי</a>
  </section>
"""

# ---------- SERVICE PAGE TEMPLATE ----------
def service_page(hero_img, hero_alt, h1_placeholder_label):
    return f"""  <section class="hero" style="min-height:44vh;">
    <img src="assets/{hero_img}" alt="{hero_alt}">
    <div class="container hero-content">
      <h1>{placeholder(h1_placeholder_label)}</h1>
    </div>
  </section>

  <section class="container">
    {placeholder('פסקת פתיחה (אינטרו)')}
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">שאלות נפוצות</span>
    <h2>שאלות ותשובות</h2>
    <div class="faq-list">
      {placeholder('פריטי FAQ (accordion) — ייכנסו כ-details/summary')}
    </div>
  </section>

  <section class="container cta-section" style="text-align:center;">
    <a href="contact.html" class="btn btn-primary">יצירת קשר</a>
  </section>
"""

MASSAGE_META_DESCRIPTION = "עיסוי משולב לטיפול בכאבי גב, צוואר וכתפיים ומתח בגוף - קיבוץ משמרות, פרדס חנה-כרכור. טיפול אישי המשלב עיסוי שוודי, רקמות עמוק ועיסוי רפואי."

MASSAGE_FAQ_PAIRS = [
    ("למה עיסוי משולב?", "לפעמים עיסוי רקמות עמוק הוא בדיוק מה שהגוף צריך, ולפעמים דווקא מגע עדין יותר. זה תלוי באדם, בסיבה שבגללה הגיע לטיפול, במה שהגוף מספר באותו יום, ואפילו במה שקורה תוך כדי הטיפול. לכן אין שני טיפולים זהים. כל טיפול נבנה מחדש, בהתאם למה שנכון לאותו רגע. הכלים בעיסוי המשולב מותאמים לתחזוקה, וגם לטיפול בכאב. טכניקות כמו טריגר פוינטס יכולות לעזור בשחרור שרירים תפוסים."),
    ("האם הטיפול כואב?", "הרבה אנשים מגיעים בגלל כאב, ועם זה אנחנו עובדים. לרוב נתמקד גם באזורים תפוסים או רגישים, אבל לא צריך לסבול כדי להשתפר. יש מגוון רחב של טכניקות, והמטרה היא למצוא את הדרך שתאפשר לגוף להשתחרר. לפעמים זה כמעט לא מורגש, ולפעמים יש אי-נוחות מסוימת - אבל כזו שמרגישה \"נכונה\", ולא כמו סבל."),
    ("האם צריך להגיע רק כשכואב?", "ממש לא. מומלץ להגיע ל\"תחזוקה\" - להפחית עומס, לשמור על תנועתיות טובה, ולאפשר לעצמך רגע שקט. יחד עם פעילות גופנית, זו השקעה פנסיונית מצוינת לטווח הארוך."),
    ("כמה זמן נמשך טיפול?", "שעה. יש אפשרות לקבוע מראש גם טיפול של 75 או 90 דקות, בתוספת תשלום."),
    ("האם צריך הכנה מיוחדת לפני ההגעה?", "לא, אבל מומלץ לפנות קצת יותר זמן ולא לאכול ארוחה כבדה לפני הטיפול. העבודה היא עם חמאת שיאה שלרוב נספגת מהר, אבל כדאי לבחור בגדים שלא נורא להכתים."),
    ("כל כמה זמן מומלץ להגיע לטיפול?", "לכל אחד מתאים מרווח אחר. אם בוחרים בסדרה של טיפולים, כדאי לעשות את הטיפול השני בטווח של 7-10 ימים מהטיפול הראשון, ואז להחליט אם להמשיך בתדירות של פעם בשבוע, פעם בשבועיים, פעם בשלושה חודשים, או רק כשצריך."),
    ("מעולם לא עשיתי עיסוי - זה מתאים גם לי?", "איזה כיף לנסות משהו בפעם הראשונה! אבל חוסר הוודאות לפעמים קצת מלחיץ - כמובן שמתאים, ואני מבטיח להסביר הכל כדי שהחוויה תהיה טובה ונינוחה."),
    ("האם אפשר לשלב עם נשימה וחשיפה לקור?", "אפשר לשלב בין שני סוגי הטיפול בהתאם לצורך ולמטרת המפגש."),
    ("למי זה מתאים?", "עיסוי משולב יכול לסייע בהפחתת כאב וסטרס, ובשיפור התנועה במגוון מצבים, בהם כאבי גב, כאבי צוואר וכתפיים, כאבי מפרקים, עומס שרירי, כאבים בעקבות פציעות ספורט ומצבים אורתופדיים שונים. כל טיפול מותאם למצב הגוף באותו יום, ומשלב טכניקות שונות בהתאם לצורך. מי שסובל מכאב או מתח כרוני - לא רק בגב, בצוואר או בכתפיים. גם אנשים בתקופות לחוצות שמרגישים \"מנותקים\" מהגוף שלהם, מי שמחפש טיפול לא-פולשני לצד טיפולים רפואיים אחרים, ומי שרוצה להעניק לעצמו זמן קבוע של האטה, הקשבה לגוף ותחזוקה."),
    ("אילו הסמכות יש לך בתחום?", "אני מוסמך בעיסוי שוודי, עיסוי רקמות עמוק ועיסוי באבנים חמות, וכן בתרפיה מנואלית ותנועה, עיסוי רפואי בכיר, וטיפול אורתופדי הוליסטי. השילוב הזה מאפשר להתאים את הטיפול בדיוק למה שהגוף צריך בכל פגישה. במהלך לימודי הנטורופתיה הוסמכתי גם כמטפל בארומתרפיה ומטפל בכיר ברפלקסולוגיה."),
]

MASSAGE_FAQ_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        } for q, a in MASSAGE_FAQ_PAIRS
    ]
}, ensure_ascii=False, indent=2)

massage_body = f"""  <section class="hero" style="min-height:44vh;">
    <img src="assets/treatment-room.png" alt="חדר עיסוי משולב">
    <div class="container hero-content">
      <span class="hero-eyebrow">קיבוץ משמרות, פרדס חנה-כרכור</span>
      <h1>עיסוי משולב</h1>
      <p style="max-width:50ch;">לטיפול בכאב ומתח</p>
    </div>
  </section>

  <section class="container">
    <p>החיים שלנו עוברים בגוף אחד בלבד.</p>
    <p>הוא הולך איתנו את כל הדרך.</p>
    <p>הוא אמור לאפשר לנו לעשות את הדברים הפשוטים של היום־יום, וגם להתמודד עם האתגרים המורכבים יותר שהחיים מזמנים לנו.</p>
    <p>אבל לפעמים זה לא מרגיש ככה.</p>
    <p>לפעמים מופיע כאב שמשבש את הכול ומשנה את החוויה.</p>
    <p>ולפעמים זו בכלל לא תחושה של כאב. אולי הגוף מרגיש עמוס. אולי נוקשה. אולי הוא פשוט כבר לא מרגיש כמו פעם.</p>
    <p>עיסוי משולב הוא דרך מצוינת לעזור לגוף להתמודד עם כאב, להפחית עומס ולאפשר לו לנוע בחופשיות ובנוחות.</p>
    <p>בטיפול אני משלב שיטות שונות, בהתאם למה שהגוף שלך צריך באותו רגע.</p>
    <p>אין טיפול קבוע, או נוסחה אחת.</p>
    <p>המטרה היא להקשיב, להבין ולבחור את הדרך המתאימה, כדי לאפשר לגוף לעשות את מה שהוא יודע לעשות בצורה טובה יותר.</p>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">מחיר</span>
    <h2>עלות הטיפול</h2>
    <div class="price-grid">
      <div class="price-card"><span class="label">טיפול יחיד</span><span class="amount">330 ₪</span></div>
      <div class="price-card"><span class="label">כרטיסייה ל-5 טיפולים</span><span class="amount">1,500 ₪</span><span class="per">לפי 300 ₪ לטיפול</span></div>
      <div class="price-card"><span class="label">כרטיסייה ל-10 טיפולים</span><span class="amount">2,800 ₪</span><span class="per">לפי 280 ₪ לטיפול</span></div>
    </div>
    <p class="price-note">כל תוספת של 15 דקות מעבר לשעה - 50 ₪.</p>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">שאלות נפוצות</span>
    <h2>שאלות ותשובות</h2>
    <div class="faq-list">
      {"".join(f'''<details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>
      ''' for q, a in MASSAGE_FAQ_PAIRS)}
    </div>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">מה מטופלים אומרים</span>
    <h2>חוויות מהטיפול</h2>
    <div class="testimonial-grid">
      <div class="testimonial-card"><p>"מעסה מוכשר ורגיש. מבין ומכבד. מרגישה שתמיד מנסה למצוא את הדרך המתאימה ביותר לפתור את הבעיות (לומד את הגוף המסוים). הקליניקה החדשה, כמו הישנה, מקסימה ונעימה. ממליצה בחום"</p><cite>מעיין גרשוני</cite></div>
      <div class="testimonial-card"><p>"שלומי הוא מטפל מקצועי, קשוב ויסודי, עם גישה רגועה ואכפתית. הוא יודע להקשיב, להבין את מקור הבעיה ולהתאים את הטיפול באופן אישי. ממליצה עליו בחום לכל מי שמחפש טיפול מקצועי ואנושי."</p><cite>טלי שגיא</cite></div>
      <div class="testimonial-card"><p>"הלכתי לטיפול אצל שלומי - קודם כל יצאתי רפויה, מרחפת, רגועה, כל כך ששעה עברה כמו 10 דקות! וגם כמישהי שמטפלת בעצמי, הרגשתי כל כך בטוחה בידיים של אדם מקצועי ויסודי שיודע לקרוא את המצב של הגוף, לעבוד על הפאשיה בצורה מדהימה, ופשוט לשחרר כאב גם פיזי וגם נפשי. הכל נעשה ברגישות, בצניעות ובחיוך. פשוט מטפל מדהים!"</p><cite>ענת ולדמן</cite></div>
      <div class="testimonial-card"><p>"עברתי אצל שלומי חוויה מתקנת. הגעתי כאובה מאוד, עם סיאטיקה קשה - הטיפול והיחס היו נהדרים, ואחרי כמה פגישות חזרתי לאיתני. ממליצה בכל פה"</p><cite>עדנה בן-יוסף</cite></div>
      <div class="testimonial-card"><p>"שלומי מטפל מקצועי, קשוב, ידיים טובות. יש לו הרבה ניסיון ויכולת להתאים את הטיפול לצרכים שהוא מברר לפני הטיפול. תמיד אני יוצאת מרוצה, והגוף בהודיה על מגע מרפא. ממליצה בחום"</p><cite>אסתר דר</cite></div>
      <div class="testimonial-card"><p>"הגעתי אליו עם כאבי גב מציקים, ותוך זמן קצר הרגשתי הקלה משמעותית. שלומי מעסה מקצועי ברמה הגבוהה ביותר - קשוב, אדיב וסבלני. ממליץ בחום לכל מי שמחפש טיפול איכותי באמת!"</p><cite>אלעד תורג'מן</cite></div>
    </div>
  </section>

  <section class="container cta-section" style="text-align:center;">
    <a href="contact.html" class="btn btn-primary">יצירת קשר</a>
  </section>
"""
BREATHWORK_META_DESCRIPTION = "נשימה וחשיפה לקור לחיזוק הגוף והנפש - קיבוץ משמרות, פרדס חנה-כרכור. מפגשים אישיים, זוגיים וסדנאות קבוצתיות עם שלומי גולן."

BREATHWORK_FAQ_PAIRS = [
    ("כמה זמן נמשך המפגש?", "מפגש אישי או זוגי נמשך כשעה. סדנאות קבוצתיות (עד 6 משתתפים) נמשכות בין 90 דקות לשעתיים, בהתאם למספר המשתתפים."),
    ("האם זה בטוח לכולם?", "הטבילה באמבטיית קרח אינה מתאימה לאנשים עם מחלות לב או כלי דם, יתר לחץ דם לא מאוזן, אפילפסיה, או לנשים בהריון, וכן במצבים בריאותיים נוספים שבהם חשיפה לקור עלולה להוות סיכון. לפני מפגש ראשון אני עורך בירור קצר על המצב הבריאותי כדי להתאים את המפגש אישית, ובמצבים המצריכים זאת אמליץ להתייעץ עם רופא לפני ההשתתפות."),
    ("מעולם לא עשיתי חשיפה לקור - איך מתחילים?", "המפגש הראשון כולל הסבר מלא על כל השלבים, וליווי צמוד לכל אורך הדרך. כדאי להגיע עם בגדים נוחים לשלב תרגילי הנשימה, בגד ים ומגבת לטבילה, ובגדים להחלפה."),
    ("כל כמה זמן מומלץ להגיע?", "התדירות משתנה מאדם לאדם, בהתאם למטרות האישיות - אבל לרוב, פעם או פעמיים בשבוע מאפשרות ליהנות מכל היתרונות של הקור. מומלץ גם לתרגל את הנשימות באופן עצמאי, ויש דרכים לתרגל חשיפה לקור גם באמצעים ביתיים. בשלב מתקדם יותר אפשר להגיע לטבילה בלבד, ללא ליווי בתרגילי הנשימה המקדימים."),
    ("אפשר לשלב עם עיסוי משולב?", "אפשר לשלב בין שני סוגי הטיפול בהתאם לצורך ולמטרת המפגש."),
    ("אילו הסמכות יש לך בתחום?", "הליווי בנשימה וחשיפה לקור מבוסס על הכשרה במודולציה עצבית (Neural Modulation)."),
]

BREATHWORK_FAQ_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        } for q, a in BREATHWORK_FAQ_PAIRS
    ]
}, ensure_ascii=False, indent=2)

breathwork_body = f"""  <section class="hero" style="min-height:44vh;">
    <img src="assets/ice-bath.png" alt="אמבטיית קרח לחשיפה לקור">
    <div class="container hero-content">
      <span class="hero-eyebrow">קיבוץ משמרות, פרדס חנה-כרכור</span>
      <h1>נשימה וחשיפה לקור</h1>
      <p style="max-width:50ch;">לחיזוק הגוף ובניית חוסן</p>
    </div>
  </section>

  <section class="container">
    <p>הקור מתחיל להשפיע כבר בהתחלה.</p>
    <p>הסקרנות כשמגיעים למפגש, הרתיעה והחשש שממש מרגישים באוויר - הכל חלק מתהליך.</p>
    <p>תרגילי הנשימה עוזרים להכין את הגוף, אבל לרוב ברגע הכניסה - הגוף לא ממהר להיכנס למים הקרים.</p>
    <p>הרגע הראשון אמנם קשה, והקול בראש צועק "לברוח", אבל עם נשימה, ויד ביד, מחפשים את הנקודה שאפשר להיאחז בה, ובוחרים להישאר גם באי-הנוחות. ואז קורה הקסם.</p>
    <p>יש שקט, בהירות, חיות ושמחה, ותחושה של מסוגלות.</p>
    <p>חשיפה לקור עשויה לתרום להתאוששות מאימונים, לתחושת ערנות, ולסייע בוויסות מערכת העצבים - יש בנושא גם מחקרים ראשוניים מעניינים, אך מדובר בתחום שעדיין נחקר. ומה שמסקרן אותי באמת הוא דווקא משהו אחר. הבחירה להישאר באי-הנוחות.</p>
    <p>היכולת לשבת ברגע הקשה, לנשום דרכו, ולגלות שיש מעבר אליו - זו בעיניי התרומה האמיתית של הקור. בטח במציאות שבה אנחנו חיים היום.</p>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">מחיר</span>
    <h2>עלות המפגש</h2>
    <div class="price-grid">
      <div class="price-card"><span class="label">סשן אישי (כשעה)</span><span class="amount">330 ₪</span></div>
      <div class="price-card"><span class="label">כרטיסייה ל-5 סשנים</span><span class="amount">1,500 ₪</span><span class="per">לפי 300 ₪ לסשן</span></div>
      <div class="price-card"><span class="label">כרטיסייה ל-10 סשנים</span><span class="amount">2,800 ₪</span><span class="per">לפי 280 ₪ לסשן</span></div>
    </div>
    <p class="price-note">השתתפות בסדנה קבוצתית (שעה עד שעתיים, 2-6 משתתפים) - 250 ₪ לאדם.</p>
    <h3 style="margin-top:2rem;">למתקדמים - טבילה בלבד</h3>
    <div class="price-grid">
      <div class="price-card"><span class="label">טבילה בודדת</span><span class="amount">100 ₪</span></div>
      <div class="price-card"><span class="label">כרטיסייה ל-5 טבילות</span><span class="amount">400 ₪</span><span class="per">לפי 80 ₪ לטבילה</span></div>
      <div class="price-card"><span class="label">כרטיסייה ל-10 טבילות</span><span class="amount">600 ₪</span><span class="per">לפי 60 ₪ לטבילה</span></div>
    </div>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">שאלות נפוצות</span>
    <h2>שאלות ותשובות</h2>
    <div class="faq-list">
      {"".join(f'''<details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>
      ''' for q, a in BREATHWORK_FAQ_PAIRS)}
    </div>
  </section>

  {BREATH_SVG}

  <section class="container">
    <span class="section-label">מה משתתפים אומרים</span>
    <h2>חוויות מהמפגש</h2>
    <div class="testimonial-grid">
      <div class="testimonial-card"><p>"תודה רבה על הליווי המדהים, אחלה אתגר וחוויה של כולם יחד!"</p></div>
      <div class="testimonial-card"><p>"תודה שלומי על ליווי מרגיע וחוויה מדהימה ולא צפויה!"</p></div>
      <div class="testimonial-card"><p>"תודה על החוויה המטורפת, הסבלנות וההקרבה לכל אחד ואחת. יצאתי באורות גבוהים."</p></div>
      <div class="testimonial-card"><p>"אחד הדברים הכי טובים שקרו לי. בלי צחוק."</p></div>
    </div>
  </section>

  <section class="container cta-section" style="text-align:center;">
    <a href="contact.html" class="btn btn-primary">יצירת קשר</a>
  </section>
"""

# ---------- ABOUT ----------
about_body = f"""  <section class="hero" style="min-height:40vh;">
    <img src="assets/corridor.png" alt="מבואת הקליניקה">
    <div class="container hero-content">
      <h1>הדרך שלי</h1>
    </div>
  </section>
  <section class="container">
    <div class="about-intro">
      <img src="assets/shlomi.webp" alt="שלומי גולן" class="portrait">
      <p style="margin:0; font-family: var(--font-display); font-size:1.3rem;">שלומי גולן</p>
    </div>
    <p>תמיד חיפשתי לגלות את ספר החוקים של גוף האדם. להבין איך פועלת המכונה המופלאה שאנחנו חיים בה.</p>
    <p>אי שם בתחילת המילניום למדתי נטורופתיה, מתוך רצון להבין איך הגוף עובד, מה משפיע עליו, ואיך אפשר לעזור לו להתמודד טוב יותר עם כאב.</p>
    <p>עם הזמן גיליתי שאין ספר חוקים אחד. יש עקרונות משותפים: תזונה טובה, תנועה מיטבית, שינה, מגע ונשימה. כל אחד מהם משפיע על איך שהגוף שלנו מרגיש ומתפקד.</p>
    <p>אחרי כמה שנים של טיפול הבנתי שההשפעה שאני הכי אוהב לראות היא זו שמתרחשת דרך המגע. בהמשך גיליתי שגם נשימה וחשיפה לקור, למרות האינסטינקט הראשוני שמרתיע מפני הקור, יכולות להשפיע בצורה עמוקה על הגוף ועל הנפש, ולעזור לבנות חוסן - דבר שאנחנו זקוקים לו במיוחד במציאות שבה אנחנו חיים.</p>
    <p>השינוי לא תמיד דרמטי, אבל לא פעם הוא נראה לעין. לפעמים מספיק לראות איך הבעת הפנים מתרככת בסוף הטיפול, הגוף פחות מתוח, התנועה חופשית יותר, ורמת הכאב יורדת.</p>
    <p>עם השנים למדתי שיטות טיפול שונות ואינספור טכניקות, אבל עם כל מטופל אני מגלה משהו חדש. אנחנו הרי לא מגיעים לטיפול אותו הדבר בכל פעם. הגוף מושפע ממה שעבר עליו, הכאב משתנה, והטיפול צריך להשתנות יחד איתו, כדי להתאים למה שקורה כאן ועכשיו.</p>
  </section>

  <section class="container cta-section" style="text-align:center;">
    <a href="contact.html" class="btn btn-primary">יצירת קשר</a>
  </section>
"""

# ---------- CONTACT ----------
contact_body = f"""  <section class="container" style="padding-top:3rem;">
    <span class="section-label">בואו נדבר</span>
    <h1>יצירת קשר ומיקום</h1>
    <p>הקליניקה נמצאת בקיבוץ משמרות, באזור פרדס חנה-כרכור.</p>
    <p>אני מטפל בימים א'-ו'. יש לתאם טיפול מראש.</p>
  </section>
  <section class="container">
    <div style="border-radius:var(--radius); overflow:hidden; border:1px solid var(--line);">
      <iframe
        src="https://www.google.com/maps?q=%D7%A7%D7%99%D7%91%D7%95%D7%A5+%D7%9E%D7%A9%D7%9E%D7%A8%D7%95%D7%AA&z=13&output=embed"
        width="100%" height="360" style="border:0; display:block;" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade" title="מפת קיבוץ משמרות"></iframe>
    </div>
  </section>
  <section class="container">
    <span class="section-label">יצירת קשר</span>
    <div class="track-card" style="max-width:420px;">
      <span class="tag">טלפון</span>
      <p style="margin:0 0 .5rem;">054-6612103</p>
      <span class="tag">וואטסאפ</span>
      <p style="margin:0;">הדרך המהירה לתאם טיפול</p>
      <a href="https://wa.me/972546612103" class="btn btn-primary" target="_blank" rel="noopener">לשליחת הודעה</a>
    </div>
  </section>
"""

# ---------- SIMPLE POLICY PAGES ----------
def policy_page(title):
    return f"""  <section class="container" style="padding-top:3rem;">
    <h1>{title}</h1>
    {placeholder(f'תוכן {title}')}
  </section>
"""

accessibility_body = f"""  <section class="container" style="padding-top:3rem;">
    <h1>הצהרת נגישות</h1>
    <p>אנו רואים חשיבות רבה במתן שירות שוויוני ונגיש לכלל הגולשים, ופועלים בהתאם לתקן הישראלי (ת"י 5568) ברמת AA, ולחוק שוויון זכויות לאנשים עם מוגבלות.</p>
    <p>התאמות הנגישות באתר כוללות:</p>
    <ul style="color:var(--ink-soft); padding-inline-start:1.3rem; margin:0 0 1.5rem;">
      <li>אפשרות להגדלת טקסט</li>
      <li>ניגודיות צבעים תואמת תקן</li>
      <li>אפשרות ניווט מלא באמצעות מקלדת</li>
      <li>טקסט חלופי (alt) לתמונות באתר</li>
    </ul>
    <h3>רכז נגישות</h3>
    <p style="margin:0;">שלומי גולן</p>
    <p style="margin:0;">טלפון: 054-6612103</p>
    <p>דוא"ל: shlomi.s.g@gmail.com</p>
    <p>אם נתקלתם בבעיית נגישות באתר, או שיש לכם הצעה לשיפור - נשמח שתפנו אליי בפרטים שלמעלה, ואטפל בפנייה בהקדם.</p>
  </section>
"""

privacy_body = f"""  <section class="container" style="padding-top:3rem;">
    <h1>מדיניות פרטיות</h1>
    <h3>איזה מידע נאסף באתר</h3>
    <p>האתר עצמו אינו אוסף או שומר מידע אישי. יצירת קשר מתבצעת באמצעות קישור לוואטסאפ, כשירות חיצוני שאינו בבעלותנו.</p>
    <h3>הצהרת בריאות</h3>
    <p>לאחר תיאום הטיפול, תקבלו קישור להצהרת בריאות שעליכם למלא. ההצהרה מנוהלת באמצעות מערכת חיצונית (My-Cliniq), והפרטים שתמלאו - כולל מידע רפואי - נשמרים בשרתי החברה המפעילה את המערכת, ולא אצלנו. מדיניות הפרטיות המלאה של החברה זמינה <a href="https://www.my-cliniq.com/%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA/" target="_blank" rel="noopener">כאן</a>.</p>
    <h3>שימוש במידע</h3>
    <p>המידע המתקבל דרך הצהרת הבריאות משמש אך ורק לצורך התאמת הטיפול עבורכם, ואינו מועבר לגורם נוסף.</p>
    <h3>פנייה בנוגע למידע האישי שלכם</h3>
    <p>לכל שאלה או בקשה בנוגע למידע שמסרתם, ניתן לפנות אליי ישירות בפרטים המופיעים באתר.</p>
  </section>
"""

cancellation_body = f"""  <section class="container" style="padding-top:3rem;">
    <h1>מדיניות ביטולים</h1>
    <p>החיים דינמיים, ולפעמים המציאות משתנה.</p>
    <p>אם יש צורך לדחות או לבטל טיפול, אשמח לעדכון מוקדם ככל האפשר. כך יהיה קל יותר למצוא מועד חדש שנוח לך, וגם לאפשר למטופלים אחרים ליהנות מהזמן שהתפנה.</p>
    <p>ניתן לשנות או לבטל טיפול ללא עלות עד 24 שעות לפני המועד שנקבע.</p>
    <p>ביטול, שינוי או אי-הגעה בתוך 24 השעות שלפני הטיפול, עלולים לחייב בתשלום חלקי או מלא עבור הטיפול שנקבע.</p>
  </section>
"""

FILES = {
    "index.html": page_shell("בית", "index.html", index_body, description="עיסוי משולב, נשימה וחשיפה לקור עם שלומי גולן - קיבוץ משמרות, פרדס חנה-כרכור. הגוף. לפני הכול."),
    "massage.html": page_shell("עיסוי משולב", "massage.html", massage_body, description=MASSAGE_META_DESCRIPTION, extra_schema=MASSAGE_FAQ_SCHEMA),
    "breathwork.html": page_shell("נשימה וחשיפה לקור", "breathwork.html", breathwork_body, description=BREATHWORK_META_DESCRIPTION, extra_schema=BREATHWORK_FAQ_SCHEMA),
    "about.html": page_shell("הדרך שלי", "about.html", about_body, description="הדרך שלי - שלומי גולן, מטפל במגע ומנחה נשימה וחשיפה לקור, על הדרך שהובילה מהמטופלת הראשונה ועד היום."),
    "contact.html": page_shell("יצירת קשר", "contact.html", contact_body, description="יצירת קשר וקביעת תור אצל שלומי גולן - קיבוץ משמרות, פרדס חנה-כרכור. וואטסאפ וטלפון."),
    "accessibility.html": page_shell("הצהרת נגישות", "accessibility.html", accessibility_body, description="הצהרת נגישות לאתר של שלומי גולן, בהתאם לתקן הישראלי ת\"י 5568 ברמת AA."),
    "privacy.html": page_shell("מדיניות פרטיות", "privacy.html", privacy_body, description="מדיניות הפרטיות של אתר שלומי גולן - איזה מידע נאסף וכיצד הוא נשמר."),
    "cancellation.html": page_shell("מדיניות ביטולים", "cancellation.html", cancellation_body, description="מדיניות ביטולים ושינויי תור אצל שלומי גולן."),
}

# ---------- ROBOTS.TXT ----------
# Search/answer bots: fetch pages live in response to a user question and
# typically link back to the source - allowed.
# Training bots: bulk-scrape content into model training data, with no
# link-back or attribution - blocked.
ROBOTS_TXT = """User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Applebot
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: meta-externalagent
Disallow: /

User-agent: Diffbot
Disallow: /

User-agent: *
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE_URL

# ---------- SITEMAP.XML ----------
SITEMAP_PRIORITY = {
    "index.html": "1.0",
    "massage.html": "0.8",
    "breathwork.html": "0.8",
    "about.html": "0.6",
    "contact.html": "0.6",
    "accessibility.html": "0.2",
    "privacy.html": "0.2",
    "cancellation.html": "0.2",
}

sitemap_urls = "\n".join(
    f"""  <url>
    <loc>{SITE_URL}/{fname}</loc>
    <priority>{SITEMAP_PRIORITY[fname]}</priority>
  </url>"""
    for fname, _, _ in PAGES
)

SITEMAP_XML = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_urls}
</urlset>
"""

FILES["robots.txt"] = ROBOTS_TXT
FILES["sitemap.xml"] = SITEMAP_XML
FILES["google98915dc4dd8df94f.html"] = "google-site-verification: google98915dc4dd8df94f.html\n"

for fname, content in FILES.items():
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(content)

print("Built", len(FILES), "pages")
