#pragma once

#if defined(__IOS__) || defined(__ANDROID__)
#include_next <cxxabi.h>
#else
#include <tp/libs/cxxrt/cxxabi.h>
#endif
