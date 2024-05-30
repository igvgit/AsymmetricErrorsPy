%include ase/OPATGaussian.i
%include ase/SymbetaDoubleIntegral.i

%{
#include "ase/SymmetricBetaGaussian.hh"
%}

%feature("notabstract") ase::SymmetricBetaGaussian;

%include "ase/SymmetricBetaGaussian.hh"

%feature("notabstract") ase::SymmetricBetaGaussian_p_h<1U,10U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<1U,15U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<1U,20U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<1U,25U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<1U,30U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<2U,10U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<2U,15U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<2U,20U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<2U,25U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<2U,30U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<3U,10U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<3U,15U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<3U,20U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<3U,25U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<3U,30U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<4U,10U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<4U,15U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<4U,20U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<4U,25U>;
%feature("notabstract") ase::SymmetricBetaGaussian_p_h<4U,30U>;

namespace ase {
    %template(SymmetricBetaGaussian_1_10) SymmetricBetaGaussian_p_h<1U,10U>;
    %template(SymmetricBetaGaussian_1_15) SymmetricBetaGaussian_p_h<1U,15U>;
    %template(SymmetricBetaGaussian_1_20) SymmetricBetaGaussian_p_h<1U,20U>;
    %template(SymmetricBetaGaussian_1_25) SymmetricBetaGaussian_p_h<1U,25U>;
    %template(SymmetricBetaGaussian_1_30) SymmetricBetaGaussian_p_h<1U,30U>;
    %template(SymmetricBetaGaussian_2_10) SymmetricBetaGaussian_p_h<2U,10U>;
    %template(SymmetricBetaGaussian_2_15) SymmetricBetaGaussian_p_h<2U,15U>;
    %template(SymmetricBetaGaussian_2_20) SymmetricBetaGaussian_p_h<2U,20U>;
    %template(SymmetricBetaGaussian_2_25) SymmetricBetaGaussian_p_h<2U,25U>;
    %template(SymmetricBetaGaussian_2_30) SymmetricBetaGaussian_p_h<2U,30U>;
    %template(SymmetricBetaGaussian_3_10) SymmetricBetaGaussian_p_h<3U,10U>;
    %template(SymmetricBetaGaussian_3_15) SymmetricBetaGaussian_p_h<3U,15U>;
    %template(SymmetricBetaGaussian_3_20) SymmetricBetaGaussian_p_h<3U,20U>;
    %template(SymmetricBetaGaussian_3_25) SymmetricBetaGaussian_p_h<3U,25U>;
    %template(SymmetricBetaGaussian_3_30) SymmetricBetaGaussian_p_h<3U,30U>;
    %template(SymmetricBetaGaussian_4_10) SymmetricBetaGaussian_p_h<4U,10U>;
    %template(SymmetricBetaGaussian_4_15) SymmetricBetaGaussian_p_h<4U,15U>;
    %template(SymmetricBetaGaussian_4_20) SymmetricBetaGaussian_p_h<4U,20U>;
    %template(SymmetricBetaGaussian_4_25) SymmetricBetaGaussian_p_h<4U,25U>;
    %template(SymmetricBetaGaussian_4_30) SymmetricBetaGaussian_p_h<4U,30U>;
}
