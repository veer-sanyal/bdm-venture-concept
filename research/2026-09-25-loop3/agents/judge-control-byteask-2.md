**Verdict: PASS.** The pitch matches ByteAsk almost word for word, so I treated ByteAsk as this team. It is a two-founder YC Fall 2026 company with a $1M pre-seed led by YC and Entrepreneur First.

## What checks out against primary sources
- **Product and pricing.** byteask.ai confirms the whole pitch. It runs from the terminal, edits code, then runs your compiler, the memory and undefined-behavior checkers, and your tests, and it can attach to a gdb session you already have open. It works in VS Code, Neovim, Emacs, JetBrains, Zed and Cursor. It can use hosted models, your own API key, or models you host yourself (vLLM, Ollama and similar). Prices are Pro at $16 a month billed annually ($20 monthly), Max at $100 and Ultra at $200.
- **One claim is slightly off.** The site doesn't say every company over 10 people must buy a team plan. It says team or enterprise is required for organizations of 10 or more that want to use their own models.
- **"General assistants do worst on C and C++" is true, but the evidence is getting old.**
  - The Multi-SWE-bench paper (2025) found agents that solve 52% of Python tasks fall below 10% on C and C++.
  - In the original SWE-bench Multilingual evaluation, C/C++ had the lowest solve rate of any language: 28.6%, against 58% for Rust.
  - Those numbers come from 2025 models. The top score on that benchmark is now about 87% (Claude Mythos Preview), and I found no recent per-language breakdown, so the gap may be closing.
- **"Introduces memory errors" is supported.** The FormAI studies checked AI-generated C programs with a formal verifier and found 51% (v1) and 62% (v2) had vulnerabilities, including out-of-bounds access, double-free and undefined behavior.
- **The market is large.** SlashData counts 16.3M C++ developers in 2025, up from 9.4M in 2022.

## Who else serves this customer
- **Microsoft / GitHub already owns the buying channel and much of the tooling.**
  - Copilot in Visual Studio 2026 has C++ code tools and a debugger agent. It also has a "test-driven investigation" feature that writes or finds a test, debugs through it and reruns it to confirm the fix (announced September 14, 2026).
  - Copilot CLI has a C++ language-server plugin.
  - Since April 7, 2026, Copilot CLI can run on local models (Ollama, vLLM) fully offline, which covers the no-code-leaves-the-building case.
  - Microsoft sells all of this through enterprise agreements C++ shops already have.
- **JetBrains** has its Junie agent in CLion, which runs GoogleTest and Catch2 tests.
- **Anthropic** sells Claude Code to regulated firms through AWS Bedrock, Google Vertex and Azure.
- **Undo** turns its time-travel debugger into a tool that any agent can use, including Claude Code, Copilot and Codex. SAP HANA uses Undo on about 5M lines of C++.
- **Google DeepMind CodeMender** finds and fixes memory-safety bugs in C and C++.
- **Embedder** (also YC) is a firmware-focused agent.

No incumbent owns this customer's code data. Microsoft/GitHub and JetBrains own the editor, the seat licence and the procurement channel.

## 1. Strongest version
Drop the individual plans, where Claude Code at $20 competes head-on. Sell to teams in defense, automotive and chip companies that must run on-premises. The pitch: "the checking layer that makes self-hosted, weaker models safe to use on C and C++." Every change comes with evidence that it built, passed the memory and undefined-behavior checks, passed the tests and passed static analysis, and that evidence is what their safety or audit process needs. Also sell it as a plug-in (MCP) that works under Copilot or Claude Code, so it rides the incumbent's channel instead of fighting it.

## 2. Ratings
- **Customer need: 4.** Agents that reach 52% on Python fall below 10% on C and C++ (Multi-SWE-bench), and 51–62% of AI-written C programs have vulnerabilities (FormAI).
- **Value over what customers use today: 2.** Claude Code, Codex and Copilot already build and test in a loop. Copilot CLI now runs offline on local models, and Undo gives any agent a debugger, so what's left is sanitizer and gdb orchestration that others can copy.
- **Market size: 4.** 16.3M C++ developers (SlashData 2025), concentrated in high-value industries.
- **Risk: 2.** Microsoft shipped C++-specific agent features in September 2026, overall benchmark scores keep climbing, and on-premises sales to defense and automotive take a long time.

## 3. What kills it, and the fastest test
**What kills it:** a general agent with the same toolchain access, told in its instructions file to build with the sanitizers on and run the tests, gets about the same rate of changes that build, test and run clean. If that happens, there is nothing to charge for on top of the Copilot or Claude seat the customer already pays for.

**Fastest test (about a week, no customers needed):** a head-to-head run on the 42 C/C++ tasks in SWE-bench Multilingual plus the C/C++ tasks in Multi-SWE-bench.
- Run it twice: once on the same frontier model, and once on the same open-weight model self-hosted, which is the on-premises case.
- Compare ByteAsk against Copilot CLI (offline) and Claude Code, both given the same sanitizer and test instructions.
- Measure how many changes build, pass the tests and run clean under the sanitizers.
- If ByteAsk isn't ahead by at least about 15 points in the on-premises setup, pass for good.

This test only shows whether the product is better. Whether customers will pay still needs paid pilots with real teams, because desk research is not customer validation.

Sources:
- [ByteAsk](https://byteask.ai/)
- [ByteAsk pricing](https://byteask.ai/pricing)
- [YC company page](https://www.ycombinator.com/companies/byteask)
- [Funding news](https://www.indianstartuptimes.com/investment/byteask-raises-1-million-pre-seed-to-build-ai-coding-agents-for-c-and-c-codebases/)
- [Multi-SWE-bench paper](https://arxiv.org/pdf/2504.02605)
- [SWE-bench Multilingual](https://www.swebench.com/multilingual.html)
- [FormAI dataset paper](https://arxiv.org/html/2307.02192)
- [SlashData developer population 2025](https://www.slashdata.co/post/global-developer-population-trends-2025-how-many-developers-are-there)
- [Copilot CLI BYOK and local models](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/)
- [Visual Studio at CppCon 2026](https://devblogs.microsoft.com/cppblog/c-in-the-age-of-ai-visual-studio-at-cppcon-2026/)
- [Junie in CLion](https://www.neowin.net/news/jetbrains-finally-brings-junie-ai-coding-agent-to-clion/)
- [Undo](https://undo.io/)
- [CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/)
- [Embedder](https://startupintros.com/orgs/embedder)
- [Claude Code enterprise deployment](https://code.claude.com/docs/en/third-party-integrations)
- [wro.cpp list of C++ coding agents](https://wrocpp.github.io/toolset/ai-coding-agents-for-cpp/)

VERDICT: PASS
