"""Builds the static pages from shared head/nav/footer. Run: python3 build.py"""
EMAIL = "clu2033@gmail.com"
BASE = "https://clu5.github.io/pica-landing/"

def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}assets/logo.png">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
'''

ACTIVE = ' class="active"'

def nav(active):
    links = [("index.html", "Home"), ("approach.html", "Approach"), ("about.html", "About")]
    items = "\n".join(
        f'      <li><a href="{h}"{ACTIVE if h == active else ""}>{t}</a></li>' for h, t in links)
    return f'''<header class="wrap">
  <nav>
    <a class="brand" href="index.html"><img src="assets/logo.png" alt="" width="30" height="30">Pica</a>
    <ul>
{items}
      <li><a class="btn btn-primary" href="index.html#contact">Join the waitlist</a></li>
    </ul>
  </nav>
</header>
'''

CONTACT = f'''  <section id="contact">
    <div class="wrap final">
      <div class="mono">Early access</div>
      <h2>Join the waitlist.</h2>
      <p>Pica is in early development. If you run a research lab or a clinical research group, email us with what you work on and we'll reach out as we open access.</p>
      <p class="email"><a href="mailto:{EMAIL}?subject=Pica">{EMAIL}</a></p>
      <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Pica%20waitlist">Join the waitlist</a>
    </div>
  </section>
'''

FOOT = f'''<footer>
  <div class="wrap">
    <p>© 2026 Pica · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p><i>Pica</i> — knowledge agents for science</p>
  </div>
</footer>

</body>
</html>
'''

GRAPH = '''    <div class="graph" aria-hidden="true">
      <svg viewBox="0 0 400 400">
        <line class="edge" x1="200" y1="200" x2="90" y2="110"/>
        <line class="edge hot" x1="200" y1="200" x2="310" y2="95"/>
        <line class="edge" x1="200" y1="200" x2="330" y2="230"/>
        <line class="edge hot" x1="200" y1="200" x2="110" y2="300"/>
        <line class="edge" x1="200" y1="200" x2="250" y2="330"/>
        <line class="edge" x1="90" y1="110" x2="60" y2="210"/>
        <line class="edge hot" x1="310" y1="95" x2="330" y2="230"/>
        <line class="edge" x1="110" y1="300" x2="60" y2="210"/>
        <line class="edge" x1="250" y1="330" x2="330" y2="230"/>
        <circle class="node" cx="90" cy="110" r="16"/>
        <circle class="node hot" cx="310" cy="95" r="18"/>
        <circle class="node" cx="330" cy="230" r="14"/>
        <circle class="node hot" cx="110" cy="300" r="17"/>
        <circle class="node" cx="250" cy="330" r="13"/>
        <circle class="node" cx="60" cy="210" r="11"/>
        <circle cx="200" cy="200" r="37" fill="var(--bg)"/>
        <image href="assets/logo.png" x="164" y="164" width="72" height="72"/>
        <text x="62" y="80">source</text>
        <text x="282" y="62">finding</text>
        <text x="300" y="268">evidence</text>
        <text x="72" y="340">protocol</text>
        <text x="228" y="368">dataset</text>
        <text x="14" y="242">gap</text>
      </svg>
    </div>
'''

ICON = {
 "refine": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16l-6 7v6l-4 2v-8z"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/></svg>',
 "current": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v4h-4"/></svg>',
}

CREDIT = '<figcaption>Eurasian magpie (<i>Pica pica</i>). Photo: Alexis Lours, <a href="https://commons.wikimedia.org/wiki/File:Eurasian_magpie_2024_03_03_02.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/4.0">CC BY 4.0</a>.</figcaption>'

index = head("Pica — Knowledge agents for science",
             "Pica builds knowledge agents for research teams. They turn lab notes, messages, GitHub repos, databases, and papers into a shared, cited knowledge base.") \
 + nav("index.html") + f"""
<main>
  <div class="wrap hero">
    <div>
      <div class="mono">Knowledge agents for science</div>
      <h1>Your team knows more than it <em>has written down</em>.</h1>
      <p class="lede">Pica builds knowledge agents for research teams. They turn lab notes, messages, GitHub repos, databases, and papers into a shared, cited knowledge base, capturing what teams know but rarely write down or share.</p>
      <div class="cta">
        <a class="btn btn-primary" href="#contact">Join the waitlist</a>
        <a class="btn btn-ghost" href="#how">See how it works</a>
      </div>
    </div>
{GRAPH}  </div>

  <section id="problem">
    <div class="wrap why">
      <blockquote>Most of what a research team knows is <span>siloed and never written up</span>.</blockquote>
      <ul>
        <li><strong>It's scattered</strong>Results live in lab notes, decisions in chat threads, methods in code, data in databases, and context in papers. No one place holds the whole picture.</li>
        <li><strong>It's tacit</strong>Why an approach was dropped, which dataset version to trust, what was already tried: it's rarely captured, and it leaves when people do.</li>
        <li><strong>It's invisible to AI tools</strong>Internal knowledge isn't in any model's training data, and search can find a document but not tell you what your team actually concluded.</li>
      </ul>
    </div>
  </section>

  <section id="what">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">What Pica does</div>
        <h2>A shared knowledge base that maintains itself.</h2>
        <p>Pica's agents work in the background, reading what your team produces and keeping a living record of what it knows.</p>
      </div>
      <div class="grid3">
        <div class="card">
          <div class="icon">{ICON["refine"]}</div>
          <h3>Captures what's known</h3>
          <p>Agents pull findings, decisions, and methods out of everyday work and organize them into linked notes, so knowledge builds up instead of getting lost.</p>
        </div>
        <div class="card">
          <div class="icon">{ICON["check"]}</div>
          <h3>Cited and checked</h3>
          <p>Every claim links back to where it came from. Pica weighs how well each finding is supported and flags where sources disagree.</p>
        </div>
        <div class="card">
          <div class="icon">{ICON["current"]}</div>
          <h3>Kept current</h3>
          <p>As work moves on, knowledge goes stale or gets superseded. Pica notices when the underlying evidence changes and updates what depends on it.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="example">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">An example</div>
        <h2>"Have we tried this before?"</h2>
        <p>A new team member wants to try an idea. Instead of asking around, they ask Pica.</p>
      </div>
      <div class="trace">
        <div class="trace-row"><span class="k">Lab notes</span><span>A similar approach was tested last spring, with <b>mixed results</b></span></div>
        <div class="trace-row"><span class="k">Messages</span><span>The team dropped it because of <b>a data quality issue</b> that has since been fixed</span></div>
        <div class="trace-row"><span class="k">GitHub</span><span>The original code is still on a branch, and the <b>fix landed later</b> in the main pipeline</span></div>
        <div class="trace-row"><span class="k">Papers</span><span>Two recent papers report the approach working in a related setting</span></div>
        <div class="trace-row hl"><span class="k">Answer</span><span>Worth revisiting. The reason it was dropped no longer applies. Every point above links to its source</span></div>
      </div>
      <p class="note">Illustrative example.</p>
    </div>
  </section>

  <section id="where">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">Where you use it</div>
        <h2>Knowledge you own, in the tools you already use.</h2>
      </div>
      <div class="grid3">
        <div class="card">
          <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/></svg></div>
          <h3>Your markdown vault</h3>
          <p>The knowledge base lives as plain markdown files, so it works with Obsidian and git. You can read, edit, and keep all of it.</p>
        </div>
        <div class="card">
          <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 14h3M8 17h6"/></svg></div>
          <h3>Web app</h3>
          <p>Ask questions, browse the knowledge map, and see the sources behind each answer, including what conflicts and what's out of date.</p>
        </div>
        <div class="card">
          <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13 5l-2 14"/></svg></div>
          <h3>API for your agents</h3>
          <p>Your own agents can query the knowledge base and contribute to it, with sources attached to every answer.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="who">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">Who it's for</div>
        <h2>Built for research teams.</h2>
      </div>
    </div>
    <div class="wrap grid2">
      <div class="insight">
        <div class="tag">Research labs</div>
        <h3>A lab memory that doesn't graduate</h3>
        <p>Results, failed attempts, and know-how are spread across people, notebooks, and threads, and they leave when people move on.</p>
        <p>Pica keeps the lab's working knowledge in one place, current and cited.</p>
      </div>
      <div class="insight">
        <div class="tag">Clinical research</div>
        <h3>Evidence you can trace</h3>
        <p>Clinical knowledge is spread across protocols, internal datasets, and fast-moving literature, and much of it can't leave the organization.</p>
        <p>Pica ties every finding to its source and flags what has been superseded.</p>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">How it works</div>
        <h2>From scattered sources to a shared knowledge base.</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Connect</h3><p>Link lab notes, messaging, GitHub, databases, and paper libraries.</p></div>
        <div class="step"><h3>Capture</h3><p>Agents extract findings, decisions, and methods, and link them to their sources.</p></div>
        <div class="step"><h3>Maintain</h3><p>As new work lands, agents reconcile conflicts and retire what's out of date.</p></div>
        <div class="step"><h3>Answer</h3><p>Ask in plain language and get a cited answer, or a clear note that the team doesn't know yet.</p></div>
      </div>
      <a class="more" href="approach.html">Our approach →</a>
    </div>
  </section>

  <section id="magpie">
    <div class="wrap magpie-strip">
      <figure class="magpie">
        <img src="assets/magpie.jpg" alt="A Eurasian magpie standing on a mossy rock" width="1280" height="853" loading="lazy">
        {CREDIT}
      </figure>
      <div>
        <div class="mono">Why Pica</div>
        <h2>Named for one of the most intelligent birds.</h2>
        <p>The magpie, <i>Pica pica</i>, recognizes itself in a mirror, uses tools, and stores food across seasons and remembers where it hid it. Our agents gather what a team knows and remember where each piece came from.</p>
        <a class="more" href="about.html">About Pica →</a>
      </div>
    </div>
  </section>

{CONTACT}</main>

""" + FOOT

approach = head("Pica Approach",
                "How Pica's knowledge agents capture, check, and maintain a research team's internal knowledge.") \
 + nav("approach.html") + """
<main>
  <div class="wrap page-hero">
    <div class="mono">Approach</div>
    <h1>Knowledge you can <em>rely on</em>.</h1>
    <p>A knowledge base written by agents is only useful if people can trust it. Pica is built around a few principles for keeping agent-maintained knowledge accurate, traceable, and up to date.</p>
  </div>

  <section>
    <div class="wrap">
      <div class="thrusts">
        <div class="thrust">
          <div class="num">01</div>
          <div><h3>Capture what isn't written down</h3></div>
          <div>
            <p>The most valuable team knowledge is often tacit: why a decision was made, what was tried and abandoned, which version of a dataset to use.</p>
            <p class="q">Pica's agents look for this knowledge in everyday work and turn it into durable, linked notes.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">02</div>
          <div><h3>Every claim has a source</h3></div>
          <div>
            <p>A knowledge base is only as good as your ability to check it.</p>
            <p class="q">Each entry links back to the notes, messages, code, data, or papers it came from, so anyone can verify it in a click.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">03</div>
          <div><h3>Weigh the evidence</h3></div>
          <div>
            <p>The same result repeated in many places isn't the same as many independent results, and agreement isn't always confirmation.</p>
            <p class="q">Pica tracks where evidence comes from, surfaces disagreements, and points to the checks that would settle them.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">04</div>
          <div><h3>Keep it current</h3></div>
          <div>
            <p>Research moves fast. Findings get revised, methods change, and old conclusions quietly go stale.</p>
            <p class="q">Pica tracks what depends on what and flags knowledge that's outdated or superseded.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">05</div>
          <div><h3>Be honest about gaps</h3></div>
          <div>
            <p>"Nothing found" is only meaningful if the search could have found it.</p>
            <p class="q">When the knowledge isn't there, Pica says so and shows where it looked.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">06</div>
          <div><h3>Spend effort where it counts</h3></div>
          <div>
            <p>Agents work within real limits on time and compute.</p>
            <p class="q">Pica focuses on the sources and questions that matter most to your team, and builds structure that makes every later question faster to answer.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

""" + CONTACT + "</main>\n\n" + FOOT

about = head("About Pica",
             "Pica is named for the magpie and builds knowledge agents for research teams.") \
 + nav("about.html") + f"""
<main>
  <div class="wrap page-hero">
    <div class="mono">About</div>
    <h1>Named for the magpie, <em>Pica pica</em>.</h1>
    <p>The Eurasian magpie is one of the most intelligent birds, and among the most intelligent of all animals. It is one of the few species known to recognize itself in a mirror. It uses tools, and it stores food across seasons and remembers where it hid it.</p>
    <p style="margin-top:16px">Pica builds agents with the same instincts for research teams: they gather what a team knows, remember where each piece came from, and keep it reliable as it changes.</p>
  </div>

  <div class="wrap">
    <figure class="magpie">
      <img src="assets/magpie.jpg" alt="A Eurasian magpie, black and white with iridescent blue-green wings and a long tail, standing on a mossy rock" width="1280" height="853" loading="lazy">
      {CREDIT}
    </figure>
  </div>

  <section>
    <div class="wrap why">
      <blockquote>Research teams don't need more generated text. They need <span>knowledge they can rely on</span>.</blockquote>
      <ul>
        <li><strong>Every claim is cited</strong>Answers link back to the exact sources they came from.</li>
        <li><strong>Honest about gaps</strong>When the knowledge isn't there, Pica says so.</li>
        <li><strong>Yours to keep</strong>Your knowledge base is plain markdown you own, not locked inside a tool.</li>
      </ul>
    </div>
  </section>

{CONTACT}</main>

""" + FOOT

for name, html in [("index.html", index), ("approach.html", approach), ("about.html", about)]:
    open(name, "w").write(html)
print("built")
