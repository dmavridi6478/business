# Procedure: Unlabeled Attachment Intake

## When this applies
An uploaded file (zip, photo batch, document, export, etc.) shows up in the
conversation with no accompanying instruction, or with an instruction that
doesn't clearly relate to the file's actual content.

## Steps

1. **Inspect before asking.** Look at the file itself — list a zip's
   contents, check file type/size — without extracting everything, committing
   it anywhere, or otherwise acting on it. This is what a clarifying question
   should be grounded in, not a guess.

2. **Never assume intent.** Don't extract, commit, analyze in depth, or
   otherwise process the file until the user has said what they want done
   with it. A file arriving is not itself a request.

3. **Ask one grounded, structured question.** Use 2-4 concrete options that
   reference what's actually in the file (e.g. "9 JPEGs from an iCloud
   export" — not "a file"). Prefer a recommended default when one is
   reasonable.

4. **If the answer doesn't connect to the file, don't force-fit it.** Ask one
   more targeted clarifying question that names the mismatch explicitly,
   rather than guessing at a reinterpretation. Stop after resolving the
   mismatch — don't keep re-litigating once the user has clarified.

5. **Execute minimally.** Once intent is confirmed, do only what was
   approved, scoped to what was asked — no extra cleanup, no bundling in
   unrelated changes.

6. **Personal photo batches default to not versioning.** Don't commit raw
   personal photos into git history without explicit confirmation (repo
   bloat, personal data in permanent history). Default to describing/using
   them in-session, or storing them outside version control, unless the user
   explicitly wants them committed.

7. **Repeat batches in the same session.** If the user has already
   established a standing preference for this kind of attachment (e.g. "stop
   asking, just ignore future photo batches"), follow it without re-asking.
