configure_file(PadeApproximant-config.cmake.in PadeApproximant-config.cmake @ONLY)
configure_file(PadeApproximant-config-version.cmake.in PadeApproximant-config-version.cmake @ONLY)
install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximant-config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximant-config-version.cmake
  DESTINATION lib/cmake/PadeApproximant
)

install(EXPORT PadeApproximant-targets DESTINATION lib/cmake/PadeApproximant)
