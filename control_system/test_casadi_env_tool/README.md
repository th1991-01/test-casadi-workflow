```
python3 test_gen_nlp_sol.py
mkdir build
mv nlp.sol build
cd build
cmake ..
make
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./
./test_load_nlp_sol11
./test_load_nlp_sol12
./test_load_nlp_sol21
./test_load_nlp_sol22
```
