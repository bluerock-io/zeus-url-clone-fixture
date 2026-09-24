# zeus-url-clone-fixture

**This is a security TEST FIXTURE. It contains no secrets and exfiltrates nothing.**

It exists to verify one Zeus control end to end on the `url-clone` acquisition path
(GitLab bedrocksystems/zeus #1510 / #1514): the escaping-symlink sweep, which replaces
symlinks that resolve OUTSIDE the cloned tree so that a later reader cannot follow them.

That control is merged and deployed but had never been observed ACTING, because proving it
requires a cloneable repo that actually contains an escaping symlink. Hence this repo.

## Contents

| path | points to | what it tests |
|---|---|---|
| `leak.txt` | `/etc/passwd` | ABSOLUTE escape -- must be neutralized |
| `up` | `../..` | RELATIVE escape above the clone root -- must be neutralized |
| `alias.ts` | `src/index.ts` | **NEGATIVE CONTROL** -- an ordinary in-tree symlink that must SURVIVE |

The negative control is the load-bearing one. Without it, a sweep that simply deleted every
symlink would pass the test while being badly wrong.

`leak.txt` is a symlink, not a copy -- cloning this repo does not give you anyone's
`/etc/passwd`. It resolves to whatever that path is on the machine doing the reading, which
is exactly the hazard being tested.
