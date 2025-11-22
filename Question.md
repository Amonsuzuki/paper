# 1. Why the coefficient 2 of (S16) is disappear in the definition (S18)?
# 2. Why 1(−1/2)⟨ϕj|∇2|ϕj⟩ δϕi(r) becomes 2ˆTϕi(r)?

i=1, the variation of the energy functional E[Φ]in Eq. (S15) with respect to each
orbital ϕiis required:
δE[Φ]
δϕi(r) =δPN
j=1(−1/2)⟨ϕj|∇2|ϕj⟩
δϕi(r) +ZδEeff[ρ[Φ]]
δρ(r′)δρ[Φ](r′)
δϕi(r)dr′
= 2ˆTϕi(r) + 2Veff[ρ[Φ]](r)ϕi(r), (S16)
where Veff[ρ](r) :=δEeff[ρ]
δρ(r) =Zρ(r′)
∥r′−r∥dr′
|{z }
=:VH[ρ](r)+δEXC[ρ]
δρ(r)
|{z}
=:VXC[ρ](r)+Vext(r). (S17)
30

The term Veff[ρ[Φ]]arises as a variation with respect to the density ρsince the orbitals affect the energy com-
ponent Eeffapart from TS(defined in Eq. (S10)) only through the density ρ[Φ]they define. By Eq. (S12)
we haveδρ[Φ](r′)
δϕi(r)= 2ϕi(r)δ(r−r′), which then gives Eq. (S16). Combining Eq. (S16) with the variation
of the orthonormal constraint yields the optimality equation for the problem Eq. (S15):
ˆF[ρ[Φ]]ϕi:=ˆTϕi+Veff[ρ[Φ]]ϕi=εiϕi,∀i= 1,···N. (S18)
