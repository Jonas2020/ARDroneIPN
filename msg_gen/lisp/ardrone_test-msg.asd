
(cl:in-package :asdf)

(defsystem "ardrone_test-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Control" :depends-on ("_package_Control"))
    (:file "_package_Control" :depends-on ("_package"))
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "Send" :depends-on ("_package_Send"))
    (:file "_package_Send" :depends-on ("_package"))
  ))