#include "RandomGenerators.hh"

namespace asepy {
    unsigned long getSeed(const unsigned long seed0)
    {
        if (seed0)
            return seed0;
        else
        {
            std::random_device rd;
            return rd();
        }
    }
}
