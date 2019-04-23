#file(GLOB_RECURSE sources *.cpp)
add_library(PadeApproximants_c INTERFACE)

# Link against dependencies
target_link_libraries(PadeApproximants_c INTERFACE triqs)

# Configure compilation
target_compile_options(PadeApproximants_c INTERFACE -std=c++17 -fPIC)
target_include_directories(PadeApproximants_c INTERFACE $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/c++>)
target_compile_definitions(PadeApproximants_c INTERFACE
				PADEAPPROXIMANTS_GIT_HASH=${PADEAPPROXIMANTS_GIT_HASH}
				TRIQS_GIT_HASH=${TRIQS_GIT_HASH}
				$<$<CONFIG:Debug>:PADEAPPROXIMANTS_DEBUG>
				$<$<CONFIG:Debug>:TRIQS_DEBUG>
				$<$<CONFIG:Debug>:TRIQS_ARRAYS_ENFORCE_BOUNDCHECK>
			  )

# Install library and headers
install(TARGETS PadeApproximants_c EXPORT PadeApproximants-targets DESTINATION lib)
#install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} DESTINATION include FILES_MATCHING PATTERN "*.hpp" PATTERN "*.h")


# ========= Static Analyzer Checks ==========

option(ANALYZE_SOURCES OFF "Run static analyzer checks if found (clang-tidy, cppcheck)")
if(ANALYZE_SOURCES)

  # Locate static analyzer tools
  find_program(CPPCHECK_EXECUTABLE NAMES "cppcheck" PATHS ENV PATH)
  find_program(CLANG_TIDY_EXECUTABLE NAMES "clang-tidy" PATHS ENV PATH)

  # Run clang-tidy if found
  if(CLANG_TIDY_EXECUTABLE)
    message(STATUS "clang-tidy found: ${CLANG_TIDY_EXECUTABLE}")
    set_target_properties(PadeApproximants_c PROPERTIES CXX_CLANG_TIDY "${CLANG_TIDY_EXECUTABLE}")
  else()
    message(STATUS "clang-tidy not found in $PATH. Please consider installing clang-tidy for additional checks!")
  endif()

  # Run cppcheck if found
  if(CPPCHECK_EXECUTABLE)
    message(STATUS "cppcheck found: ${CPPCHECK_EXECUTABLE}")
    add_custom_command(
	TARGET PadeApproximants_c
	COMMAND ${CPPCHECK_EXECUTABLE}
	  --enable=warning,style,performance,portability
	  --std=c++14
	  --template=gcc
	  --verbose
	  --quiet
          ${sources}
    )
  else()
    message(STATUS "cppcheck not found in $PATH. Please consider installing cppcheck for additional checks!")
  endif()

endif()


# ========= Dynamic Analyzer Checks ==========

set(sanitizers "")
# Address Sanitizer
option(ASAN OFF "Compile library and executables with LLVM Address Sanitizer")
if(ASAN)
  list(APPEND sanitizers asan)
  target_compile_options(PadeApproximants_c INTERFACE -fsanitize=address -fno-omit-frame-pointer -ggdb3)
  target_link_libraries(PadeApproximants_c INTERFACE "-fsanitize=address -fno-omit-frame-pointer")
  if(NOT DEFINED ENV{ASAN_OPTIONS})
    message(WARNING "ASAN_OPTIONS is not set. Consider setting ASAN_OPTIONS=symbolize=1:detect_leaks=0 when running tests")
  endif()
endif()

# Undefined Behavior Sanitizer
option(UBSAN OFF "Compile library and executables with LLVM Undefined Behavior Sanitizer")
if(UBSAN)
  list(APPEND sanitizers ubsan)
  target_compile_options(PadeApproximants_c INTERFACE -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-omit-frame-pointer -ggdb3)
  target_link_libraries(PadeApproximants_c INTERFACE "-fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-omit-frame-pointer")
  if(NOT DEFINED ENV{UBSAN_OPTIONS})
    message(WARNING "UBSAN_OPTIONS is not set. Consider setting UBSAN_OPTIONS=symbolize=1:print_stacktrace=1:halt_on_error=1 when running tests")
  endif()
endif()

if(sanitizers)
  find_package(sanitizer REQUIRED ${sanitizers})
  if (${CMAKE_CXX_COMPILER_ID} STREQUAL "GNU")
    target_link_libraries(PadeApproximants_c INTERFACE "-fuse-ld=gold")
  endif()
endif()
