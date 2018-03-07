# xorg
- enable caps lock via modifier(FN?)+CTRL/ESC (currently my caps lock key is set to CTRL when used as a modifier and ESC otherwise)
# i3wm
- move all windows in [current workspace] to workspace [num]
- containers
	- optionally preserve container layout when closing a window
	- open a window in a new container instead of splitting current container
		- Or, open an empty container
	- requires a manual WM instead of dynamic?
- command to move focus to previous window (bound to $mod+tab)
	- similar to CMD+TAB default behavior on MacOS
		- except: window switching should be exact; MacOS will simply switch to the nearest window of the previous program (if you are running multiple windows of the same program switching does not garuntee you return to the exact previous window rather than any window running the same program)
	- maybe rofi already has easy support for this...
- (better window rotation?)
- more descriptive window titles (e.g. windows should give process information not just program information; e.g. "urxvt: vim" or "urxvt: ranger" instead of a bunch of windows that just say "urxvt")
- make mod+hjkl always accurate to window position (e.g. mod+l always moves focus to the window directly right of current focused window)
- replacing workspaces with wmii-like tagging would be worth trying
# qutebrowser
- define custom command [mycommand] so :mycommand is valid
	- maybe just making aliases for existing commands will suite my needs... not sure
- swap ; and : as in my vimrc
- stop 'open -t' from switching automatically view to the new tab
- find a command/keyboard-shortcut for deselecting/defocusing any page element (in VimFX for firefox ESC does this)
- stop automatically moving me to the top of the page while I'm typing a search that shit is very annoying
# rofi
- figure out how to execute arbitrary commands
	- arithmetic?
- implement home directory file searching
# vim
- binding j and k to gj and gk (respectively) is useful for one-off j/k commands but annoying for navigating with [count]j/k commands; ideally, j/k would act like gj/gk when pressed without count but would act like normal j/k when proceeded by a count
