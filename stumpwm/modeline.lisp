(in-package :stumpwm)

(load-module "battery-portable")


;; (setf *bar-med-color* "^B^8")
;; (setf *bar-hi-color* "^B^3")
;; (setf *bar-crit-color* "^B^1")

;; (setf *colors*
;;       '("black"
;;        "red"
;;        "green"
;;        "yellow"
;;        "blue"
;;        "magenta"
;;        "cyan"
;;        "white"
;;        "GreenYellow"
;;        "#009696"))
;; (update-color-map (current-screen))


(setf *group-format* " %t ")
(setf *window-format* "%m%50t ")
;; (setf *window-format* "%m%n%s%20t ")
(setf *mode-line-timeout* 2)

(setf *screen-mode-line-format*
	  (list "^B^7 %g | ^n^b^7 %W ^> %B"
			#|
			'(:eval (stumpwm:run-shell-command "date" t))
			|#
			))

(setf *mode-line-border-width* 0)
;;(setf *mode-line-background-color* "#000809")
;;(setf *mode-line-foreground-color* "DeepSkyBlue")
