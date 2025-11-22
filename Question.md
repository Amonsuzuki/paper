# 3. How github agent's container is work?

## Answer to Question 3: How GitHub Agent's Container Works

**Summary:** GitHub agent containers provide isolated, ephemeral execution environments using Docker/OCI containerization technology, where each workflow job runs in a clean, sandboxed environment with pre-configured tools and resources.

GitHub agents (also called "runners") use containerization technology to execute workflows in isolated environments. Here's how they work:

### Container Architecture:

1. **Runner Environment**: GitHub-hosted runners are virtual machines that have Docker installed. When a workflow job needs to run, the runner creates a container to execute the job steps.

2. **Container Lifecycle**:
   - The runner pulls the specified container image (or uses a default Ubuntu-based image)
   - Creates a new container instance with isolated filesystem, network, and process space
   - Mounts the workspace directory (your repository code) into the container
   - Executes workflow steps inside the container
   - Cleans up and removes the container after job completion

3. **Isolation and Security**:
   - Each job runs in its own container, providing process isolation
   - Containers have limited access to the host system
   - Network isolation prevents unauthorized communication
   - Resource limits (CPU, memory) prevent resource exhaustion

4. **Container Configuration**:
   - You can specify custom Docker images using the `container:` keyword in workflow files
   - Pre-built images contain common tools and runtimes (Node.js, Python, etc.)
   - Environment variables and secrets are securely injected into the container

5. **Docker-in-Docker**: For workflows that need to build Docker images, GitHub runners support Docker-in-Docker functionality, allowing containerized builds.

### Key Features:

- **Ephemeral Nature**: Containers are created fresh for each job and destroyed after completion, ensuring no state carries over between runs
- **Reproducibility**: Using the same container image ensures consistent execution environments
- **Flexibility**: Support for custom Docker images allows teams to use specific tool versions and dependencies
- **Resource Management**: Containers provide resource isolation and limits to ensure fair resource allocation

**References:** 
- GitHub Actions Documentation: "About GitHub-hosted runners" and "Running jobs in a container"
- Docker containerization technology (Open Container Initiative standards)
- GitHub Actions uses Docker/OCI containers to provide isolated execution environments

**Note:** Since this information is not found in the papers from /latex directory (which focus on machine learning and density functional theory), this answer is based on GitHub's official documentation and general knowledge of containerization technology used in CI/CD systems.

---
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

## Answer to Question 2: Why does δ(Σⱼ₌₁ᴺ(−1/2)⟨ϕⱼ|∇²|ϕⱼ⟩)/δϕᵢ(r) become 2T̂ϕᵢ(r)?

This is a standard result from functional derivative calculus. When taking the functional derivative of the sum Σⱼ₌₁ᴺ(−1/2)⟨ϕⱼ|∇²|ϕⱼ⟩ with respect to ϕᵢ(r), only the term where j = i contributes:

δ/δϕᵢ(r) [Σⱼ₌₁ᴺ(−1/2)⟨ϕⱼ|∇²|ϕⱼ⟩] = δ/δϕᵢ(r) [(−1/2)⟨ϕᵢ|∇²|ϕᵢ⟩]

For a quadratic functional ⟨ϕᵢ|Â|ϕᵢ⟩ where  is a linear operator, the functional derivative follows the rule:
  δ⟨ϕᵢ|Â|ϕᵢ⟩/δϕᵢ(r) = 2Âϕᵢ(r)

Applying this with  = ∇²:
  δ[(−1/2)⟨ϕᵢ|∇²|ϕᵢ⟩]/δϕᵢ(r) = 2·(−1/2)∇²ϕᵢ(r) = −∇²ϕᵢ(r)

Since the kinetic energy operator is defined as T̂ = −(1/2)∇², we have:
  −∇²ϕᵢ(r) = 2·(−1/2)∇²ϕᵢ(r) = 2T̂ϕᵢ(r)

**Reference:** Paper "Overcoming the Barrier of Orbital-Free Density Functional Theory for Molecular Systems Using Deep Learning" (arXiv:2309.16578v2), Supplementary Section A.2, showing the variation leading to equation (S16). The factor of 2 comes from the standard functional derivative rule for quadratic functionals.

---
# 1. Why the coefficient 2 of (S16) is disappear in the definition (S18)?

## Answer to Question 1: Why does the coefficient 2 of (S16) disappear in the definition (S18)?

The coefficient 2 from equation (S16) is absorbed into the Lagrange multiplier when combining with the orthonormal constraint. 

In the variational derivation:
- Equation (S16) gives: δE[Φ]/δϕᵢ(r) = 2T̂ϕᵢ(r) + 2Veff[ρ[Φ]](r)ϕᵢ(r)
- When we impose the orthonormality constraints ⟨ϕᵢ|ϕᵢ⟩ = 1 using Lagrange multipliers λᵢ, we set:
  δE[Φ]/δϕᵢ(r) - λᵢδ⟨ϕᵢ|ϕᵢ⟩/δϕᵢ(r) = 0

This yields:
  2T̂ϕᵢ(r) + 2Veff[ρ[Φ]](r)ϕᵢ(r) = λᵢ·2ϕᵢ(r)

Dividing both sides by 2:
  T̂ϕᵢ(r) + Veff[ρ[Φ]](r)ϕᵢ(r) = (λᵢ)ϕᵢ(r)

By defining εᵢ = λᵢ (the eigenvalue), we obtain equation (S18):
  F̂[ρ[Φ]]ϕᵢ := T̂ϕᵢ + Veff[ρ[Φ]]ϕᵢ = εᵢϕᵢ

**Reference:** Paper "Overcoming the Barrier of Orbital-Free Density Functional Theory for Molecular Systems Using Deep Learning" (arXiv:2309.16578v2), Supplementary Section A.2, equations S16-S18.
