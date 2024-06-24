import os
import casadi
print("casadi.__version__",casadi.__version__)

name = "nlp"
x = casadi.SX.sym("x")
y = casadi.SX.sym("y")
nlp = {"x":casadi.vertcat(x,y),
        "f":x**3 + x**2 + 8*x + 4*y**2 + 3*x*y,
        "g":x**2 + y**2 - 1}
solver = casadi.nlpsol("solver", "ipopt", nlp)
print(solver(x0=[0, 1],lbg=0, ubg=0))

cname = solver.generate_dependencies("nlp.c") 

oname_O3 = name + ".so"
cmd = "gcc -fPIC -shared " + cname  + " -o3 " + " -o " + oname_O3
print("cmd:", cmd)
os.system(cmd)

solver_sample_O3 = casadi.nlpsol("solver", "ipopt", "./"+oname_O3)
print(solver_sample_O3(x0=[0, 1],lbg=0, ubg=0))
