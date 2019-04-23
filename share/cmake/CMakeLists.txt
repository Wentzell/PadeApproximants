configure_file(PadeApproximants-config.cmake.in PadeApproximants-config.cmake @ONLY)
configure_file(PadeApproximants-config-version.cmake.in PadeApproximants-config-version.cmake @ONLY)
install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximants-config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximants-config-version.cmake
  DESTINATION lib/cmake/PadeApproximants
)

install(EXPORT PadeApproximants-targets DESTINATION lib/cmake/PadeApproximants)
