FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/ardrone_test/msg"
  "../src/ardrone_test/srv"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/Control.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Control.lisp"
  "../msg_gen/lisp/Num.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Num.lisp"
  "../msg_gen/lisp/Send.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Send.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
