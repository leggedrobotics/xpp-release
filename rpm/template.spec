Name:           ros-melodic-xpp-vis
Version:        1.0.9
Release:        0%{?dist}
Summary:        ROS xpp_vis package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/leggedrobotics/xpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-kdl-parser
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-tf
Requires:       ros-melodic-visualization-msgs
Requires:       ros-melodic-xpp-msgs
Requires:       ros-melodic-xpp-states
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-kdl-parser
BuildRequires:  ros-melodic-robot-state-publisher
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-visualization-msgs
BuildRequires:  ros-melodic-xpp-msgs
BuildRequires:  ros-melodic-xpp-states

%description
Visualization for the XPP Motion Framework.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Jul 10 2018 Alexander W. Winkler <winklera@ethz.ch> - 1.0.9-0
- Autogenerated by Bloom

