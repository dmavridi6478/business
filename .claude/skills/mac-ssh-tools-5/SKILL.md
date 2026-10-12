---
name: mac-ssh-tools-5
description: The @henryxagi "SSH without the tool sprawl - MXterm and 4 more for your servers" carousel - MXterm (SSH and an SFTP panel beside your agents), Termius (modern SSH and SFTP client for Mac), Cyberduck (FTP, SFTP and cloud storage in one browser), SSH Keys Manager (local SSH keys and Git identities) and Core Tunnel (SSH tunnels in one place) - with what each does, what is unverified, and key-handling safety rules. Use when choosing Mac tools for servers, SFTP, SSH keys or tunnels.
---

# Mac SSH tools (5)

| App | Tagline (slide) | Notes |
|---|---|---|
| MXterm | SSH and an SFTP panel, beside your agents | see `agent-terminals-mac-5`; verify source |
| Termius | a modern SSH and SFTP client for Mac | established commercial app with a free tier; sync features store hosts in their cloud |
| Cyberduck | FTP, SFTP and cloud storage in one browser | long-standing open-source client; S3, WebDAV, Dropbox, OneDrive etc. |
| SSH Keys Manager | manage local SSH keys and Git identities | slide shows keys list with fingerprints; verify publisher before trusting it with private keys |
| Core Tunnel | manage SSH tunnels in one place | local and remote port forwarding, per-tunnel status; verify publisher |

No licences, links or versions on the slides; screenshots are mock-ups on laptop frames.

## Safety
1. A key manager can read private keys: use apps from the official site or App Store, and prefer ones that use the system keychain or ssh-agent.
2. Use passphrases and per-purpose keys; revoke any key you pasted into a tool you stop using.
3. Tunnels expose services: bind to 127.0.0.1 and close what you do not need.
4. Cloud sync of hosts and keys is a trust decision.
Command: `/ssh-tool-pick`. Related: `agent-terminals-mac-5`, `secrets-management`, `/installer-safety-check`.
