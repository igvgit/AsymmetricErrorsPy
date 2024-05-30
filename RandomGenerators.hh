#ifndef ASEPY_RANDOMGENERATORS_HH_
#define ASEPY_RANDOMGENERATORS_HH_

#include <cstdlib>
#include <random>

#include "ase/CPPRandomGen.hh"

namespace asepy {
    unsigned long getSeed(unsigned long seed0);

    struct DRand48 : public ase::AbsRNG
    {
        inline virtual ~DRand48() override {}
        inline double operator()() override {return drand48();}
    };

    class MersenneTwister32 : public ase::AbsRNG
    {
    public:
        inline explicit MersenneTwister32(const unsigned long seed = 0)
            : eng_(getSeed(seed)), gen_(eng_) {}

        inline virtual ~MersenneTwister32() override {}

        inline double operator()() override {return gen_();}

    private:
        MersenneTwister32(const MersenneTwister32&) = delete;
        MersenneTwister32& operator=(const MersenneTwister32&) = delete;

        std::mt19937 eng_;
        ase::CPPRandomGen<std::mt19937> gen_;
    };

    class MersenneTwister64 : public ase::AbsRNG
    {
    public:
        inline explicit MersenneTwister64(const unsigned long seed = 0)
            : eng_(getSeed(seed)), gen_(eng_) {}

        inline virtual ~MersenneTwister64() override {}

        inline double operator()() override {return gen_();}

    private:
        MersenneTwister64(const MersenneTwister64&) = delete;
        MersenneTwister64& operator=(const MersenneTwister64&) = delete;

        std::mt19937_64 eng_;
        ase::CPPRandomGen<std::mt19937_64> gen_;
    };
}

#endif // ASEPY_RANDOMGENERATORS_HH_
