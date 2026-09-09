(ch-5)=
# 5. Application of Non-Inertial and Rotating Frames

<!-- Source PDF page 101; printed label 92. -->

::::{admonition} Learning Objectives

- Describe the fictitious forces of a rotating frame

- Solve physics problems with the Earth as a non-inertial frame

- Solve the Foucault Pendulum problem

::::

In this chapter, we will use non-inertial and rotating frames of reference to solve physics problems. Please see [Chapter 4](#ch-4) for an introduction to non-inertial and rotating frames.

(sec-5-1)=
## 5.1 Rotating versus Accelerating Frames

In [Chapter 4](#ch-4), we derived the equations for acceleration and velocity in a non-inertial frame when there was only linear acceleration ([Chapter 4.2](#sec-4-2)) and when there was rotation ([Chapter 4.4](#sec-4-4)). Note that these two equations are connected.

The equation for acceleration in a rotating frame is:

$$
\vec{a}^{\prime }= \vec{a} - \vec{\alpha} \times \vec{r}^{\prime }- 2\vec{\omega} \times \vec{v}^{\prime }- \vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) - \vec{A}
$$ (eq-5-1)

where the parameters with primes are in the rotating reference frame and the parameters without primes are measured in an inertial frame. See [Chapter 4.5](#sec-4-5) for what each of these terms mean. If your system is *not* rotating, then $\vec{\alpha} = \vec{\omega}$ = 0 and we recover the same equation for a linear non-inertial frame from [Chapter 4.2](#sec-4-2),

$$
\vec{a}^{\prime }= \vec{a} - \vec{A} =\Rightarrow \mathrm{for} \mathrm{no} \mathrm{rotation}
$$ (eq-5-2)

where $\vec{A}$ is the acceleration of the non-inertial frame relative to the inertial frame.

Similarly, the equation for velocity in a rotating frame is:

$$
\vec{v}^{\prime }= \vec{v} - \vec{\omega} \times \vec{r}^{\prime }- \vec{u}
$$ (eq-5-3)

where we have added an extra term, $\vec{u}$, to represent the velocity of the origin in the noninertial frame relative to the inertial frame.

Finally, we defined the fictitious forces as,

(eq-5-4)=
:::{image} ../images/math/p101-79b4d00afd2e.svg
:alt: Mathematical expression from source PDF page 101
:class: source-equation
:align: center
:::

<!-- Source PDF page 102; printed label 93. -->

where the four labeled terms are the four fictitious force: the azimuthal force, the Coriolis force, the centrifugal force, and the translational force. Note how each of these forces are defined with negative signs because they act opposite the direction of acceleration.

In the next two sections, we will look at examples of the centrifugal force and the Coriolis force. The azimuthal force will be left for practice. See [Chapter 4](#ch-4) for examples of the translation force.

(sec-5-2)=
## 5.2 Centrifugal Fictitious Force

The centrifugal force is a consequence of a rotating frame and has the form of

$$
\vec{F}_{cent}= -m\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime })
$$ (eq-5-5)

Note that the acceleration from the centrifugal force is $\vec{\omega}\times (\vec{\omega}\times \vec{r}^{\prime })$ and this acceleration has the same form as the centripetal acceleration associated with circular motion (see [Chapter 1](#ch-1)). If you have circular motion, $\vec{\omega} \perp \vec{r}$ and $|\vec{F}_{circ}| = m\omega ^{2}r = \frac{mv^{2}}{r}$.

::::{admonition} Centrifugal vs Centripetal Acceleration

In rotational motion, we have two similar sounding accelerations, the centrifugal and centripetal acceleration. These should be treated differently, and neither should really be considered a real force. The centrifugal force is a fictitious force that arises from being in a rotating reference frame. The centripetal acceleration is a description of the acceleration coming from a different force (e.g., gravity, friction, tension). As a result, we do not include a “centripetal force” on any free-body diagrams (although the centrifugal force would be required in a non-inertial frame free-body diagram).

::::

While similar in magnitude, the direction of the centrifugal force is not the same as the direction of the centripetal acceleration. The centrifugal force points radially outward for rotating frames, whereas the centripetal acceleration points radially inward. This should make intuitive sense as fictitious forces act in the opposite direction to the acceleration in the inertial frame (negative sign in the Equation (5.5).

To prove that the centrifugal force is radially outward, let’s go through an example vector cross product for uniform circular motion with its axis of rotation pointing up $(\hat{k}^{\prime })$. Even though we have a radial dependence with our cross product, we will use Cartesian coordinates for the rotating frame $(\hat{\imath}^{\prime },\hat{\jmath}^{\prime },\hat{k}^{\prime })$. The reason is, in our rotating frame, the radial vector will move with the non-inertial coordinate system. That is, from the perspective of a non-inertial observer rotating with the coordinate system, the radial vector does not change. So we can define our radial vector as being along the $x-$axis $(\vec{r}^{\prime }= r\hat{\imath}^{\prime })$ for example, and as the system rotates, our radial vector will remain along the $\hat{\imath}^{\prime }$ direction (both the position and the coordinates are rotating in this inertial frame).

Using $\vec{\omega} = \omega \hat{k}^{\prime }$ and $\vec{r}^{\prime }= r\hat{\imath}^{\prime }$, the centrifugal acceleration is $\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) = \omega \hat{k}^{\prime }\times (\omega \hat{k}^{\prime }\times r\hat{\imath}^{\prime })$. To solve this problem, we need to do two cross products. First, we will do the cross product

<!-- Source PDF page 103; printed label 94. -->

in brackets. (See [Chapter 1.5.2](#sec-1-5-2) for review on computing the cross product).

$$
\begin{aligned}
\hat{\imath}^{\prime }\hat{\jmath}^{\prime }\hat{k}^{\prime } \\
\vec{\omega} \times \vec{r}^{\prime }&= |0 0 \omega | = \hat{\imath}^{\prime }(0 - 0) + \hat{\jmath}^{\prime }(r\omega - 0) + \hat{k}^{\prime }(0 - 0) = r\omega \hat{\jmath}^{\prime } \\
r 0 0
\end{aligned}
$$

Then we will take our solution to that first cross product and apply that to the second cross product.

$$
\begin{aligned}
\hat{\imath}^{\prime }\hat{\jmath}^{\prime }\hat{k}^{\prime } \\
\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) &= |0 0 \omega | = \hat{\imath}^{\prime }(0 - r\omega ^{2}) + \hat{\jmath}^{\prime }(0 - 0) + \hat{k}^{\prime }(0 - 0) = -r\omega ^{2}\hat{\imath}^{\prime } \\
0 r\omega 0
\end{aligned}
$$ (eq-5-6)

So the direction of the resulting vector from $\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime })$ is along the radial line, pointing inward toward the origin (negative value). But the centrifugal fictitious force is equal to $\vec{F}_{cent}= -m\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) = mr\omega ^{2}\hat{\imath}^{\prime }$, which means that $\vec{F}_{cent}$ is pointing radially outward (away from the origin).

::::{admonition} Centrifugal Force in Practice

The outward acceleration of the centrifugal force is why laundry sticks to the sides of a top-loading washing machine during the high spin cycle, why you stick to the walls of an amusement park ride that spins very quickly, and why centrifuges are called centrifuges. These are all cases where the objects in question (clothes, people, lab materials) are in a non-inertial frame that is spinning. The rotating frame pushes things outward.

::::

(example-5-1)=

::::{admonition} Sample Problem 5-1

A cat with mass $m$ sits on a turntable at a radial position of R. The turntable is spinning at a constant angular velocity of $\vec{\omega} = \omega \hat{k}$ (see [Figure 5.1](#fig-5-1)). If the coefficient of static friction between the cat and the table is $\mu$, **what is the maximum rotation** **rate before the cat starts to slip?**

**Solution**

Inertial Frame: In the inertial frame, the cat’s acceleration is

$$
\vec{a} = -\omega ^{2}R\hat{r}
$$

which is just the centripetal acceleration. The force behind this acceleration is actually

::::

<!-- Source PDF page 104; printed label 95. -->

friction with the table. The friction force points inward toward the center, because the rotation makes the cat want to move outward (centrifugal force).

$$
\vec{f} = -\mu N\hat{r} = -\mu mg\hat{r}
$$

where $N$ is the normal force. Since there is no vertical motion, $N = mg$. The cat will start to lose balance when the acceleration from rotation equals the (static) friction force. Any additional rotation, and the cat will start to move. From Newton’s second law, we get:

$$
\sum \vec{F} = -m\vec{a}
$$

$$
f = -m\omega ^{2}R\hat{r}
$$

$$
-\mu mg\hat{r} = -m\omega ^{2}R\hat{r}
$$

:::{image} ../images/math/p104-c558868ab844.svg
:alt: Mathematical expression from source PDF page 104
:class: source-equation
:align: center
:::

So in the inertial frame, we can describe the cat’s motion and the condition for slipping fairly easily. **What about the non-inertial frame?**

Cat’s Frame: The cat is our observer in the rotating frame, which means that the cat will experience fictitious forces. [Figure 5.1](#fig-5-1) shows the free-body diagram from the cat’s perspective with vectors showing the gravitational force and the centrifugal force. Note that no other fictitious forces act on the cat, since it isn’t moving and the table is rotating at a constant rate.

:::{figure} ../images/figures/figure-5-1.png
:label: fig-5-1
:enumerator: 5.1
:alt: Figure shows a diagram of the cat on a turntable with relevant forces labelled.
:width: 310px

Free-body diagram for the cat on a spinning turntable. The labeled forces are the gravitational force $(F_{g})$, the normal force $(N)$, friction $(f)$, and the centrifugal force $(F_{cent})$. The three forces in purple are the forces that we would identify in an inertial frame. The centrifugal force in black is only in the cat’s frame.
:::

Compared to the inertial frame, the cat would identify one additional force. The centrifugal force. So the sum of all forces would be:

$$
m\vec{a}^{\prime }= \vec{F}_{I}+ \vec{F}_{cent}
$$

where $\vec{F}_{I}$ is the total force in the inertial frame (the real forces). From the cat’s perspective, however, it isn’t moving. The cat is just sitting and the world is moving around it. So to the cat, $\vec{a}^{\prime }$ = 0.

<!-- Source PDF page 105; printed label 96. -->

::::{admonition} Continued

Taking $\vec{a}^{\prime }$ = 0, we get:

$$
0 = \vec{F}_{I}+ \vec{F}_{cent}
$$

0 = $f + F_{cent}=\Rightarrow$ only inertial force is friction 0 = $-\mu mg + mR\omega ^{2}=\Rightarrow f$ and $F_{cent}$ act in opposite directions

:::{image} ../images/math/p105-523b09c630ba.svg
:alt: Mathematical expression from source PDF page 105
:class: source-equation
:align: center
:::

which is the same solution as the inertial frame (as expected). The difference is that we have identified the fictitious centrifugal force for the non-inertial frame.

1. Fictitious force act like a modification of gravity (e.g., effective gravity) in the non-inertial frame. Depending on the problem, the effective gravity vector can be at an angle relative to the vertical. Assuming there is only the centrifugal force acting on the cat, what is the equation for the angle for the effective gravity in terms of $\omega, R$, and $g$? Hint, add the $F_{g}$ and $F_{cent}$ vectors.

2. What is the rotation rate if the angle from the vertical is $2^{\circ}$ and $R$ = 2 m?

3. If the coefficient of static friction with the table is $\mu = 0.2$, what is the maximum angular speed $(\omega _{\max})$ before the cat starts to slip?

4. What is the angle, relative to the vertical, of the effective gravity acting on the cat when $\omega = \omega _{\max}$?

::::

::::{admonition} Lance’s Thoughts

For a rotating frame of reference, you start with five potential fictitious forces. Most of the time, you’ll be able to eliminate at least some of them based on whether the object is moving or accelerating inside the rotating frame and whether the non-inertial frame is rotating or moving at a constant rate. Look for terms that will equal zero.

In the sample problem above, we only had centrifugal force to worry about. Since the cat, seen from inside the rotating frame, isn’t moving at all, we can eliminate the linear and Coriolis accelerations. Since the rotation is at a constant rate and the axis of rotation isn’t moving, we can eliminate the azimuthal and translational accelerations. With four out of five fictitious forces gone, this becomes a much easier problem to solve.

::::

(sec-5-3)=
## 5.3 Coriolis Fictitious Force

The Coriolis force is a consequence of an object moving in a rotating frame. The force equation is:

$$
\vec{F}_{Cor}= -2m\vec{\omega} \times \vec{v}^{\prime }
$$ (eq-5-7)

<!-- Source PDF page 106; printed label 97. -->

Like the centrifugal force, the Coriolis force depends on a vector cross product. So we need to look at the direction.

Let’s assume that we have a rotating system with $\vec{\omega} = \omega \hat{k}^{\prime }$ and we have a particle of mass $m$ in this system moving radially outward with a constant velocity in the rotating frame with $\vec{v}^{\prime }= v^{\prime }\hat{\imath}^{\prime }$. As in the previous section, we will use Cartesian coordinates for simplicity, because the mass is rotating with the system such that our radial vector will remain along the $\hat{\imath}^{\prime }$ direction.

Using $\vec{\omega} = \omega \hat{k}^{\prime }$ and $\vec{v}^{\prime }= v^{\prime }\hat{\imath}^{\prime }$, we need to solve $\vec{\omega} \times \vec{v}^{\prime }= \omega \hat{k}^{\prime }\times (v^{\prime }\hat{\imath}^{\prime })$ for the Coriolis force.

$$
\begin{aligned}
\hat{\imath}^{\prime }\hat{\jmath}^{\prime }\hat{k}^{\prime } \\
\vec{\omega} \times \vec{v}^{\prime }&= |0 0 \omega | = \hat{\imath}^{\prime }(0 - 0) + \hat{\jmath}^{\prime }(v^{\prime }\omega - 0) + \hat{k}^{\prime }(0 - 0) = v^{\prime }\omega \hat{\jmath}^{\prime } \\
v^{\prime }0 0
\end{aligned}
$$ (eq-5-8)

But the Coriolis fictitious force is equal to $\vec{F}_{Cor}= -2m\vec{\omega} \times \vec{v}^{\prime }= -2mv^{\prime }\omega \hat{\jmath}^{\prime }$. So the Coriolis force is in the negative $\hat{\jmath}^{\prime }$ direction. You may notice this force if you’ve ever tried walking on a rotating surface (e.g., a merry-go-round). You feel off balance.

[Figure 5.2](#fig-5-2) shows the fictitious forces for a particle that is moving outward with a constant velocity on a rotating reference frame. There are two fictitious forces in this case, the Coriolis force (due to motion in a rotating frame) and the centrifugal force (due to the rotating frame itself).

:::{figure} ../images/figures/figure-5-2.png
:label: fig-5-2
:enumerator: 5.2
:alt: Figure shows the rotating x-prime y-prime coordinate plane with vectors for the fictitious forces.
:width: 228px

Overhead view of a rotating frame with a particle of mass $m$ moving at a speed $v^{\prime }$ in the rotating frame. From the particle’s perspective, there are two fictitious forces, the centrifugal force $(F_{cent})$ and the Coriolis force $(F_{Cor})$. Both forces only exist in the non-inertial (rotating) frame.
:::

::::{tip} Quick Questions

1. Can you have a case where the centrifugal force is zero and the Coriolis force is non-zero? If yes, under which circumstances?

::::

<!-- Source PDF page 107; printed label 98. -->

(example-5-2)=

::::{admonition} Sample Problem 5-2

Let’s return to the question of the cat sitting on a turntable from [Sample Problem 5-1](#example-5-1). Now, the cat starts to move radially outward at a constant speed of $v^{\prime }\hat{\imath}^{\prime }$. **At what** **radius will the cat start to slip?**

**Solution**

Inertial Frame: In the inertial frame, the net force acting on the cat is still friction with the table. But due to the combination of a rotation frame and the cat is moving, friction is no longer radial (e.g., we cannot say that the cat is undergoing simple circular motion). It is *much easier* to solve this problem in the cat’s reference frame.

The Cat’s Frame: From the cat’s perspective, there is no acceleration because it is moving at a constant velocity. So we can simplify the equation of motion with $\vec{a}^{\prime }$ = 0. But there are two fictitious forces acting on the cat. So the force equation becomes:

$$
m\vec{a}^{\prime }= m\vec{a} + \vec{F}_{fic}
$$

$$
0 = \vec{F}_{I}+ \vec{F}_{cent}+ \vec{F}_{Cor}
$$

where $\vec{F}_{I}$ is the net force in the inertial frame. In this problem, we have $\vec{\omega} = \omega \hat{k} = \omega \hat{k}^{\prime }$ and both the radial position and the velocity vectors are along the $\hat{\imath}^{\prime }$ in the cat’s frame (these do not change from $\hat{\imath}^{\prime }$, because the cat is rotating with the reference frame). That means we can use our previous solutions for the centrifugal and Coriolis forces (see Equations 5.6 and 5.8).

The Coriolis force is constant because the cat’s velocity and the table’s angular velocity are both constant. The Coriolis force is:

$$
\vec{F}_{Cor}= -2m\vec{\omega} \times \vec{v}^{\prime }= -2m\omega \hat{k}^{\prime }\times (v^{\prime }\hat{\imath}^{\prime }) = -2mv^{\prime }\omega \hat{\jmath}^{\prime }
$$

The centrifugal force is not constant, however, because the cat’s position is changing. The cat’s position can be described by $\vec{r}^{\prime }= x^{\prime }\hat{\imath}^{\prime }$, where $\dot{x}^{\prime }= v^{\prime }$.

$$
\vec{F}_{cent}= -m\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) = -m\omega \hat{k}^{\prime }\times (\omega \hat{k}^{\prime }\times x^{\prime }\hat{\imath}^{\prime }) = m\omega ^{2}x^{\prime }\hat{\imath}^{\prime }
$$

Combining these equations into the force equation from the cat’s perspective, we have:

$$
0 = \vec{F}_{I}+ \vec{F}_{cent}+ \vec{F}_{Cor}
$$

$$
0 = \vec{F}_{I}+ m\omega ^{2}x^{\prime }\hat{\imath}^{\prime }- 2mv^{\prime }\omega \hat{\jmath}^{\prime }
$$

$$
\vec{F}_{I}= 2mv^{\prime }\omega \hat{\jmath}^{\prime }- m\omega ^{2}x^{\prime }\hat{\imath}^{\prime }
$$

::::

<!-- Source PDF page 108; printed label 99. -->

::::{admonition} Continued

We now have an equation for the net inertial force, which is only friction in this case (gravity and the normal force will cancel because the cat doesn’t leave the surface of the table). [Figure 5.3](#fig-5-3) shows the direction of $\vec{F}_{I}$ in pink. Note that $\vec{F}_{I}$ is not radial because the two fictitious forces make the cat want to move in two perpendicular directions. Solving for $\vec{F}_{I}$ is very challenging in the inertial frame.

:::{figure} ../images/figures/figure-5-3.png
:label: fig-5-3
:enumerator: 5.3
:alt: shows the rotating x-prime y-prime coordinate plane with vectors for the fictitious forces and the inertial force.
:width: 217px

Same as [Figure 5.2](#fig-5-2), but with the net force from the inertial frame included in pink. Note that $\vec{F}_{I}= -\vec{F}_{cent}- \vec{F}_{Cor}$ by definition (see above for the equation). So the net force in the inertial frame is acting on an angle.
:::

We can use the net inertial force to get the net acceleration in the inertial frame as $\vec{a} = 2v^{\prime }\omega \hat{\jmath}^{\prime }- \omega ^{2}x^{\prime }\hat{\imath}^{\prime }$. Note that this acceleration is not constant and it is not radial.

The condition for slipping is when the net force acting on a system has a magnitude that is equal to the static friction force, $|\vec{F}_{I}| \le f = \mu mg$.

$$
\mu mg = |\vec{F}_{I}|
$$

$$
\mu mg = |2mv^{\prime }\omega \hat{\jmath}^{\prime }- m\omega ^{2}x^{\prime }\hat{\imath}^{\prime }|
$$

:::{image} ../images/math/p108-808ea92403fb.svg
:alt: Mathematical expression from source PDF page 108
:class: source-equation
:align: center
:::

$$
\mu ^{2}g^{2}= 4(v^{\prime })^{2}\omega ^{2}+ \omega ^{4}(x^{\prime })^{2}
$$

$$
\begin{aligned}
(x^{\prime})^{2}&= \frac{\mu ^{2}g^{2}- 4(v^{\prime})^{2}\omega ^{2}}{\omega ^{4}} \\
x^{\prime}&= \frac{\sqrt{\mu} ^{2}g^{2}- 4(v^{\prime})^{2}\omega ^{2}}{\omega ^{2}}
\end{aligned}
$$

So this is the maximum radial distance that the cat can reach before the combination of fictitious forces exceed the condition for slipping.

1. Consider the case where the cat walks inward toward the origin instead of outward. What is the *Coriolis* force in this case?

2. Sketch [Figure 5.3](#fig-5-3) in the case where the cat walks toward the origin.

::::

<!-- Source PDF page 109; printed label 100. -->

(sec-5-4)=
## 5.4 Earth as a Non-Inertial Frame

The Earth is rotating, which means the Earth is a non-inertial reference frame. To think about the fictitious forces acting on the Earth, it helps to think in 3-D.

Consider [Figure 5.4](#fig-5-4), which shows the position of a person on Earth’s surface. Ignoring Earth’s orbit around the Sun, we can set the inertial reference frame to the center of the planet (rotation is zero there) and we can set the non-inertial reference frame to the position of the person at the surface. Note: this example is a case where the inertial and rotating frames do not have the same origin. But the distance between them, $R$ is fixed.

:::{figure} ../images/figures/figure-5-4.png
:label: fig-5-4
:enumerator: 5.4
:alt: Figure shows the relationship between the inertial x-y-z coordinate centered on the Earth and the rotating x-prime, y-prime, z-prime coordinate system on the Earth’s surface.
:width: 293px

A coordinate system on Earth. The point shown is fixed to the surface of the Earth. The red coordinates show the non-inertial reference frame for an observer at this location $(O^{\prime })$. The black coordinates show the inertial reference frame at the center of the Earth, a distance $R$ from the point. Also shown are the latitude $\theta$, polar angle $\varphi$, and distance to the rotation axis $\rho$.
:::

Our observer is located at the point shown in [Figure 5.4](#fig-5-4). This person is at a latitude of $\theta$, where the equator is located at the $x,y-$plane of the inertial frame. We can also describe the person’s position using the polar angle $\varphi$ (also called the colatitude), where $\varphi = 90-\theta$. In the inertial frame, these angles do not change (e.g., the latitude of a fixed point on Earth does not change), but the $x,y$ axes rotate about the $z$ axis due to Earth’s spin.

The observer on Earth’s surface has a different coordinate system that is fixed from their perspective (they don’t see the rotation). For example, here on Earth we define up and down, North and South, East and West, and those directions are fixed from our reference, even though we are on a moving surface. North is always north. Up is always up. The Earth’s motion does not change your perspective on those directions.

In this textbook, we will define up as $+\hat{k}^{\prime }$, East as $+\hat{\imath}^{\prime }$, and North as $+\hat{\jmath}^{\prime }$ for an observer in the rotating reference frame. Subsequently, down, West, and South will be the negative unit vector directions. Note that from the reference of the observer, the axis of rotation for the Earth is not along any of the unit vector axes. [Figure 5.5](#fig-5-5) shows the $\hat{k}^{\prime }$ and $\hat{\jmath}^{\prime }$ components of Earth’s angular velocity vector for an observer at a latitude of $\theta$. Note that the component of $\omega$ in the non-inertial frame depends on latitude.

From [Figure 5.5](#fig-5-5), Earth’s angular velocity vector can be described as

$$
\vec{\omega} = \omega \cos \theta \hat{\jmath}^{\prime }+ \omega \sin \theta \hat{k}^{\prime }
$$ (eq-5-9)

Thus, non-inertial motion on Earth’s surface will vary with latitude.

<!-- Source PDF page 110; printed label 101. -->

:::{figure} ../images/figures/figure-5-5.png
:label: fig-5-5
:enumerator: 5.5
:alt: Figure 5.5 from the source textbook
:width: 390px

(a) A person at a latitude of $\theta$. The moving coordinate system has $\hat{k}^{\prime }$ normal to the surface whereas $\vec{\omega}$ is in the $\hat{k}$ direction of the inertial frame (see also, Figure 5.4). (b) Zoom in of the reference frame at a latitude of $\theta$ showing the components of $\vec{\omega}$ in the $\hat{k}^{\prime }$ and $\hat{\jmath}^{\prime }$ coordinates.
:::

For a person on Earth’s surface moving with a constant velocity, there will be fictitious forces acting on them because they are in a non-inertial frame. Let’s look at what is at play.

$$
\vec{a}^{\prime }= \vec{a} - \vec{\alpha} \times \vec{r}^{\prime }- 2\vec{\omega} \times \vec{v}^{\prime }- \vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) - \vec{A}
$$

We can simplify this equation. We will assume that (1) the Earth’s rotation is constant$1$, so $\alpha = \dot{\omega}$ = 0 and (2) the origin of the non-inertial frame has no translation acceleration relative to the origin of the inertial frame $(R$ is constant, $A = \ddot{R}$ = 0). Moreover, if the person is moving with a constant velocity on Earth’s surface, $\vec{a}^{\prime }$ = 0. Taking these simplifications, the remaining fictitious forces are the centrifugal and the Coriolis forces.

$$
0 = \vec{a} - 2\vec{\omega} \times \vec{v}^{\prime }- \vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime })
$$

Let’s start with the centrifugal force, $F_{cent}= -m\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime })$.

[Figure 5.6](#fig-5-6) shows the breakdown of the vector directions from the two cross products. Since $\vec{\omega}$ is not along the $\hat{k}^{\prime }$ axis and it is not perpendicular to $\vec{R}$ , getting the direction is not intuitive. You can use the right hand rule (see [Chapter 1.5.2](#sec-1-5-2)), to estimate the direction, where $\vec{\omega}\times \vec{R}$ points mostly into the page, and $\vec{\omega}\times (\vec{\omega}\times \vec{R}$ ) points mostly toward the Earth’s axis of rotation. Thus, we should expect the centrifugal force to mostly point away from the axis of rotation.

The total magnitude of the centrifugal force should therefore be given by

$$
|\vec{F}_{cen}| = m\omega ^{2}R\sin \varphi = m\omega ^{2}R\cos \theta
$$

where $\varphi$ is the angle between the axis of rotation and the radius vectors (see [Figure 5.6](#fig-5-6)). Note that $\sin \varphi = \cos \theta$, and that the $\sin \varphi$ term only comes from the first cross product,

$$
(\vec{\omega} \times \vec{r}^{\prime }).
$$

As for the direction, the centrifugal force should be along an axis that is perpendicular to the rotation axis (e.g., $\hat{\rho}$ ). We can verify this by using the vector cross product, where the

$$
\begin{aligned}
^{1}\mathrm{The} \mathrm{Earth} \mathrm{is} \mathrm{actually} \mathrm{slowing} \mathrm{down} \mathrm{in} \mathrm{rotation} \mathrm{due} \mathrm{to} \mathrm{torques} \mathrm{with} \mathrm{the} \mathrm{Moon}, \mathrm{but} \mathrm{the} \mathrm{change} \mathrm{is} \mathrm{very} \\
\mathrm{small} \mathrm{and} \mathrm{can} \mathrm{be} \mathrm{considered} \mathrm{negligible}.
\end{aligned}
$$

<!-- Source PDF page 111; printed label 102. -->

:::{figure} ../images/figures/figure-5-6.png
:label: fig-5-6
:enumerator: 5.6
:alt: Figure shows the vector directions for the centrifugal force for an observer on Earth’s surface.
:width: 455px

The vector cross product solution for the centrifugal force at a position that is at a latitude of $\theta$ from the equator. The point $P$ is undergoing circular motion with a radius of $\rho$, with $\rho = R\sin \varphi = R\cos \theta$.
:::

observer is located at $\vec{R}\hat{k}^{\prime }$ and the Equation for Earth’s angular motion in the non-inertial frame from Equation 5.9.

$$
\begin{aligned}
\hat{\imath}^{\prime }\hat{\jmath}^{\prime }\hat{k}^{\prime } \\
\vec{\omega} \times \vec{r}^{\prime }&= |0 \omega \cos \theta \omega \sin \theta | = \hat{\imath}^{\prime }(R\omega \cos \theta) + \hat{\jmath}^{\prime }(0 - 0) + \hat{k}^{\prime }(0 - 0) = R\omega \cos \theta \hat{\imath}^{\prime } \\
0 0 R
\end{aligned}
$$

$$
\begin{aligned}
\hat{\imath}^{\prime }\hat{\jmath}^{\prime }\hat{k}^{\prime } \\
\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) &= | 0 \omega \cos \theta \omega \sin \theta | \\
R\omega \cos \theta 0 0 \\
&= \hat{\imath}^{\prime }(0 - 0) + \hat{\jmath}^{\prime }(\omega ^{2}R\cos \theta \sin \theta) + \hat{k}^{\prime }(-\omega ^{2}R\cos ^{2}\theta)
\end{aligned}
$$

$$
= \omega ^{2}R\cos \theta \sin \theta \hat{\jmath}^{\prime }- \omega ^{2}R\cos ^{2}\theta \hat{k}^{\prime }
$$

Thus, the centrifugal force will be:

$$
\vec{F}_{cen}= -m\omega ^{2}R\cos \theta \sin \theta \hat{\jmath}^{\prime }+ m\omega ^{2}R\cos ^{2}\theta \hat{k}^{\prime }
$$

which is pointing in a direction that is South and up. Looking at [Figure 5.6](#fig-5-6), that direction point away from the rotation axis.

::::{tip} Quick Question

1. What is the direction of the centrifugal force if you are located at the Equator? Does this answer make sense? Consider [Figure 5.6](#fig-5-6) from the perspective of someone standing on the equator.

::::

<!-- Source PDF page 112; printed label 103. -->

By contrast, gravity from the Earth is directed toward the center of the Earth, which will be along the $-\hat{k}^{\prime }$ direction, by definition. That means we have two vectors with different directions. The effective gravity will be the sum of these two vectors.

Taking the magnitude of $\vec{F}_{cen}$, we have:

:::{image} ../images/math/p112-50897b6437de.svg
:alt: Mathematical expression from source PDF page 112
:class: source-equation
:align: center
:::

:::{image} ../images/math/p112-37f8e1e2e507.svg
:alt: Mathematical expression from source PDF page 112
:class: source-equation
:align: center
:::

$$
= m\omega ^{2}R\cos \theta
$$

which is what we expected using the right-hand rule and the simple vector cross product.

The total magnitude of the centrifugal force is quite small. The centrifugal force is *largest* at the equator $(\theta$ = 0). Taking $R$ = 6370 km for the Earth’s radius and $\omega = 7.27 \times 10^{-5}$ $\mathrm{s}^{-1}$ for the rotation rate, the centrifugal acceleration is 0.034 m $\mathrm{s}^{-2}$, which is $< 1\%$ of the magnitude of acceleration from Earth’s gravitational field at the surface.

So for an observer on the surface of the Earth, we can generally ignore the centrifugal force from Earth’s rotation. It has a negligible effect. Thus, our vector equation for a person on Earth’s surface becomes:

$$
\vec{a}^{\prime }= \vec{a} - 2\vec{\omega} \times \vec{v}^{\prime }
$$

where the remaining motion is just from the inertial forces and the Coriolis force.

(sec-5-5)=
## 5.5 Foucault’s Pendulum

Foucault’s pendulum is a classic example of the Coriolis force in action. Consider a simple pendulum (mass hanging from an ideal string) that is also frictionless at its pivot point. Only two forces act on this pendulum, tension and gravity (see [Chapter 3](#ch-3) and [Figure 5.7](#fig-5-7)).

:::{figure} ../images/figures/figure-5-7.png
:label: fig-5-7
:enumerator: 5.7
:alt: Cartoon showing the tension and gravitational forces for a Foucault pendulum.
:width: 150px

A Foucault pendulum of mass $m$ and length $\ell$. The pivot point at $P$ does not move and has no friction. Two forces act in the inertial frame, tension $(\vec{T}$ ) and gravity $(\vec{F}_{g})$. Gravity points down, tension is directed to the pivot. Note that the pendulum is moving near Earth’s surface, so we will want to use only the non-inertial coordinate system.
:::

When set in motion, the pendulum will have a non-zero Coriolis force. Ignoring the azimuthal and centrifugal forces (negligible), we can simplify the non-inertial frame acceleration as (see previous section):

$$
\vec{a}^{\prime }= \vec{a} - 2\vec{\omega} \times \vec{v}^{\prime }
$$

where $a$ is the acceleration due to the net (real) forces acting on the pendulum in the inertial frame and $-2\vec{\omega} \times \vec{v}^{\prime }$ is from the Coriolis force.

<!-- Source PDF page 113; printed label 104. -->

**1. Finding the inertial forces:** The inertial forces are gravity and tension. Gravity acts down $(-\hat{k}^{\prime }$ direction) in the non-inertial frame. So we need to convert tension to our non-inertial reference frame by finding its components along $\hat{\imath}^{\prime },\hat{\jmath}^{\prime },\hat{k}^{\prime }$. [Figure 5.8](#fig-5-8) shows the break down of the tension, $\vec{T}$ in red, into the non-inertial coordinate system.

:::{figure} ../images/figures/figure-5-8.png
:label: fig-5-8
:enumerator: 5.8
:alt: Figure 5.8 from the source textbook
:width: 325px

Vector diagram for tension in a pendulum relative to $\hat{\imath}^{\prime },\hat{\jmath}^{\prime },\hat{k}^{\prime }$. Left: A 3-D view of the tension. The tension is shown by the red arrow. The pendulum makes an angle $\delta$ with respect to $\hat{k}^{\prime }$. The black arrows at the bottom show the component of tension in the $x^{\prime },y^{\prime }$ plane and along the $x^{\prime }$ and $y^{\prime }$ axes. Right: A bird’s eye view of the $x^{\prime },y^{\prime }$ plane with the component of tension and the pendulum rope length in this plane.
:::

The component of tension in the $x^{\prime }- y^{\prime }$ plane is $T \sin \delta$, where $\delta$ is the angle between the pendulum and the vertical. This vector points inward toward the origin (because it is a restoring force). [Figure 5.8](#fig-5-8) also shows the component of the pendulum rope length in the $x^{\prime }- y^{\prime }$ plane in blue, given by $\ell \sin \delta$ for a rope of length $\ell$.

Using [Figure 5.8](#fig-5-8) with a bit of algebra, you can get,

$$
\vec{T} = - \frac{Tx^{\prime}}{\ell} \hat{\imath}^{\prime}- \frac{Ty^{\prime}}{\ell} \hat{\jmath}^{\prime}+ \frac{T(\ell - z^{\prime})}{\ell} \hat{k}^{\prime}
$$

Note the negative signs for the $x^{\prime }$ and $y^{\prime }$ components. This should make sense as these would be a restoring force and restoring forces are always negative.

For the $z^{\prime }$ component, we can use the vector dot product because we know the angle between tension and $\hat{k}^{\prime }$ is $\delta$. So $T_{z^{\prime }}= T \cos \delta$. We can define $\cos \delta$ from the length of the rope because it is fixed. The pendulum height is given by $z^{\prime }= \ell -\ell \cos \delta$, so we can solve for $\cos \delta = \frac{\ell -z^{\prime}}{\ell}$. For small angles, $z^{\prime }\approx 0$ so $T_{z^{\prime }}\approx T$.

For the $x^{\prime }$ and $y^{\prime }$ components, we use the projection of $T$ into the $x^{\prime }- y^{\prime }$ plane. The right panel of [Figure 5.8](#fig-5-8) shows this projection. The $x^{\prime }-$component is given by $T_{x^{\prime }}= T \sin \delta \sin \alpha$, where $\sin \alpha = \frac{x^{\prime}}{\ell \sin \delta}$, so $T_{x^{\prime }}$ simplifies to $T_{x^{\prime}}= \frac{Tx^{\prime}}{\ell}$. Similar arguments can be made for $T_{y^{\prime }}$.

::::{tip} Quick Question

1. Go through the algebra and verify that you get $\vec{T} = - \frac{Tx^{\prime}}{\ell} \hat{\imath}^{\prime}- \frac{Ty^{\prime}}{\ell} \hat{\jmath}^{\prime}+ \frac{T(\ell -z^{\prime})}{\ell} \hat{k}^{\prime}$ for a pendulum that is displaced by an angle $\delta$ from the vertical.

::::

**2. Finding the non-inertial forces:** For our pendulum, the only non-inertial force we

<!-- Source PDF page 114; printed label 105. -->

need to consider is the Coriolis force (the centrifugal force is negligible). In [Section 5.3](#sec-5-3) we found the Coriolis force for a velocity in 1-D. The Foucault pendulum, however, moves in $\hat{\imath}^{\prime },\hat{\jmath}^{\prime },\hat{k}^{\prime }$. If we assume small angles, then $z^{\prime }\ll \ell$ and any motion in the vertical direction $(\hat{k}^{\prime })$ will be negligible and we can approximate the velocity by $\vec{v}^{\prime }= \vec{v}^{\prime }= \dot{x}^{\prime }\hat{\imath}^{\prime }+ \dot{y}^{\prime }\hat{\jmath}^{\prime }$.

Using $\vec{\omega}$ from Equation 5.9 and $\vec{v}^{\prime }= \dot{x}^{\prime }\hat{\imath}^{\prime }+ \dot{y}^{\prime }\hat{\jmath}^{\prime }$, we can solve for the Coriolis force.

$$
\begin{aligned}
\hat{\imath}^{\prime }\hat{\jmath}^{\prime }\hat{k}^{\prime } \\
\vec{\omega} \times \vec{v}^{\prime }&= |0 \omega \cos \theta \omega \sin \theta | = (-\dot{y}^{\prime }\omega \sin \theta)\hat{\imath}^{\prime }+ (\dot{x}^{\prime }\omega \sin \theta)\hat{\jmath}^{\prime }+ (-\dot{x}^{\prime }\omega \cos \theta)\hat{k}^{\prime } \\
\dot{x}^{\prime }\dot{y}^{\prime }0
\end{aligned}
$$

The solution to the Coriolis force is then:

$$
\vec{F}_{Cor,x^{\prime }}= 2m\dot{y}^{\prime }\omega \sin \theta
$$

$$
\vec{F}_{Cor,y^{\prime }}= -2m\dot{x}^{\prime }\omega \sin \theta
$$

for the $x^{\prime }$ and $y^{\prime }$ axes, respectively. Again, we’re going to ignore the $\hat{k}^{\prime }$ component and focus on the deflection in $\hat{\imath}^{\prime }$ and $\hat{\jmath}^{\prime }$.

**3. Finding the acceleration** We have descriptions for gravity, tension, and the Coriolis force in our non-inertial reference frame. We can now solve for the acceleration. For simplicity, we will do this for the $x^{\prime }$ and $y^{\prime }$ components separately. Since we are assuming negligible motion in $z^{\prime }$, we can ignore all forces (inertial or fictitious) in the $z^{\prime }$ direction. The remaining forces in $x^{\prime }$ and $y^{\prime }$ are the inertial tension force and the fictitious Coriolis force.

$$
\begin{aligned}
m\ddot{x}^{\prime}&= - \frac{Tx^{\prime}}{l} + 2m\omega \sin \theta \dot{y}^{\prime} \\
m\ddot{y}^{\prime}&= - \frac{Ty^{\prime}}{l} - 2m\omega \sin \theta \dot{x}^{\prime}
\end{aligned}
$$

where $\theta$ is the latitude of the observer. if we assume that the angle of displacement is small, then $T \approx mg$. So we can simplify the above as:

$$
\begin{aligned}
\ddot{x}^{\prime}&= - \frac{g}{l} x^{\prime}+ (2\omega \sin \theta)\dot{y}^{\prime} \\
\ddot{y}^{\prime}&= - \frac{g}{l} y^{\prime}- (2\omega \sin \theta)\dot{x}^{\prime}
\end{aligned}
$$

The above equations are differential equations of motion. Note that for a given observer on Earth, $\omega$ and $\theta$ are constant. The first term should look familiar. This is the solution for a simple pendulum that is displaced by a small angle from equilibrium. If $\omega$ = 0, then we recover the differential equation of motion for an ordinary pendulum in an inertial frame.

The second terms comes from the Coriolis force and describe a deflection in the pendulum’s swing. This deflection always acts perpendicular to the velocity vector in the plane of motion. So instead of just oscillating back and forth in a straight line, the pendulum will slowly turn (precess) as it oscillates back and forth. The magnitude of the Coriolis force is small, but it changes the direction of the pendulum just enough that it will trace out a circle over time.

<!-- Source PDF page 115; printed label 106. -->

::::{admonition} Foucault Pendulums

Stirling Hall at Queen’s University has a Foucault pendulum! Visit the pendulum at different times of day and note which direction it is swinging in and how that direction changes from morning to afternoon relative to the hall. If you want to wait and watch a full rotation, note that it takes many hours (see quick questions below).

Alternatively, here is [a great video that shows the full rotation of a Foucault pendulum](https://www.youtube.com/watch?v=se84vG6bzoA) sped up.

::::

For northern latitudes $(\theta > 0)$, the pendulum will rotate clockwise due to the Coriolis force, and for southern latitudes $(\theta < 0)$, the pendulum will rotate counter-clockwise due to the Coriolis force. At the equator, $\theta$ = 0, and there is no deflection in the $x^{\prime }$ and $y^{\prime }$ plane. So a Foucault pendulum at the equator is just an ordinary pendulum that oscillates back and forth.

The time it takes the pendulum to complete one full circle depends on the latitude. The period for one full circle due to the Coriolis force is given by:

$$
t_{F}= \frac{2\pi}{\omega \sin \theta} = \frac{24h}{\sin \theta}
$$

So the Foucault pendulum offers a direct way to measure your latitude. At the North and South pole, this period is exactly 24 hours (the length of 1 day). You can say that the Earth is rotating below the pendulum as it oscillates in place due to the Coriolis force. As you approach the equator, the period gets longer. The experiment of Foucault’s pendulum was monumental for showing Earth’s rotation and that the Earth is a non-inertial frame.

::::{tip} Quick Questions

1. How long would it take the Striling Hall Foucault pendulum to complete one full rotation (Kingston has $\theta$ = 45 deg)?

2. The length of a day on Venus is almost the same as its year. If the Earth had a spin that was almost the same length as its year, what would that mean for the motion of a Foucault pendulum?

::::

(sec-5-6)=
## 5.6 Real-World Application

Although forces like the centrifugal force and Coriolis force are fictitious, we can see the effects of rotating references frames on objects and ourselves. A centrifuge is a device that rotates an object around a fixed axis very quickly. In laboratories, these high rotation speeds are used to separate out different substances into layers by their densities allowing pristine samples to be collected. The effective force can be hundreds or thousands of times that of a standard Earth gravity.

Rotating rides at amusement parks operate at lower speeds that centrifuges, but those on the rides feel similar effects. When on one of these rides, you would feel your body move

<!-- Source PDF page 116; printed label 107. -->

outward, often against the wall. Space agencies also use systems like centrifuges for highgravity simulation during astronaut training. Astronauts leaving or returning to Earth feel changes in effective gravity that can affect the blood flow to their heads and make them pass out. With training, the astronauts can simulate those conditions and learn to function.

Courtesy of the ESA astronaut Andreas Mogensen, [this video shows](https://www.youtube.com/watch?v=Hgz7kJJSksM) the view from outside and inside a training centrifuge in operation.

Fisher Scientific provides [a primer on centrifuge theory](https://www.fishersci.se/se/en/scientific-products/centrifuge-guide/centrifugation-theory.html).

(sec-5-7)=
## 5.7 Summary

::::{admonition} Key Takeaways

This chapter applies the basic concepts of non-inertial frames from [Chapter 4](#ch-4) to more complex problems. In particular, this chapter expands on the Coriolis and centrifugal fictitious forces in rotating frames. The general equation for the fictitious forces are,

:::{image} ../images/math/p116-b25ac2a6fc7b.svg
:alt: Mathematical expression from source PDF page 116
:class: source-equation
:align: center
:::

This chapter also introduces the Earth to be a non-inertial frame. To first order, the physics problems from [Chapter 2](#ch-2) and 3 assume that the Earth is an inertial frame of reference. This approximation is generally fine, as the fictitious forces do not greatly affect these types of physics problems. Try the practice problems below to see the magnitude of some of these forces.

But for some types of high-precision physics, such as weather patterns, satellite orbits, and Foucault pendulums, you need to take into account the fictitious forces that arise from a non-inertial Earth-bound reference frame. This chapter goes through a few examples, highlighting how to breakdown and simplify such problems.

::::

::::{admonition} Important Equations

**For No Rotation:**

$$
\vec{a}^{\prime }= \vec{a} - \vec{A}
$$

$$
\vec{v}^{\prime }= \vec{v} - \vec{u}
$$

**Rotating Frame:**

$$
\vec{a}^{\prime }= \vec{a} - \vec{\alpha} \times \vec{r}^{\prime }- 2\vec{\omega} \times \vec{v}^{\prime }- \vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime }) - \vec{A}
$$

$$
\vec{v}^{\prime }= \vec{v} - \vec{\omega} \times \vec{r}^{\prime }- \vec{u}
$$

::::

<!-- Source PDF page 117; printed label 108. -->

::::{admonition} Continued

**Rotation Frame Fictitious Forces:**

:::{image} ../images/math/p117-9f5e20ed3b20.svg
:alt: Mathematical expression from source PDF page 117
:class: source-equation
:align: center
:::

**Earth’s rotation axis for an observer on the surface:**

$$
\vec{\omega} = \omega \cos \theta \hat{\jmath}^{\prime }+ \omega \sin \theta \hat{k}^{\prime }
$$

**Centrifugal Force:**

$$
\vec{F}_{cent}= -m\vec{\omega} \times (\vec{\omega} \times \vec{r}^{\prime })
$$

**Coriolis Force:**

$$
\vec{F}_{Cor}= -2m\vec{\omega} \times \vec{v}^{\prime }
$$

::::

<!-- Source PDF page 118; printed label 109. -->

(sec-5-8)=
## 5.8 Practice Problems

See [Appendix C](#app-c) for answers to the practice problems.

(problem-5-1)=

::::{admonition} Practice Problem 5-1

For the following questions, which fictitious force(s) are non-zero?

a) A cannon fires a cannonball from the surface of the Earth.

b) A ladybug is sitting at the edge of a stationary on a merry-go-round that is spinning at a constant speed.

c) A ladybug is sitting at the edge of a decelerating merry-go-round.

d) A lady bug is walking towards the edge of a merry-go-round that is spinning at a constant speed.

e) A lady bug is running towards the edge of a merry-go-round that is decelerating its spin speed and has gone off the rails and is moving away from its starting point with a constant acceleration.

::::

(problem-5-2)=

::::{admonition} Practice Problem 5-2

Astronauts use a training centrifuge to simulate the high gravity conditions they can experience during launch and re-entry. NASA uses a centrifuge that is 8.84 m in diameter for astronaut training.

a) Find the expression for the centrifugal acceleration.

b) The centrifuge can simulate accelerations that are equivalent to $20g$ (20 times Earth’s gravity). How fast must it be rotating to reach that acceleration? Give your units in revolutions per second.

c) Plot angular velocity versus centrifugal acceleration from $1g$ to $20g$. Adjust your plot for different size centrifuges and see how the values change.

::::

<!-- Source PDF page 119; printed label 110. -->

(problem-5-3)=

::::{admonition} Practice Problem 5-3

A cat sits on a rotating table that is rotating in the counter-clockwise direction with an angular velocity that is decelerating. Draw a free-body diagram showing the correct directions of the fictitious forces acting on the cat.

:::{figure} ../images/figures/figure-5-9.png
:label: fig-5-9
:enumerator: 5.9
:alt: Figure shows the cat’s position on the x-prime axis on a rotating turntable.
:width: 217px

Figure for [Problem 5-9](#problem-5-9).
:::

::::

(problem-5-4)=

::::{admonition} Practice Problem 5-4

Typical vinyl records spin $33 \frac{1}{3}$ times per minute. What is the magnitude and direction of the Coriolis Force experienced by a ladybug $(m = 0.02$ g) that is crawling radially outward with a velocity of 1 cm $\mathrm{s}^{-1}$ at a distance of 10 cm from the axis of rotation?

::::

(problem-5-5)=

::::{admonition} Practice Problem 5-5

An amusement park ride spins its riders in a large circle and then tilts the circle into a vertical position. Before it begins to tilt, it has to accelerate to an angular velocity that will allow its riders to be safe at the top of the tilted circle. Assume the ride has a radius of 12 m.

a) During the acceleration phase of the ride, what fictitious forces will the riders experience?

b) The ride reaches a maximum centrifugal acceleration of $1g$ before it tilts. Find the angular acceleration if it takes 90 seconds to reach its maximum speed and it gets there with a constant angular acceleration.

c) Find the magnitude of the azimuthal force and centrifugal force halfway through the acceleration phase (e.g., at 45 seconds).

::::

<!-- Source PDF page 120; printed label 111. -->

(problem-5-6)=

::::{admonition} Practice Problem 5-6

A race car driver at the Indy 500 races (latitude is 40 deg N) is traveling south in their reference frame.

a) What is the direction of the Coriolis force acting on the driver?

b) If the race car driver hits a speed of 200 km/h going due north at the Indy 500 races, what is the magnitude of the Coriolis force acting on this driver relative to the force of gravity (e.g., $F_{Cor}/F_{g})$? You can assume that the angular velocity for the Earth is

$$
7.27 \times 10^{-5}\mathrm{s}^{-1}).
$$

::::

(problem-5-7)=

::::{admonition} Practice Problem 5-7

A group of astronauts crash land on a planet with an unknown angular velocity of rotation. The astronauts have a Foucault pendulum, and they measure the period of precession of 38 hours at their unknown latitude of $\theta$. The astronauts then walk north and estimate their new position as being $10^{\circ}$ above the original latitude. They then measure a new period of precession for the Foucault pendulum of 31 hours. What was the original latitude of the crash landing? (Hint, you may find the following trig identity helpful: $\sin (\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta)$

::::

(problem-5-8)=

::::{admonition} Practice Problem 5-8

On a physics field trip, you drop a pebble from rest in the elevator shaft of the CN Tower (latitude of 43.5 deg, height of 500 m). As the pebble falls, it is deflected along the $x^{\prime }-$ axis. If $+\hat{\imath}^{\prime }$ is East and $-\hat{\imath}^{\prime }$ is West, what is the magnitude and direction of the deflection in $x^{\prime }$? (Hint, you will need to solve for the deflection as a function of $\dot{z}^{\prime }$ to answer this question. You can assume that the deflection is small such that only the velocity from $\dot{z}^{\prime }$ matters for the Coriolis force. Use an angular velocity of $7.27\times 10^{-5}\mathrm{s}^{-1}$ for the Earth.)

::::

<!-- Source PDF page 121; printed label 112. -->

(problem-5-9)=

::::{admonition} Practice Problem 5-9

A bead of mass $m$ sits at the end of a smooth frictionless rod of length $L$ that is rotating about one end at a rate of $\omega$ as shown in the figure below. The bead is given a little push which so that it starts moving.

a) What is the magnitude and direction of the centrifugal and Coriolis forces?

b) What is the magnitude and direction of the inertial force?

c) Draw a free-body diagram for the bead in the rotating frame. What inertial force(s) are acting on the bead?

d) Use the differential equation of motion to find the equation for $x(t)$ if the initial velocity given to the bead is $\omega L$. (Hint, you may find the following equation helpful: $\ddot{x} - C^{2}x = 0 \rightarrow x(t) = Ae^{Ct}+ Be^{-Ct}$, where $A,B,C$ are constants)

:::{figure} ../images/figures/figure-5-10.png
:label: fig-5-10
:enumerator: 5.10
:alt: Figure for Problem 5-10.
:width: 217px

The bead is pushed along the positive $x^{\prime }-$axis.
:::

::::
