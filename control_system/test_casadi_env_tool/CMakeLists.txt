cmake_minimum_required(VERSION 3.8)
project(casadi_cpp_example)
set(CMAKE_MODULE_PATH $ENV{HOME}/casadi/cmake)
find_package(CASADI REQUIRED)
find_package(IPOPT REQUIRED)

add_executable(test_load_nlp_sol11 test_load_nlp_sol1.cpp)
target_link_libraries(test_load_nlp_sol11
  ${CASADI_LIBRARIES}
  ${IPOPT_LIBRARIES}
  #${IPOPT_LIBRARY_DIRS}
  )
  
add_executable(test_load_nlp_sol12 test_load_nlp_sol1.cpp)
target_link_libraries(test_load_nlp_sol12
  ${CASADI_LIBRARIES}
  #${IPOPT_LIBRARIES}
  ${IPOPT_LIBRARY_DIRS}
  )
  
add_executable(test_load_nlp_sol21 test_load_nlp_sol2.cpp)
target_link_libraries(test_load_nlp_sol21
  ${CASADI_LIBRARIES}
  ${IPOPT_LIBRARIES}
  #${IPOPT_LIBRARY_DIRS}
  )
  
add_executable(test_load_nlp_sol22 test_load_nlp_sol2.cpp)
target_link_libraries(test_load_nlp_sol22
  ${CASADI_LIBRARIES}
  #${IPOPT_LIBRARIES}
  ${IPOPT_LIBRARY_DIRS}
  )
