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
    links = [("index.html", "Home"), ("research.html", "Research"), ("about.html", "About")]
    items = "\n".join(
        f'      <li><a href="{h}"{ACTIVE if h == active else ""}>{t}</a></li>' for h, t in links)
    return f'''<header class="wrap">
  <nav>
    <a class="brand" href="index.html"><img src="assets/logo.png" alt="" width="30" height="30">Pica</a>
    <ul>
{items}
      <li><a class="btn btn-primary" href="about.html#contact">Contact</a></li>
    </ul>
  </nav>
</header>
'''

CONTACT = f'''  <section id="contact">
    <div class="wrap final">
      <div class="mono">Contact</div>
      <h2>Bring Pica to your lab.</h2>
      <p>We're working with a small group of research teams. Tell us what you're working on and we'll be in touch.</p>
      <p class="email"><a href="mailto:{EMAIL}?subject=Pica">{EMAIL}</a></p>
      <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Pica%20early%20access">Request early access</a>
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

index = head("Pica — Knowledge agents for science",
             "Pica builds knowledge agents that turn scattered research into a shared, reliable knowledge layer — refined in the background, checked by independent evidence, and kept current.") \
 + nav("index.html") + f'''
<main>
  <div class="wrap hero">
    <div>
      <div class="mono">Knowledge agents for science</div>
      <h1>Turn scattered research into <em>working knowledge</em>.</h1>
      <p class="lede">Pica's agents work in the background, refining your lab's sources into a shared knowledge layer, checking each other's work, and keeping it current as the evidence changes.</p>
      <div class="cta">
        <a class="btn btn-primary" href="#contact">Request early access</a>
        <a class="btn btn-ghost" href="research.html">Read the research</a>
      </div>
    </div>
{GRAPH}  </div>

  <section id="problem">
    <div class="wrap why">
      <blockquote>The knowledge that matters most in science is <span>distributed, specialized, and internal</span>.</blockquote>
      <ul>
        <li><strong>It isn't in the training data</strong>Lab notebooks, protocols, unpublished results, and internal datasets are invisible to general-purpose models.</li>
        <li><strong>It isn't always factual</strong>It's full of hypotheses, judgment calls, and results that later get superseded.</li>
        <li><strong>Today's tools start from scratch</strong>Retrieval finds what exists but can't separate evidence from noise. Agents re-read every source on every question and leave nothing behind.</li>
      </ul>
    </div>
  </section>

  <section id="what">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">What Pica does</div>
        <h2>A knowledge layer that gets better with use.</h2>
        <p>Most knowledge agents will mostly talk to each other, and meet people only through simple interfaces. That makes trust in the shared layer the thing to get right.</p>
      </div>
      <div class="grid3">
        <div class="card">
          <div class="icon">{ICON["refine"]}</div>
          <h3>A knowledge refinery</h3>
          <p>Agents turn raw sources into durable structure: extracted findings, indexes, crosswalks between datasets, and documentation of each source. Each question becomes cheaper and better answered than the last. Knowledge compounds.</p>
        </div>
        <div class="card">
          <div class="icon">{ICON["check"]}</div>
          <h3>Reliable from unreliable parts</h3>
          <p>Every finding is scored by how much independent evidence supports it. Five agents repeating one shared run count once, and the search behind a "best" result stays on the record.</p>
        </div>
        <div class="card">
          <div class="icon">{ICON["current"]}</div>
          <h3>Kept current</h3>
          <p>As new work lands, parts of any knowledge base go stale or get superseded. Pica tracks what depends on what and rechecks when the evidence underneath shifts.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">How it works</div>
        <h2>From scattered sources to grounded answers.</h2>
      </div>
      <div class="steps">
        <div class="step"><h3>Connect</h3><p>Point Pica at papers, notebooks, datasets, and internal documents. Nothing has to be cleaned up first.</p></div>
        <div class="step"><h3>Refine</h3><p>Background agents decide what's worth building, within a budget, and maintain it against drift.</p></div>
        <div class="step"><h3>Check</h3><p>Findings are weighed by independent support, and the next check goes where it would change the most.</p></div>
        <div class="step"><h3>Answer</h3><p>Every claim is cited to its source. When the knowledge isn't there, Pica says so and names the gap.</p></div>
      </div>
    </div>
  </section>

  <section id="research">
    <div class="wrap">
      <div class="section-head">
        <div class="mono">Research</div>
        <h2>Reliable knowledge from unreliable agents.</h2>
        <p>Pica grows out of research at the MIT Media Lab on how agent-written knowledge can be more reliable than any agent that contributes to it.</p>
      </div>
      <div class="grid2">
        <div class="insight">
          <div class="tag">Economics</div>
          <h3>Knowledge structure is capital</h3>
          <p>Agents work under real budgets of tokens, tool calls, and time, and most of the value sits in a small share of sources.</p>
          <p>Pica treats what agents build as an investment: chosen for expected value, maintained, and retired when it stops paying off.</p>
        </div>
        <div class="insight">
          <div class="tag">Independence</div>
          <h3>Agreement isn't confirmation</h3>
          <p>Agents can agree without adding any independent support, and models tend to over-count repeated evidence.</p>
          <p>Pica records where each piece of evidence came from and counts it once.</p>
        </div>
        <div class="insight">
          <div class="tag">Selection</div>
          <h3>The best result hides the search</h3>
          <p>A result that was the best of forty attempts can reproduce perfectly and still fail on new data.</p>
          <p>Pica keeps the history behind a finding, not just the winner.</p>
        </div>
        <div class="insight">
          <div class="tag">Experimental design</div>
          <h3>Spend checks where they matter</h3>
          <p>A rerun, fresh data, and an audit each cost something and each answer a different doubt.</p>
          <p>Pica picks the check expected to improve the conclusion most per unit of cost.</p>
        </div>
      </div>
      <a class="more" href="research.html">Read more about the research →</a>
    </div>
  </section>

  <section id="magpie">
    <div class="wrap magpie-strip">
      <figure class="magpie">
        <img src="assets/magpie.jpg" alt="A Eurasian magpie standing on a mossy rock" width="1280" height="853" loading="lazy">
        <figcaption>Eurasian magpie (<i>Pica pica</i>). Photo: Alexis Lours, <a href="https://commons.wikimedia.org/wiki/File:Eurasian_magpie_2024_03_03_02.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/4.0">CC BY 4.0</a>.</figcaption>
      </figure>
      <div>
        <div class="mono">Why Pica</div>
        <h2>Named for one of the most intelligent birds.</h2>
        <p>The magpie, <i>Pica pica</i>, recognizes itself in a mirror, uses tools, and stores food across seasons and remembers where it hid it. Our agents gather what a field knows and remember where each piece came from.</p>
        <a class="more" href="about.html">About Pica →</a>
      </div>
    </div>
  </section>

{CONTACT}</main>

''' + FOOT

research = head("Pica Research",
                "The research behind Pica: building a body of knowledge, written and maintained by agents, that is more reliable than any agent contributing to it.") \
 + nav("research.html") + '''
<main>
  <div class="wrap page-hero">
    <div class="mono">Research</div>
    <h1>Reliable knowledge from <em>unreliable agents</em>.</h1>
    <p>Knowledge agents will work asynchronously and at scale, maintaining a shared knowledge layer in the background. Most will talk mainly to each other, and only a few will deal with people directly. One agent's error becomes another agent's input, so reliability has to be built into the layer itself.</p>
  </div>

  <section>
    <div class="wrap">
      <div class="mono">The question</div>
      <p class="question">How do we build a body of knowledge, written and maintained by agents, that is <span>more reliable than any agent contributing to it</span>?</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <div class="mono">Research directions</div>
        <h2>Four problems we work on.</h2>
      </div>
      <div class="thrusts">
        <div class="thrust">
          <div class="num">01</div>
          <div><h3>Budgeted knowledge refinement</h3></div>
          <div>
            <p>Agents can build durable artifacts, such as indexes, extracted findings, crosswalks between datasets, and source documentation, that make later work cheaper and better. Most systems build only throwaway context, and every query pays the full cost of understanding each source again.</p>
            <p class="q">Which artifacts are worth building under a budget, how should they be maintained as sources drift, and when should they be retired? The measure of success is compounding: answer quality per unit of cost improving as the knowledge base grows.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">02</div>
          <div><h3>Assessing evidence</h3></div>
          <div>
            <p>Every finding has a history: the data, seeds, and model behind it, the reports its author read, and the attempts made before choosing what to report. Reports can agree without adding independent support, and a best-of-many result can reproduce perfectly and still fail to generalize.</p>
            <p class="q">How do reuse and selection change the support a set of reports provides, and can an evaluator learn from that history how likely a finding is to hold under independent evaluation?</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">03</div>
          <div><h3>Choosing checks</h3></div>
          <div>
            <p>A check, whether a new run, fresh evaluation data, or an audit of the attempts behind a result, costs compute, time, or expert attention. Consider a result reported by three agents, two of which share a run, that was also the best of forty configurations. Each check answers a different doubt.</p>
            <p class="q">Given the assessment and the cost of checking, which experiment should run next? We treat this as experimental design: pick the check expected to improve the conclusion most per unit of cost.</p>
          </div>
        </div>
        <div class="thrust">
          <div class="num">04</div>
          <div><h3>Knowledge that stays current</h3></div>
          <div>
            <p>A shared knowledge base keeps changing as work progresses and evidence arrives, and parts of it become outdated, superseded, or stale. Unlike code, knowledge has no test suite, and much of it is judgment rather than fact.</p>
            <p class="q">What stands in for regression tests for knowledge? We study blind spots, maps of which questions the knowledge base can and can't answer, and how to say "not found" honestly, which is only evidence when the search could have found it.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="section-head">
        <div class="mono">Foundations</div>
        <h2>Selected prior work.</h2>
        <p>Earlier research on deciding what data is worth acquiring and when a model's output can be trusted.</p>
      </div>
      <ul class="pubs">
        <li><span class="t">Data acquisition via experimental design for data markets</span><span class="m">Lu, Huang, Karimireddy, Vepakomma, Jordan, Raskar · NeurIPS 2024</span></li>
        <li><span class="t">Federated conformal predictors for distributed uncertainty quantification</span><span class="m">Lu, Yu, Karimireddy, Jordan, Raskar · ICML 2023</span></li>
      </ul>
    </div>
  </section>

''' + CONTACT + '</main>\n\n' + FOOT

about = head("About Pica",
             "Pica is named for the magpie and builds knowledge agents for science.") \
 + nav("about.html") + '''
<main>
  <div class="wrap page-hero">
    <div class="mono">About</div>
    <h1>Named for the magpie, <em>Pica pica</em>.</h1>
    <p>The Eurasian magpie is one of the most intelligent birds, and among the most intelligent of all animals. It is one of the few species known to recognize itself in a mirror. It uses tools, and it stores food across seasons and remembers where it hid it.</p>
    <p style="margin-top:16px">Pica builds agents with the same instincts for science: they gather what a field knows, remember where each piece came from, and keep it reliable as it changes.</p>
  </div>

  <div class="wrap">
    <figure class="magpie">
      <img src="assets/magpie.jpg" alt="A Eurasian magpie, black and white with iridescent blue-green wings and a long tail, standing on a mossy rock" width="1280" height="853" loading="lazy">
      <figcaption>Eurasian magpie (<i>Pica pica</i>). Photo: Alexis Lours, <a href="https://commons.wikimedia.org/wiki/File:Eurasian_magpie_2024_03_03_02.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/4.0">CC BY 4.0</a>.</figcaption>
    </figure>
  </div>

  <section>
    <div class="wrap why">
      <blockquote>Science doesn't need more generated text. It needs <span>knowledge it can rely on</span>.</blockquote>
      <ul>
        <li><strong>Every claim is cited</strong>Answers link back to the exact sources they came from.</li>
        <li><strong>Honest about gaps</strong>When the knowledge isn't there, Pica says so and says where it looked.</li>
        <li><strong>Built for researchers</strong>Made for the way research actually happens, with knowledge that is distributed, specialized, and still being worked out.</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap person">
      <div>
        <h3>Charles Lu</h3>
        <div class="role">Founder</div>
      </div>
      <div class="prose">
        <p>PhD researcher at the <strong>MIT Media Lab</strong> working on trustworthy knowledge agents. Previously led development of deep learning models for medical imaging at <strong>Massachusetts General Hospital</strong>, including an FDA-cleared device for ischemic stroke.</p>
        <p>Research on data acquisition, distributed uncertainty quantification, and how language models report what they find, published at NeurIPS and ICML. NSF Graduate Research Fellow.</p>
      </div>
    </div>
  </section>

''' + CONTACT + '</main>\n\n' + FOOT

for name, html in [("index.html", index), ("research.html", research), ("about.html", about)]:
    open(name, "w").write(html)
print("built")
