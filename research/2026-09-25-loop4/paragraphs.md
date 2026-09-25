# Loop 4 paragraphs, as given to judges (2026-09-25)

Each judge received exactly one paragraph inside the METHOD judge prompt. Judges did not know which paragraphs are YC controls.

## Controls

**C-herdr (herdr).** Install count is from herdr.dev (1,046,795 on 2026-09-25). Pricing is not published; the last sentence gives the usual model for open-source developer infrastructure.

> Developers now run fleets of AI coding agents, often for hours or days, across laptops, servers and sandboxes. Keeping track of that work has become the bottleneck: which agent is blocked, which has finished, which terminal it is in, and why everything died when the laptop closed. This company makes an open-source runtime for coding agents. A background server on each machine owns the agents' terminal sessions, so work survives disconnects, closed laptops and dropped connections. It detects each agent and sorts them into a queue (working, blocked, done) across every project, so developers look only when an agent needs them. They can check in from the terminal, another machine or a phone, and software can drive it through a command line, a socket API and plugins. It reports over a million installs. Customers are developers and engineering teams running several coding agents. Revenue would come from hosted and team features on top of the free runtime.

**C-hopper (Hopper).** Latency and price figures are from withhopper.com (the company's own comparison against GPT-4.1).

> Companies running AI voice agents on phone calls need speech recognition, speech synthesis and a language model that respond fast enough to sound natural, and general-purpose model APIs add delay and cost to every call. This company post-trains speech-to-text, text-to-speech and speech language models on a customer's own production calls, then serves those models and keeps improving them against the customer's live traffic, so they fit its vocabulary, callers and call flows. It reports a time to first token of about 80 milliseconds, against about 600 for GPT-4.1, and $0.50 per million input tokens against $2. Customers are companies that run voice agents at volume, such as contact-center and voice-AI platforms. Revenue comes from usage-based inference fees.

**C-oro (ORO AI).** From oroagents.com and its docs. Pricing is not published; the last sentence gives the usual model for a benchmark that feeds its own model.

> AI agents are starting to shop on people's behalf, but there is no good way to measure whether a shopping agent can finish a long, messy purchase, such as keeping to a budget when the preferred item sells out. Fixed test sets go stale and get memorized. This company runs an open, continuously changing benchmark for commerce agents. Builders submit shopping agents; independent validators run them in sandboxed stores against problems generated fresh each day, and a judge scores the agent's reasoning at every step. The top agent earns rewards for as long as it holds the lead. Every run is kept, and the best step-by-step traces train the company's own commerce model. It runs on the Bittensor network, where rewards are paid in the network's token. Customers are retailers, commerce platforms and agent builders that need a tested shopping agent or training data. Revenue would come from licensing that model and data.
