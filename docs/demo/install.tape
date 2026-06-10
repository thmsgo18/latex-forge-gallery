# Gallery README GIF: install a template from the gallery, then use it.
# Regenerate with: ./docs/demo/record.sh  (from the repo root)
# Note: the download of the gallery archive is cut from the recording (Hide/Show).

Output docs/assets/demo-install.gif

Set FontSize 15
Set Width 1100
Set Height 600
Set Padding 18
Set Theme "Catppuccin Mocha"
Set TypingSpeed 40ms

Hide
Type "rm -rf /tmp/forge-gallery-demo && mkdir -p /tmp/forge-gallery-demo && cd /tmp/forge-gallery-demo && latex-forge template remove awesome-cv >/dev/null 2>&1; clear"
Enter
Show

Type "latex-forge template install https://github.com/thmsgo18/latex-forge-gallery/tree/main/templates/cv/awesome-cv"
Sleep 800ms
Enter
# Skip the archive download wait.
Hide
Sleep 150s
Show
Sleep 3s

Type "latex-forge create --name my-cv --template awesome-cv"
Sleep 600ms
Enter
Sleep 3s
# Decline the "Open project in VS Code?" prompt.
Enter
Sleep 4s
