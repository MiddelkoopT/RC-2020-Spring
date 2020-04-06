(setq make-backup-files nil)
(menu-bar-mode -1)

(require 'package)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/"))
(package-initialize)
