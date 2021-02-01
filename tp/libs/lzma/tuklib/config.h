#pragma once

#if defined(__APPLE__)
#include "config_darwin.h"
#endif

#if defined(__linux__)
#include "config_linux.h"
#endif

#undef ASSUME_RAM
#define ASSUME_RAM 16
