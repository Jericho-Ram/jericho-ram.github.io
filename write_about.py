import re
html = open('about.html').read()
body = """<main>
<h1>What I've built, what I haven't, and how I work</h1>

<h2>What I've built</h2>
<p>...</p>

<h2>What I haven't</h2>
<p>...</p>

<h2>How I work</h2>
<p>...</p>

<p><a href="contact.html">Send one dataset and one question you want ranked</a></p>
</main>"""
html = re.sub(r'<main>.*?</main>', body, html, flags=re.S)
open('about.html','w').write(html)
