/* Auto-generated by genmsg_cpp for file /home/stealth/rosfuerte_workspace/ardrone_test/msg/Send.msg */
#ifndef ARDRONE_TEST_MESSAGE_SEND_H
#define ARDRONE_TEST_MESSAGE_SEND_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"


namespace ardrone_test
{
template <class ContainerAllocator>
struct Send_ {
  typedef Send_<ContainerAllocator> Type;

  Send_()
  : aat_pitch(0.0)
  , aat_roll(0.0)
  , aat_yaw(0.0)
  , aat_ax(0.0)
  , aat_ay(0.0)
  , aat_az(0.0)
  , aat_alt(0)
  , aat_temp(0)
  , textos()
  {
  }

  Send_(const ContainerAllocator& _alloc)
  : aat_pitch(0.0)
  , aat_roll(0.0)
  , aat_yaw(0.0)
  , aat_ax(0.0)
  , aat_ay(0.0)
  , aat_az(0.0)
  , aat_alt(0)
  , aat_temp(0)
  , textos(_alloc)
  {
  }

  typedef float _aat_pitch_type;
  float aat_pitch;

  typedef float _aat_roll_type;
  float aat_roll;

  typedef float _aat_yaw_type;
  float aat_yaw;

  typedef float _aat_ax_type;
  float aat_ax;

  typedef float _aat_ay_type;
  float aat_ay;

  typedef float _aat_az_type;
  float aat_az;

  typedef int32_t _aat_alt_type;
  int32_t aat_alt;

  typedef int32_t _aat_temp_type;
  int32_t aat_temp;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _textos_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  textos;


  typedef boost::shared_ptr< ::ardrone_test::Send_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ardrone_test::Send_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct Send
typedef  ::ardrone_test::Send_<std::allocator<void> > Send;

typedef boost::shared_ptr< ::ardrone_test::Send> SendPtr;
typedef boost::shared_ptr< ::ardrone_test::Send const> SendConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::ardrone_test::Send_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::ardrone_test::Send_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace ardrone_test

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::ardrone_test::Send_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::ardrone_test::Send_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::ardrone_test::Send_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e4f1b7bac35fec1113ab457a402d9ef0";
  }

  static const char* value(const  ::ardrone_test::Send_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe4f1b7bac35fec11ULL;
  static const uint64_t static_value2 = 0x13ab457a402d9ef0ULL;
};

template<class ContainerAllocator>
struct DataType< ::ardrone_test::Send_<ContainerAllocator> > {
  static const char* value() 
  {
    return "ardrone_test/Send";
  }

  static const char* value(const  ::ardrone_test::Send_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::ardrone_test::Send_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float32 aat_pitch\n\
float32 aat_roll\n\
float32 aat_yaw\n\
float32 aat_ax\n\
float32 aat_ay\n\
float32 aat_az\n\
\n\
int32 aat_alt\n\
int32 aat_temp\n\
\n\
string textos\n\
\n\
";
  }

  static const char* value(const  ::ardrone_test::Send_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::ardrone_test::Send_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.aat_pitch);
    stream.next(m.aat_roll);
    stream.next(m.aat_yaw);
    stream.next(m.aat_ax);
    stream.next(m.aat_ay);
    stream.next(m.aat_az);
    stream.next(m.aat_alt);
    stream.next(m.aat_temp);
    stream.next(m.textos);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Send_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ardrone_test::Send_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::ardrone_test::Send_<ContainerAllocator> & v) 
  {
    s << indent << "aat_pitch: ";
    Printer<float>::stream(s, indent + "  ", v.aat_pitch);
    s << indent << "aat_roll: ";
    Printer<float>::stream(s, indent + "  ", v.aat_roll);
    s << indent << "aat_yaw: ";
    Printer<float>::stream(s, indent + "  ", v.aat_yaw);
    s << indent << "aat_ax: ";
    Printer<float>::stream(s, indent + "  ", v.aat_ax);
    s << indent << "aat_ay: ";
    Printer<float>::stream(s, indent + "  ", v.aat_ay);
    s << indent << "aat_az: ";
    Printer<float>::stream(s, indent + "  ", v.aat_az);
    s << indent << "aat_alt: ";
    Printer<int32_t>::stream(s, indent + "  ", v.aat_alt);
    s << indent << "aat_temp: ";
    Printer<int32_t>::stream(s, indent + "  ", v.aat_temp);
    s << indent << "textos: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.textos);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ARDRONE_TEST_MESSAGE_SEND_H
