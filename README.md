# ModernUO AMP repository repair (minimal starter)

This replaces the earlier experimental template files. It is NOT a tested automatic installer. It deliberately provides no Update stage.

1. Keep `illusive817/ModernUO-AMP:main` disconnected from AMP until reviewed.
2. On GitHub in the repository root, replace `manifest.json`, `modernuo.kvp`, `modernuoconfig.json`, `modernuometaconfig.json`, and `modernuoports.json` with this package. You may preserve old files in git history; do not upload the ZIP itself.
3. The repo metadata uses the existing unique ID and a unique `IllusiveUO` prefix, with origin and URL set to this repository.
4. Run `python3 validate_repo.py` locally after extraction. This checks syntax and referenced files, NOT AMP compatibility or actual launch.
5. Only reconnect after the template is reviewed; if the full application list disappears again, remove the custom repository registration immediately.

Caveats: AMP 2.8.0.10 compatibility, ModernUO startup, and the game-data download are not confirmed. `App.UpdateSources=[]` is intentional. ModernUO still needs a compiled distribution and separately acquired UO classic client data.
