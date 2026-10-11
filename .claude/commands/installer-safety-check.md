---
description: Vet an install command (especially curl | sh or npx setup) before running it, and give a safer alternative
argument-hint: <the install command or URL>
---

For the installer in "$ARGUMENTS": say what it runs and as which user, whether it pipes a download into a shell, fetches anything else, edits shell profiles or system paths, or asks for sudo. List what to check (repo owner, release signature or checksum, pinned version, a read of the script) and give a safer path: download the script, read it, verify the checksum, or build from source or use a package manager, ideally in a container or VM. Do not run the command. Related skill: `buildwithneej-5-repos-oct9`.
