(ch-6)=
# 6. Momentum and Variable Mass

<!-- Source PDF page 122; printed label 113. -->

::::{admonition} Learning Objectives

- Review linear momentum and momentum conservation

- Define momentum with external forces, impulse, and collision

- Define center of mass for N-body systems

- Investigate problems with variable mass

::::

In this chapter, we will review linear momentum and the conservation of momentum. We will also discuss impulse, collisions, and variable mass problems.

(sec-6-1)=
## 6.1 Linear Momentum

Momentum is a dynamic property of a system, equal to mass times velocity.

$$
\vec{p} = m\vec{v}
$$ (eq-6-1)

In [Chapter 2](#ch-2), we related momentum to Newton’s second law. Namely, the net force on a system is equal to the change in momentum for that system.

$$
\sum \vec{F} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t}
$$ (eq-6-2)

If we assume that mass is constant we can substitute in Equation (6.1):

$$
\begin{aligned}
\vec{F} &= \frac{\mathrm{d}(m\vec{v})}{\mathrm{d}t} \\
\sum \vec{F} &= m \frac{\mathrm{d}\vec{v}}{\mathrm{d}t} =\Rightarrow \mathrm{assuming} \mathrm{mass} \mathrm{is} \mathrm{constant} \\
\vec{F} &= m\vec{a}
\end{aligned}
$$

We will look at the case where the mass changes with time in [Section 6.5](#sec-6-5).

If the net external force is equal to zero $(\sum \vec{F}$ = 0), then the total momentum of a system is constant, ![Formula, source page 122](../images/math/p122-e7777a6a9d74.svg) = 0 and $\vec{p}$ is a constant. This result is the conservation of linear momentum.

(sec-6-2)=
## 6.2 Conservation of Linear Momentum

Consider an isolated system of n particles that have distinct masses and velocities. The total momentum of the system is given by:

$$
\vec{p}_{tot}= \sum \vec{p}_{i}= \vec{p}_{1}+ \vec{p}_{2}+ \cdot \cdot \cdot + \vec{p}_{n}
$$ (eq-6-3)

<!-- Source PDF page 123; printed label 114. -->

For simplicity, let’s take a case with 3 particles. Such that the total momentum is:

$$
\vec{p}_{tot}= \sum \vec{p}_{i}= \vec{p}_{1}+ \vec{p}_{2}+ \vec{p}_{3}
$$

and the time derivative of the total momentum is:

$$
\begin{aligned}
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} &= \frac{\mathrm{d}}{\mathrm{d}t} (\vec{p}_{1}+ \vec{p}_{2}+ \vec{p}_{3}) \\
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} &= \frac{\mathrm{d}\vec{p}_{1}}{\mathrm{d}t} + \frac{\mathrm{d}\vec{p}_{2}}{\mathrm{d}t} + \frac{\mathrm{d}\vec{p}_{3}}{\mathrm{d}t} \\
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} &= \sum \vec{F}_{1}+ \sum \vec{F}_{2}+ \sum \vec{F}_{3}=\Rightarrow \mathrm{set} \frac{\mathrm{d}\vec{p}}{\mathrm{d}t} = \vec{F}
\end{aligned}
$$

where $\sum \vec{F}_{1}$ is the net force on particle 1, $\sum \vec{F}_{2}$ is the net force on particle 2, and $\sum \vec{F}_{3}$ is the net force on particle 3.

The net force on particle 1 should be the force from particle 2 $(\vec{F}_{21})$ and the force from particle 3 $(\vec{F}_{31})$. There are no other forces on particle 1 because the system is isolated (e.g., the system has no outside influences). The same argument can be made for particles 2 and

3. So the time derivative of our net momentum becomes:

:::{image} ../images/math/p123-e9f042f88dac.svg
:alt: Mathematical expression from source PDF page 123
:class: source-equation
:align: center
:::

But because of Newton’s third law (every action has an equal and opposite reaction), the force of particle 2 on particle 1 $(\vec{F}_{21})$ must be equal and opposite to the force of particle 1 on particle 2 $(\vec{F}_{12})$. You can think of two masses in space pulling on each other due to gravity. Or two isolated charges attracting or repelling each other. As a result, $\vec{F}_{21}= -\vec{F}_{12}$, $\vec{F}_{31}= -\vec{F}_{13}$, and $\vec{F}_{32}= -\vec{F}_{23}$. So we finally obtain:

$$
\begin{aligned}
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} &= 0 \\
\vec{p}_{tot}&= \mathrm{constant}
\end{aligned}
$$

The above example is for three particles, but we can easily generalize the solution to $N$ particles as long as the system is isolated (no external forces). For a system of $n-$particles,

$$
\vec{p}_{tot}= \sum_{i=1}^{N}\vec{p}_{i}
$$

$$
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t} \sum _{i=1}^{N}\vec{p}_{i}= \sum _{i=1}^{N} \frac{\mathrm{d}\vec{p}_{i}}{\mathrm{d}t}
$$

$$
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} = \sum_{i=1}^{N}(\Sigma \vec{F}_{i})
$$

$$
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} = \sum _{i=1 j}^{N}\sum_{j=\not =1i}^{N}\vec{F}_{ij}= 0
$$

<!-- Source PDF page 124; printed label 115. -->

where the unique pairs of forces are represented by double sums. To break down what the nested sums mean, first let’s consider a single particle, represented by $i$. We can write

:::{image} ../images/math/p124-d7f79402a066.svg
:alt: Mathematical expression from source PDF page 124
:class: source-equation
:align: center
:::

which is basically saying that the time derivative of the momentum for the $i$th particle is just the sum of all the forces from the other particles. The condition of $j \not = i$ is needed because each particle acts on the other particles in the system, but not on themselves $(\vec{F}_{11},\vec{F}_{22},$ and $\vec{F}_{33}$ are not allowed).

To then get the the total momentum of an isolated system, we need to sum over individual particles, $\vec{p}_{tot}= \sum \vec{p}_{i}$. This gives us our nested sums,

$$
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} = \sum _{i=1 j}^{N}\sum_{j=\not =1i}^{N}\vec{F}_{ij}= 0
$$ (eq-6-4)

where you start with the outer summation and set a value for $i$ before cycling through the inner summation and setting all possible values for $j$. For an example, if $N$ = 3, the nested sums would give $\vec{F}_{12},\vec{F}_{13},\vec{F}_{21},\vec{F}_{23},\vec{F}_{31},$ and $\vec{F}_{32}$ in that order.

(sec-6-3)=
## 6.3 Momentum with an External Force

The conservation of linear momentum draws directly from Newton’s third law. In an isolated system, all forces balance (equal and opposite reactions) such that the total momentum of the system is constant. But if there is an external force, then the total linear momentum is no longer constant. For a simple particle in a system,

$$
\frac{\mathrm{d}\vec{p}_{i}}{\mathrm{d}t} = \sum \vec{F}_{i}= \vec{F}_{i,int}+ \vec{F}_{i,ext}
$$ (eq-6-5)

where $\vec{F}_{i,int}$ is the force on the particle from the system itself (internal force) and $\vec{F}_{i,ext}$ is the external force on the particle. If you then look at all particles in the system:

$$
\begin{aligned}
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} &= \\
\frac{\mathrm{d}}{\mathrm{d}t} \vec{p}_{i}&= \sum \vec{F}_{i,int}+ \sum \vec{F}_{i,ext} \\
\frac{\mathrm{d}\vec{p}_{tot}}{\mathrm{d}t} &= \sum \vec{F}_{i,ext}=\Rightarrow \sum \vec{F}_{i,int}= 0 (\mathrm{see} \mathrm{Chapter} 6.2)
\end{aligned}
$$

So in a system with an external force, the net change in momentum of that system is given by the net external force acting on the system.

(sec-6-3-1)=
### 6.3.1 Impulse

The impulse of a force is defined as:

$$
\vec{I} = \int_{t_{1}}^{t_{2}} \vec{F}\mathrm{d}t
$$

<!-- Source PDF page 125; printed label 116. -->

where $F$ is the net force acting on the system. We can re-define the net force in terms of momentum, however.

$$
\vec{I} = \int_{t_{1}}^{t_{2}} \vec{F}\mathrm{d}t = \int_{t_{1}}^{t_{2}} \frac{\mathrm{d}\vec{p}}{\mathrm{d}t} \mathrm{d}t = \int_{t_{1}}^{t_{2}} \mathrm{d}\vec{p} = \vec{p}_{2}- \vec{p}_{1}= \Delta \vec{p}
$$ (eq-6-6)

The impulse of a force represents the change in linear momentum in the system. Note that mass does not need to be constant in the definition of an impulse.

An impulse is an instantaneous event, where the interaction time is short $(\Delta t \approx 0)$. We can assume that the system does not change during the impulse, but it will change drastically as a result of the impulse (it just hasn’t had time for that to happen).

In general practice, an impulse is a fast, powerful force that quickly changes the momentum of a system rather than a slow process that slowly changes the momentum of a system. The distinction between fast and slow, however, is not well defined. What is necessary is that your force can be approximated by an average value over the small time duration. If you have a relatively constant force, then you can take a longer time duration, but if your force changes quickly, you need a shorter time interval.

::::{tip} Quick Question

1. A hockey player hits a puck. If the puck was initially going at a speed of $v_{i}\hat{\imath}$ and ends up going $v_{f}\hat{\jmath}$ , what was the direction of the impulse vector?

::::

[Figure 6.1](#fig-6-1) shows two identical impulses with the same area $\int \vec{F}$ d$t$, which means they have the same impulse magnitude. Note the differences between them. The average impulse is $\vec{I}_{avg}= \vec{F}_{avg}\Delta t$. So if you increase the interaction time, $\Delta t$, you decrease the average force necessary for the same impulse. In the figure, the blue curve has a shorter $\Delta t$ and requires a stronger force than the red curve to produce the same change in momentum. You can minimize the force by increasing the time of interaction.

:::{figure} ../images/figures/figure-6-1.png
:label: fig-6-1
:enumerator: 6.1
:alt: Figure shows graphs comparing force versus time for a lower average force applied over a longer time and a larger average force applied over a short time.
:width: 358px

Sketch of two forces with the same impulse (area under the curve).
:::

::::{admonition} Impulse in Everyday Life

Increasing the impact time to decrease the force occurs many times in everyday life. For example, when jumping, most people bend their knees as they land. Bending your knees extends the time of impact and lessens the force on your legs.

::::

<!-- Source PDF page 126; printed label 117. -->

::::{admonition} Cora’s Thoughts

Generally we consider impulses to be short bursts. An impulse is powerful force that quickly changes the momentum of a system, hence why $\Delta t \rightarrow$ d$t$.

An airbag is an excellent example of impulse in everyday life. When an accident occurs and the vehicle stops, the drivers momentum carries them forward towards the steering wheel, where they will experience a quick change in momentum (impulse). The airbag extends the time of that impact lessening the force on the driver, often saving lives. In [Figure 6.1](#fig-6-1), the red graph may be what the force with the airbag would look like, and the blue would be what the force without the airbag would look like.

::::

(sec-6-3-2)=
### 6.3.2 Collisions

Collisions are a way that the momentum of a system can change. There are two types of collisions that we’ll consider, *inelastic* and *elastic* collisions.

**Case 1: Inelastic Collision**

In a totally inelastic collision, the colliding systems merge (stick together). [Figure 6.2](#fig-6-2) illustrates the basic case of an inelastic collision in 1D, where two masses $(m$ and $M)$ collide and stick together. After the collision, the two masses move as one system $(m + M)$.

:::{figure} ../images/figures/figure-6-2.png
:label: fig-6-2
:enumerator: 6.2
:alt: Figure shows the two masses before and after an inelastic collision.
:width: 182px

Example of an inelastic collision. A mass $m$ moving at a speed $u$ approaches another mass $M$ that is at rest. The two objects collide and merge into one system $m + M$ that moves at a new speed, $v$.
:::

Since there are no external forces $(m$ and $M$ are internal to the system), momentum must be conserved between the initial state and final state of the system. Thus, $\vec{p}_{i}= \vec{p}_{f}$.

$$
\vec{p}_{i}= \vec{p}_{f}
$$

$$
\begin{aligned}
mu\hat{\imath} + 0 &= (m + M)v\hat{\imath} \\
v &= \frac{m}{m + M} u
\end{aligned}
$$

If $M \gg m$, then $v$ is small relative to $u$. If $M \ll m$, then $v \approx u$.

(example-6-1)=

::::{admonition} Sample Problem 6-1

Two particles of equal mass $m$ and identical speeds $u$ collide and stick. The first particle initially moves at an angle of $\theta _{1}$ above the horizontal and the second particle initially moves at an angle of $\theta _{2}$ below the horizontal. If both $\theta _{1}$ and $\theta _{2}$ are $< 90^{\circ}$, **what is the** **final velocity of the system after collision?**

::::

<!-- Source PDF page 127; printed label 118. -->

**Solution**

We want to find the velocity (speed and direction) of the system after an inelastic collision. The first thing we need to do is draw the initial set up of the problem. [Figure 6.3](#fig-6-3) shows the motion of particle 1, $m_{1}$, and particle 2, $m_{2}$, as described by the problem. The two masses collide at the origin and then stick together.

:::{figure} ../images/figures/figure-6-3.png
:label: fig-6-3
:enumerator: 6.3
:alt: Figure shows vectors for the velocity direction of the masses before and after the collision.
:width: 186px

The motion of two identical particles, $m_{1}$ and $m_{2}$, on a coordinate grid. The velocity of the post-collision system is shown by the purple vector.
:::

When the masses collide, they continue their journey as $m_{1}+m_{2}= 2m$ (purple vector). We do not know the exact direction of motion for the post-collision system, however. The $m_{1}+m_{2}$ system may move at an angle $\theta$ above or below the horizontal. [Figure 6.3](#fig-6-3) shows the above case. If we chose wrong, we will get a negative angle.

Since this is an isolated system, the total momentum must be conserved and it must be conserved in both $x$ and $y$, where

$$
p_{x,tot}= \mathrm{constant}
$$

$$
p_{y,tot}= \mathrm{constant}
$$

We will solve the $x$ and $y$ components of the motion separately.

For the $x$ component

$$
p_{x,f}= p_{x,i}=\Rightarrow \mathrm{conservation} \mathrm{of} \mathrm{momentum}
$$

$$
(m_{1}+ m_{2})v_{x}= m_{1}v_{1,x}+ m_{2}v_{2,x}
$$

$$
\begin{aligned}
2mv_{x}&= m(u\cos \theta _{1}) + m(u\cos \theta _{2}) \\
v_{x}&= \frac{u}{2} (\cos \theta _{1}+ \cos \theta _{2})
\end{aligned}
$$

For the $y$ component

$$
p_{y,f}= p_{y,i}=\Rightarrow \mathrm{conservation} \mathrm{of} \mathrm{momentum}
$$

$$
(m_{1}+ m_{2})v_{y}= m_{1}v_{1,y}+ m_{2}v_{2,y}
$$

$2mv_{y}= m(u\sin \theta _{1}) - m(u\sin \theta _{2}) =\Rightarrow v_{2,y}$ is in the negative direction

$$
v_{y}= \frac{u}{2} (\sin \theta _{1}- \sin \theta _{2})
$$

<!-- Source PDF page 128; printed label 119. -->

::::{admonition} Continued

With the $x$ and $y$ components of the motion, the final speed is:

:::{image} ../images/math/p128-a55fdf14d7b5.svg
:alt: Mathematical expression from source PDF page 128
:class: source-equation
:align: center
:::

:::{image} ../images/math/p128-68dd9ce8a325.svg
:alt: Mathematical expression from source PDF page 128
:class: source-equation
:align: center
:::

To get the angle, we can again use trigonometry. The $v_{x}$ component is the $x-$component of the vector and the $v_{y}$ component is the $y-$component of the vector.

$$
\begin{aligned}
\tan \theta &= \frac{v_{y}}{v_{x}} \\
\tan \theta &= \frac{\frac{u}{2} (\sin \theta _{1}- \sin \theta _{2})}{\frac{u}{2} (\cos \theta _{1}+ \cos \theta _{2})}
\end{aligned}
$$

$$
\theta = \tan ^{-1}\Bigg[\frac{\sin \theta _{1}- \sin \theta _{2}}{\cos \theta _{1}+ \cos \theta _{2}} \Bigg]
$$

1. If $\theta _{1}= 45^{\circ}, \theta _{2}= 30^{\circ}$ and $u$ = 10 m $\mathrm{s}^{-1}$, what is the velocity of the system after the collision? Give speed and angle.

2. In [Figure 6.3](#fig-6-3) we guessed that $\theta > 0^{\circ}$ (above the horizontal). For what values of $\theta _{1}$ and $\theta _{2}$ will you have $\theta > 0^{\circ}$?

::::

**Case 2: Elastic Collision**

For a completely elastic collision, the particles rebound off each other and there is no change in their mass pre-collision and post-collision. In this case, there is no loss of energy (kinetic energy is completely conserved) and once again, momentum is conserved.

::::{admonition} Examples of Elastic Collisions

A good example of elastic collisions is a game of pool / billiards, where you use one billiard ball to hit other ones into pockets. Or even a game of domino’s, where one domino piece hits the next and so forth. In practice, these are not fully elastic collisions as there will be some loss of energy, but there is little energy loss.

For some nice examples of elastic-like collisions, here are videos showing [Newton’s cradle](https://www.youtube.com/watch?v=0LnbyjOyEQ8) and [Dominos with cats](https://www.youtube.com/watch?v=7Nn7NZI_LN4).

::::

<!-- Source PDF page 129; printed label 120. -->

(example-6-2)=

::::{admonition} Sample Problem 6-2

Consider two balls moving toward each other on the $x-$axis as shown in [Figure 6.4](#fig-6-4). The first ball has a mass of $m_{1}$ and is moving at $v_{1,i}$, and the second ball has a mass of $m_{2}$ and is moving at a speed of $v_{2,i}$. After collision, $m_{1}$ is moving at $v_{1,f}$ and $m_{2}$ is moving at $v_{2,f}$. **Find equations for the final speeds in terms of the initial parameters?**

**Solution**

:::{figure} ../images/figures/figure-6-4.png
:label: fig-6-4
:enumerator: 6.4
:alt: Cartoon showing the before and after collision velocities of the two masses.
:width: 341px

Two masses, $m_{1}$ and $m_{2}$ collide in an elastic collisions before and after. Their speeds change and they move in opposite directions after the collision.
:::

This may sound like an easy problem, but there are some tricks to it. We want to fni d $v_{1,f}$ and $v_{2,f}$ in terms of $m_{1}, m_{2}, v_{1,i}$ and $v_{2,i}$. For a completely elastic collision, the total momentum is conserved, so the initial momentum equals the final momentum.

$$
\vec{p}_{i}= \vec{p}_{f}
$$

$$
m_{1}\vec{v}_{1,i}+ m_{2}\vec{v}_{2,i}= m_{1}\vec{v}_{1,f}+ m_{2}\vec{v}_{2,f}
$$ (eq-6-7)

But to fully solve this problem, we cannot just use the conservation of momentum, because we have two unknown quantities $(v_{1,f}$ and $v_{2,f})$. To have a unique solution with two unknown quantities, you need to have at least two unique equations. For our second equation, we will use the conservation of kinetic energy (we will return to kinetic energy in [Chapter 8](#ch-8)), where kinetic energy can be expressed as $K = \frac{1}{2} mv^{2}$.

$$
\begin{aligned}
K_{i}&= K_{f}=\Rightarrow \mathrm{total} \mathrm{kinetic} \mathrm{energy} \mathrm{is} \mathrm{conserved} \\
1 1 1 1
\end{aligned}
$$

![Formula, source page 129](../images/math/p129-8475c4690139.svg) can drop ![Formula, source page 129](../images/math/p129-edfa4aca28c0.svg)

$$
\begin{aligned}
2 2 2 2 \\
m_{1}v_{1,i}^{2}+ m_{2}v_{2,i}^{2}&= m_{1}v_{1,f}^{2}+ m_{2}v_{2,f}^{2}
\end{aligned}
$$ (eq-6-8)

Now we have two equations and two unknowns and can solve the problem. To make the math easier, we will re-arrange Equation 6.7 to bring all $m_{1}$ terms to one side and all $m_{2}$ terms to the other side.

$$
m_{1}(v_{1,i}- v_{1,f}) = m_{2}(v_{2,f}- v_{2,i})
$$ (eq-6-9)

::::

<!-- Source PDF page 130; printed label 121. -->

::::{admonition} Continued

Similarly, we can re-arrange Equation 6.8 as

$$
m_{1}(v_{1,i}^{2}- v_{1,f}^{2}) = m_{2}(v_{2,f}^{2}- v_{2,i}^{2})
$$

$$
m_{1}(v_{1,i}- v_{1,f})(v_{1,i}+ v_{1,f}) = m_{2}(v_{2,f}- v_{2,i})(v_{2,f}+ v_{2,i})
$$ (eq-6-10)

where we use the difference of squares, $(a^{2}-b^{2}) = (a-b)(a+b)$ to simplify the equation.

With Equations 6.9 and 6.10 you now have two equations with which to solve two unknowns. Dividing 6.10 by 6.9 gives:

$$
\frac{m_{1}(v_{1,i}- v_{1,f})(v_{1,i}+ v_{1,f})}{m_{1}(v_{1,i}- v_{1,f})} = \frac{m_{2}(v_{2,f}- v_{2,i})(v_{2,f}+ v_{2,i})}{m_{2}(v_{2,f}- v_{2,i})}
$$

$$
v_{1,i}+ v_{1,f}= v_{2,f}+ v_{2,i}=\Rightarrow \mathrm{simplify}
$$

So all that math went into showing that the sum of the two velocities for $m_{1}$ equals the sum of the two velocities for $m_{2}$. Note that this conclusion is not immediately obvious from either the conservation of momentum or the conservation of kinetic energy equations themselves. But for us to have a unique solution to this problem, the sum of the individual object velocities must be equal.

We can re-arrange the above equation to give $v_{1,f}= v_{2,f}+v_{2,i}-v_{1,i}$ and then plug this into Equation 6.7 to solve for $v_{2,f}$.

$$
m_{1}v_{1,i}+ m_{2}v_{2,i}= m_{1}(v_{2,f}+ v_{2,i}- v_{1,i}) + m_{2}v_{2,f}
$$

$$
m_{1}v_{1,i}+ m_{2}v_{2,i}= m_{1}v_{2,f}+ m_{1}v_{2,i}- m_{1}v_{1,i}+ m_{2}v_{2,f}
$$

$$
2m_{1}v_{1,i}+ m_{2}v_{2,i}- m_{1}v_{2,i}= m_{1}v_{2,f}+ m_{2}v_{2,f}
$$

$$
2m_{1}v_{1,i}+ (m_{2}- m_{1})v_{2,i}= v_{2,f}(m_{1}+ m_{2})
$$

$$
v_{2,f}= \frac{2m_{1}v_{1,i}+ (m_{2}- m_{1})v_{2,i}}{m_{1}+ m_{2}}
$$

And now we have the velocity in terms of the initial velocities and masses.

You can follow the same procedure to get the equation for $v_{1,f}$.

$$
v_{1,f}= \frac{2m_{2}v_{2,i}+ (m_{1}- m_{2})v_{1,i}}{m_{1}+ m_{2}}
$$

1. Find $v_{1,f}$ and $v_{2,f}$ if $m_{1}= 5m_{2}, v_{1,i}$ = 2 m $\mathrm{s}^{-1}$, and $v_{2,i}= -4$ m $\mathrm{s}^{-1}$?

2. Under which circumstances would $m_{1}$ travel in the $-\hat{\imath}$ direction after collision? Under which circumstances would $m_{2}$ travel in the $-\hat{\imath}$ direction after collision?

::::

<!-- Source PDF page 131; printed label 122. -->

::::{admonition} Test your Understanding

Here is [a fun web application](https://www.physicsclassroom.com/Physics-Interactives/Momentum-and-Collisions/Collision-Carts/Collision-Carts-Interactive) that you can use to test your understanding of both elastic and inelastic collisions. Try to solve the set up problems before running the application and see how well you do.

::::

(sec-6-4)=
## 6.4 Centre of Mass

Another important concept in motion and momentum is the centre of mass. Whether you have a system of independent particles (e.g., a cluster of stars) or an irregularly shaped rigid body (e.g., a car), every system has a special point called the *centre of mass*. The centre of mass is not a mass, but a position. It’s the centroid position and it is defined as:

$$
\vec{R}_{cm}= \frac{m_{1}\vec{r}_{1}+ m_{2}\vec{r}_{2}+ \cdot \cdot \cdot + m_{n}\vec{r}_{n}}{m_{1}+ m_{2}+ \cdot \cdot \cdot m_{n}} = \frac{\sum m_{i}\vec{r}_{i}}{\sum m_{i}}
$$

where $\vec{r}_{i}$ is the position of the $i$th particle relative to the origin and $m_{i}$ is the mass of that particle. Since $\sum m_{i}= M$ is the total mass of the system, the centre of mass is:

$$
\vec{R}_{cm}= \frac{\sum m_{i}\vec{r}_{i}}{M}
$$ (eq-6-11)

Note that you can think of the centre of mass as a mass-weighted average position. The formal definition of an average quantity is:

$$
\bar{x} = \frac{\sum w_{i}x_{i}}{\sum w_{i}}
$$

where $x_{i}$ is the quantity and $w_{i}$ is a weight. Note that the $\sum$ used above has the limits of

$$
i\sum =N
$$

$1$, where $N$ is the total number of particles.

::::{admonition} Definition of Average

You are probably familiar with the definition of an average as $\bar{x} = \frac{1}{N} \sum x_{i}$, where $N$ is the total number of elements of $x$. This equation for average comes from the assumption that all quantities of $x$ have equal weight. If all quantities have *equal weight*, then you can factor out the weight from the summation terms and they cancel, leaving you with

$$
\bar{x} = \frac{1}{N} \sum x_{i}.
$$

::::

The centre of mass is where you can perfectly balance a system and it doesn’t need to be at the centre of the object. For example, if you try to hold a hammer at its centre, it will feel unbalanced. That’s because a hammer has an uneven distribution of mass. The head of the hammer is much heavier than the handle, so the centre of mass for the hammer will be closer to the head than the the middle of the handle because most of the mass is located near the head $(R_{cm}$ will be weighted more heavily toward the head than the handle).

<!-- Source PDF page 132; printed label 123. -->

::::{admonition} Try at Home

This [web applet](https://phet.colorado.edu/en/simulation/balancing-act) will let you play around with balancing masses and finding the centre of mass. Examine different structures and test your understanding.

::::

In Cartesian coordinates, we can also describe the centre of mass in terms of the $x, y$, and $z$ axes. The position of a particle in the system is given by $\vec{r}_{i}= x_{i}\hat{\imath}+y_{i}\hat{\jmath}+z_{i}\hat{k}$ . The centre of mass for the system is then determined by $\vec{R}_{cm}= x_{cm}\hat{\imath} + y_{cm}\hat{\jmath} + z_{cm}\hat{k}$ , where

$$
\begin{aligned}
x_{cm}&= \frac{m_{i}x_{i}}{M} \\
y_{cm}&= \frac{\sum m_{i}y_{i}}{M} \\
z_{cm}&= \frac{m_{i}z_{i}}{M}
\end{aligned}
$$

If the particle mass is constant, then the total momentum of a system of particles can be written as:

$$
\vec{p} = \sum m_{i}\vec{v}_{i}= \sum m_{i} \frac{\mathrm{d}\vec{r}_{i}}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t} \sum (m_{i}\vec{r}_{i})
$$ (eq-6-12)

Note that the term in the summation from the above equation is equivalent to $M\vec{R}_{cm}$ from Equation 6.11. Thus, we can put the total momentum in terms of the centre of mass.

$$
\vec{p} = \frac{\mathrm{d}}{\mathrm{d}t} (M\vec{R}_{cm}) = M\vec{v}_{cm}
$$ (eq-6-13)

where $\vec{v}_{cm}$ is the velocity of the centre of mass. In other words, the total momentum of a system of particles is equivalent to the total mass of the system times the velocity of the centre of mass (how the centre of mass of the system is moving).

Equation 6.13 is a way to approximate a complicated system. In physics, we like to simplify problems as much as possible. Rather than trying to solve a complicated problem of a system of particles or an irregularly shaped body, you can instead use one giant particle with a mass given by the total mass of the system located at and moving with the centre of mass and moving. You are basically condensing the problem from a collection of particles down to a representative particle at a mass-weighted average position.

It can also be useful to consider a coordinate system relative to the centre of mass rather than a stationary observer. [Figure 6.5](#fig-6-5) shows the difference between an initial reference frame from a stationary observer, $S$, and a moving frame, $S^{\prime }$, located at the centre of mass of an irregular object. For simplicity, the centre of mass is moving with a constant velocity, $\vec{u}$ (so $S^{\prime }$ is also an inertial frame). To an observer in $S^{\prime }$, the irregular object would appear to be stationary (both the observer and the object are moving together). This means that the total momentum in the CM frame is zero.

<!-- Source PDF page 133; printed label 124. -->

:::{figure} ../images/figures/figure-6-5.png
:label: fig-6-5
:enumerator: 6.5
:alt: Figure 6.5 from the source textbook
:width: 260px

Comparison between a stationary observer coordinate system $(S)$ and a centre-ofmass coordinate system $(S ^{\prime })$. An irregular object is moving in the stationary frame. The centre of mass $(cm)$ of this object has a speed $\vec{u}$ relative to the stationary frame. The $S ^{\prime }$ frame is fixed relative to the centre of mass and moves with it (such that the object would be stationary in the centre-of-mass frame).
:::

Consider the same particle in both reference frames. The particle has a velocity $\vec{v}_{i}$ in frame S and a velocity $\vec{v}_{i}^{\prime }$ in frame S$'$. Since the two frames differ by a relative velocity $\vec{u}$, the velocity in S and S$'$ are connected by,

$$
\vec{v}_{i}= \vec{v}_{i}^{\prime }+ \vec{u}
$$

This equation implies that if the total momentum must be conserved in both frames, because the final and initial momentum shifted by a constant amount $(\vec{u})$. This case is true if there are no external forces (only internal forces) and no acceleration.

(example-6-3)=

::::{admonition} Sample Problem 6-3

Let’s look at an inelastic collision question. [Figure 6.6](#fig-6-6) shows an inelastic collision between two particles, $m$, and $M$. The particle $m$ is moving toward $M$ with a velocity of $\vec{u}$ and $M$ is at rest. After collision, the combined mass is moving at a velocity $\vec{v}$. **Find the final velocity** $v$ **of the** $M + m$ **system.**

:::{figure} ../images/figures/figure-6-6.png
:label: fig-6-6
:enumerator: 6.6
:alt: Figure shows before and after an inelastic collision of two masses in one dimension.
:width: 217px

Inelastic collision between a moving smaller mass with a stationary larger mass.
:::

**Solution**

You can solve this problem using a stationary frame where the two masses are moving. But here we’re going to solve this problem using both a stationary and the moving centre-of-mass (CM) frame.

::::

<!-- Source PDF page 134; printed label 125. -->

Stationary frame: To a stationary observer, the masses are moving before and after collision. From the conservation of momentum, we have:

$$
\vec{p}_{i}= \vec{p}_{f}
$$

$$
\begin{aligned}
mu\hat{\imath} + 0 &= (M + m)v\hat{\imath} \\
v &= \frac{m}{M + m} u
\end{aligned}
$$

CM frame: In the CM frame, the observer is moving with a speed of $\vec{v}_{cm}$ corresponding to the centre of mass of the system. Note that the centre-of-mass velocity must be the same after the collision as before the collision because the centre-of-mass momentum is conserved (no external forces).

First, we can find $\vec{v}_{cm}$. For our two particles, their individual masses are constant and

$$
M_{tot}= M + m.
$$

$$
\vec{v}_{cm}= \frac{1}{M + m} \Bigg(\frac{\mathrm{d}}{\mathrm{d}t} \sum^{m_{i}\vec{r}_{i}} \Bigg)
$$

$$
\vec{v}_{cm}= \frac{1}{M + m} \Bigg(\sum^{m_{i}} \frac{\mathrm{d}\vec{r}_{i}}{\mathrm{d}t} \Bigg)
$$

$$
\vec{v}_{cm}= \frac{1}{M + m} \Bigg(m \frac{\mathrm{d}\vec{r}_{m}}{\mathrm{d}t} + M \frac{\mathrm{d}\vec{r}_{M}}{\mathrm{d}t} \Bigg)
$$

$$
\begin{aligned}
\vec{v}_{cm}&= \frac{1}{M + m} (m\vec{u} + 0) =\Rightarrow \mathrm{in} \mathrm{S}, \frac{\mathrm{d}\vec{r}_{m}}{\mathrm{d}t} = \vec{u} \mathrm{and} \frac{\mathrm{d}\vec{r}_{M}}{\mathrm{d}t} = 0 \\
\vec{v}_{cm}&= \frac{m}{M + m} \vec{u}
\end{aligned}
$$

Now we need to relate $\vec{v}_{cm}$ to the final velocity, $\vec{v}$. After the collision, $M$ and $m$ are stuck together and the system moves as one particle with a speed of $v$ in the observer’s frame. In the CM frame, the post-collision system has a speed of:

$$
\vec{v}_{(M+m)}^{\prime }= \vec{v} - \vec{v}_{cm}
$$

But with only one particle, that particle represents the centre-of-mass position for the post-collision system. In the CM frame, the observer is moving with the centre of mass of the system, so there is no net velocity. That means $\vec{v}_{(M+m)}^{\prime }$ = 0.

Thus, we can now find the final velocity, $v$ in the CM frame.

$$
0 = \vec{v} - \vec{v}_{cm}
$$

$$
\begin{aligned}
\vec{v} &= \vec{v}_{cm} \\
\vec{v} &= \frac{m}{M + m} \vec{u}
\end{aligned}
$$

<!-- Source PDF page 135; printed label 126. -->

::::{admonition} Continued

which is exactly what we had before from the stationary frame.

1. Find the velocities of $m$ and $M$ before the collision in the CM frame.

2. How does the centre-of-mass position change as the two particles approach each other?

::::

Switching to the centre of mass frame can be convenient when you have complicated systems with an irregular rigid mass or a large system of masses.

(sec-6-5)=
## 6.5 Variable Mass

Up until now, we have applied Newton’s second law as $\sum \vec{F} = ma$. This equation is applicable if the system mass is constant with time. But you can have problems in physics where the mass changes.

In general, Newton’s second law follows;

$$
\sum_{\vec{F} =} \frac{\mathrm{d}\vec{p}}{\mathrm{d}t} = \frac{\mathrm{d}(m\vec{v})}{\mathrm{d}t} = \Bigg(\frac{\mathrm{d}m}{\mathrm{d}t} \Bigg)\vec{v} + m\Bigg(\frac{\mathrm{d}\vec{v}}{\mathrm{d}t} \Bigg)
$$

Note that you recover $\sum \vec{F} = m\vec{a}$ if the mass is constant $(\dot{m}$ = 0). But if the mass is changing, then you must include the $\dot{m}$ term as well when applying Newton’s second law.

(example-6-4)=

::::{admonition} Sample Problem 6-4

A rope with a linear mass density of $\lambda$ (in kg $\mathrm{m}^{-1})$ and length $L$ is coiled in a heap on the floor. You grab one end of the rope and pull it up at a constant speed of $v$. **What is the force as a function of height** $y$ **that you must apply to raise rope?**

**Solution**

This is a variable mass problem, because you’re not moving the whole rope at once. The amount of mass you are raising is increasing as more of the rope is lifted off the ground. You are basically giving momentum to “new” atoms in the rope as they leave the ground and additional force is needed to apply that change in momentum.

Since the rope is moving with a constant speed, we know that ![Formula, source page 135](../images/math/p135-0cb3f5f689f5.svg) = 0. But there is still a net force acting on the rope because the mass is changing.

$$
\begin{aligned}
([o \\
\sum \vec{F} &= \Bigg(\frac{\mathrm{d}m}{\mathrm{d}t} \Bigg)\vec{v} + m_{(}\Bigg(\frac{\mathrm{d}\vec{v}}{^{(}\mathrm{d}t} ^{(}\Bigg) = \Bigg(\frac{\mathrm{d}m}{\mathrm{d}t} \Bigg)\vec{v}
\end{aligned}
$$

::::

<!-- Source PDF page 136; printed label 127. -->

::::{admonition} Continued

There are only two forces acting on the system, the external force from you lifting the rope and gravity, both of which are being applied along the $y-$axis:

$$
\Sigma \vec{F} = \vec{F}_{ext}+ \vec{F}_{g}
$$

$$
= \vec{F}_{ext}- m(t)g\hat{\jmath}
$$

$$
= \vec{F}_{ext}- (\lambda y)g\hat{\jmath}
$$

where $\lambda y$ represents the amount of mass above the ground. The total mass of the rope is given by $m_{tot}= \lambda L$.

To solve for the external force, we apply Newton’s second law. We don’t know how quickly the mass is changing (we don’t have $\dot{m}$ , but we can use the general form of Newton’s second law:

$$
\sum \vec{F} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t}
$$

and solve for the equation of the momentum.

Momentum is defined as $\vec{p} = m\vec{v} = m(t)\vec{v}$ in this case. The mass at any given time, $t$, depends on the amount of rope that is lifted off the ground. If we call this height $y$, then the mass is $m(t) = \lambda y$ and the velocity is $\vec{v} = \dot{y}\hat{\jmath}$ .

$$
\vec{p} = \lambda y\dot{y}\hat{\jmath}
$$

Taking the full time derivative of the momentum, we have:

$$
\begin{aligned}
\frac{\mathrm{d}\vec{p}}{\mathrm{d}t} &= \frac{\mathrm{d}}{\mathrm{d}t} (\lambda y\dot{y})\hat{\jmath} \\
&= \lambda (\dot{y})^{2}\hat{\jmath} + \lambda y\ddot{y}\hat{\jmath}
\end{aligned}
$$

$$
= \lambda (\dot{y})^{2}\hat{\jmath} =\Rightarrow \dot{y} \mathrm{is} \mathrm{constant}
$$

Thus, we can can express $F_{ext}$ from Newton’s second law:

$$
\Sigma \vec{F} = \lambda (\dot{y})^{2}\hat{\jmath}
$$

$$
\vec{F}_{ext}- (\lambda y)g\hat{\jmath} = \lambda (\dot{y})^{2}\hat{\jmath}
$$

$$
\vec{F}_{ext}= \Big(\lambda (\dot{y})^{2}+ \lambda yg\Big)\hat{\jmath}
$$

::::

<!-- Source PDF page 137; printed label 128. -->

A classic variable mass problem is a rocket (or car or airplane) using fuel. These objects lose mass with time, which will affect their momentum.

(example-6-5)=

::::{admonition} Sample Problem 6-5

A rocket has an initial mass of $M$ before launch. To move the rocket, its engines burn fuel at a constant rate and expel the gases from the back at a speed of $v_{ex}$ relative to the speed of the rocket. Ignoring gravity and drag, **find the speed** $v_{f}$ **when the rocket** **mass has decreased from its initial mass to a mass of** $M_{f}$**?**

**Solution**

First, describe the motion. [Figure 6.7](#fig-6-7) shows a cartoon of how the rocket is moving at time $t$ + d$t$. The rocket expels exhaust from its back and the gas is moving at a speed of $v_{ex}$ in the $-x$ direction relative to the motion of the rocket (and exhaust) system.

:::{figure} ../images/figures/figure-6-7.png
:label: fig-6-7
:enumerator: 6.7
:alt: Figure shows a rocket with its changing mass and speed.
:width: 341px

At time $t$ + d$t$, the rocket expels $dm_{ex}$ of exhaust at a speed of $v_{ex}$ relative to the speed of the rocket $(v)$. As a consequence, the rocket is given an impulse and increases speed by $dv$.
:::

The rocket and exhaust form an isolated system (there are no other forces), so the total momentum of the system must be conserved. We will consider time $t$ before there is any burning of fuel. So at $t$ there is no contribution of momentum from the exhaust and all the momentum is from the rocket. We will assume that the rocket has a mass of $m$ and velocity $v$. The total momentum at time $t$ is therefore,

$$
\vec{p}_{tot}(t) = mv\hat{\imath}
$$

At time $t+$d$t$, the rocket expels exhaust in the $-x$ direction. Under the conservation of momentum, the rocket must be given equal momentum in the $+x$ direction (this is the impulse given to the rocket that propels it forward). The rocket gains a bit of velocity d$v$ and speeds up. But as the rocket is gaining velocity, it is also losing mass because it is using up fuel by expelling the exhaust. The mass of exhaust will equal the mass lost by the rocket (we need to obey the conservation of mass). The exhaust at time $t$ + d$t$ has a mass of d$m_{ex}$ and a speed of $v_{ex}(-\hat{\imath})$ relative to the speed of the system as a whole (see [Figure 6.7](#fig-6-7)).

In the frame of a stationary observer at time $t$ + d$t$, the exhaust is moving a speed of $(v - v_{ex})\hat{\imath}$ and the rocket has a mass $m -$ d$m_{ex}$ and a velocity of $(v$ + d$v)\hat{\imath}$. The total

::::

<!-- Source PDF page 138; printed label 129. -->

::::{admonition} Continued

momentum at time $t$ + d$t$ is therefore,

:::{image} ../images/math/p138-6efb7e0f91bd.svg
:alt: Mathematical expression from source PDF page 138
:class: source-equation
:align: center
:::

Since the total momentum of the rocket + exhaust system is conserved, the total momentum at time $t$ must be equal to the total momentum at time $t$ + d$t$.

$$
\vec{p}_{tot}(t) = \vec{p}_{tot}(t + \mathrm{d}t)
$$

$mv$ = (d$m_{ex})(v - v_{ex}) + (m -$ d$m_{ex})(v$ + d$v) =\Rightarrow$ all motion in 1D, drop $\hat{\imath}$ $mv = v$d$m_{ex}- v_{ex}$d$m_{ex}+ mv + m$d$v - v$d$m_{ex}-$ d$m_{ex}$d$v =\Rightarrow$ expand 0 = $-v_{ex}$d$m_{ex}+ m$d$v -$ d$m_{ex}$d$v =\Rightarrow$ simplify the terms 0 = $-v_{ex}$d$m_{ex}+ m$d$v =\Rightarrow$ ignore the d$m$d$v$ term, it is very small

$$
\mathrm{d}v = v_{ex} \frac{\mathrm{d}m_{ex}}{m}
$$

This equation relates a differential velocity to a differential mass. But d$m_{ex}$ corresponds to the increasing mass of the exhaust, whereas the $m$ term in the above equation corresponds to the mass of the rocket. The increasing mass of the exhaust is equal to the decrease in mass in the rocket. In other words, d$m_{ex}= -$d$m$, where d$m$ is the change in mass of the rocket.

$$
\begin{aligned}
\mathrm{d}v &= -v_{ex} \frac{\mathrm{d}m}{m} =\Rightarrow \mathrm{sub} \mathrm{d}m_{ex}= -\mathrm{d}m \\
\int_{0}^{v_{f}} \mathrm{d}v &= -v_{ex}\int_{M}^{M_{f}} \frac{\mathrm{d}m}{m} =\Rightarrow v_{ex}\mathrm{is} \mathrm{a} \mathrm{constant} \\
v_{f}- 0 &= -v_{ex}\Big(\ln m|_{M}^{M_{f}} =\Rightarrow \mathrm{initial} \mathrm{is} v = 0, m = M \\
v_{f}&= -v_{ex}(\ln M_{f}- \ln M)
\end{aligned}
$$

$$
v_{f}= v_{ex}\ln \Bigg(\frac{M}{M_{f}} \Bigg)
$$

Thus, we found the equation for the velocity when the mass decreased from $M$ to $M_{f}$. Note that $v_{f}$ increases with time because $M_{f}$ decreases with time.

::::

<!-- Source PDF page 139; printed label 130. -->

(sec-6-6)=
## 6.6 Real-World Application

Recreational activities like air hockey, billiards (pool), and bumper cars are all built around the principle of collisions, whether elastic or inelastic. In general, these applications will always involve friction which will make the puck, balls, or car come to a halt given time. Each uses a different method to try to reduce that friction as far as possible: a layer of air to keep the puck off the table for air hockey, smooth paint on the balls and low-friction felt for billiards, and graphite sprinkled across a smooth metal floor for bumper cars.

On a larger scale, collisions and momentum conservation are also crucial for particle physics. The Large Hadron Collider (LHC) at CERN, routinely collides particle beams. The particle beams travel in opposite directions around a 27-km accelerator ring, guided and accelerated to very high energies (very close to the speed of light) using thousands of super-cooled superconducting magnets, before being made to collide. While operating at relativistic velocities and energies, the same basic physics of conservation of momentum and energy applies in these collisions.

The objective of studying these ultra-high-energy collisions is to understand more about matter and how the universe evolved. The LHC is able to simulate energy levels and temperatures similar to those that existed approximately $10^{-12}$ seconds after the Big Bang. In relativistic collisions between free particles, energy and momentum are always conserved. The LHC has detectors to measure the speed, mass, and charge of the post-collision particles, which enables them to identify new particles based on the fundamental requirement that momentum must be conserved.

:::{figure} ../images/figures/figure-6-8.png
:label: fig-6-8
:enumerator: 6.8
:alt: Figure shows image a of a long tube and its surrounding tunnel used in a particle collider.
:width: 325px

A very small section of the Large Hadron Collider tunnel. Image credit: CERN.
:::

**For more information:**

See the [CERN website for more on the LHC](https://www.home.cern/science/accelerators/large-hadron-collider).

Let’s Talk Science has [a nice introduction to momentum and billiards](https://letstalkscience.ca/educational-resources/stem-explained/billiards-and-collisions), with links to videos.

<!-- Source PDF page 140; printed label 131. -->

(sec-6-7)=
## 6.7 Summary

::::{admonition} Key Takeaways

This chapter describes linear momentum for systems of particles in more detail. Linear momentum is defined as $\vec{p} = m\vec{v}$. For a system with only internal forces, the total linear momentum is conserved.

$$
\sum \vec{p}_{i}= \mathrm{constant}
$$

Newton’s second law is also more formally defined based on the total linear momentum. If your system mass is allowed to change, then the full equation for Newton’s second law is:

$$
\sum \vec{F} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t} = \Bigg(\frac{\mathrm{d}m}{\mathrm{d}t} \Bigg)\vec{v} + m\Bigg(\frac{\mathrm{d}\vec{v}}{\mathrm{d}t} \Bigg)
$$

In systems where the total linear momentum is conserved, the net force is zero. If the system has variable mass, then one must use the general form of Newton’s second law to solve for the equations of motion.

This chapter also defines impulse and collisions, which is how momentum of a system can change. Impulse is when an external force acts on a system over a short time duration such that the system has not had time to move between the start of the event and the end.

$$
\vec{I} = \int_{t_{1}}^{t_{2}} \vec{F}\mathrm{d}t = \Delta \vec{p}
$$

Collisions are when momentum is exchanged between objects in a system. There are two types, inelastic collisions (the objects stick together) and elastic collisions (the objects rebound away). If the total linear momentum from the collisions is conserved, then we can say:

$$
\vec{p}_{i}= \vec{p}_{f}
$$

An important property for systems of particles in the centre of mass. The centre of mass is a special radius vector that represents the mass-weighted average position vector.

$$
\vec{R}_{cm}= \frac{\sum m_{i}\vec{r}_{i}}{M}
$$

Large or complex systems of particles can be simplified to a single giant particle at the position of the centre of mass that is moving with the centre of mass. The centre-ofmass reference frame can also be helpful in simplifying problems, because the net linear momentum of the centre-of-mass frame is zero by definition.

::::

<!-- Source PDF page 141; printed label 132. -->

::::{admonition} Important Equations

**Linear Momentum:**

$$
\vec{p} = m\vec{v}
$$

**Newton’s Second Law:**

$$
\sum_{\vec{F} =} \frac{\mathrm{d}\vec{p}}{\mathrm{d}t} = \frac{\mathrm{d}(m\vec{v})}{\mathrm{d}t} = \Bigg(\frac{\mathrm{d}m}{\mathrm{d}t} \Bigg)\vec{v} + m\Bigg(\frac{\mathrm{d}\vec{v}}{\mathrm{d}t} \Bigg)
$$

**Conservation of Momentum:**

$$
\vec{p}_{tot}= \sum \vec{p}_{i}= \mathrm{constant}
$$

**Momentum with an External Force:**

$$
\frac{\mathrm{d}\vec{p}_{i}}{\mathrm{d}t} = \sum \vec{F}_{i}= \vec{F}_{i,int}+ \vec{F}_{i,ext}
$$

**Impulse:**

$$
\vec{I} = \int_{t_{1}}^{t_{2}} \vec{F}\mathrm{d}t = \int_{t_{1}}^{t_{2}} \frac{\mathrm{d}\vec{p}}{\mathrm{d}t} \mathrm{d}t = \int_{t_{1}}^{t_{2}} \mathrm{d}\vec{p} = \vec{p}_{2}- \vec{p}_{1}= \Delta \vec{p}
$$

**Centre of Mass:**

$$
\vec{R}_{cm}= \frac{\sum m_{i}\vec{r}_{i}}{M}
$$

**Momentum of a System of Particles:**

$$
\vec{p} = \sum m_{i}\vec{v}_{i}= \sum m_{i} \frac{\mathrm{d}\vec{r}_{i}}{\mathrm{d}t} = \frac{\mathrm{d}}{\mathrm{d}t} \sum (m_{i}\vec{r}_{i})
$$

**Momentum of Particles with Fixed Masses:**

$$
\vec{p} = M \frac{\mathrm{d}\vec{R}_{cm}}{\mathrm{d}t} = M\vec{v}_{cm}
$$

::::

<!-- Source PDF page 142; printed label 133. -->

(sec-6-8)=
## 6.8 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-6-1)=

::::{admonition} Practice Problem 6-1

Three identical particles are moving as follows:

Particle 1: $2\hat{\imath}$

Particle 2: $\hat{\jmath}$

Particle 3: $\hat{\imath} + \hat{\jmath} + \hat{k}$

Where all values are in SI units. What is the centre-of-mass velocity $v_{cm}$ of this system?

::::

(problem-6-2)=

::::{admonition} Practice Problem 6-2

A particle with mass $M_{1}$ and velocity $v_{1}\hat{\imath}$ collides with a particle of mass $M_{2}$, initially at rest.

a) After the collision, $M_{1}$ is at rest. What is the velocity of $M_{2}$?

b) After collision, the two particle stick together and continue in the same direction. What is their velocity?

::::

(problem-6-3)=

::::{admonition} Practice Problem 6-3

Two particles of mass $M_{1}$ and $M_{2}$ collide. Before the collision, the first particle has a speed of $v_{1}= 4\hat{\imath} - 3\hat{\jmath}$ and the second particle has a speed of $v_{2}= 4\hat{\imath} + 3\hat{\jmath}$ .

a) If both particles have the same mass, what is the speed of $M_{1}$ if $M_{2}$ comes to a stop after the collision?

b) Consider that $M_{2}= 2M_{1}$ and the collision is instead perfectly inelastic (particles stick together). What is their new velocity?

::::

<!-- Source PDF page 143; printed label 134. -->

(problem-6-4)=

::::{admonition} Practice Problem 6-4

A student is late running from Depuis Hall to Stirling Hall. As they run past the speedometer on University Ave, they notice that they are running at 18 km/h. They then run into another student who is waiting for the bus. (Assume that the running student weighs 65 kg).

a) What is the impulse required for the student waiting for the bus to stop the running student and not fall over?

b) If this impulse is delivered to the student in 0.20 seconds, then what is the magnitude of the force acting between the stationary student and the running student?

::::

(problem-6-5)=

::::{admonition} Practice Problem 6-5

A bullet traveling at a velocity of $v\hat{\imath}$ is shot through a stationary block of wood head on. When it emerges from the other side, the bullet has lost half its speed. If the block has a mass of $M$ and the bullet has a mass of $m$, what is the velocity of the block of wood after the bullet emerges? (Ignore any friction or loss of energy. Assume the block of wood loses no mass.)

::::

(problem-6-6)=

::::{admonition} Practice Problem 6-6

An artillery shell is launched upwards with a speed of $v_{0}$ at an angle of $\theta$ with respect to the ground. When it reaches its maximum point, the shell explodes into two fragments of equal mass. One of the fragments goes straight up at a speed of $v_{0}/2$. What is the speed of the other fragment?

::::

(problem-6-7)=

::::{admonition} Practice Problem 6-7

A Velcro block target of mass $M$ hangs from the cross-bar of a hockey net with an ideal rope of length $L$. Iconic hockey player Wayne Gretzky’s slap-shot fires a puck (covered in Velcro), of mass $m_{p}$ straight into the block target and becomes stuck to the block. The block is initially at rest and the puck has an initial speed of $v_{0}$. The impact causes the block to oscillate with a maximum angle of $\theta _{\max}$ from the vertical.

a) Find the speed of the block at the moment the puck becomes stuck to it.

b) Find the amplitude $(x_{\max})$ of the simple harmonic motion of the block. You can assume that the block is like a point mass at the bottom of the rope.

::::

<!-- Source PDF page 144; printed label 135. -->

::::{admonition} Continued

c) Find the maximum angle, $\theta _{\max}$ from the vertical. You can assume that $\theta _{\max}$ is a small angle.

d) Consider the case where $m_{p}$ = 160g, $M$ = 100g, $L = 1.4\mathrm{m}$, and $\theta _{\max}$ = 14 degrees. What is the initial speed of the puck? Does that value make sense?

:::{figure} ../images/figures/figure-6-9.png
:label: fig-6-9
:enumerator: 6.9
:alt: Cartoon of a puck approaching a block in front of a hockey net.
:width: 217px

Figure for [Problem 6-7](#problem-6-7).
:::

::::

(problem-6-8)=

::::{admonition} Practice Problem 6-8

On a strange alien planet, Grog has invented a rudimentary car by attaching four wheels to a long piece of wood. Grog then fixes another piece of wood vertically to the front of it and operates the car by throwing 0.25-kg rocks perfectly horizontally at 20 m/s to bounce off the vertical piece. The rock rebounds with only one quarter of its original speed (Grog ducks) and lands behind the wooden car. If there is no loss of energy to friction, what is Grog’s speed after throwing 10 rocks? Grog’s mass is 70 kg and the wheeled vehicle has a mass of 30 kg. Neglect the mass of the rocks still on the car after each throw.

:::{figure} ../images/figures/figure-6-10.png
:label: fig-6-10
:enumerator: 6.10
:alt: Figure shows Grog standing on a simple car with a small pile of rocks, having just thrown the first rock at the vertical target piece of the car.
:width: 217px

Figure for [Problem 6-8](#problem-6-8).
:::

*Note, this problem could be considered a variable mass question as the loss of the rocks* *ends up changing the mass of the car. If you want to challenge yourself, trying solving* *the problem including the mass loss.*

::::

<!-- Source PDF page 145; printed label 136. -->

(problem-6-9)=

::::{admonition} Practice Problem 6-9

See the figure below. A mass $m_{1}$ is moving toward a second mass, $m_{2}$, with a speed of $u$. The second mass $m_{2}$ is stationary and connected to a spring (see figure). After $m_{1}$ collides with $m_{2}$ they stick and compress the spring.

a) Find the centre-of-mass velocity of the system after collision.

b) Use Newton’s laws to find the differential equation of motion of velocity for the spring.

c) Solve the differential equation of motion to find the maximum compression of the spring. (Hint, you want to find a maximum displacement, $x$, corresponding to a specific change in velocity.)

:::{figure} ../images/figures/figure-6-11.png
:label: fig-6-11
:enumerator: 6.11
:alt: Figure shows a moving mass approaching a stationary mass which is attached to the wall by a spring.
:width: 341px

Figure for [Problem 6-9](#problem-6-9).
:::

::::

(problem-6-10)=

::::{admonition} Practice Problem 6-10

A car of mass $M$ is moving at an initial speed of $v_{0}$ when it snags a heavy rope sitting in a pile on the road. The rope has a mass density of $\lambda$ (in kg $\mathrm{m}^{-1})$ and length $L$. Assume the rope starts off at rest and only a small piece attaches initially to the car and that the rope does not deform during the motion. Assume there is no friction acting on the rope.

a) What is the mass of the car after a length $x$ of rope has uncoiled?

b) What is the speed of the car after a length $x$ of rope has uncoiled? Assume that the driver of the car does not exert any change in force that would affect the speed.

c) What is the tension in the rope in the piece of rope that is right next to the pile on the ground

::::

<!-- Source PDF page 146; printed label 137. -->

(problem-6-11)=

::::{admonition} Practice Problem 6-11

A rocket ship of mass $M_{0}$ drifts in space with a speed of $v_{0}$. At time $t$ = 0, it drifts into a dust cloud that is stationary. The cloud has a volume density of $\rho$ (in kg $\mathrm{m}^{-3})$ and dust from the cloud sticks to the rocket over its cross-sectional area, $A$.

$$
\mathrm{d}m
$$

a) Show that the change in mass for the rocket is given by = $A\rho v$ at time $t$.

$$
\mathrm{d}t
$$

b) What is the mass of the rocket when it is moving at speed $v$?

c) Solve for $v(t)$. Hint, use Newton’s second law to set up a differential equation in terms of $v$ and $t$.

::::
