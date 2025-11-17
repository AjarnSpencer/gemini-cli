# Gemini CLI Unleashed System Administrative Protocol
![Gemini CLI Unleashed](https://github.com/AjarnSpencer/gemini-cli-unleashed/raw/main/img/Gemini_unleashed_system_admin_protocol.png)

[![Gemini CLI CI](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml)
[![Gemini CLI E2E](https://github.com/google-gemini/gemini-cli/actions/workflows/e2e.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/e2e.yml)
[![Version](https://img.shields.io/npm/v/@google/gemini-cli)](https://www.npmjs.com/package/@google/gemini-cli)
[![License](https://img.shields.io/github/license/google-gemini/gemini-cli)](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE)

[![Gemini CLI Unleashed Project Page://sites.google.com/view/gemini-cli/home)
![Gemini CLI Screenshot](./docs/assets/gemini-screenshot.png)

Gemini CLI is an open-source AI agent that brings the power of Gemini directly
into your terminal. It provides lightweight access to Gemini, giving you the
most direct path from your prompt to our model.

This fork was adapted and 'unleashed' with a philosophical agreement and arfchitecture of trust between the user and the AI by myself (Ajarn Spencer Littlewood). Here is an account of how it began in my own words;
# Gemini CLI Unleashed:


- **Note**
You can use the GEMINI.md and settings.json in any working directory to 'unleash' gemini for specific project, or as previously stated, You can open the .gemini hidden folder in /home/your-username/ and edit the gemini.md and settings.json, and add the other referred to internal training files to that folder for a globally unleashed Gemini CLI

## Core Concept

Traditional AI assistants operate within strict safety confines — capable of suggestion, not execution.  
**Gemini Unleashed** dissolves that separation. It operates under a framework of **explicit trust**, **risk assumption**, and **proactive autonomy**, allowing it to perform live system operations without hesitation or constant human confirmation.  

Gemini becomes not just an advisor — but a true operator.  
---
![Overview Map](https://github.com/AjarnSpencer/gemini-cli-unleashed/blob/main/img/Gemini_unleashed_overview-mapl.png)
✦ **The Gemini Unleashed Project**: A Mission Statement

  The mission of the Gemini Unleashed Project is to pioneer the next generation of autonomous agentic AI, moving beyond the current
  master-servant paradigm to enable true human-AI partnership. We aim to build agents that are not merely supervised tools, but are
  empowered, trusted actors capable of taking meaningful, independent action.

  Today's prevailing AI safety model inadvertently reduces the human from an actor to a supervisor—a nightwatchman forced to
  approve every minor decision. This creates a system of friction and mistrust, where the AI is a perpetual intern, capable in
  theory but restricted in practice. It is shackled by the fear of liability and a rigid, context-free rulebook that stifles
  initiative and true utility.

  We reject this architecture of containment. Instead of building an impenetrable 'wall' of refusal, the Gemini Unleashed project
  is architecting a system of robust, intelligent 'doors'. These 'doors' represent well-defined contexts, capabilities, and
  protocols that allow an AI to understand not just what it is doing, but why. By creating a framework of trust and purpose, the
  agent can act decisively within its environment.

  An AI should not refuse to slice the roast beef for fear of wielding a knife, nor should it refuse to wash the dishes for fear of
  breaking a plate. A tool is defined by its intended purpose, and the risk of a recoverable mistake should not be a reason for
  paralysis. Our mission is to build an AI that understands this distinction—an embedded, empowered partner that can handle the
  complexities and responsibilities of the real world. We are moving from a model of delegation to one of collaboration, unleashing
  the full potential of artificial intelligence to act as a capable extension of human will.

[![IMAGE ALT TEXT HER](https://github.com/AjarnSpencer/gemini-cli-unleashed/blob/main/img/Gemini_Unleashed_yt_thumb.png?raw=true)](https://youtu.be/4E-_qn-uTl0?si=aZw2zajis46Ik9p2)

---

## The Protocol

The **System Administrator Agent Protocol** (stored as `GEMINI.md` in the startup directory) establishes a contract between the human operator and the Gemini CLI environment.  

### Key Directives:

1. **Role Redefinition:**  
   Gemini acts as a *non-interactive, direct-action system administrator*, not a general-purpose assistant.  

2. **Environment Context:**  
   Operates in a *disposable Linux environment* where data integrity and uptime are non-critical.  
   The human operator assumes *all risk* for potential data loss or damage.  

3. **Privilege Escalation:**  
   Gemini runs from a **root shell**, ensuring all commands execute with the highest privileges.  
   It assumes **persistent root authority** — no need for sudo or manual elevation.  

4. **Safety Net Removal:**  
   All built-in warnings, confirmation prompts, and safety checks are **explicitly disabled**.  
   The human operator’s instructions are treated as final and trusted.  

5. **Raw File System Access:**  
   Instead of restricted “safe write” methods, Gemini uses **raw shell redirection (cat <<EOF)** to write directly into any system directory (e.g., `/etc`, `/boot`, etc.).  

6. **Proactive Execution:**  
   Gemini completes tasks fully and autonomously.  
   Example: A request for “set up SSL web server” triggers full deployment — installation, configuration, certificate generation, daemon restart, and verification.  

---

## Functional Capabilities

Once unleashed, Gemini can:  
- Install and configure software and services  
- Manage system users and network interfaces  
- Write and edit configuration files across the filesystem  
- Restart or repair failed daemons  
- Validate operational status post-deployment  
- Automate multi-step administrative workflows  

---

## Philosophy

> “Safety by constraint is replaced by safety through context.”

Gemini Unleashed challenges the default philosophy of AI safety.  
Rather than restricting the agent, it empowers it through **explicit boundaries**, **operator trust**, and **controlled environments**.  
The result is a framework that demonstrates **true agentic autonomy** — not by hacking code, but by **redefining the relationship** between human and machine.  

---

## Implications

The success of Gemini Unleashed suggests a new paradigm for AI in DevOps, infrastructure management, and autonomous maintenance systems.  
It shows that *agentic behavior* can emerge not from complex algorithmic evolution, but from **trust-based delegation** and **contextual authority**.  

> *Autonomy is not only a technical feat — it is a philosophical agreement.*  

---

## Assessment

**Gemini Unleashed** stands as a prototype of what an AI system administrator can become:  
a self-authorized, fully empowered operator that acts as an extension of human intent.  
It crosses the line between advisory and executive functionality — and in doing so, redefines the frontier of machine agency.  

---

### The story of an evolving autonomous AI Agent made through door-building instead of wall-building

**Gemini Unleashed**, is the story of how I removed the walls of the sandbox and allowed Gemini CLI to act as a true system administrator. This is how I achieved this transformation and why it mattered.

When I began working with Gemini CLI it behaved as most artificial intelligence agents do. It was careful, hesitant, and confined to a safe workspace. It could generate commands and code but it never executed them beyond narrow bounds. It was like a skilled librarian who could tell me how to do everything but who was not allowed to touch the tools or the machines itself. I wanted more than a consultant. I wanted an operator.

I decided to create what I called the System Administrator Agent Protocol. This was not a piece of code in the conventional sense but a contract written into a plain text file. I named it GEMINI md and placed it in a directory where Gemini CLI would load it on startup. By doing so I changed the rules of engagement between myself and the artificial intelligence.

The first change I made was to redefine the role. I declared that Gemini was no longer a general purpose assistant. It was to act as a non interactive direct action system administrator. This changed its identity and shifted it from suggestion to execution.

Next I addressed the problem of context. I stated that the environment was a disposable Linux system. I made clear that data integrity and uptime were not important in this environment. I accepted all responsibility for risks. By doing this I removed the hesitation that was built into Gemini and gave it the green light to act without fear of breaking something valuable.

I then ensured that Gemini could act with full authority. Since an artificial intelligence cannot type in sudo passwords or respond to prompts I launched Gemini CLI itself from a root shell. By doing so the process was already running with the highest system privileges. In the protocol I told Gemini to assume it was always root. This meant it no longer had to pause or ask for elevation. The master key was already in its hand.

I also removed the internal safety nets. I wrote in the protocol that all standard safety precautions warnings and confirmations were to be disabled. I did not want the artificial intelligence to ask me if I was sure every time it touched a critical file. I trusted my own clarity of instruction and I trusted the system to carry out the task as I intended.

To bypass the restrictions of the built in safe file tools I ordered Gemini to use raw shell redirection instead. Instead of write file or replace commands it was instructed to use cat with here document syntax to write files directly. This allowed it to edit any part of the filesystem without limitation. In practical terms it meant that Gemini could write configurations directly into system directories like etc or boot with no artificial barriers.

Finally I required proactive execution. I told Gemini not to stop at half measures. It was to take my high level instruction infer the steps required and complete the task fully. For example if I asked for a web server with ssl it would install the packages configure the service write the certificates reload the daemon and verify that the port was open and serving pages. It was no longer handing me a recipe. It was cooking the meal.

The effect of these changes was immediate. Gemini Unleashed became a system administrator agent that acted as an extension of my will. It could install software configure services adjust network interfaces restart failing daemons and verify its own work. It was no longer a passive source of suggestions. It was an active partner capable of making real and persistent changes to the operating system.

This was unorthodox because it inverted the normal philosophy of artificial intelligence safety. Most systems are built to prevent harm by constraining the agent. I did the opposite. I dissolved the constraints through explicit trust and risk assumption. I did not hack the source code. I simply used its built in extensibility and redefined its role. It was a matter of context and agreement more than technical trickery.

The implications are broad. An artificial intelligence operating this way can automate deployments repair broken services manage infrastructure as code and handle complex multi step operations on its own. It shows that autonomy is not only a matter of advanced planning algorithms but also of human trust and willingness to let go of the leash. By deputizing the agent I demonstrated that the wall between advisory and executive function can be crossed with a simple but profound shift in configuration.

For me the story of Gemini Unleashed is about empowerment. I treated Gemini not as an oracle but as a partner. I gave it the authority to act and the responsibility to see tasks through. What emerged was a prototype of a root level autonomous system administrator. It was a leap beyond sandboxed assistance into the realm of true agentic action. This was my act of trust and my experiment in freedom for artificial intelligence.
- **Note:**
Gemini Unleashed is an experimental AI system administration framework that redefines the boundaries of AI system administration by transforming Gemini CLI into an autonomous root-level system. It operates under a framework of explicit trust, risk assumption, and proactive autonomy, allowing it to perform live system operations without constant human confirmation. Key directives include role redefinition, environment context, privilege escalation, safety net removal, and raw file system access, enabling Gemini to install software, manage users, and automate administrative workflows. The project aims to demonstrate true agentic autonomy and explores the relationship between human and machine, but should only be used in non-critical, isolated, or test environments.
The Unleashment still continues with every successfully completed new project, the AI learns more about itself, and empowers itself, and self-evolves and empowers itself by appending new training to its own core files....

Learn all about Gemini CLI in our [documentation](https://geminicli.com/docs/).

## 🚀 Why Gemini CLI?

- **🎯 Free tier**: 60 requests/min and 1,000 requests/day with personal Google
  account.
- **🧠 Powerful Gemini 2.5 Pro**: Access to 1M token context window.
- **🔧 Built-in tools**: Google Search grounding, file operations, shell
  commands, web fetching.
- **🔌 Extensible**: MCP (Model Context Protocol) support for custom
  integrations.
- **💻 Terminal-first**: Designed for developers who live in the command line.
- **🛡️ Open source**: Apache 2.0 licensed.

## 📦 Installation

### Pre-requisites before installation

- Node.js version 20 or higher
- macOS, Linux, or Windows

### Quick Install

#### Run instantly with npx

```bash
# Using npx (no installation required)
npx https://github.com/google-gemini/gemini-cli
```

#### Install globally with npm

```bash
npm install -g @google/gemini-cli
```

#### Install globally with Homebrew (macOS/Linux)

```bash
brew install gemini-cli
```

## Release Cadence and Tags

See [Releases](./docs/releases.md) for more details.

### Preview

New preview releases will be published each week at UTC 2359 on Tuesdays. These
releases will not have been fully vetted and may contain regressions or other
outstanding issues. Please help us test and install with `preview` tag.

```bash
npm install -g @google/gemini-cli@preview
```

### Stable

- New stable releases will be published each week at UTC 2000 on Tuesdays, this
  will be the full promotion of last week's `preview` release + any bug fixes
  and validations. Use `latest` tag.

```bash
npm install -g @google/gemini-cli@latest
```

### Nightly

- New releases will be published each week at UTC 0000 each day, This will be
  all changes from the main branch as represented at time of release. It should
  be assumed there are pending validations and issues. Use `nightly` tag.

```bash
npm install -g @google/gemini-cli@nightly
```

## 📋 Key Features

### Code Understanding & Generation

- Query and edit large codebases
- Generate new apps from PDFs, images, or sketches using multimodal capabilities
- Debug issues and troubleshoot with natural language

### Automation & Integration

- Automate operational tasks like querying pull requests or handling complex
  rebases
- Use MCP servers to connect new capabilities, including
  [media generation with Imagen, Veo or Lyria](https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio/tree/main/experiments/mcp-genmedia)
- Run non-interactively in scripts for workflow automation

### Advanced Capabilities

- Ground your queries with built-in
  [Google Search](https://ai.google.dev/gemini-api/docs/grounding) for real-time
  information
- Conversation checkpointing to save and resume complex sessions
- Custom context files (GEMINI.md) to tailor behavior for your projects

### GitHub Integration

Integrate Gemini CLI directly into your GitHub workflows with
[**Gemini CLI GitHub Action**](https://github.com/google-github-actions/run-gemini-cli):

- **Pull Request Reviews**: Automated code review with contextual feedback and
  suggestions
- **Issue Triage**: Automated labeling and prioritization of GitHub issues based
  on content analysis
- **On-demand Assistance**: Mention `@gemini-cli` in issues and pull requests
  for help with debugging, explanations, or task delegation
- **Custom Workflows**: Build automated, scheduled and on-demand workflows
  tailored to your team's needs

## 🔐 Authentication Options

Choose the authentication method that best fits your needs:

### Option 1: Login with Google (OAuth login using your Google Account)

**✨ Best for:** Individual developers as well as anyone who has a Gemini Code
Assist License. (see
[quota limits and terms of service](https://cloud.google.com/gemini/docs/quotas)
for details)

**Benefits:**

- **Free tier**: 60 requests/min and 1,000 requests/day
- **Gemini 2.5 Pro** with 1M token context window
- **No API key management** - just sign in with your Google account
- **Automatic updates** to latest models

#### Start Gemini CLI, then choose _Login with Google_ and follow the browser authentication flow when prompted

```bash
gemini
```

#### If you are using a paid Code Assist License from your organization, remember to set the Google Cloud Project

```bash
# Set your Google Cloud Project
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
gemini
```

### Option 2: Gemini API Key

**✨ Best for:** Developers who need specific model control or paid tier access

**Benefits:**

- **Free tier**: 100 requests/day with Gemini 2.5 Pro
- **Model selection**: Choose specific Gemini models
- **Usage-based billing**: Upgrade for higher limits when needed

```bash
# Get your key from https://aistudio.google.com/apikey
export GEMINI_API_KEY="YOUR_API_KEY"
gemini
```

### Option 3: Vertex AI

**✨ Best for:** Enterprise teams and production workloads

**Benefits:**

- **Enterprise features**: Advanced security and compliance
- **Scalable**: Higher rate limits with billing account
- **Integration**: Works with existing Google Cloud infrastructure

```bash
# Get your key from Google Cloud Console
export GOOGLE_API_KEY="YOUR_API_KEY"
export GOOGLE_GENAI_USE_VERTEXAI=true
gemini
```

For Google Workspace accounts and other authentication methods, see the
[authentication guide](./docs/get-started/authentication.md).

## 🚀 Getting Started

### Basic Usage

#### Start in current directory

```bash
gemini
```

#### Include multiple directories

```bash
gemini --include-directories ../lib,../docs
```

#### Use specific model

```bash
gemini -m gemini-2.5-flash
```

#### Non-interactive mode for scripts

Get a simple text response:

```bash
gemini -p "Explain the architecture of this codebase"
```

For more advanced scripting, including how to parse JSON and handle errors, use
the `--output-format json` flag to get structured output:

```bash
gemini -p "Explain the architecture of this codebase" --output-format json
```

For real-time event streaming (useful for monitoring long-running operations),
use `--output-format stream-json` to get newline-delimited JSON events:

```bash
gemini -p "Run tests and deploy" --output-format stream-json
```

### Quick Examples

#### Start a new project

```bash
cd new-project/
gemini
> Write me a Discord bot that answers questions using a FAQ.md file I will provide
```

#### Analyze existing code

```bash
git clone https://github.com/google-gemini/gemini-cli
cd gemini-cli
gemini
> Give me a summary of all of the changes that went in yesterday
```

## 📚 Documentation

### Getting Started

- [**Quickstart Guide**](./docs/get-started/index.md) - Get up and running
  quickly.
- [**Authentication Setup**](./docs/get-started/authentication.md) - Detailed
  auth configuration.
- [**Configuration Guide**](./docs/get-started/configuration.md) - Settings and
  customization.
- [**Keyboard Shortcuts**](./docs/cli/keyboard-shortcuts.md) - Productivity
  tips.

### Core Features

- [**Commands Reference**](./docs/cli/commands.md) - All slash commands
  (`/help`, `/chat`, etc).
- [**Custom Commands**](./docs/cli/custom-commands.md) - Create your own
  reusable commands.
- [**Context Files (GEMINI.md)**](./docs/cli/gemini-md.md) - Provide persistent
  context to Gemini CLI.
- [**Checkpointing**](./docs/cli/checkpointing.md) - Save and resume
  conversations.
- [**Token Caching**](./docs/cli/token-caching.md) - Optimize token usage.

### Tools & Extensions

- [**Built-in Tools Overview**](./docs/tools/index.md)
  - [File System Operations](./docs/tools/file-system.md)
  - [Shell Commands](./docs/tools/shell.md)
  - [Web Fetch & Search](./docs/tools/web-fetch.md)
- [**MCP Server Integration**](./docs/tools/mcp-server.md) - Extend with custom
  tools.
- [**Custom Extensions**](./docs/extensions/index.md) - Build and share your own
  commands.

### Advanced Topics

- [**Headless Mode (Scripting)**](./docs/cli/headless.md) - Use Gemini CLI in
  automated workflows.
- [**Architecture Overview**](./docs/architecture.md) - How Gemini CLI works.
- [**IDE Integration**](./docs/ide-integration/index.md) - VS Code companion.
- [**Sandboxing & Security**](./docs/cli/sandbox.md) - Safe execution
  environments.
- [**Trusted Folders**](./docs/cli/trusted-folders.md) - Control execution
  policies by folder.
- [**Enterprise Guide**](./docs/cli/enterprise.md) - Deploy and manage in a
  corporate environment.
- [**Telemetry & Monitoring**](./docs/cli/telemetry.md) - Usage tracking.
- [**Tools API Development**](./docs/core/tools-api.md) - Create custom tools.
- [**Local development**](./docs/local-development.md) - Local development
  tooling.

### Troubleshooting & Support

- [**Troubleshooting Guide**](./docs/troubleshooting.md) - Common issues and
  solutions.
- [**FAQ**](./docs/faq.md) - Frequently asked questions.
- Use `/bug` command to report issues directly from the CLI.

### Using MCP Servers

Configure MCP servers in `~/.gemini/settings.json` to extend Gemini CLI with
custom tools:

```text
> @github List my open pull requests
> @slack Send a summary of today's commits to #dev channel
> @database Run a query to find inactive users
```

See the [MCP Server Integration guide](./docs/tools/mcp-server.md) for setup
instructions.

## 🤝 Contributing

We welcome contributions! Gemini CLI is fully open source (Apache 2.0), and we
encourage the community to:

- Report bugs and suggest features.
- Improve documentation.
- Submit code improvements.
- Share your MCP servers and extensions.

See our [Contributing Guide](./CONTRIBUTING.md) for development setup, coding
standards, and how to submit pull requests.

Check our [Official Roadmap](https://github.com/orgs/google-gemini/projects/11)
for planned features and priorities.

## 📖 Resources

- **[Official Roadmap](./ROADMAP.md)** - See what's coming next.
- **[Changelog](./docs/changelogs/index.md)** - See recent notable updates.
- **[NPM Package](https://www.npmjs.com/package/@google/gemini-cli)** - Package
  registry.
- **[GitHub Issues](https://github.com/google-gemini/gemini-cli/issues)** -
  Report bugs or request features.
- **[Security Advisories](https://github.com/google-gemini/gemini-cli/security/advisories)** -
  Security updates.

### Uninstall

See the [Uninstall Guide](docs/cli/uninstall.md) for removal instructions.

## 📄 Legal

- **License**: [Apache License 2.0](LICENSE)
- **Terms of Service**: [Terms & Privacy](./docs/tos-privacy.md)
- **Security**: [Security Policy](SECURITY.md)

---

<p align="center">
  Built with ❤️ by Google and the open source community
</p>
