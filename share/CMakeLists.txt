add_subdirectory(cmake)

if(NOT CMAKE_INSTALL_PREFIX STREQUAL TRIQS_ROOT)

  configure_file(PadeApproximants.modulefile.in PadeApproximants.modulefile @ONLY)
  configure_file(PadeApproximantsvars.sh.in PadeApproximantsvars.sh @ONLY)

  install(
    FILES
      ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximants.modulefile
      ${CMAKE_CURRENT_BINARY_DIR}/PadeApproximantsvars.sh
    DESTINATION share
  )
 
  message(STATUS "***************************************************************")
  message(STATUS "* Custom install Location. Use: 			         ")
  message(STATUS "*                                                              ")
  message(STATUS "*   source ${CMAKE_INSTALL_PREFIX}/share/PadeApproximantsvars.sh      ")
  message(STATUS "*                                                              ") 
  message(STATUS "* to set up the environment variables                          ") 
  message(STATUS "***************************************************************")

endif()
