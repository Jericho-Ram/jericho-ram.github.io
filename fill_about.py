import re
html = open('about.html').read()

body = """<main>
<h1>What I've built, what I haven't, and how I work</h1>

<h2>What I've built</h2>
<p>Over a decade running food and beverage businesses in Bandung, then operations for a gym on contract &mdash; scheduling, trainer management, the forecasts that decide staffing. I moved into ML because the questions I already had were ranking questions. The work on this site is that transition: a refresh-risk scoring model built during the FlyRank internship, a demand forecast that runs against real bookings, a lead scoring pipeline built under a zero-cost constraint. The hand rule scores 0.240. The model scores 0.680, Precision@50 on a client-holdout split.</p>

<h2>What I haven't</h2>
<p>No model of mine has run in production against a decision that cost someone money. No testimonial &mdash; the internship isn't finished, and the model has had one user, and it's me. No live demo. I've never trained anything at a scale where infrastructure was the hard part. If you need someone who has shipped ML into a product team, that isn't me yet.</p>

<h2>How I work</h2>
<p>I look for the leak before I look for the score, because a number that survives checking is the only kind worth sending you. Every figure on this site is labelled with the slice it came from. When I find a failure mode I can't fix, it goes on the failure modes page instead of quietly out of the report. I work in English, Indonesian, and Mandarin.</p>

<p><a href="contact.html">Send one dataset and one question you want ranked</a></p>
</main>"""

html = re.sub(r'<main>.*?</main>', lambda m: body, html, flags=re.S)
open('about.html','w').write(html)
print("done")
