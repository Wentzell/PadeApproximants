# Generated automatically using the command :
# c++2py ../../c++/triqs/utility/pade_approximants.hpp -p --members_read_only -N triqs::utility --target_file_only -a PadeApproximants -m pade_approximants -o pade_approximants -C pytriqs --cxxflags="-std=c++17"
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "pade_approximants", doc = "", app_name = "PadeApproximants")

# Imports
module.add_imports(*[])

# Add here all includes
module.add_include("triqs/utility/pade_approximants.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <cpp2py/converters/complex.hpp>
#include <triqs/cpp2py_converters/arrays.hpp>

using namespace triqs::utility;
""")


# The class pade_approximant
c = class_(
        py_type = "PadeApproximant",  # name of the python class
        c_type = "triqs::utility::pade_approximant",   # name of the C++ class
        doc = """""",   # doc of the C++ class
        hdf5 = False,
)

c.add_constructor("""(triqs::arrays::vector<dcomplex> z_in_, triqs::arrays::vector<dcomplex> u_in)""", doc = """""")

c.add_call(signature = "dcomplex(dcomplex u)", doc = "call op")
c.add_call(signature = "dcomplex(double u)", doc = "call op")

module.add_class(c)



module.generate_code()
