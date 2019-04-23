add_subdirectory(cmake)

if(NOT CMAKE_INSTALL_PREFIX STREQUAL TRIQS_ROOT)

  configure_file(PadeApproximant.modulefile.in PadeApproximant.modulefile @ONLY)
  configure_file(PadeApproximantvars.sh.in PadeApproximantvars.sh @ONLY)

  install(
    FILES
      ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximant.modulefile
      ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximantvars.sh
    DESTINATION share
  )
 
  message(STATUS "***************************************************************")
  message(STATUS "* Custom install Location. Use: 			         ")
  message(STATUS "*                                                              ")
  message(STATUS "*   source ${CMAKE_INSTALL_PREFIX}/share/PadeApproximantvars.sh      ")
  message(STATUS "*                                                              ") 
  message(STATUS "* to set up the environment variables                          ") 
  message(STATUS "***************************************************************")

endif()
