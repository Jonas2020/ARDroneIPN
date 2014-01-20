; Auto-generated. Do not edit!


(cl:in-package ardrone_test-msg)


;//! \htmlinclude Send.msg.html

(cl:defclass <Send> (roslisp-msg-protocol:ros-message)
  ((aat_pitch
    :reader aat_pitch
    :initarg :aat_pitch
    :type cl:float
    :initform 0.0)
   (aat_roll
    :reader aat_roll
    :initarg :aat_roll
    :type cl:float
    :initform 0.0)
   (aat_yaw
    :reader aat_yaw
    :initarg :aat_yaw
    :type cl:float
    :initform 0.0)
   (aat_ax
    :reader aat_ax
    :initarg :aat_ax
    :type cl:float
    :initform 0.0)
   (aat_ay
    :reader aat_ay
    :initarg :aat_ay
    :type cl:float
    :initform 0.0)
   (aat_az
    :reader aat_az
    :initarg :aat_az
    :type cl:float
    :initform 0.0)
   (aat_alt
    :reader aat_alt
    :initarg :aat_alt
    :type cl:integer
    :initform 0)
   (aat_temp
    :reader aat_temp
    :initarg :aat_temp
    :type cl:integer
    :initform 0)
   (textos
    :reader textos
    :initarg :textos
    :type cl:string
    :initform ""))
)

(cl:defclass Send (<Send>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Send>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Send)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ardrone_test-msg:<Send> is deprecated: use ardrone_test-msg:Send instead.")))

(cl:ensure-generic-function 'aat_pitch-val :lambda-list '(m))
(cl:defmethod aat_pitch-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_pitch-val is deprecated.  Use ardrone_test-msg:aat_pitch instead.")
  (aat_pitch m))

(cl:ensure-generic-function 'aat_roll-val :lambda-list '(m))
(cl:defmethod aat_roll-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_roll-val is deprecated.  Use ardrone_test-msg:aat_roll instead.")
  (aat_roll m))

(cl:ensure-generic-function 'aat_yaw-val :lambda-list '(m))
(cl:defmethod aat_yaw-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_yaw-val is deprecated.  Use ardrone_test-msg:aat_yaw instead.")
  (aat_yaw m))

(cl:ensure-generic-function 'aat_ax-val :lambda-list '(m))
(cl:defmethod aat_ax-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_ax-val is deprecated.  Use ardrone_test-msg:aat_ax instead.")
  (aat_ax m))

(cl:ensure-generic-function 'aat_ay-val :lambda-list '(m))
(cl:defmethod aat_ay-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_ay-val is deprecated.  Use ardrone_test-msg:aat_ay instead.")
  (aat_ay m))

(cl:ensure-generic-function 'aat_az-val :lambda-list '(m))
(cl:defmethod aat_az-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_az-val is deprecated.  Use ardrone_test-msg:aat_az instead.")
  (aat_az m))

(cl:ensure-generic-function 'aat_alt-val :lambda-list '(m))
(cl:defmethod aat_alt-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_alt-val is deprecated.  Use ardrone_test-msg:aat_alt instead.")
  (aat_alt m))

(cl:ensure-generic-function 'aat_temp-val :lambda-list '(m))
(cl:defmethod aat_temp-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:aat_temp-val is deprecated.  Use ardrone_test-msg:aat_temp instead.")
  (aat_temp m))

(cl:ensure-generic-function 'textos-val :lambda-list '(m))
(cl:defmethod textos-val ((m <Send>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ardrone_test-msg:textos-val is deprecated.  Use ardrone_test-msg:textos instead.")
  (textos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Send>) ostream)
  "Serializes a message object of type '<Send>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aat_pitch))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aat_roll))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aat_yaw))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aat_ax))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aat_ay))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'aat_az))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'aat_alt)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'aat_temp)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'textos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'textos))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Send>) istream)
  "Deserializes a message object of type '<Send>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aat_pitch) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aat_roll) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aat_yaw) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aat_ax) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aat_ay) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'aat_az) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'aat_alt) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'aat_temp) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'textos) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'textos) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Send>)))
  "Returns string type for a message object of type '<Send>"
  "ardrone_test/Send")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Send)))
  "Returns string type for a message object of type 'Send"
  "ardrone_test/Send")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Send>)))
  "Returns md5sum for a message object of type '<Send>"
  "e4f1b7bac35fec1113ab457a402d9ef0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Send)))
  "Returns md5sum for a message object of type 'Send"
  "e4f1b7bac35fec1113ab457a402d9ef0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Send>)))
  "Returns full string definition for message of type '<Send>"
  (cl:format cl:nil "float32 aat_pitch~%float32 aat_roll~%float32 aat_yaw~%float32 aat_ax~%float32 aat_ay~%float32 aat_az~%~%int32 aat_alt~%int32 aat_temp~%~%string textos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Send)))
  "Returns full string definition for message of type 'Send"
  (cl:format cl:nil "float32 aat_pitch~%float32 aat_roll~%float32 aat_yaw~%float32 aat_ax~%float32 aat_ay~%float32 aat_az~%~%int32 aat_alt~%int32 aat_temp~%~%string textos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Send>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     4 (cl:length (cl:slot-value msg 'textos))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Send>))
  "Converts a ROS message object to a list"
  (cl:list 'Send
    (cl:cons ':aat_pitch (aat_pitch msg))
    (cl:cons ':aat_roll (aat_roll msg))
    (cl:cons ':aat_yaw (aat_yaw msg))
    (cl:cons ':aat_ax (aat_ax msg))
    (cl:cons ':aat_ay (aat_ay msg))
    (cl:cons ':aat_az (aat_az msg))
    (cl:cons ':aat_alt (aat_alt msg))
    (cl:cons ':aat_temp (aat_temp msg))
    (cl:cons ':textos (textos msg))
))
