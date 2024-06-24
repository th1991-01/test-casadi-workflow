#include <casadi/casadi.hpp>
using namespace casadi;

int main()
{
  // Function solver = nlpsol("solver", "ipopt", "nlp.so");
  Function solver = nlpsol("solver", "ipopt", "/home/proxima/test_casadi_env_tool/build/nlp.so");
  std::vector<double> x0;
  x0.push_back(0.0);
  x0.push_back(1.0);
  std::map<std::string, DM> arg = {{"lbg", 0},
    {"ubg", 0},
    {"x0", x0}};
  auto res = solver(arg);
  return 0;
}
