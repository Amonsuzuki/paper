# 3. How does GitHub agent's container work?

---
# 2. Why does $\frac{\delta \sum_{j=1}^{N}(-\frac{1}{2})\langle\phi_j|\nabla^2|\phi_j\rangle}{\delta \phi_i(r)}$ become $2\hat{T}\phi_i(r)$?

## Background from the Paper

For $i=1$, the variation of the energy functional $E[\Phi]$ in Eq. (S15) with respect to each orbital $\phi_i$ is required:

$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = \frac{\delta \sum_{j=1}^{N}\left(-\frac{1}{2}\right)\langle\phi_j|\nabla^2|\phi_j\rangle}{\delta \phi_i(r)} + \int \frac{\delta E_{eff}[\rho[\Phi]]}{\delta \rho(r')}\frac{\delta \rho[\Phi](r')}{\delta \phi_i(r)}dr'
$$

$$
= 2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r) \quad \text{(S16)}
$$

where

$$
V_{eff}[\rho](r) := \frac{\delta E_{eff}[\rho]}{\delta \rho(r)} = \int \frac{\rho(r')}{\|r'-r\|}dr' + \frac{\delta E_{XC}[\rho]}{\delta \rho(r)} + V_{ext}(r)
$$

$$
= \underbrace{\int \frac{\rho(r')}{\|r'-r\|}dr'}_{=: V_H[\rho](r)} + \underbrace{\frac{\delta E_{XC}[\rho]}{\delta \rho(r)}}_{=: V_{XC}[\rho](r)} + V_{ext}(r) \quad \text{(S17)}
$$

The term $V_{eff}[\rho[\Phi]]$ arises as a variation with respect to the density $\rho$ since the orbitals affect the energy component $E_{eff}$ apart from $T_S$ (defined in Eq. (S10)) only through the density $\rho[\Phi]$ they define. By Eq. (S12) we have:

$$
\frac{\delta \rho[\Phi](r')}{\delta \phi_i(r)} = 2\phi_i(r)\delta(r-r')
$$

which then gives Eq. (S16). Combining Eq. (S16) with the variation of the orthonormal constraint yields the optimality equation for the problem Eq. (S15):

$$
\hat{F}[\rho[\Phi]]\phi_i := \hat{T}\phi_i + V_{eff}[\rho[\Phi]]\phi_i = \varepsilon_i\phi_i, \quad \forall i = 1, \ldots, N \quad \text{(S18)}
$$

## Answer to Question 2

**Why does $\frac{\delta}{\delta\phi_i(r)}\left[\sum_{j=1}^{N}\left(-\frac{1}{2}\right)\langle\phi_j|\nabla^2|\phi_j\rangle\right]$ become $2\hat{T}\phi_i(r)$?**

This is a standard result from functional derivative calculus. When taking the functional derivative of the sum $\sum_{j=1}^{N}\left(-\frac{1}{2}\right)\langle\phi_j|\nabla^2|\phi_j\rangle$ with respect to $\phi_i(r)$, only the term where $j = i$ contributes:

$$
\frac{\delta}{\delta\phi_i(r)}\left[\sum_{j=1}^{N}\left(-\frac{1}{2}\right)\langle\phi_j|\nabla^2|\phi_j\rangle\right] = \frac{\delta}{\delta\phi_i(r)}\left[\left(-\frac{1}{2}\right)\langle\phi_i|\nabla^2|\phi_i\rangle\right]
$$

For a quadratic functional $\langle\phi_i|\hat{A}|\phi_i\rangle$ where $\hat{A}$ is a linear operator, the functional derivative follows the rule:

$$
\frac{\delta\langle\phi_i|\hat{A}|\phi_i\rangle}{\delta\phi_i(r)} = 2\hat{A}\phi_i(r)
$$

Applying this with $\hat{A} = \nabla^2$:

$$
\frac{\delta}{\delta\phi_i(r)}\left[\left(-\frac{1}{2}\right)\langle\phi_i|\nabla^2|\phi_i\rangle\right] = 2 \cdot \left(-\frac{1}{2}\right)\nabla^2\phi_i(r) = -\nabla^2\phi_i(r)
$$

Since the kinetic energy operator is defined as $\hat{T} = -\frac{1}{2}\nabla^2$, we have:

$$
-\nabla^2\phi_i(r) = 2 \cdot \left(-\frac{1}{2}\right)\nabla^2\phi_i(r) = 2\hat{T}\phi_i(r)
$$

**Reference:** Paper "Overcoming the Barrier of Orbital-Free Density Functional Theory for Molecular Systems Using Deep Learning" (arXiv:2309.16578v2), Supplementary Section A.2, showing the variation leading to equation (S16). The factor of 2 comes from the standard functional derivative rule for quadratic functionals.

---
# 1. Why does the coefficient 2 of (S16) disappear in the definition (S18)?

## Answer to Question 1

**Why does the coefficient 2 of (S16) disappear in the definition (S18)?**

The coefficient 2 from equation (S16) is absorbed into the Lagrange multiplier when combining with the orthonormal constraint. 

### Detailed Explanation

In the variational derivation:

**Step 1:** Equation (S16) gives:

$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} = 2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r)
$$

**Step 2:** When we impose the orthonormality constraints $\langle\phi_i|\phi_i\rangle = 1$ using Lagrange multipliers $\lambda_i$, we set:

$$
\frac{\delta E[\Phi]}{\delta \phi_i(r)} - \lambda_i\frac{\delta\langle\phi_i|\phi_i\rangle}{\delta \phi_i(r)} = 0
$$

**Step 3:** This yields:

$$
2\hat{T}\phi_i(r) + 2V_{eff}[\rho[\Phi]](r)\phi_i(r) = \lambda_i \cdot 2\phi_i(r)
$$

**Step 4:** Dividing both sides by 2:

$$
\hat{T}\phi_i(r) + V_{eff}[\rho[\Phi]](r)\phi_i(r) = \lambda_i\phi_i(r)
$$

**Step 5:** By defining $\varepsilon_i = \lambda_i$ (the eigenvalue), we obtain equation (S18):

$$
\hat{F}[\rho[\Phi]]\phi_i := \hat{T}\phi_i + V_{eff}[\rho[\Phi]]\phi_i = \varepsilon_i\phi_i
$$

### Summary

Therefore, the coefficient 2 is **absorbed into the Lagrange multiplier** when enforcing the orthonormality constraint. The factor appears on both sides of the equation and cancels out when we divide through by 2. ∎

**Reference:** Paper "Overcoming the Barrier of Orbital-Free Density Functional Theory for Molecular Systems Using Deep Learning" (arXiv:2309.16578v2), Supplementary Section A.2, equations S16-S18.
