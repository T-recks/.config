(in-package :stumpwm)

;; terminal setup var and functio setup for use in this config file
(defvar *terminal* "urxvt")
(defcommand exec-terminal (cmd) (:string)
  (run-commands (format nil "exec ~A -e ~A" *terminal* cmd)))
;; terminal binding
(define-key *root-map* (kbd "RET")
  (format nil "exec ~A" *terminal*))
;; remove unused bindings
(define-key *root-map* (kbd "c") nil)
(undefine-key *root-map* (kbd "C-c")) ; just a wrapper for the above

;; swapping defaults
(define-key *root-map* (kbd "s") "hsplit")
(define-key *root-map* (kbd "S") "vsplit")
(define-key *root-map* (kbd "'") "windowlist")
(define-key *root-map* (kbd "\"") "select")
(define-key *groups-map* (kbd "'") "grouplist")
(define-key *groups-map* (kbd "\"") "gselect")

;; duplicating defaults
(define-key *root-map* (kbd "q") "only")

;; some control commands
(define-key *top-map* (kbd "XF86ScreenSaver") "run-shell-command bash ~/.config/i3/scripts/lock/lock.sh")

(define-key *top-map* (kbd "XF86MonBrightnessDown") "run-shell-command xbacklight -dec 5")
(define-key *top-map* (kbd "XF86MonBrightnessUp") "run-shell-command xbacklight -inc 5")

(define-key *top-map* (kbd "XF86AudioLowerVolume") "run-shell-command amixer -q sset Master,0 1- unmute")
(define-key *top-map* (kbd "XF86AudioRaiseVolume") "run-shell-command amixer -q sset Master,0 1+ unmute")
(define-key *top-map* (kbd "XF86AudioMute") "run-shell-command amixer -q sset Master,0 toggle")

(define-key *top-map* (kbd "XF86AudioPlay") "run-shell-command mpc toggle")
(define-key *top-map* (kbd "XF86AudioNext") "run-shell-command mpc next")
(define-key *top-map* (kbd "XF86AudioPrev") "run-shell-command mpc prev")
(define-key *top-map* (kbd "XF86AudioStop") "run-shell-command mpc stop")

;; launch mode
(defvar *launch-map* nil)
(setf *launch-map*
  (let ((c (make-sparse-keymap)))
    (define-key c (kbd "b") "exec qutebrowser")
    (define-key c (kbd "B") "exec waterfox")
    ;; (define-key c (kbd "e") "exec emacsclient -ca \"\"")
    (define-key c (kbd "m") "exec-terminal ncmpcpp")
	(define-key c (kbd "M") "exec thunderbird")
	(define-key c (kbd "n") "exec-terminal newsboat")
	(define-key c (kbd "N") "exec-terminal neofetch")
    (define-key c (kbd "i") "exec-terminal htop")
    ;; (define-key c (kbd "a") "exec-terminal mc")
    (define-key c (kbd "r") "exec-terminal ranger")
    ;; (define-key c (kbd "d") "exec nautilus")
    ;; (define-key c (kbd "p") "exec pavucontrol")
    ;; (define-key c (kbd "m") "exec emacsclient -c -e '(unread-mail)'")
    ;; (define-key c (kbd "y") "exec-terminal wicd-curses")
    ;; (define-key c (kbd "r") "exec redshift")
    ;; (define-key c (kbd "R") "exec killall redshift")
    ;; (define-key c (kbd "Pause") "exec mts-enable")
	(define-key c (kbd ".") "mymenu")
    c))

(define-key *root-map* (kbd ".") '*launch-map*)
