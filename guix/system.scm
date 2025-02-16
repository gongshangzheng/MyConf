;; This is an operating system configuration generated
;; by the graphical installer.
;;
;; Once installation is complete, you can learn and modify
;; this file to tweak the system configuration, and pass it
;; to the 'guix system reconfigure' command to effect your
;; changes.


;; Indicate which modules to import to access the variables
;; used in this configuration.

(define-module (your-module)
  ;; ...
  ;; some stuff here
  ;; ...
  #:use-module (nongnu packages nvidia))
(define transform
  (options->transformation
   '((with-graft . "mesa=nvda"))))

 (define %xorg-config
   "Section \"Device\"
      Identifier     \"Device0\"
      Driver         \"nvidia\"
      VendorName     \"NVIDIA Corporation\"
      BoardName      \"GeForce GTX 1050 Ti\"
  EndSection")

(use-modules (gnu) (nongnu packages linux))
(use-modules (guix transformations))
(use-service-modules cups desktop networking ssh xorg)

(operating-system
 (kernel linux)
 (firmware (list linux-firmware))
 (locale "en_GB.utf8")
 (timezone "Europe/Paris")
 (keyboard-layout (keyboard-layout "us"))
 (host-name "guiz")
 (kernel-arguments (append
                    '("modprobe.blacklist=nouveau")
                    %default-kernel-arguments))
  ;; The list of user accounts ('root' is implicit).
  (users (cons* (user-account
                  (name "xinyu")
                  (comment "Xinyu")
                  (group "users")
                  (home-directory "/home/xinyu")
                  (supplementary-groups '("wheel" "netdev" "audio" "video")))
                %base-user-accounts))

  ;; Packages installed system-wide.  Users can also install packages
  ;; under their own account: use 'guix search KEYWORD' to search
  ;; for packages and 'guix install PACKAGE' to install a package.
  (packages (append (list (specification->package "emacs")
                          (specification->package "emacs-exwm")
                          (specification->package "bspwm")
                          (specification->package "sxhkd")
                          (specification->package
                           "emacs-desktop-environment")) %base-packages))

  ;; Below is the list of system services.  To search for available
  ;; services, run 'guix system search KEYWORD' in a terminal.
  (services
   (append (list (service gnome-desktop-service-type)
                 (simple-service
                  'custom-udev-rules udev-service-type
                  (list nvidia-driver))
                 (service kernel-module-loader-service-type
                          '("ipmi_devintf"
                            "nvidia"
                            "nvidia_modeset"
                            "nvidia_uvm"))
                 (service slim-service-type
                          (slim-configuration
                           (xorg-configuration (xorg-configuration
                                                (modules (cons* nvidia-driver %default-xorg-modules))
                                                (server (transform xorg-server))
                                                (drivers '("nvidia"))))))
                 ;; To configure OpenSSH, pass an 'openssh-configuration'
                 ;; record as a second argument to 'service' below.
                 (service openssh-service-type)
                 (service cups-service-type)
                 (set-xorg-configuration
                  (xorg-configuration (keyboard-layout keyboard-layout))))

           ;; This is the default list of services we
           ;; are appending to.
           %desktop-services))
  (bootloader (bootloader-configuration
                (bootloader grub-efi-bootloader)
                (targets (list "/boot/efi"))
                (keyboard-layout keyboard-layout)))

  ;; The list of file systems that get "mounted".  The unique
  ;; file system identifiers there ("UUIDs") can be obtained
  ;; by running 'blkid' in a terminal.
  (file-systems (cons* (file-system
                         (mount-point "/home")
                         (device (uuid
                                  "668ffc59-5107-4254-912c-3548679568d5"
                                  'ext4))
                         (type "ext4"))
                       (file-system
                         (mount-point "/")
                         (device (uuid
                                  "299d5f88-fa0e-4ff1-ad8a-7432bf8175bd"
                                  'ext4))
                         (type "ext4"))
                       (file-system
                         (mount-point "/boot/efi")
                         (device (uuid "994E-8445"
                                       'fat32))
                         (type "vfat")) %base-file-systems)))
