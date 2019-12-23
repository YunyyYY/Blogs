---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

## Intractable integrals

> ### Reference
>
> 1. https://ermongroup.github.io/cs228-notes/inference/variational/
> 2. https://theclevermachine.wordpress.com/2012/09/22/monte-carlo-approximations/.



### Monte Carlo Approximation

Using statistical methods we often run into integrals that take the form:
$$
I=\int_{a}^{b} h(x) g(x) d x
$$
Sometimes such an integral can be evaluated analytically. When a closed form solution does not exist, numeric integration methods can be applied. However, numerical methods quickly become intractable for any practical application that requires more than a small number of dimensions. This is where **Monte Carlo approximation** comes in. 

Monte Carlo approximation allows us to calculate an estimate for the value of $I$ by transforming the  integration problem into a procedure of sampling values from a tractable probability distribution and calculating the average of those samples. 

If function $g(x)$ fullfills the following two criteria:
$$
g(x) \geq 0, x \in(a, b)
$$
and its integral is finite
$$
\int_{a}^{b} g(x)=C<\infty
$$
then we can define a corresponding probability distribution on the interval $(a, b)$
$$
p(x)=\frac{g(x)}{C}
$$
Then we can restate the original integration as
$$
I=C \int_{a}^{b} h(x) p(x) d x=C \mathbb{E}_{p(x)}[h(x)]
$$
If we can *sample* values of $x$ using $p(x)$, then the value of  the original integral $I$ is simply a scaled version of the expected value of the integrand function $h(x)$ calculated using those samples. Turns out that the expected value $\mathbb E_{p(x)}[h(x)]$ can be easily approximated by the sample mean:
$$
\mathbb{E}_{p(x)}[h(x)] \approx \frac{1}{N} \sum_{i}^{N} h\left(x_{i}\right)
$$
where samples $x_i, i = 1...N$ are drawn independently from $p(x)$. This leads to a simple 4-Step Procedure for performing Monte Carlo approximation to the integral $I$:

1. Identify $h(x)$
2. Identify $g(x)$ and determine $p(x)$ and $C$
3. Draw $N$ independent samples from $p(x)$
4. Evaluate $I = C \mathbb E[h(x)] \approx \frac{C}{N} \sum_i^N h(x_i)$

The larger the number of samples $N$ we draw, the better our approximation to the actual value of $I$.

> #### Example $I=\int_{0}^{1} x e^{x} d x$
>
> We can calculate the closed form solution of this integral using integration by parts:
> $$
> \begin{array}{l}
> {u=x, d v=e^{x}} \\ 
> {d u=d x, v=e^{x}}
> \end{array}
> $$
> And the result is
> $$
> \begin{aligned}
> I &=u v-\int v d u = x e^{x}-\int e^{x} d x \\ 
> &=x e^{x}-\left.e^{x}\right|_{0} ^{1} =\left.e^{x}(x-1)\right|_{0} ^{1} =0-(-1)=1
> \end{aligned}
> $$
> Next we calculate the  Monte Carlo approximation of this integral.
>
> 1. indentify $h(x)=x e^{x}$
> 2. identify $g(x)=1$ and determine the probability distribution function $p(x) \in (a,b) = (0,1)$. 
> 3. According to the definition expression for $p(x)$ given above we detemine $p(x)$ to be $p(x)=\frac{g(x)}{\int_{a}^{b} g(x) d x}=\frac{1}{b-a}$, which is the definition for the uniform distribution $\operatorname{uni}(0,1)$.
> 4. calculate the Monte Carlo approximation as $I=C \mathbb{E}_{p(x)} h(x)\approx \frac{1}{N} \sum_{i=1}^{N} x_{i} e^{x_{i}}$



### Markov chain Monte Carlo

Markov chain Monte Carlo (MCMC) methods comprise a class of algorithms for sampling from a probability distribution. By constructing a Markov chain that has the desired distribution as its equilibrium distribution, one can obtain a sample of the desired distribution by recording states from the chain. The more steps that are included, the more closely the distribution of the sample matches the actual desired distribution.

Most sampling-based inference algorithms are instances of Markov Chain Monte-Carlo (MCMC); two popular MCMC methods are Gibbs sampling and Metropolis-Hastings.





### Variational inference

Sampling-based methods have several important shortcomings:

- Although they are guaranteed to find a globally optimal solution given enough time, it is difficult to tell how close they are to a good solution given the finite amount of time that they have in practice.
- In order to quickly reach a good solution, MCMC methods require choosing an appropriate sampling technique (e.g. a good proposal in Metropolis-Hastings). Choosing this technique can be an art in itself.

An alternative approach to approximate inference is the **variational family** of algorithms. The main differences between sampling and variational techniques are that:

- Unlike sampling-based methods, variational approaches will almost never find the globally optimal solution.
- However, we will always know if they have converged. In some cases, we will even have bounds on their accuracy.
- In practice, variational inference methods often scale better and are more amenable to techniques like stochastic gradient optimization, parallelization over multiple processors, and acceleration using GPUs.

The main idea of variational methods is to cast inference as an optimization problem. Suppose we are given an intractable probability distribution $p$. Variational techniques will try to solve an optimization problem over a class of tractable distributions $Q$ in order to find a $q\in Q$ that is most similar to $p$. We will then query $q$ (rather than $p$) in order to get an approximate solution.





### Variational Bayesian methods

Variational Bayesian methods are a family of techniques for approximating intractable integrals arising in Bayesian inference and machine learning. They are typically used in complex statistical models consisting of observed variables (usually termed "data") as well as unknown parameters and latent variables, with various sorts of relationships among the three types of random variables, as might be described by a graphical model. As typical in Bayesian inference, the parameters and latent variables are grouped together as "unobserved variables". Variational Bayesian methods are primarily used for two purposes:

1. To provide an analytical approximation to the posterior probability of the unobserved variables, in order to do statistical inference over these variables.
2. To derive a lower bound for the marginal likelihood (sometimes called the "evidence") of the observed data (i.e. the marginal probability of the data given the model, with marginalization performed over unobserved variables). This is typically used for performing model selection, the general idea being that a higher marginal likelihood for a given model indicates a better fit of the data by that model and hence a greater probability that the model in question was the one that generated the data. (See also the Bayes factor article.)