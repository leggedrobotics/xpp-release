Name:           ros-kinetic-xpp-quadrotor
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS xpp_quadrotor package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/leggedrobotics/xpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-xpp-vis
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-xpp-vis

%description
The URDF file for a quadrotor to be used with the xpp packages and a simple rviz
publisher of quadrotor tfs. Adapted from Daniel Mellinger, Nathan Michael, Vijay
Kumar, &quot;Trajectory Generation and Control for Precise Aggressive Maneuvers
with Quadrotors&quot;.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Apr 18 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.6-0
- Autogenerated by Bloom

* Thu Feb 01 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.5-0
- Autogenerated by Bloom

* Wed Jan 03 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.4-0
- Autogenerated by Bloom

* Fri Nov 03 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.3-0
- Autogenerated by Bloom

* Fri Oct 27 2017 Alexander W. Winkler <winklera@ethz.ch> - 1.0.1-0
- Autogenerated by Bloom

